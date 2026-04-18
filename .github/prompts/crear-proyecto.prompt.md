---
mode: agent
description: Crea el proyecto integrador semanal del bootcamp Redis con TODOs, tests y estructura completa.
---

Crea el proyecto integrador para `${input:semana:Ruta de la semana (ej: bootcamp/week-01-intro_redis_y_strings/3-proyecto)}`.

Nombre del proyecto: **${input:nombre:Nombre del proyecto (ej: Mini Blog Cache)}**
Descripción: **${input:descripcion:Qué construye el estudiante (ej: sistema de caché para artículos de blog con contadores de visitas)}**
Estructuras Redis a usar: **${input:estructuras:Estructuras de datos involucradas (ej: Strings con TTL, INCR)}**

## Archivos a crear

```
3-proyecto/
├── README.md
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
├── redis.conf
└── starter/
    ├── main.py
    └── tests/
        └── test_${nombre_snake}.py
```

## Formato de `starter/main.py`

- Funciones con docstrings completos (Args, Returns, Examples)
- Type hints en todos los parámetros y retornos
- TODOs con instrucciones claras (qué comando Redis usar, pasos a seguir)
- Bloque `if __name__ == "__main__"` con demo interactivo
- Conexión Redis leyendo variables de entorno

```python
def funcion(r: redis.Redis, param: str) -> str | None:
    """
    Descripción.

    Args:
        r: instancia de Redis
        param: descripción

    Returns:
        descripción del retorno, None si no existe

    Examples:
        >>> funcion(r, "valor")
        "resultado"
    """
    # TODO: Implementar con COMANDO_REDIS
    # 1. Paso 1
    # 2. Paso 2
    # Clave: patron:de:clave
    pass
```

## Formato de tests

- Usar `fakeredis.FakeRedis(decode_responses=True)`
- Fixture `r` por función (aislamiento total)
- Mínimo 3 tests por función pública
- Cubrir: caso base, caso vacío/None, caso límite
- Tests nombrados: `test_nombre_funcion_caso_que_verifica`

## Reglas del README del proyecto

1. Descripción del proyecto y qué aprenderá el estudiante
2. Estructura de claves Redis que debe usar
3. Lista de funciones a implementar con firma
4. Criterios de aceptación (cuándo está "completo")
5. Cómo ejecutar: `docker compose up --build` y `pytest`
6. Puntaje por función (suma 100%)

## Dependencias estándar (requirements.txt)

```
redis==5.2.1
fakeredis==2.26.2
pytest==8.3.5
```

**NO crear la carpeta `solution/`** — está en `.gitignore`.
