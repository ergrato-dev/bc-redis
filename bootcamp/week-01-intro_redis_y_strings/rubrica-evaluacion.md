# Rúbrica de Evaluación — Semana 01

## Introducción a Redis y Strings

---

## 📊 Distribución de Evidencias

| Tipo | Peso | Mínimo para aprobar |
| ---- | ---- | ------------------- |
| Conocimiento 🧠 | 30% | 70% |
| Desempeño 💪 | 40% | 70% |
| Producto 📦 | 30% | 70% |

---

## 🧠 Conocimiento (30%)

### Cuestionario teórico

| Pregunta | Puntos |
| -------- | ------ |
| ¿Qué significa que Redis es "in-memory"? ¿Qué ventaja y qué riesgo implica? | 10 |
| ¿Cuál es la diferencia entre `SETEX key 60 valor` y `SET key valor EX 60`? | 10 |
| ¿Por qué se debe evitar `KEYS *` en producción? ¿Qué comando usar en su lugar? | 10 |
| ¿Qué retorna `GET` si la clave no existe? ¿Cómo distingues "clave ausente" de "valor vacío"? | 10 |
| ¿Cuándo usarías `INCR` en lugar de `GET` + suma en Python + `SET`? | 10 |
| Nombra tres diferencias entre Redis y una base de datos relacional como PostgreSQL | 10 |
| ¿Qué hace `SETNX`? ¿Para qué patrón es útil? | 10 |
| Explica el ciclo de vida de una clave con TTL: creación, consulta, expiración | 10 |
| ¿Qué información entrega `INFO server`? Menciona tres campos clave | 10 |
| ¿Qué tipos de codificación interna puede usar Redis para un String? | 10 |

**Total: 100 puntos → 30% de la nota final**

---

## 💪 Desempeño (40%)

### Práctica 01 — Primeros pasos

| Criterio | Puntos |
| -------- | ------ |
| Levanta Redis 8 con Docker Compose sin errores | 15 |
| Se conecta a redis-cli y ejecuta PING correctamente | 10 |
| Usa SELECT para navegar entre bases de datos | 10 |
| Usa SCAN para iterar claves sin KEYS * | 15 |
| Usa TYPE, TTL y OBJECT ENCODING sobre claves reales | 15 |
| Usa EXPIRE y verifica expiración con TTL | 15 |
| Usa INFO server y lee al menos 3 campos relevantes | 20 |

**Subtotal Práctica 01: 100 puntos**

### Práctica 02 — Strings con Python

| Criterio | Puntos |
| -------- | ------ |
| Conecta redis-py con decode_responses=True | 10 |
| Implementa SET/GET con JSON serializado correctamente | 15 |
| Implementa INCR/INCRBY para contador de visitas | 15 |
| Implementa SETEX/EXPIRE para cache con TTL | 20 |
| Usa MSET/MGET para operaciones en batch | 20 |
| Verifica existencia con EXISTS antes de GET | 10 |
| Usa GETDEL para cache invalidation | 10 |

**Subtotal Práctica 02: 100 puntos**

**Nota Desempeño = (Práctica 01 + Práctica 02) / 2 → 40% de la nota final**

---

## 📦 Producto (30%)

### Proyecto — Mini Blog Cache

| Criterio | Puntos |
| -------- | ------ |
| **Funcionalidad** | |
| `cache_article()` almacena artículo con TTL correcto | 15 |
| `get_article()` retorna None si no existe, dict si existe | 15 |
| `increment_views()` incrementa contador atómicamente | 10 |
| `get_views()` retorna el conteo actual de vistas | 10 |
| `invalidate_cache()` elimina clave y retorna True/False | 10 |
| `is_cached()` usa EXISTS (no GET) para verificar | 10 |
| **Calidad** | |
| Todas las funciones tienen type hints correctos | 10 |
| Claves Redis siguen el patrón `objeto:id:campo` | 10 |
| Tests pasan con fakeredis | 10 |

**Total Proyecto: 100 puntos → 30% de la nota final**

---

## 🏆 Cálculo de Nota Final

```
Nota Final = (Conocimiento × 0.30) + (Desempeño × 0.40) + (Producto × 0.30)
```

| Rango | Calificación |
| ----- | ------------ |
| 90–100 | Sobresaliente |
| 80–89 | Notable |
| 70–79 | Aprobado |
| < 70 | Recuperación |

> ⚠️ Se debe obtener mínimo **70 puntos en cada tipo de evidencia** para aprobar la semana.
