# Setup con Docker

Esta es la forma **recomendada** de trabajar en el bootcamp. Garantiza Redis 8.x,
RedisInsight y Python 3.13 en cualquier sistema operativo sin instalar nada en el host.

---

## Requisitos Previos

| Herramienta | Versión mínima | Verificar |
| ----------- | -------------- | --------- |
| Docker | 27.5+ | `docker --version` |
| Docker Compose | 2.32+ | `docker compose version` |
| Git | cualquiera | `git --version` |

Si no tienes Docker instalado, sigue primero el
[Bootcamp Docker](https://github.com/ergrato-dev/bc-docker).

---

## Instalación de Docker por Sistema Operativo

### Linux (Ubuntu / Debian)

```bash
# Desinstalar versiones anteriores
sudo apt-get remove docker docker-engine docker.io containerd runc

# Instalar dependencias
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg

# Agregar clave GPG oficial de Docker
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | \
    sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Agregar repositorio de Docker
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] \
  https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Instalar Docker Engine + Compose
sudo apt-get update
sudo apt-get install -y docker-ce docker-ce-cli containerd.io \
    docker-buildx-plugin docker-compose-plugin

# Agregar usuario al grupo docker (sin necesidad de sudo)
sudo usermod -aG docker $USER
newgrp docker

# Verificar
docker --version
docker compose version
```

### macOS

Instala [Docker Desktop](https://www.docker.com/products/docker-desktop/) desde el sitio oficial.

```bash
# Verificar instalación
docker --version
docker compose version
```

### Windows

Instala [Docker Desktop](https://www.docker.com/products/docker-desktop/) con WSL2 backend.

> Asegúrate de que WSL2 esté habilitado: `wsl --install` en PowerShell como administrador.

---

## Entorno Base del Bootcamp

Cada semana tiene su propio `docker-compose.yml`. El patrón estándar incluye tres servicios:

```yaml
services:
  redis:
    image: redis:8-alpine          # Redis 8 ligero
    ports:
      - "6379:6379"
    volumes:
      - redis_data:/data
      - ./redis.conf:/usr/local/etc/redis/redis.conf
    command: redis-server /usr/local/etc/redis/redis.conf

  app:
    build: .                       # Python 3.13 con redis-py
    depends_on:
      - redis
    environment:
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - REDIS_PASSWORD=bootcamp2026
    volumes:
      - .:/app

  redisinsight:
    image: redis/redisinsight:2.58 # GUI web para explorar Redis
    ports:
      - "5540:5540"
    depends_on:
      - redis

volumes:
  redis_data:
```

---

## Comandos Esenciales

### Ciclo de vida de una semana

```bash
# 1. Ir a la carpeta de la semana
cd bootcamp/week-01-intro_redis_y_strings/2-practicas/practica-01-primeros-pasos

# 2. Levantar todos los servicios
docker compose up -d

# 3. Verificar que están corriendo
docker compose ps

# 4. Conectarse a redis-cli
docker compose exec redis redis-cli -a bootcamp2026

# 5. Ver logs de Redis en tiempo real
docker compose logs -f redis

# 6. Ejecutar código Python
docker compose exec app python starter/main.py

# 7. Ejecutar tests
docker compose exec app python -m pytest starter/tests/ -v

# 8. Al terminar: detener sin borrar datos
docker compose down

# 9. Detener Y eliminar todos los datos (reset completo)
docker compose down -v
```

### Depuración

```bash
# Ver todos los contenedores (incluyendo detenidos)
docker ps -a

# Inspeccionar un contenedor específico
docker inspect redis-bootcamp

# Ver uso de recursos en tiempo real
docker stats

# Acceder a la shell del contenedor Redis
docker compose exec redis sh

# Acceder a la shell del contenedor Python
docker compose exec app bash

# Reiniciar solo Redis sin recrear el contenedor
docker compose restart redis

# Reconstruir la imagen Python (cuando cambias requirements.txt)
docker compose up --build app
```

---

## Configuración `redis.conf` Estándar

Todos los entornos del bootcamp usan esta configuración base:

```conf
# Networking
bind 0.0.0.0
port 6379
protected-mode no

# Autenticación (cambiar en producción)
requirepass bootcamp2026

# Memoria
maxmemory 256mb
maxmemory-policy allkeys-lru

# Persistencia RDB
save 900 1
save 300 10
save 60 10000
dbfilename dump.rdb
dir /data

# Logging
loglevel notice
logfile ""

# Slow log — registra comandos > 10ms
slowlog-log-slower-than 10000
slowlog-max-len 128
```

---

## RedisInsight

RedisInsight es la interfaz gráfica oficial de Redis. Se incluye en todos los entornos Docker del bootcamp.

**Acceso**: [http://localhost:5540](http://localhost:5540)

**Conexión inicial**:

1. Abre http://localhost:5540 en el navegador
2. Haz clic en "Add Redis database"
3. Completa:
   - **Host**: `redis` (nombre del servicio en Docker)
   - **Port**: `6379`
   - **Password**: `bootcamp2026`
4. Haz clic en "Add Redis Database"

**Funcionalidades útiles**:

- **Browser**: explora claves con filtros por tipo y patrón
- **CLI**: ejecuta comandos con autocompletado
- **Profiler**: monitorea comandos en tiempo real
- **Memory Analyzer**: detecta claves que consumen más memoria
- **Slow Log**: inspecciona comandos lentos

---

## Solución de Problemas Comunes

### Puerto 6379 ocupado

```bash
# Encontrar el proceso que usa el puerto
sudo lsof -i :6379

# Detener Redis local si está corriendo
sudo systemctl stop redis   # Linux
brew services stop redis     # macOS
```

### Contenedor no inicia

```bash
# Ver el error completo
docker compose logs redis

# Error común: permiso denegado en el volumen
sudo chown -R $USER:$USER ./data
```

### redis-cli no puede autenticarse

```bash
# Verificar que la contraseña coincide con redis.conf
docker compose exec redis redis-cli -a bootcamp2026 PING

# Si da "WRONGPASS", revisar redis.conf → requirepass
docker compose exec redis cat /usr/local/etc/redis/redis.conf | grep requirepass
```

### RedisInsight no conecta a Redis

En RedisInsight, usar **`redis`** como host (no `localhost` ni `127.0.0.1`), porque ambos contenedores están en la red interna de Docker Compose.

---

## Siguientes Pasos

- [Semana 01 — Introducción a Redis y Strings](../../bootcamp/week-01-intro_redis_y_strings/README.md)
- [Setup sin Docker (alternativa)](./local.md)
