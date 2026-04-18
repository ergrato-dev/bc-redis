import json
import os

import redis

# Conexión a Redis — decode_responses=True convierte bytes a str automáticamente
r = redis.Redis(
    host=os.environ.get("REDIS_HOST", "redis"),
    port=int(os.environ.get("REDIS_PORT", 6379)),
    password=os.environ.get("REDIS_PASSWORD", "bootcamp2026"),
    decode_responses=True,
)

# ============================================
# PASO 1: Conexión y SET/GET básico
# ============================================
print("--- Paso 1: Conexión y SET/GET ---")

# Descomenta las siguientes líneas:
# print(f"Ping: {r.ping()}")
# r.set("hello", "world")
# print(f"Valor almacenado: {r.get('hello')}")
# print(f"Clave inexistente: {r.get('nonexistent')}")


# ============================================
# PASO 2: Cache de objeto JSON con TTL
# ============================================
print("\n--- Paso 2: Cache JSON con TTL ---")

# user = {"id": 42, "name": "Alice", "email": "alice@example.com"}

# Descomenta las siguientes líneas:
# r.setex("cache:user:42", 300, json.dumps(user))
# if r.exists("cache:user:42"):
#     cached = json.loads(r.get("cache:user:42"))
#     print(f"Cache hit: {cached}")
# print(f"TTL restante: {r.ttl('cache:user:42')} segundos")


# ============================================
# PASO 3: Contadores atómicos
# ============================================
print("\n--- Paso 3: Contadores atómicos ---")

# Limpia el contador antes del ejercicio para resultados predecibles
# r.delete("article:1:views")
# r.delete("product:1:rating")

# Descomenta las siguientes líneas:
# views = r.incr("article:1:views")
# print(f"Vistas después de INCR: {views}")
# r.incrby("article:1:views", 5)
# print(f"Vistas después de INCRBY 5: {r.get('article:1:views')}")
# r.incrbyfloat("product:1:rating", 0.5)
# print(f"Rating después de INCRBYFLOAT 0.5: {r.get('product:1:rating')}")


# ============================================
# PASO 4: Batch MSET/MGET
# ============================================
print("\n--- Paso 4: Batch MSET/MGET ---")

# Descomenta las siguientes líneas:
# r.mset({
#     "user:1:name": "Alice",
#     "user:2:name": "Bob",
#     "user:3:name": "Carol",
# })
# names = r.mget("user:1:name", "user:2:name", "user:99:name")
# print(f"Nombres: {names}")


# ============================================
# PASO 5: SET NX — crear solo si no existe
# ============================================
print("\n--- Paso 5: SET NX ---")

# Limpia antes del ejercicio
# r.delete("registered:emails:alice@example.com")

# Descomenta las siguientes líneas:
# registered = r.set("registered:emails:alice@example.com", "1", nx=True)
# print(f"Registrado: {registered}")
# registered_again = r.set("registered:emails:alice@example.com", "1", nx=True)
# print(f"Registrado otra vez: {registered_again}")
