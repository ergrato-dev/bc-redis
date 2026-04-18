"""
Tests para Mini Blog Cache — Semana 01

Usa fakeredis para tests completamente aislados (sin Redis real).
"""

import pytest
import fakeredis

# Parchear la conexión Redis antes de importar main
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from main import (
    cache_article,
    get_article,
    is_cached,
    increment_views,
    get_views,
    invalidate_cache,
)
import main


@pytest.fixture(autouse=True)
def fake_redis(monkeypatch):
    """Reemplaza la conexión Redis real con FakeRedis para cada test."""
    fake_r = fakeredis.FakeRedis(decode_responses=True)
    monkeypatch.setattr(main, "r", fake_r)
    yield fake_r
    fake_r.flushall()


# ---------------------------------------------------------------------------
# Tests de cache_article
# ---------------------------------------------------------------------------

def test_cache_article_returns_true_for_existing(fake_redis):
    result = cache_article(1)
    assert result is True


def test_cache_article_returns_false_for_nonexistent(fake_redis):
    result = cache_article(999)
    assert result is False


def test_cache_article_stores_json_in_redis(fake_redis):
    cache_article(1)
    raw = fake_redis.get("cache:article:1")
    assert raw is not None
    data = __import__("json").loads(raw)
    assert data["id"] == 1
    assert data["title"] == "Introducción a Redis"


def test_cache_article_sets_ttl(fake_redis):
    cache_article(1, ttl=60)
    ttl = fake_redis.ttl("cache:article:1")
    assert 0 < ttl <= 60


# ---------------------------------------------------------------------------
# Tests de get_article
# ---------------------------------------------------------------------------

def test_get_article_returns_dict_when_cached(fake_redis):
    cache_article(2)
    article = get_article(2)
    assert article is not None
    assert article["id"] == 2


def test_get_article_returns_none_when_not_cached(fake_redis):
    result = get_article(99)
    assert result is None


# ---------------------------------------------------------------------------
# Tests de is_cached
# ---------------------------------------------------------------------------

def test_is_cached_returns_true_when_exists(fake_redis):
    cache_article(1)
    assert is_cached(1) is True


def test_is_cached_returns_false_when_not_exists(fake_redis):
    assert is_cached(55) is False


# ---------------------------------------------------------------------------
# Tests de increment_views y get_views
# ---------------------------------------------------------------------------

def test_increment_views_starts_at_one(fake_redis):
    views = increment_views(1)
    assert views == 1


def test_increment_views_is_cumulative(fake_redis):
    increment_views(1)
    increment_views(1)
    views = increment_views(1)
    assert views == 3


def test_get_views_returns_zero_when_no_counter(fake_redis):
    assert get_views(99) == 0


def test_get_views_returns_current_count(fake_redis):
    increment_views(2)
    increment_views(2)
    assert get_views(2) == 2


# ---------------------------------------------------------------------------
# Tests de invalidate_cache
# ---------------------------------------------------------------------------

def test_invalidate_cache_returns_true_when_existed(fake_redis):
    cache_article(1)
    result = invalidate_cache(1)
    assert result is True


def test_invalidate_cache_returns_false_when_not_existed(fake_redis):
    result = invalidate_cache(99)
    assert result is False


def test_invalidate_cache_removes_article_from_redis(fake_redis):
    cache_article(1)
    invalidate_cache(1)
    assert is_cached(1) is False


def test_invalidate_cache_does_not_remove_view_counter(fake_redis):
    cache_article(1)
    increment_views(1)
    increment_views(1)
    invalidate_cache(1)
    # El contador de vistas NO debe eliminarse con el cache
    assert get_views(1) == 2
