# Setup sin Docker (Instalación Local)

> ⚠️ Esta opción es para casos donde Docker **no puede** instalarse. Se recomienda
> siempre usar [Docker](./docker.md) para garantizar Redis 8.x y un entorno idéntico
> al de todos los estudiantes.

---

## Requisitos del Sistema

| Sistema Operativo | Soporte |
| ----------------- | ------- |
| Linux (Ubuntu 22.04+, Debian 12+) | ✅ Completo |
| Linux (Fedora 39+, RHEL 9+, Rocky Linux 9+) | ✅ Completo |
| macOS 13+ (Ventura o superior) | ✅ Completo |
| Windows 10/11 con WSL2 | ✅ Via WSL2 |
| Windows nativo (sin WSL2) | ⚠️ Limitado — no recomendado |

---

## 1. Instalar Redis 8.x

### Linux (Ubuntu / Debian)

Redis 8.x no está en los repositorios predeterminados de Ubuntu. Instala desde el repositorio oficial:

```bash
# Instalar dependencias
sudo apt-get update
sudo apt-get install -y lsb-release curl gpg

# Agregar repositorio oficial de Redis
curl -fsSL https://packages.redis.io/gpg | \
    sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/redis-archive-keyring.gpg] \
    https://packages.redis.io/deb $(lsb_release -cs) main" | \
    sudo tee /etc/apt/sources.list.d/redis.list

# Instalar Redis
sudo apt-get update
sudo apt-get install -y redis

# Verificar versión (debe ser 8.x)
redis-server --version
# Redis server v=8.x.x ...

# Iniciar Redis
sudo systemctl start redis
sudo systemctl enable redis  # iniciar en boot

# Verificar que responde
redis-cli PING
# → PONG
```

### Linux (Fedora / RHEL / Rocky Linux)

Redis 8.x no está en los repositorios base de Fedora. Instala desde el repositorio oficial:

```bash
# Instalar dependencias
sudo dnf install -y curl gpg

# Agregar repositorio oficial de Redis
curl -fsSL https://packages.redis.io/gpg | sudo gpg --dearmor -o /usr/share/keyrings/redis-archive-keyring.gpg

sudo tee /etc/yum.repos.d/redis.repo << 'EOF'
[redis]
name=Redis
baseurl=https://packages.redis.io/rpm/rhel9/$basearch
enabled=1
gpgcheck=1
gpgkey=https://packages.redis.io/gpg
EOF

# Instalar Redis
sudo dnf install -y redis

# Verificar versión (debe ser 8.x)
redis-server --version
# Redis server v=8.x.x ...

# Iniciar Redis
sudo systemctl start redis
sudo systemctl enable redis  # iniciar en boot

# Verificar que responde
redis-cli PING
# → PONG
```

> **Fedora 40+**: el paquete `redis` en los repos de Fedora puede ofrecer Redis 7.x.
> Si necesitas exactamente Redis 8.x, usa el repositorio oficial de arriba.

### macOS

```bash
# Instalar Homebrew si no lo tienes
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Instalar Redis 8
brew install redis

# Iniciar Redis como servicio
brew services start redis

# Verificar versión
redis-server --version
# Redis server v=8.x.x ...

# Verificar que responde
redis-cli PING
# → PONG
```

### Windows (WSL2 — recomendado)

```powershell
# 1. Habilitar WSL2 (PowerShell como administrador)
wsl --install

# 2. Reiniciar el equipo

# 3. Abrir Ubuntu desde el menú de inicio

# 4. Seguir las instrucciones de Linux arriba dentro de WSL2
```

---

## 2. Configurar Redis

### Archivo de configuración

El archivo por defecto está en `/etc/redis/redis.conf` (Linux) o en la ruta que muestra `redis-server --version`.

Crea una configuración personalizada para el bootcamp:

```bash
# Crear directorio para la configuración del bootcamp
mkdir -p ~/bootcamp-redis

# Crear redis.conf
cat > ~/bootcamp-redis/redis.conf << 'EOF'
bind 127.0.0.1
port 6379
protected-mode yes
requirepass bootcamp2026
maxmemory 256mb
maxmemory-policy allkeys-lru
save 900 1
save 300 10
save 60 10000
dbfilename dump.rdb
dir ~/bootcamp-redis/data
loglevel notice
logfile ~/bootcamp-redis/redis.log
slowlog-log-slower-than 10000
slowlog-max-len 128
EOF

mkdir -p ~/bootcamp-redis/data
```

### Iniciar Redis con la configuración del bootcamp

```bash
# Iniciar con la configuración personalizada
redis-server ~/bootcamp-redis/redis.conf

# En otra terminal, verificar conexión con contraseña
redis-cli -a bootcamp2026 PING
# → PONG
```

### Iniciar Redis automáticamente (opcional)

**Linux (systemd):**

```bash
# Crear servicio systemd personalizado
sudo tee /etc/systemd/system/redis-bootcamp.service << 'EOF'
[Unit]
Description=Redis Bootcamp
After=network.target

[Service]
ExecStart=/usr/bin/redis-server /home/TU_USUARIO/bootcamp-redis/redis.conf
Restart=always
User=TU_USUARIO

[Install]
WantedBy=multi-user.target
EOF

# Reemplaza TU_USUARIO con tu nombre de usuario real
sudo sed -i "s/TU_USUARIO/$USER/g" /etc/systemd/system/redis-bootcamp.service

sudo systemctl daemon-reload
sudo systemctl enable redis-bootcamp
sudo systemctl start redis-bootcamp
```

