"""
Mini Blog Cache — Proyecto Semana 01

Sistema de cache para artículos de blog usando Redis Strings.
Implementa las funciones marcadas con TODO.

Convención de claves:
  cache:article:{article_id}  → artículo serializado como JSON
  views:article:{article_id}  → contador de vistas (integer)
"""

import json
import os

import redis

# ---------------------------------------------------------------------------
# Conexión a Redis
# ---------------------------------------------------------------------------

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    password=os.environ.get("REDIS_PASSWORD", "bootcamp2026"),
    decode_responses=True,
    socket_connect_timeout=5,
)

# ---------------------------------------------------------------------------
# Base de datos simulada (fuente de verdad)
# En producción esto sería una query a PostgreSQL
# ---------------------------------------------------------------------------

ARTICLES_DB: dict[int, dict] = {
    1: {"id": 1, "title": "Introducción a Redis", "author": "Alice", "content": "Redis es una base de datos en memoria..."},
    2: {"id": 2, "title": "Redis Strings explicado", "author": "Bob", "content": "Los strings son la estructura más versátil..."},
    3: {"id": 3, "title": "Casos de uso de Redis", "author": "Carol", "content": "Redis se usa en caching, rate limiting..."},
}

DEFAULT_TTL = 300  # 5 minutos

# ---------------------------------------------------------------------------
# Funciones a implementar
# ---------------------------------------------------------------------------


def cache_article(article_id: int, ttl: int = DEFAULT_TTL) -> bool:
    """
    Almacena un artículo en Redis con TTL.
    Si el artículo no existe en ARTICLES_DB, retorna False.

    Args:
        article_id: ID del artículo a cachear
        ttl: Tiempo de vida en segundos (default: 300)

    Returns:
        True si se almacenó correctamente, False si el artículo no existe
    """
    # TODO: Implementar
    # 1. Buscar el artículo en ARTICLES_DB (retornar False si no existe)
    # 2. Serializar el artículo con json.dumps()
    # 3. Almacenar en Redis con la clave "cache:article:{article_id}" y el TTL
    # 4. Retornar True
    pass


def get_article(article_id: int) -> dict | None:
    """
    Recupera un artículo del cache Redis.
    No consulta ARTICLES_DB — solo retorna lo que hay en cache.

    Args:
        article_id: ID del artículo

    Returns:
        dict con los datos del artículo, o None si no está en cache
    """
    # TODO: Implementar
    # 1. Hacer GET de "cache:article:{article_id}"
    # 2. Si es None, retornar None
    # 3. Deserializar con json.loads() y retornar
    pass


def is_cached(article_id: int) -> bool:
    """
    Verifica si un artículo está en cache usando EXISTS.
    No hace GET — solo comprueba existencia.

    Args:
        article_id: ID del artículo

    Returns:
        True si la clave existe en Redis, False si no
    """
    # TODO: Implementar
    # 1. Usar r.exists() — retorna int (1=existe, 0=no existe)
    # 2. Convertir a bool y retornar
    pass


def increment_views(article_id: int) -> int:
    """
    Incrementa el contador de vistas de un artículo de forma atómica.
    Crea el contador desde 0 si no existe.

    Args:
        article_id: ID del artículo

    Returns:
        El nuevo valor del contador después del incremento
    """
    # TODO: Implementar
    # 1. Usar INCR sobre "views:article:{article_id}"
    # 2. Retornar el valor resultante (ya es int)
    pass


def get_views(article_id: int) -> int:
    """
    Obtiene el número actual de vistas de un artículo.

    Args:
        article_id: ID del artículo

    Returns:
        Número de vistas (0 si el contador no existe)
    """
    # TODO: Implementar
    # 1. Hacer GET de "views:article:{article_id}"
    # 2. Si es None, retornar 0
    # 3. Convertir a int y retornar
    pass


def invalidate_cache(article_id: int) -> bool:
    """
    Elimina un artículo del cache (no elimina el contador de vistas).

    Args:
        article_id: ID del artículo

    Returns:
        True si la clave existía y fue eliminada, False si no existía
    """
    # TODO: Implementar
    # 1. Usar DEL sobre "cache:article:{article_id}"
    # 2. DEL retorna el número de claves eliminadas (int)
    # 3. Retornar True si se eliminó 1 clave, False si fue 0
    pass


# ---------------------------------------------------------------------------
# Demo
# ---------------------------------------------------------------------------

if __name__ == "__main__":
    print("=== Mini Blog Cache — Demo ===\n")

    # Cachear artículos
    for article_id in [1, 2, 3]:
        success = cache_article(article_id, ttl=120)
        print(f"Artículo {article_id} cacheado: {success}")

    print()

    # Simular lecturas con conteo de vistas
    for _ in range(3):
        article = get_article(1)
        if article:
            views = increment_views(1)
            print(f"[CACHE HIT] '{article['title']}' — vistas: {views}")

    print()

    # Artículo inexistente
    result = cache_article(999)
    print(f"Cachear artículo inexistente (999): {result}")
    print(f"¿Artículo 999 en cache? {is_cached(999)}")

    print()

    # Invalidar cache
    print(f"Vistas artículo 1 antes de invalidar: {get_views(1)}")
    invalidated = invalidate_cache(1)
    print(f"Cache artículo 1 invalidado: {invalidated}")
    print(f"¿Artículo 1 en cache después de invalidar? {is_cached(1)}")
    print(f"Vistas artículo 1 después de invalidar (el contador persiste): {get_views(1)}")
