---
applyTo: "**/docker-compose.yml"
---

# Instrucciones para docker-compose.yml

## Estructura estándar del bootcamp

Todo `docker-compose.yml` del bootcamp sigue este patrón:

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
      - REDIS_HOST=redis
      - REDIS_PORT=6379
      - REDIS_PASSWORD=bootcamp2026
    volumes:
      - .:/app
    working_dir: /app

  redisinsight:
    image: redis/redisinsight:2.58
    ports:
      - "5540:5540"
    depends_on:
      - redis

volumes:
  redis_data:
```

## Reglas

- Imagen Redis: siempre `redis:8-alpine` (versión exacta del bootcamp)
- RedisInsight: siempre `redis/redisinsight:2.58`
- Password: `bootcamp2026` en entorno de desarrollo
- El servicio `app` NUNCA expone puertos al host (solo se accede vía `docker compose exec`)
- Usar `depends_on` para orden de arranque
- Volumen nombrado para datos Redis (no bind mount de directorio)
- Las prácticas solo de CLI (sin Python) pueden omitir el servicio `app`

## redis.conf mínimo

```conf
bind 0.0.0.0
port 6379
protected-mode no
requirepass bootcamp2026
maxmemory 256mb
maxmemory-policy allkeys-lru
loglevel notice
logfile ""
```
