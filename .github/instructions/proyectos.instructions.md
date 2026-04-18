---
applyTo: "**/3-proyecto/**/*.py"
---

# Instrucciones para archivos Python de Proyectos

## Formato: TODOs para implementar desde cero

Los proyectos SÍ usan TODOs. El estudiante implementa las funciones completas.

### Estructura de una función con TODO

```python
def nombre_funcion(r: redis.Redis, param: tipo) -> tipo_retorno:
    """
    Descripción clara de qué hace la función.

    Args:
        r: instancia de Redis
        param: descripción del parámetro

    Returns:
        descripción del valor de retorno

    Examples:
        >>> nombre_funcion(r, "valor")
        "resultado_esperado"
    """
    # TODO: Implementar con COMANDO_REDIS
    # 1. Paso 1 en español
    # 2. Paso 2 en español
    # Clave a usar: patron:de:clave
    pass
```

## Reglas

- Todas las funciones DEBEN tener docstring con Args, Returns y Examples
- Type hints obligatorios en todos los parámetros y retornos
- Los TODOs deben indicar QUÉ comando Redis usar y los pasos a seguir
- El archivo `starter/main.py` incluye un bloque `if __name__ == "__main__"` con demo
- Los tests están en `starter/tests/test_*.py` usando `fakeredis`
- La carpeta `solution/` está en `.gitignore` (solo para instructores)

## Tests con fakeredis

```python
# tests/test_nombre.py
import pytest
import fakeredis
from main import nombre_funcion

@pytest.fixture
def r() -> fakeredis.FakeRedis:
    """Redis en memoria para tests aislados."""
    return fakeredis.FakeRedis(decode_responses=True)

def test_nombre_caso_base(r: fakeredis.FakeRedis) -> None:
    resultado = nombre_funcion(r, "param")
    assert resultado == "esperado"
```

## Convención de claves en proyectos

Usar el patrón `recurso:identificador` documentado en el README del proyecto:

```python
# Ejemplo: proyecto "Mini Blog Cache"
# cache:article:{article_id}  → JSON del artículo
# views:article:{article_id}  → contador entero
```
