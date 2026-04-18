<p align="center">
  <img src="assets/bootcamp-header.svg" alt="Bootcamp Redis Zero to Hero" width="900">
</p>

<p align="center">
  <a href="#"><img src="https://img.shields.io/badge/license-CC%20BY--NC--SA%204.0-lightgrey.svg" alt="License CC BY-NC-SA 4.0"></a>
  <a href="#"><img src="https://img.shields.io/badge/weeks-12-DC382D.svg" alt="12 Weeks"></a>
  <a href="#"><img src="https://img.shields.io/badge/hours-96-orange.svg" alt="96 Hours"></a>
  <a href="#"><img src="https://img.shields.io/badge/Redis-8.x-DC382D?logo=redis&logoColor=white" alt="Redis 8.x"></a>
  <a href="#"><img src="https://img.shields.io/badge/Python-3.13-3776AB?logo=python&logoColor=white" alt="Python 3.13"></a>
</p>

<p align="center">
  <a href="README.md"><img src="https://img.shields.io/badge/🇪🇸_Español-DC382D?style=for-the-badge&logoColor=white" alt="Versión en Español"></a>
</p>

---

## Overview

A **12-week intensive bootcamp** (~96 hours) that takes students from zero to confident with Redis — as an in-memory database, caching engine, message broker, and real-time data processing platform.

**Exit level:** Redis Engineer Junior/Mid

### Learning Outcomes

By the end of the bootcamp, students will be able to:

- ✅ Master all native Redis data structures (strings, lists, sets, hashes, sorted sets, streams)
- ✅ Implement caching, session store, and rate limiting patterns with Redis
- ✅ Design and build messaging systems with Pub/Sub and Redis Streams
- ✅ Write Lua scripts and use transactions for complex atomic operations
- ✅ Optimize performance with pipelining, pooling, and eviction configuration
- ✅ Integrate Redis in Python applications with redis-py (sync and async)
- ✅ Implement distributed locks, job queues, and leaderboards with Redis
- ✅ Configure high availability with Replication, Sentinel, and Cluster
- ✅ Secure and monitor Redis in production environments (ACLs, TLS, RedisInsight)
- ✅ Design and execute persistence, backup, and recovery strategies

---

## Curriculum

### Fundamentals (Weeks 1–4) — 32 hours

| Week                                                   | Topic                                         | Status      |
| ------------------------------------------------------ | --------------------------------------------- | ----------- |
| [01](bootcamp/week-01-intro_redis_y_strings/README.md) | Introduction to Redis, redis-cli, and Strings | ✅ Complete |
| [02](bootcamp/week-02-listas/README.md)                | Lists                                         | 🔲 Pending  |
| [03](bootcamp/week-03-sets/README.md)                  | Sets                                          | 🔲 Pending  |
| [04](bootcamp/week-04-hashes_y_sorted_sets/README.md)  | Hashes, Sorted Sets, Persistence & Security   | 🔲 Pending  |

### Advanced Structures & Patterns (Weeks 5–8) — 32 hours

| Week                                                       | Topic                        | Status     |
| ---------------------------------------------------------- | ---------------------------- | ---------- |
| [05](bootcamp/week-05-pubsub/README.md)                    | Pub/Sub                      | 🔲 Pending |
| [06](bootcamp/week-06-streams/README.md)                   | Redis Streams                | 🔲 Pending |
| [07](bootcamp/week-07-transacciones_y_scripting/README.md) | Transactions & Lua Scripting | 🔲 Pending |
| [08](bootcamp/week-08-pipelining_y_benchmarking/README.md) | Pipelining & Benchmarking    | 🔲 Pending |

### Python Integration (Weeks 9–10) — 16 hours

| Week                                                | Topic                                         | Status     |
| --------------------------------------------------- | --------------------------------------------- | ---------- |
| [09](bootcamp/week-09-redis_py_sincrono/README.md)  | redis-py Sync — Application Patterns          | 🔲 Pending |
| [10](bootcamp/week-10-redis_py_asincrono/README.md) | redis-py Async — Locks, Queues & Leaderboards | 🔲 Pending |

### High Availability & Production (Weeks 11–12) — 16 hours

