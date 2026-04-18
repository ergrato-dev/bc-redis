<!-- markdownlint-disable -->
<!-- cspell:disable -->

# 🤖 Instrucciones para GitHub Copilot

## 📋 Contexto del Bootcamp

Este es un **Bootcamp de Redis Zero to Hero** estructurado para llevar a estudiantes de
cero a héroe en el dominio de Redis como base de datos en memoria, motor de caching,
broker de mensajes y plataforma de procesamiento de datos en tiempo real.

### 📊 Datos del Bootcamp

- **Duración**: 12 semanas (~3 meses)
- **Dedicación semanal**: 8 horas
- **Total de horas**: ~96 horas
- **Nivel de salida**: Redis Engineer Junior/Mid
- **Enfoque**: Redis moderno (8.x) con integración Python 3.13
- **Stack**: Redis 8.x, redis-py 5.2.1, Python 3.13, Docker 27.5+, RedisInsight

---

## 🎯 Objetivos de Aprendizaje

Al finalizar el bootcamp, los estudiantes serán capaces de:

- ✅ Dominar todas las estructuras de datos nativas de Redis (strings, lists, sets, hashes, sorted sets, streams)
- ✅ Implementar patrones de caching, session store y rate limiting con Redis
- ✅ Diseñar y construir sistemas de mensajería con Pub/Sub y Redis Streams
- ✅ Escribir scripts Lua y usar transacciones para operaciones atómicas complejas
- ✅ Optimizar rendimiento con pipelining, pooling y configuración de eviction
- ✅ Integrar Redis en aplicaciones Python con redis-py (sync y async)
- ✅ Implementar distributed locks, job queues y leaderboards con Redis
- ✅ Configurar alta disponibilidad con Replicación, Sentinel y Cluster
- ✅ Asegurar y monitorear Redis en entornos productivos (ACLs, TLS, RedisInsight)
- ✅ Diseñar y ejecutar estrategias de persistencia, backup y recuperación

---

## 📚 Estructura del Bootcamp

### Distribución por Etapas

#### **Fundamentos (Semanas 1-4)** — 32 horas

- Introducción a Redis: qué es, cuándo usarlo, instalación vía Docker
- redis-cli: navegación, comandos esenciales, debugging básico
- Strings: SET/GET/MSET/INCR/DECR/APPEND/GETRANGE, expiraciones y TTL
- Listas: LPUSH/RPUSH/LPOP/RPOP/LRANGE/LLEN/LPOS, casos de uso (queues, stacks)
- Sets: SADD/SMEMBERS/SINTER/SUNION/SDIFF, operaciones de conjuntos
- Hashes: HSET/HGET/HGETALL/HDEL/HINCRBY, modelado de entidades
- Sorted Sets: ZADD/ZRANGE/ZRANK/ZSCORE/ZRANGEBYSCORE, leaderboards y rangos
- Persistencia: RDB, AOF, configuración de redis.conf
- Seguridad básica: requirepass, bind, redis.conf hardening

#### **Estructuras Avanzadas y Patrones (Semanas 5-8)** — 32 horas

- Pub/Sub: PUBLISH/SUBSCRIBE/PSUBSCRIBE/PUNSUBSCRIBE, patrones de mensajería
- Redis Streams: XADD/XREAD/XRANGE/XGROUP/XACK/XPENDING, consumer groups
- Comparación Pub/Sub vs Streams: cuándo usar cada uno
- Transacciones: MULTI/EXEC/DISCARD/WATCH, garantías ACID en Redis
- Scripting Lua: EVAL/EVALSHA, atomicidad, registro de scripts
- Pipelining: batching de comandos, reducción de round-trips
- Benchmarking: redis-benchmark, métricas clave, tuning

##### 🏗️ Progresión de Patrones de Mensajería (Semanas 5-6)

| Semana | Mecanismo | Características Clave                        |
| ------ | --------- | -------------------------------------------- |
| 05     | Pub/Sub   | Fire-and-forget, fan-out, sin persistencia   |
| 06     | Streams   | Persistencia, consumer groups, at-least-once |

