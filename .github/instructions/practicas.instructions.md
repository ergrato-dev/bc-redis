---
applyTo: "**/2-practicas/**/*.py"
---

# Instrucciones para archivos Python de Prácticas

## Formato: código comentado para descomentar

Las prácticas NO usan TODOs. El estudiante aprende descomentando código ya escrito.

### Estructura de cada paso

```python
# ============================================
# PASO N: Título descriptivo del paso
# ============================================
print("--- Paso N: Descripción breve ---")

# Explicación del concepto en español (1-3 líneas)
# Por qué se usa este comando/patrón

# Descomenta las siguientes líneas:
# r.comando(...)
# resultado = r.otro_comando(...)
# print(f"Resultado: {resultado}")
```

## Reglas

- Cada archivo `starter/main.py` debe tener entre 3 y 6 pasos
- Los imports van al inicio del archivo, también comentados
- Usar `decode_responses=True` en todas las conexiones
- Leer `REDIS_HOST`, `REDIS_PORT`, `REDIS_PASSWORD` de variables de entorno
- Las conexiones Redis usan el hostname `redis` (nombre del servicio Docker)
- Type hints en todas las funciones helper si las hay
- Sin carpeta `solution/` — el código comentado ES la solución

## Ejemplo de conexión estándar

```python
# import os
# import redis

# r = redis.Redis(
#     host=os.environ.get("REDIS_HOST", "redis"),
#     port=int(os.environ.get("REDIS_PORT", 6379)),
#     password=os.environ.get("REDIS_PASSWORD", "bootcamp2026"),
#     decode_responses=True,
# )
```

## Limpieza al final

El último paso SIEMPRE limpia las claves creadas durante la práctica:

```python
# ============================================
# LIMPIEZA: Eliminar claves de la práctica
# ============================================
# r.delete("clave:1", "clave:2", ...)
# print("Claves eliminadas.")
```