**macOS (launchd):**

```bash
# Redis ya se inicia con brew services start redis
# Para usar la configuración personalizada:
brew services stop redis
redis-server ~/bootcamp-redis/redis.conf --daemonize yes
```

---

## 3. Instalar Python 3.13

### Linux

```bash
# Ubuntu 24.04 incluye Python 3.12; para 3.13 instala con deadsnakes PPA
python3 --version

# Ubuntu/Debian — instala Python 3.13 con deadsnakes PPA
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
sudo apt-get install -y python3.13 python3.13-venv python3.13-dev

# Fedora 40+ — Python 3.13 ya está disponible en los repositorios base
sudo dnf install -y python3.13 python3.13-devel

# Crear alias (opcional)
echo 'alias python=python3.13' >> ~/.bashrc
source ~/.bashrc
```

### macOS

```bash
brew install python@3.13

# Verificar
python3.13 --version
```

---

## 4. Configurar Entorno Virtual Python

Cada semana/proyecto del bootcamp requiere un entorno virtual aislado:

```bash
# Ir a la carpeta del proyecto (ej: práctica 02)
cd bootcamp/week-01-intro_redis_y_strings/2-practicas/practica-02-strings

# Crear entorno virtual
python3.13 -m venv .venv

# Activar entorno virtual
source .venv/bin/activate      # Linux / macOS
# .venv\Scripts\activate       # Windows (PowerShell)

# Instalar dependencias
pip install -r requirements.txt

# Verificar
python -c "import redis; print(redis.__version__)"
# → 5.2.1

# Ejecutar el ejercicio
python starter/main.py
```

### Variables de entorno (sin Docker)

Sin Docker Compose no hay inyección automática de variables de entorno. Configúralas manualmente:

```bash
# Opción 1: exportar en la terminal actual
export REDIS_HOST=127.0.0.1
export REDIS_PORT=6379
export REDIS_PASSWORD=bootcamp2026

# Opción 2: crear archivo .env y cargar con python-dotenv
# Agrega python-dotenv==1.1.0 a requirements.txt
# En tu código:
# from dotenv import load_dotenv
# load_dotenv()
```

---

## 5. Instalar RedisInsight (opcional)

Sin Docker, RedisInsight se instala como aplicación de escritorio:

1. Descarga desde [https://redis.io/insight/](https://redis.io/insight/)
2. Instala la versión para tu sistema operativo
3. Abre RedisInsight y conecta:
   - **Host**: `127.0.0.1`
   - **Port**: `6379`
   - **Password**: `bootcamp2026`

---

## 6. Diferencias con el Entorno Docker

Al trabajar sin Docker, ten en cuenta estas diferencias:

| Aspecto | Docker | Local |
| ------- | ------ | ----- |
| Host de Redis | `redis` (nombre del servicio) | `127.0.0.1` o `localhost` |
| Iniciar Redis | `docker compose up -d` | `redis-server redis.conf` |
| redis-cli | `docker compose exec redis redis-cli` | `redis-cli` directo |
| Ejecutar Python | `docker compose exec app python` | `python` (con venv activo) |
| Variables de entorno | definidas en `docker-compose.yml` | exportar manualmente |
| Limpiar datos | `docker compose down -v` | `redis-cli FLUSHALL` o borrar dump.rdb |

---

## 7. Verificación Final del Entorno

Ejecuta este script de verificación para confirmar que todo funciona:

```bash
python3 - << 'EOF'
import redis
import sys

r = redis.Redis(
    host="127.0.0.1",
    port=6379,
    password="bootcamp2026",
    decode_responses=True,
)

try:
    pong = r.ping()
    print(f"✓ Conexión a Redis: {pong}")

    r.set("bootcamp:test", "hello")
    value = r.get("bootcamp:test")
    print(f"✓ SET/GET funciona: {value}")

    r.delete("bootcamp:test")
    print(f"✓ Redis versión: {r.info('server')['redis_version']}")
    print("\n¡Entorno listo para el bootcamp!")

except redis.AuthenticationError:
    print("✗ Error: contraseña incorrecta. Verifica requirepass en redis.conf")
    sys.exit(1)
except redis.ConnectionError:
    print("✗ Error: no se puede conectar a Redis. ¿Está corriendo redis-server?")
    sys.exit(1)
EOF
```

---

## Solución de Problemas

### `redis-cli: command not found`

```bash
# Ubuntu / Debian
sudo apt-get install -y redis-tools

# Fedora / RHEL / Rocky Linux
sudo dnf install -y redis

# macOS
brew install redis
```

### `WRONGPASS invalid username-password pair`

Verifica que `requirepass` en `redis.conf` coincide con la contraseña que usas:

```bash
grep requirepass ~/bootcamp-redis/redis.conf
# requirepass bootcamp2026
```

### `Address already in use :6379`

Otro proceso ocupa el puerto 6379:

```bash
# Encontrar el proceso
sudo lsof -i :6379

# Detener Redis del sistema si está corriendo
sudo systemctl stop redis
```

### Python no encuentra el módulo `redis`

El entorno virtual no está activado:

```bash
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Siguientes Pasos

- [Semana 01 — Introducción a Redis y Strings](../../bootcamp/week-01-intro_redis_y_strings/README.md)
- [Volver a opciones de setup](./README.md)