#### **Integración con Python (Semanas 9-10)** — 16 horas

- redis-py síncrono: ConnectionPool, StrictRedis, serialización JSON/Pickle
- redis-py asíncrono: AsyncRedis, aioredis patterns, async pipelines
- Patrones de aplicación: Caching con decoradores, Session Store
- Rate Limiting: algoritmo sliding window y token bucket con Redis
- Distributed Locks: algoritmo Redlock, safety y liveness guarantees
- Job Queues: implementación con Lists y Streams
- Leaderboards en tiempo real con Sorted Sets

#### **Alta Disponibilidad y Producción (Semanas 11-12)** — 16 horas

- Replicación: replica-of, replication lag, read replicas
- Redis Sentinel: setup, failover automático, configuración de clientes
- Redis Cluster: sharding con hash slots, resharding, limitaciones
- Monitoreo: comando INFO, RedisInsight, métricas críticas
- Seguridad avanzada: ACLs, TLS, renaming/disabling commands
- Performance tuning: maxmemory, políticas de eviction, slow log
- Backup y recuperación: BGSAVE, BGREWRITEAOF, estrategias de migración
- Proyecto final integrador

---

## 🗂️ Estructura de Carpetas

Cada semana sigue esta estructura estándar:

```
bootcamp/week-XX-tema_principal/
├── README.md                 # Descripción y objetivos de la semana
├── rubrica-evaluacion.md     # Criterios de evaluación detallados
├── 0-assets/                 # Imágenes, diagramas y recursos visuales
├── 1-teoria/                 # Material teórico (archivos .md)
├── 2-practicas/              # Ejercicios guiados paso a paso
├── 3-proyecto/               # Proyecto semanal integrador
├── 4-recursos/               # Recursos adicionales
│   ├── ebooks-free/          # Libros electrónicos gratuitos
│   ├── videografia/          # Videos y tutoriales recomendados
│   └── webgrafia/            # Enlaces y documentación
└── 5-glosario/               # Términos clave de la semana (A-Z)
    └── README.md
```

### 📁 Carpetas Raíz

- **`assets/`**: Recursos visuales globales (logos, headers, etc.)
- **`docs/`**: Documentación general que aplica a todo el bootcamp
- **`scripts/`**: Scripts de automatización y utilidades
- **`bootcamp/`**: Contenido semanal del bootcamp

---

## 🎓 Componentes de Cada Semana

### 1. **Teoría** (1-teoria/)

- Archivos markdown con explicaciones conceptuales
- Ejemplos de comandos redis-cli con salidas esperadas
- Diagramas SVG de arquitecturas y flujos de datos
- Referencias a documentación oficial de Redis

### 2. **Prácticas** (2-practicas/)

- Ejercicios guiados paso a paso
- Incremento progresivo de dificultad
- Combinan redis-cli (semanas 1-8) y Python/redis-py (semanas 9-12)
- Casos de uso del mundo real

#### 📋 Formato de Ejercicios

Los ejercicios son **tutoriales guiados**, NO tareas con TODOs. El estudiante aprende
descomentando código o ejecutando los comandos indicados:

**README.md del ejercicio:**

```markdown
### Paso 1: Almacenar y recuperar una sesión de usuario

Concepto: Redis usa strings para almacenar cualquier valor binario. JSON serializado
es el patrón más común para sesiones.

\`\`\`bash

# redis-cli

SET session:user:42 '{"id":42,"name":"Alice","role":"admin"}' EX 3600
GET session:user:42
TTL session:user:42
\`\`\`

**Abre `starter/main.py`** y descomenta la sección correspondiente.
```

**starter/main.py:**

```python
# ============================================
# PASO 1: Almacenar sesión de usuario en Redis
# ============================================
print("--- Paso 1: Session Store básico ---")

# import json
# import redis

# r = redis.Redis(host="redis", port=6379, decode_responses=True)

# session_data = {"id": 42, "name": "Alice", "role": "admin"}

# Descomenta las siguientes líneas:
# r.setex("session:user:42", 3600, json.dumps(session_data))
# result = json.loads(r.get("session:user:42"))
# print(f"Sesión recuperada: {result}")
# print(f"TTL restante: {r.ttl('session:user:42')} segundos")
```

