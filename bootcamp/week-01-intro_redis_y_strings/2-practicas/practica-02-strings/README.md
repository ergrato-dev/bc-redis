# Práctica 02 — Strings con Python

## 🎯 Objetivos

- Conectarse a Redis desde Python con redis-py
- Implementar cache con SET/GET y TTL
- Usar contadores atómicos con INCR
- Trabajar con JSON serializado en strings
- Usar MSET/MGET para operaciones en batch

---

## 📚 Requisitos Previos

- Práctica 01 completada
- Teoría [04 — Strings](../../1-teoria/04-strings.md) completada

---

## 🐳 Levantar el Entorno

```bash
docker compose up --build -d
```

Estructura:

```
practica-02-strings/
├── README.md
├── docker-compose.yml
├── Dockerfile
├── redis.conf
├── requirements.txt
└── starter/
    └── main.py        ← descomenta sección por sección
```

---

## 📝 Pasos

### Paso 1: Conectar redis-py y primer SET/GET

Concepto: redis-py es el cliente oficial Python para Redis. Con `decode_responses=True` los valores se devuelven como strings, no como bytes.

```python
import redis
import os

r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    password=os.environ.get("REDIS_PASSWORD", "bootcamp2026"),
    decode_responses=True,
)

r.ping()  # → True
r.set("hello", "world")
print(r.get("hello"))  # → "world"
print(r.get("nonexistent"))  # → None
```

**Abre `starter/main.py`** y descomenta la sección `# PASO 1`.

---

### Paso 2: Cache de objetos JSON con TTL

Concepto: Redis no entiende JSON, pero podemos serializar con `json.dumps()` y deserializar con `json.loads()`. El TTL asegura que el cache se invalide automáticamente.

```python
import json

user = {"id": 42, "name": "Alice", "email": "alice@example.com"}

# Almacenar con TTL de 5 minutos
r.setex("cache:user:42", 300, json.dumps(user))

# Verificar existencia antes de recuperar
if r.exists("cache:user:42"):
    cached = json.loads(r.get("cache:user:42"))
    print(f"Cache hit: {cached}")

print(f"TTL restante: {r.ttl('cache:user:42')} segundos")
```

**Descomenta la sección `# PASO 2` en `starter/main.py`**.

---

### Paso 3: Contadores atómicos

Concepto: INCR es una operación atómica. Aunque 100 clientes ejecuten INCR al mismo tiempo, el contador siempre será correcto. No hay condiciones de carrera.

```python
# INCR crea la clave con valor 0 si no existe, luego incrementa
views = r.incr("article:1:views")
print(f"Vistas: {views}")  # → 1

# Incrementar en N
r.incrby("article:1:views", 5)
print(r.get("article:1:views"))  # → "6"

# Incremento decimal
r.incrbyfloat("product:1:rating", 0.5)
print(r.get("product:1:rating"))  # → "0.5"
```

**Descomenta la sección `# PASO 3` en `starter/main.py`**.

---

### Paso 4: Batch con MSET/MGET

Concepto: MSET y MGET reducen los round-trips de red. En lugar de N operaciones de red, se hace 1.

```python
# MSET: múltiples keys en una sola llamada
r.mset({
    "user:1:name": "Alice",
    "user:2:name": "Bob",
    "user:3:name": "Carol",
})

# MGET: retorna lista con None para claves inexistentes
names = r.mget("user:1:name", "user:2:name", "user:99:name")
print(names)  # → ["Alice", "Bob", None]
```

**Descomenta la sección `# PASO 4` en `starter/main.py`**.

---

### Paso 5: SET NX para flags únicos

Concepto: SET NX (set if not exists) garantiza que una operación solo se ejecuta una vez, incluso con múltiples clientes concurrentes.

```python
# Intentar registrar un email (operación idempotente)
registered = r.set("registered:emails:alice@example.com", "1", nx=True)
print(f"Registrado: {registered}")  # → True (primera vez)

registered_again = r.set("registered:emails:alice@example.com", "1", nx=True)
print(f"Registrado otra vez: {registered_again}")  # → None (ya existía)
```

**Descomenta la sección `# PASO 5` en `starter/main.py`**.

---

## ✅ Verificación

```bash
# Ejecutar el script completo
docker compose exec app python starter/main.py
```

Salida esperada:

```
--- Paso 1: Conexión y SET/GET ---
Ping: True
Valor almacenado: world
Clave inexistente: None

--- Paso 2: Cache JSON con TTL ---
Cache hit: {'id': 42, 'name': 'Alice', 'email': 'alice@example.com'}
TTL restante: 299 segundos

--- Paso 3: Contadores atómicos ---
Vistas después de INCR: 1
Vistas después de INCRBY 5: 6
Rating después de INCRBYFLOAT 0.5: 0.5

--- Paso 4: Batch MSET/MGET ---
Nombres: ['Alice', 'Bob', None]

--- Paso 5: SET NX ---
Registrado: True
Registrado otra vez: None
```

- [ ] Todos los pasos imprimen la salida esperada
- [ ] No hay errores de conexión ni de tipo

---

## 🛑 Detener el Entorno

```bash
docker compose down -v
```
