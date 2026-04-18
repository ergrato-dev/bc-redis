# Práctica 01 — Primeros Pasos con redis-cli

## 🎯 Objetivos

- Levantar Redis con Docker Compose
- Navegar el entorno con redis-cli
- Inspeccionar claves: tipo, TTL y codificación
- Iterar claves de forma segura con SCAN

---

## 📚 Requisitos Previos

- Teoría [01 — ¿Qué es Redis?](../../1-teoria/01-que-es-redis.md) completada
- Teoría [02 — Instalación con Docker](../../1-teoria/02-instalacion-con-docker.md) completada
- Teoría [03 — redis-cli](../../1-teoria/03-redis-cli.md) completada
- Docker y Docker Compose instalados y funcionando

---

## 🐳 Levantar el Entorno

```bash
# Desde la carpeta de esta práctica
docker compose up -d

# Verificar que Redis está corriendo
docker compose ps
```

Estructura del entorno:

```
practica-01-primeros-pasos/
├── README.md          ← este archivo
├── docker-compose.yml ← entorno Docker
├── redis.conf         ← configuración Redis
└── starter/
    └── seed.sh        ← carga datos de prueba
```

---

## 📝 Pasos

### Paso 1: Conectarse a redis-cli

Concepto: redis-cli es el cliente de línea de comandos de Redis. Permite ejecutar cualquier comando directamente.

```bash
# Conectarse dentro del contenedor
docker compose exec redis redis-cli -a bootcamp2026
```

Ejecuta los siguientes comandos y verifica las salidas:

```bash
PING
# → PONG

PING "Redis responde"
# → "Redis responde"

INFO server
# (observa: redis_version, uptime_in_seconds, used_memory_human)
```

**Abre `starter/seed.sh`** y ejecútalo para cargar datos de prueba:

```bash
docker compose exec redis sh /data/seed.sh
```

---

### Paso 2: Explorar bases de datos

Concepto: Redis tiene 16 bases de datos (0-15). Cada una es un namespace aislado.

```bash
# Ver cuántas claves hay en la base de datos actual
DBSIZE
# → (integer) 10  (aproximado, depende del seed)

# Cambiar a base de datos 1 (vacía)
SELECT 1
DBSIZE
# → (integer) 0

# Volver a base de datos 0
SELECT 0
```

---

### Paso 3: Inspeccionar claves con SCAN

Concepto: SCAN itera las claves de forma incremental sin bloquear Redis. Es la alternativa segura a KEYS *.

```bash
# Iteración completa desde cursor 0
SCAN 0
# → 1) "7"         ← nuevo cursor
# → 2) 1) "article:1:views"
#       2) "user:42:name"
#       3) ...

# Continuar con el cursor devuelto
SCAN 7
# → 1) "0"         ← cursor 0 = iteración completa
# → 2) 1) "session:user:1"
#       2) ...

# Filtrar por patrón
SCAN 0 MATCH "user:*"

# Filtrar por tipo
SCAN 0 TYPE string
```

---

### Paso 4: Conocer el tipo y la codificación

Concepto: TYPE muestra la estructura de datos. OBJECT ENCODING muestra cómo Redis la almacena internamente.

```bash
# Tipo de varias claves del seed
TYPE user:42:name
# → string

TYPE article:1:views
# → string

# Codificación interna
OBJECT ENCODING user:42:name
# → "embstr"   (string ≤ 44 bytes)

OBJECT ENCODING article:1:views
# → "int"      (número entero almacenado como entero nativo)

SET long:string "Este es un string muy largo que supera los cuarenta y cuatro bytes exactos"
OBJECT ENCODING long:string
# → "raw"      (string > 44 bytes)
```

---

### Paso 5: Verificar y manipular TTL

Concepto: TTL retorna los segundos de vida restantes. -1 = sin expiración. -2 = clave no existe.

```bash
# Ver TTL de una clave sin expiración
TTL user:42:name
# → (integer) -1

# Añadir expiración de 60 segundos
EXPIRE user:42:name 60
# → (integer) 1

TTL user:42:name
# → (integer) 59

# Espera 5 segundos y vuelve a comprobar
TTL user:42:name
# → (integer) 54

# Eliminar la expiración
PERSIST user:42:name
# → (integer) 1

TTL user:42:name
# → (integer) -1

# Clave que ya venía con TTL del seed
TTL session:user:1
# → (integer) 3540  (aprox)

# Clave que no existe
TTL user:9999:name
# → (integer) -2
```

---

### Paso 6: Consultar métricas del servidor

Concepto: INFO provee telemetría completa del servidor Redis.

```bash
INFO memory
# Observa: used_memory_human, maxmemory_human, maxmemory_policy

INFO keyspace
# → db0:keys=10,expires=2,avg_ttl=3600000

INFO stats
# Observa: total_commands_processed, instantaneous_ops_per_sec
```

---

## ✅ Verificación

Asegúrate de haber podido:

- [ ] Conectarte a redis-cli con autenticación
- [ ] Ejecutar DBSIZE y SELECT 0/1
- [ ] Usar SCAN para listar claves sin KEYS *
- [ ] Usar TYPE y OBJECT ENCODING sobre diferentes claves
- [ ] Usar TTL, EXPIRE y PERSIST
- [ ] Leer la sección de memory de INFO

---

## 🛑 Detener el Entorno

```bash
docker compose down
```