> ⚠️ **IMPORTANTE**: Los ejercicios NO tienen carpeta `solution/`. El estudiante aprende
> descomentando el código y verificando que funcione correctamente.

#### ❌ NO usar este formato en ejercicios:

```python
# ❌ INCORRECTO - Este formato es para PROYECTOS, no ejercicios
def store_session(user_id: int, data: dict) -> None:
    result = None  # TODO: Implementar
    return result
```

#### ✅ Usar este formato en ejercicios:

```python
# ✅ CORRECTO - Código comentado para descomentar
# Descomenta las siguientes líneas:
# r.setex(f"session:user:{user_id}", 3600, json.dumps(data))
# print(f"Sesión almacenada: {r.get(f'session:user:{user_id}')}")
```

### 3. **Proyecto** (3-proyecto/)

- Proyecto integrador que consolida lo aprendido en la semana
- README.md con instrucciones claras
- Código inicial en `starter/`
- Carpeta `solution/` oculta (en `.gitignore`) solo para instructores
- Criterios de evaluación específicos

#### 📋 Formato de Proyecto (con TODOs)

A diferencia de los ejercicios, el proyecto SÍ usa TODOs para que el estudiante implemente
desde cero:

**starter/main.py:**

```python
# ============================================
# FUNCIÓN: build_leaderboard
# Construye un leaderboard en tiempo real con Sorted Sets
# ============================================

import redis

r = redis.Redis(host="redis", port=6379, decode_responses=True)

def add_score(player: str, score: float, board: str = "global") -> None:
    """
    Agrega o actualiza el puntaje de un jugador en el leaderboard.

    Args:
        player: Nombre del jugador
        score: Puntaje a agregar (incremental)
        board: Nombre del leaderboard (default: "global")
    """
    # TODO: Implementar con ZINCRBY
    # 1. Usar ZINCRBY para incrementar el puntaje del jugador
    # 2. La clave debe seguir el patrón: leaderboard:{board}
    pass


def get_top(n: int = 10, board: str = "global") -> list[dict]:
    """
    Retorna el top N de jugadores con sus puntajes.

    Args:
        n: Cantidad de jugadores a retornar
        board: Nombre del leaderboard

    Returns:
        list[dict]: Lista de dicts con 'player' y 'score', ordenada descendente
    """
    # TODO: Implementar con ZRANGE ... REV WITHSCORES LIMIT
    # 1. Usar ZRANGE con REV=True y withscores=True
    # 2. Limitar a los primeros n resultados
    # 3. Retornar como lista de dicts
    pass
```

> 📁 **Estructura del proyecto:**
>
> ```
> 3-proyecto/
> ├── README.md          # Instrucciones del proyecto
> ├── starter/           # Código inicial para el estudiante
> └── solution/          # ⚠️ OCULTA - Solo para instructores
> ```
>
> La carpeta `solution/` está en `.gitignore` y NO se sube al repositorio público.

### 4. **Recursos** (4-recursos/)

