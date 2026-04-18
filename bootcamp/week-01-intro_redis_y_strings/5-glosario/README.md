# Glosario — Semana 01

Términos clave introducidos en la Semana 01. Ordenados alfabéticamente.

---

## A

**AOF (Append-Only File)**
Mecanismo de persistencia de Redis que registra cada operación de escritura en un archivo de log. Permite recuperar todos los datos tras un reinicio. Ver también: RDB.

**Atomicidad**
Propiedad de una operación que se ejecuta completamente o no se ejecuta en absoluto, sin que ningún otro cliente pueda observar un estado intermedio. En Redis, todas las operaciones individuales son atómicas por diseño (single-threaded).

---

## C

**Cache**
Almacenamiento temporal de datos costosos de calcular o recuperar, con el objetivo de servirlos más rápido en accesos futuros. Redis es la herramienta de cache más usada en la industria.

**Cache hit**
Cuando los datos solicitados están disponibles en el cache y se sirven desde Redis sin consultar la fuente de verdad.

**Cache miss**
Cuando los datos solicitados NO están en el cache. Se debe consultar la fuente de verdad (ej: PostgreSQL) y luego guardar el resultado en Redis.

**Cache invalidation**
Proceso de eliminar o expirar una entrada del cache cuando los datos subyacentes cambian. Uno de los problemas más difíciles en sistemas distribuidos.

---

## D

**decode_responses**
Parámetro de redis-py que convierte automáticamente las respuestas de bytes a strings Python. Siempre usar `decode_responses=True` salvo que necesites trabajar con datos binarios.

---

## E

**Eviction**
Proceso automático por el cual Redis elimina claves para liberar memoria cuando se alcanza `maxmemory`. La política de eviction configura qué claves eliminar primero (ej: `allkeys-lru`).

**EXISTS**
Comando Redis que verifica si una clave existe. Retorna `1` (existe) o `0` (no existe). Usar EXISTS en lugar de GET cuando solo necesitas verificar existencia.

---

## I

**In-memory**
Característica de Redis de almacenar todos los datos en RAM. Esto le da latencia sub-milisegundo, pero limita la capacidad total y requiere estrategias de persistencia.

**INCR**
Comando Redis que incrementa el valor entero de una clave en 1, de forma atómica. Si la clave no existe, la crea con valor 0 y luego incrementa a 1. Complejidad O(1).

---

## K

**Key (clave)**
Identificador único para un valor en Redis. Siempre es un string. Convención de este bootcamp: `objeto:subtipo:id` en lowercase (ej: `user:42:name`, `cache:article:5`).

---

## L

**LRU (Least Recently Used)**
Política de eviction que elimina primero las claves que llevan más tiempo sin ser accedidas. Es la política más común en sistemas de cache.

---

## M

**maxmemory**
Directiva de `redis.conf` que limita la memoria máxima que puede usar Redis. Cuando se alcanza, la política de eviction decide qué claves eliminar.

**MGET / MSET**
Comandos para leer (MGET) o escribir (MSET) múltiples claves en una sola operación de red. Reducen los round-trips y mejoran el rendimiento en operaciones batch.

---

## N

**Namespace**
Prefijo en el nombre de la clave que agrupa claves relacionadas. Ej: `cache:article:*` agrupa todos los artículos en cache. Redis no tiene namespaces nativos, se simulan con convenciones de nombre.

**nil**
Valor especial que retorna Redis cuando una clave no existe. En redis-py se mapea a `None` en Python.

---

## P

**Persistencia**
Mecanismo para guardar los datos de Redis en disco y recuperarlos tras un reinicio. Redis ofrece dos mecanismos: RDB (snapshots) y AOF (log de operaciones).

**Pipeline**
Mecanismo de redis-py para enviar múltiples comandos al servidor en una sola llamada de red, sin esperar respuestas intermedias. Reduce drásticamente la latencia en operaciones batch.

**PING**
Comando de diagnóstico que verifica que Redis responde. Retorna `PONG`. Equivalente al "Hello, World!" de Redis.

---

## R

**RDB (Redis Database Backup)**
Mecanismo de persistencia que toma snapshots periódicos del dataset completo. Es más compacto que AOF pero puede perder las últimas operaciones si Redis cae entre snapshots.

**redis-cli**
Cliente de línea de comandos oficial de Redis. Permite ejecutar cualquier comando directamente desde la terminal.

**redis-py**
Cliente Python oficial para Redis. Proporciona una API síncrona y asíncrona para todos los comandos Redis.

**requirepass**
Directiva de `redis.conf` que establece la contraseña de autenticación. Siempre configurar en todos los entornos, incluyendo desarrollo.

---

## S

**SCAN**
Comando para iterar claves de forma incremental y no bloqueante. La alternativa segura a `KEYS *` en producción. Usa un cursor que se va actualizando en cada llamada.

**SET NX (Set If Not Exists)**
Variante de SET que solo crea la clave si no existe. Útil para distributed locks simples y operaciones idempotentes.

**SETEX**
Comando que combina SET + EXPIRE en una operación atómica. Equivalente moderno: `SET key value EX seconds`.

**Single-threaded**
Característica del motor de comandos de Redis: procesa un comando a la vez. Garantiza atomicidad de todas las operaciones sin necesidad de locks explícitos.

**String**
La estructura de datos más básica de Redis. Puede almacenar texto, números enteros, decimales o datos binarios. Tamaño máximo: 512 MB por clave.

---

## T

**TTL (Time To Live)**
Tiempo de vida restante de una clave en segundos. TTL = -1 significa sin expiración. TTL = -2 significa que la clave no existe. Se consulta con el comando `TTL key`.

**Throughput**
Número de operaciones que Redis puede procesar por segundo. Redis puede manejar hasta ~1 millón de operaciones/segundo en hardware estándar.

---

## V

**Volatile**
Clave que tiene una expiración configurada (TTL > 0). Las políticas de eviction `volatile-*` solo afectan a claves volátiles.
