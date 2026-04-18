# Proyecto — Mini Blog Cache

## 🎯 Descripción

Implementa un sistema de cache para artículos de blog. La aplicación Python consultará Redis antes de ir a la "base de datos" (simulada), almacenará los artículos con TTL configurable y contará las vistas de forma atómica.

Este proyecto consolida todos los comandos String de la semana en un caso de uso real.

---

## 📋 Funcionalidades a Implementar

| Función | Descripción | Comando Redis |
| ------- | ----------- | ------------- |
| `cache_article()` | Almacena artículo JSON con TTL | `SETEX` |
| `get_article()` | Recupera artículo del cache | `GET` |
| `is_cached()` | Verifica si un artículo está en cache | `EXISTS` |
| `increment_views()` | Incrementa contador de vistas | `INCR` |
| `get_views()` | Obtiene vistas actuales | `GET` |
| `invalidate_cache()` | Elimina artículo del cache | `DEL` |
| `get_cache_stats()` | Resumen de todos los artículos en cache | `MGET` + `SCAN` |

---

## 🗂️ Estructura

```
3-proyecto/
├── README.md          ← este archivo
├── docker-compose.yml
├── Dockerfile
├── redis.conf
├── requirements.txt
└── starter/
    ├── main.py        ← implementa los TODOs aquí
    └── tests/
        └── test_blog_cache.py  ← tests con fakeredis
```

---

## 🐳 Levantar el Entorno

```bash
docker compose up --build -d

# Ejecutar la aplicación
docker compose exec app python starter/main.py

# Ejecutar tests
docker compose exec app python -m pytest starter/tests/ -v
```

---

## 📌 Convención de Claves

Las claves Redis deben seguir el patrón `objeto:id:campo`:

| Dato | Clave Redis |
| ---- | ----------- |
| Artículo en cache | `cache:article:{article_id}` |
| Contador de vistas | `views:article:{article_id}` |

---

## 📊 Criterios de Evaluación

Ver [rubrica-evaluacion.md](../rubrica-evaluacion.md) — sección Producto.

---

## 💡 Hints

- `r.setex(key, ttl, value)` — almacena con TTL en segundos
- `r.exists(key)` retorna `int`, no `bool` — en Python `1` es truthy
- `r.incr(key)` crea la clave con valor 0 si no existe, luego incrementa
- Serializa con `json.dumps()` y deserializa con `json.loads()`
- Los tests usan `fakeredis.FakeRedis` — no necesitan Redis real