| Week                                                         | Topic                                               | Status     |
| ------------------------------------------------------------ | --------------------------------------------------- | ---------- |
| [11](bootcamp/week-11-alta_disponibilidad/README.md)         | High Availability — Replication, Sentinel & Cluster | 🔲 Pending |
| [12](bootcamp/week-12-produccion_y_proyecto_final/README.md) | Production & Final Integrative Project              | 🔲 Pending |

---

## Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/ergrato-dev/bc-redis.git
cd bc-redis

# 2. Read the setup guide
cat docs/setup/README.md

# 3. Go to week 1
cd bootcamp/week-01-intro_redis_y_strings
docker compose up -d

# 4. Connect to Redis CLI
docker compose exec redis redis-cli
```

---

## Tech Stack

| Tool           | Version | Purpose                          |
| -------------- | ------- | -------------------------------- |
| Redis          | 8.x     | In-memory database engine        |
| redis-py       | 5.2.1   | Python client (sync & async)     |
| Python         | 3.13    | Integration language             |
| fakeredis      | 2.35.1  | In-memory Redis for testing      |
| pytest         | 8.3.5   | Testing framework                |
| pytest-asyncio | 0.24.0  | Async testing                    |
| Docker         | 27.5+   | Containerization                 |
| Docker Compose | 2.32+   | Orchestration                    |
| RedisInsight   | 2.58    | GUI for exploration & monitoring |

> **Development environment:** Docker only — Redis is never installed locally.

---

## Repository Structure

```
bc-redis/
├── README.md                           ← Spanish version
├── README_EN.md                        ← This file
├── assets/                             ← Global visual assets
├── docs/
│   └── setup/                          ← Install guides (Docker, local, Fedora)
├── bootcamp/
│   ├── week-01-intro_redis_y_strings/  ← ✅ Complete
│   ├── week-02-listas/
│   ├── week-03-sets/
│   ├── week-04-hashes_y_sorted_sets/
│   ├── week-05-pubsub/
│   ├── week-06-streams/
│   ├── week-07-transacciones_y_scripting/
│   ├── week-08-pipelining_y_benchmarking/
│   ├── week-09-redis_py_sincrono/
│   ├── week-10-redis_py_asincrono/
│   ├── week-11-alta_disponibilidad/
│   └── week-12-produccion_y_proyecto_final/
└── .github/
    ├── copilot-instructions.md
    ├── instructions/                   ← Automatic Copilot rules
    └── prompts/                        ← Reusable agent prompts
```

Each week follows this structure:

```
week-XX-topic/
├── README.md               ← Objectives and navigation
├── rubrica-evaluacion.md   ← Evaluation rubric
├── 0-assets/               ← SVG diagrams
├── 1-teoria/               ← Theory files (.md)
├── 2-practicas/            ← Guided exercises (uncomment-to-learn format)
├── 3-proyecto/             ← Weekly integrative project (TODO format)
├── 4-recursos/             ← Ebooks, videos, references
└── 5-glosario/             ← Key terms A–Z
```

---

## Weekly Time Budget (8 hours)

| Activity           | Time  |
| ------------------ | ----- |
| Theory             | 2 h   |
| Practice exercises | 3.5 h |
| Weekly project     | 2.5 h |

---

## Evaluation Model

Each week is assessed on three evidence types:

| Category       | Weight | Description                              |
| -------------- | ------ | ---------------------------------------- |
| Knowledge 🧠   | 30%    | Redis commands and concepts quizzes      |
| Performance 💪 | 40%    | redis-cli and Python practical exercises |
| Product 📦     | 30%    | Functional deliverable project           |

Minimum passing score: **70% per category**.

---

## Redis Key Naming Convention

```bash
# Pattern: object:subtype:id  (lowercase, colon-separated)
SET   user:42:email        "alice@example.com"
HSET  user:42              name "Alice" role "admin"
ZADD  leaderboard:global   1500 "alice"
LPUSH queue:emails:pending "job:123"
XADD  events:stream        * action "login" user_id "42"
```

---

## Documentation

- [Setup with Docker](docs/setup/docker.md)
- [Local setup (Ubuntu / Fedora / macOS)](docs/setup/local.md)
- [Copilot Instructions](.github/copilot-instructions.md)

---

## Contributing

This repository follows the bootcamp workflow. To report issues or propose improvements,
open an issue on [GitHub](https://github.com/ergrato-dev/bc-redis/issues).

---

<p align="center">
  Redis Zero to Hero — ergrato.dev · April 2026
</p>