- **ebooks-free/**: Libros gratuitos relevantes sobre Redis y sistemas distribuidos
- **videografia/**: Videos tutoriales complementarios
- **webgrafia/**: Documentación oficial, artículos y referencias

### 5. **Glosario** (5-glosario/)

- Términos técnicos de Redis ordenados alfabéticamente
- Definiciones claras con ejemplos de comandos
- Comparaciones con conceptos de bases de datos relacionales cuando aplique

---

## 📝 Convenciones de Código

### Nomenclatura de Claves Redis

```bash
# ✅ BIEN - patrón objeto:id:campo
SET user:42:email "alice@example.com"
SET user:42:score 1500
HSET user:42 name "Alice" email "alice@example.com"

# ✅ BIEN - patrón objeto:tipo:identificador
SADD followers:user:42 100 101 102
ZADD leaderboard:global 1500 "alice"
LPUSH queue:emails:pending "job:123"

# ❌ MAL - sin estructura, difícil de mantener
SET u42email "alice@example.com"
SET USEREMAILALICE "alice@example.com"
```

### Convenciones de Nombres

- **Claves Redis**: `objeto:subtipo:id` en lowercase con `:` como separador
- **Variables Python**: snake_case
- **Constantes Python**: UPPER_SNAKE_CASE
- **Clases Python**: PascalCase
- **Archivos Python**: snake_case.py
- **Idioma**: Inglés para código y claves, español para documentación

### Código Python con redis-py

```python
# ✅ BIEN - usar type hints siempre
import redis
import json
from typing import Any

def get_cached_user(r: redis.Redis, user_id: int) -> dict | None:
    raw = r.get(f"user:{user_id}:data")
    if raw is None:
        return None
    return json.loads(raw)

# ✅ BIEN - usar async para operaciones I/O en contextos async
import redis.asyncio as aioredis

async def get_cached_user_async(r: aioredis.Redis, user_id: int) -> dict | None:
    raw = await r.get(f"user:{user_id}:data")
    if raw is None:
        return None
    return json.loads(raw)

# ✅ BIEN - pipeline para operaciones en batch
def bulk_set_scores(r: redis.Redis, scores: dict[str, float]) -> None:
    with r.pipeline() as pipe:
        for player, score in scores.items():
            pipe.zadd("leaderboard:global", {player: score})
        pipe.execute()

# ❌ MAL - sin type hints
def get_cached_user(r, user_id):
    return json.loads(r.get(f"user:{user_id}:data"))

# ❌ MAL - N operaciones individuales en lugar de pipeline
def bulk_set_scores_bad(r, scores):
    for player, score in scores.items():
        r.zadd("leaderboard:global", {player: score})  # N round-trips
```

---

## 🛠️ Stack Tecnológico

| Herramienta    | Versión | Propósito                         |
| -------------- | ------- | --------------------------------- |
| Redis          | 8.x     | Motor de base de datos en memoria |
| redis-py       | 5.2.1   | Cliente Python (sync y async)     |
| Python         | 3.13    | Lenguaje de integración           |
| fakeredis      | 2.35.1  | Redis en memoria para testing     |
| pytest         | 8.3.5   | Testing                           |
| pytest-asyncio | 0.24.0  | Testing async                     |
| Docker         | 27.5+   | Containerización                  |
| Docker Compose | 2.32+   | Orquestación                      |
| RedisInsight   | 2.58    | GUI para exploración y monitoreo  |

---

## 🧪 Testing

El bootcamp enseña testing de operaciones Redis con **pytest** y **fakeredis**.

### Estructura de Tests

```python
# tests/test_leaderboard.py
import pytest
import fakeredis
from src.leaderboard import add_score, get_top

@pytest.fixture
def r():
    """Redis fake en memoria para tests aislados."""
    return fakeredis.FakeRedis(decode_responses=True)

def test_add_score_creates_entry(r: fakeredis.FakeRedis) -> None:
    add_score(r, "alice", 100.0)
    assert r.zscore("leaderboard:global", "alice") == 100.0

def test_get_top_returns_sorted_desc(r: fakeredis.FakeRedis) -> None:
    add_score(r, "alice", 300.0)
    add_score(r, "bob", 100.0)
    add_score(r, "carol", 500.0)

    top = get_top(r, n=3)
    assert top[0]["player"] == "carol"
    assert top[0]["score"] == 500.0
    assert top[1]["player"] == "alice"

def test_get_top_respects_limit(r: fakeredis.FakeRedis) -> None:
    for i in range(10):
        add_score(r, f"player:{i}", float(i * 10))
    assert len(get_top(r, n=3)) == 3
```

### Testing Async

```python
# tests/test_cache.py
import pytest
import fakeredis.aioredis
from src.cache import get_cached_user, set_cached_user

@pytest.fixture
async def ar():
    return fakeredis.aioredis.FakeRedis(decode_responses=True)

@pytest.mark.asyncio
async def test_cache_miss_returns_none(ar) -> None:
    result = await get_cached_user(ar, user_id=999)
    assert result is None

@pytest.mark.asyncio
async def test_cache_hit_returns_data(ar) -> None:
    user = {"id": 1, "name": "Alice"}
    await set_cached_user(ar, user_id=1, data=user, ttl=60)
    result = await get_cached_user(ar, user_id=1)
    assert result == user
```

---

## 📖 Documentación

### README.md de Semana

Debe incluir:

1. **Título y descripción**
2. **🎯 Objetivos de aprendizaje**
3. **📚 Requisitos previos**
4. **🗂️ Estructura de la semana**
5. **📝 Contenidos** (con enlaces a teoría/prácticas)
6. **⏱️ Distribución del tiempo** (8 horas)
7. **📌 Entregables**
8. **🔗 Navegación** (anterior/siguiente semana)

### Archivos de Teoría

```markdown
# Título del Tema

## 🎯 Objetivos

- Objetivo 1
- Objetivo 2

## 📋 Contenido

### 1. Introducción

### 2. Conceptos Clave

### 3. Comandos Esenciales

### 4. Ejemplos Prácticos

### 5. Casos de Uso del Mundo Real

## 📚 Recursos Adicionales

## ✅ Checklist de Verificación
```

---

## 🎨 Recursos Visuales y Estándares de Diseño

### Formato de Assets

- ✅ **Preferir SVG** para todos los diagramas, iconos y gráficos
- ❌ **NO usar ASCII art** para diagramas o visualizaciones
- ✅ Usar PNG/JPG solo para screenshots o fotografías
- ✅ Optimizar imágenes antes de incluirlas

### Criterio para Assets SVG por Semana

Los assets SVG en `0-assets/` de cada semana tienen un propósito educativo específico:

- ✅ **Apoyo visual para comprensión de estructuras de datos Redis**
- ✅ **Diagramas de arquitectura** (flujo Pub/Sub, topología Cluster, Sentinel failover)
- ✅ **Visualización de patrones** (caching flow, rate limiting, distributed lock)
- ✅ **Headers de semana** para identificación visual

**Reglas de vinculación:**

1. Todo SVG debe estar **vinculado en al menos un archivo** de teoría o práctica
2. Usar sintaxis markdown: `![Descripción](../0-assets/nombre.svg)`
3. Incluir texto alternativo descriptivo para accesibilidad
4. Nombrar archivos descriptivamente: `sorted-set-structure.svg`, `pubsub-flow.svg`

```markdown
<!-- Ejemplo de vinculación correcta en teoría -->

## Flujo Pub/Sub en Redis

![Diagrama del flujo de mensajes Publisher → Channel → Subscribers](../0-assets/pubsub-flow.svg)

Como se observa en el diagrama, el publisher envía mensajes al channel sin conocer
cuántos subscribers hay...
```

### Tema Visual

- 🌙 **Tema dark** para todos los assets visuales
- ❌ **Sin degradés** (gradients) en diseños
- ✅ Colores sólidos y contrastes claros
- ✅ Paleta consistente basada en rojo Redis (#DC382D)

### Tipografía

- ✅ **Fuentes sans-serif** exclusivamente
- ✅ Recomendadas: Inter, Roboto, Open Sans, System UI
- ❌ **NO usar fuentes serif** (Times, Georgia, etc.)
- ✅ Mantener jerarquía visual clara

---

## 🌐 Idioma y Nomenclatura

### Código y Claves Redis

- ✅ **Claves Redis y código en inglés** (variables, funciones, clases, key patterns)
- ✅ **Comentarios de código en inglés**
- ✅ Usar términos técnicos estándar de la industria

```python
# ✅ CORRECTO - inglés
async def get_rate_limit_count(r: aioredis.Redis, user_id: int, window: int) -> int:
    # Fetch current request count for user within sliding window
    key = f"rate_limit:user:{user_id}:{window}"
    return int(await r.get(key) or 0)

# ❌ INCORRECTO - español en código
async def obtener_conteo_limite(r, id_usuario: int, ventana: int) -> int:
    # Obtener conteo actual de solicitudes del usuario
    clave = f"limite_tasa:usuario:{id_usuario}:{ventana}"
    return int(await r.get(clave) or 0)
```

### Documentación

- ✅ **Documentación en español** (READMEs, teoría, guías)
- ✅ Explicaciones y tutoriales en español
- ✅ Comentarios educativos en español cuando expliquen conceptos

```python
# ✅ CORRECTO - código en inglés, explicación en español
def sliding_window_rate_limit(r: redis.Redis, user_id: int, max_requests: int) -> bool:
    # En Redis, usamos un Sorted Set donde el score es el timestamp Unix
    # Esto nos permite eliminar entradas antiguas con ZREMRANGEBYSCORE
    now = time.time()
    window_start = now - 60  # ventana de 60 segundos
    key = f"rate_limit:user:{user_id}"

    with r.pipeline() as pipe:
        pipe.zremrangebyscore(key, 0, window_start)
        pipe.zadd(key, {str(now): now})
        pipe.zcard(key)
        pipe.expire(key, 60)
        results = pipe.execute()

    return results[2] <= max_requests
```

---

## 🔐 Mejores Prácticas

### Código Limpio

- Nombres de claves Redis descriptivos y con namespace consistente
- Funciones pequeñas con una sola responsabilidad
- Siempre especificar TTL en claves que no deben crecer indefinidamente
- Usar pipelines cuando se ejecuten múltiples comandos relacionados
- Preferir estructuras de datos apropiadas (Hash vs String serializado)

### Seguridad

- ✅ Usar `requirepass` en todos los entornos (dev, staging, prod)
- ✅ Configurar `bind` para restringir acceso por IP
- ✅ Usar ACLs en producción (Redis 6+): `ACL SETUSER`
- ✅ Habilitar TLS para tráfico en tránsito en producción
- ✅ Deshabilitar comandos peligrosos: `rename-command FLUSHALL ""`
- ✅ Nunca exponer el puerto 6379 directamente a internet
- ✅ Validar y sanitizar todos los inputs antes de construir claves Redis

```python
# ✅ CORRECTO - validar input antes de construir clave
def get_user_session(r: redis.Redis, user_id: str) -> dict | None:
    if not user_id.isalnum():  # Previene key injection
        raise ValueError(f"Invalid user_id format: {user_id}")
    raw = r.get(f"session:user:{user_id}")
    return json.loads(raw) if raw else None
```

### Rendimiento

- Usar `SCAN` en lugar de `KEYS *` en producción (nunca bloquea el servidor)
- Usar pipelines para reducir round-trips de red
- Configurar `maxmemory` y política de eviction apropiada
- Monitorear `slowlog` para detectar comandos lentos
- Usar `OBJECT ENCODING` para entender cómo Redis almacena internamente
- Lazy expiration: `OBJECT IDLETIME` para claves sin uso

---

## 📊 Evaluación

Cada semana incluye **tres tipos de evidencias**:

1. **Conocimiento 🧠** (30%): Cuestionarios sobre comandos Redis y conceptos
2. **Desempeño 💪** (40%): Ejercicios prácticos en redis-cli y Python
3. **Producto 📦** (30%): Proyecto entregable funcional

### Criterios de Aprobación

- Mínimo **70%** en cada tipo de evidencia
- Entrega puntual de proyectos
- Código funcional y bien documentado
- Tests pasando con fakeredis (semanas 9-12)

---

## 🚀 Metodología de Aprendizaje

### Estrategias Didácticas

- **Aprendizaje Basado en Proyectos (ABP)**: Proyectos semanales integradores
- **Práctica Deliberada**: Ejercicios incrementales con redis-cli y Python
- **Redis Challenges**: Problemas del mundo real (caching, messaging, leaderboards)
- **Code Review**: Revisión de código entre estudiantes
- **Live Coding**: Sesiones en vivo de implementación de patrones

### Distribución del Tiempo (8h/semana)

- **Teoría**: 2 horas
- **Prácticas**: 3.5 horas
- **Proyecto**: 2.5 horas

---

## 🤖 Instrucciones para Copilot

Cuando trabajes en este proyecto:

### Límites de Respuesta

1. **Divide respuestas largas**
   - ❌ **NUNCA generar respuestas que superen los límites de tokens**
   - ✅ **SIEMPRE dividir contenido extenso en múltiples entregas**
   - ✅ Crear contenido por secciones, esperar confirmación del usuario
   - ✅ Priorizar calidad sobre cantidad en cada entrega
   - Razón: Evitar pérdida de contenido y garantizar completitud

2. **Estrategia de División**
   - Para semanas completas: dividir por carpetas (teoria → practicas → proyecto)
   - Para archivos grandes: dividir por secciones lógicas
   - Siempre indicar claramente qué parte se entrega y qué falta
   - Esperar confirmación del usuario antes de continuar

### Entorno de Desarrollo con Docker

- ✅ **USAR Docker** para ejecutar Redis, nunca instalar Redis localmente
- ✅ **docker compose** para orquestar Redis + aplicación Python + RedisInsight
- ✅ Crear archivos `.env` para configuración de conexión
- Estructura recomendada para proyectos:

  ```
  proyecto/
  ├── docker-compose.yml    # Redis + app + RedisInsight
  ├── Dockerfile            # Imagen de la aplicación Python
  ├── redis.conf            # Configuración personalizada de Redis
  ├── .env.example          # Variables de entorno (template)
  ├── .env                  # Variables de entorno (ignorado en git)
  └── src/                  # Código fuente Python
  ```

- Comandos esenciales:

  ```bash
  # Levantar Redis + app
  docker compose up --build

  # Conectar al redis-cli dentro del contenedor
  docker compose exec redis redis-cli

  # Ver logs de Redis
  docker compose logs -f redis

  # Detener y limpiar
  docker compose down -v
  ```

- **docker-compose.yml** de referencia:

  ```yaml
  services:
    redis:
      image: redis:8-alpine
      ports:
        - "6379:6379"
      volumes:
        - redis_data:/data
        - ./redis.conf:/usr/local/etc/redis/redis.conf
      command: redis-server /usr/local/etc/redis/redis.conf

    app:
      build: .
      depends_on:
        - redis
      environment:
        - REDIS_URL=redis://redis:6379

    redisinsight:
      image: redis/redisinsight:2.58
      ports:
        - "5540:5540"
      depends_on:
        - redis

  volumes:
    redis_data:
  ```

### Generación de Código

1. **Usa siempre sintaxis Python moderna (3.13)**
   - Type hints obligatorios en todas las funciones
   - Union types con `|` en lugar de `Union[]`
   - Genéricos nativos (`list[str]`, `dict[str, int]`)
   - f-strings para formateo de claves Redis

2. **Comandos Redis en ejemplos**
   - Incluir siempre la salida esperada de redis-cli en bloques de código
   - Usar `redis-cli` con comentarios explicativos:

   ```bash
   # Almacenar con expiración de 1 hora
   SET session:user:42 '{"name":"Alice"}' EX 3600
   # → OK

   # Verificar TTL restante
   TTL session:user:42
   # → 3599
   ```

3. **Cliente Python redis-py**
   - ✅ Siempre usar `decode_responses=True` para recibir strings
   - ✅ Usar `ConnectionPool` para aplicaciones de producción
   - ✅ Usar `pipeline()` para operaciones en batch:

   ```python
   r = redis.Redis(
       host=os.environ["REDIS_HOST"],
       port=int(os.environ.get("REDIS_PORT", 6379)),
       password=os.environ.get("REDIS_PASSWORD"),
       decode_responses=True,
       socket_connect_timeout=5,
   )
   ```

4. **Testing con fakeredis**
   - ✅ **SIEMPRE usar fakeredis** en tests (nunca conectar a Redis real en tests)
   - ✅ Un fixture de `FakeRedis` por test o por función para tests aislados

5. **Comenta el código de manera educativa**
   - Explica por qué se elige una estructura de datos sobre otra
   - Incluye referencias a la documentación oficial de Redis cuando sea útil
   - Usa comentarios que enseñen, no solo describan
   - Menciona la complejidad algorítmica cuando sea relevante (ej: ZADD es O(log N))

6. **Proporciona ejemplos completos y funcionales**
   - Código que se pueda copiar, ejecutar con Docker y ver resultados
   - Incluye casos de uso realistas (e-commerce, gaming, APIs de producción)
   - Muestra tanto lo que se debe hacer como lo que se debe evitar

### Creación de Contenido

1. **Estructura clara y progresiva**
   - De comandos simples a patrones complejos
   - Cada semana construye sobre la anterior
   - Repetición espaciada de patrones clave entre semanas

2. **Ejemplos del mundo real**
   - Leaderboards de videojuegos con Sorted Sets
   - Session stores con Strings/Hashes y TTL
   - Rate limiting con Sorted Sets o Lua
   - Colas de trabajo con Lists o Streams
   - Pub/Sub para notificaciones en tiempo real
   - Distributed locks con SET NX PX

3. **Enfoque en "por qué Redis"**
   - Siempre explicar por qué Redis es la elección correcta para el caso de uso
   - Comparar con alternativas (base de datos relacional, Kafka, etc.)
   - Explicar las trade-offs (velocidad vs durabilidad, simplicidad vs features)

### Respuestas y Ayuda

1. **Explicaciones claras**
   - Lenguaje simple y directo
   - Analogías útiles (ej: Sorted Set = tabla de clasificación física)
   - Vincular siempre con casos de uso reales

2. **Código comentado**
   - Explicar cada paso importante
   - Destacar por qué se usa una estructura de datos específica
   - Señalar posibles errores comunes (ej: KEYS \* en producción)

3. **Recursos adicionales**
   - Referencias a la documentación oficial: https://redis.io/docs/
   - Redis University: https://university.redis.io/
   - Try Redis interactivo: https://try.redis.io/

---

## 📚 Referencias Oficiales

- **Redis Documentation**: https://redis.io/docs/
- **redis-py Documentation**: https://redis-py.readthedocs.io/
- **Redis Commands Reference**: https://redis.io/commands/
- **Redis University**: https://university.redis.io/
- **fakeredis Documentation**: https://github.com/cunla/fakeredis-py
- **RedisInsight**: https://redis.io/insight/

---

## 🔗 Enlaces Importantes

- **Repositorio**: https://github.com/ergrato-dev/bc-redis
- **Documentación general**: [docs/README.md](docs/README.md)
- **Primera semana**: [bootcamp/week-01-intro_redis_y_strings/README.md](bootcamp/week-01-intro_redis_y_strings/README.md)

---

## ✅ Checklist para Nuevas Semanas

Cuando crees contenido para una nueva semana:

- [ ] Crear estructura de carpetas completa
- [ ] README.md con objetivos y estructura
- [ ] Material teórico en `1-teoria/`
- [ ] Ejercicios prácticos en `2-practicas/` (formato descomentar, NO TODOs)
- [ ] Proyecto integrador en `3-proyecto/` (formato TODOs)
- [ ] Recursos adicionales en `4-recursos/`
- [ ] Glosario de términos Redis en `5-glosario/`
- [ ] Rúbrica de evaluación
- [ ] Verificar coherencia con semanas anteriores
- [ ] Revisar progresión de dificultad
- [ ] Probar todos los comandos redis-cli y código Python de ejemplos
- [ ] Verificar que claves Redis siguen la convención `objeto:subtipo:id`

---

## 💡 Notas Finales

- **Prioridad**: Claridad sobre brevedad
- **Enfoque**: Aprendizaje práctico con redis-cli antes que código Python
- **Objetivo**: Preparar ingenieros que entiendan Redis desde los fundamentos hasta producción
- **Filosofía**: Dominar las estructuras de datos nativas primero; la integración viene después
- **Anti-patrón a evitar**: No tratar Redis como un simple caché; enseñar todo su potencial

---

_Última actualización: Abril 2026_
_Versión: 1.0_
