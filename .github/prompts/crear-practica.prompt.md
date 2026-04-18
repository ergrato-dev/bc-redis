---
mode: agent
description: Crea una práctica guiada (código comentado) para una semana del bootcamp Redis.
---

Crea la práctica **${input:nombre:Nombre de la carpeta (ej: practica-03-hashes)}** en `${input:semana:Ruta de la semana (ej: bootcamp/week-02-listas_y_sets/2-practicas)}`.

Tema de la práctica: **${input:tema:Descripción breve del tema a practicar}**

## Archivos a crear

```
practica-NN-tema/
├── README.md
├── docker-compose.yml
├── redis.conf
├── Dockerfile              ← solo si hay código Python
├── requirements.txt        ← solo si hay código Python
└── starter/
    └── main.py             ← solo si hay código Python
```

## Formato del README

El README debe tener:

1. Descripción del objetivo
2. Cómo iniciar el entorno (`docker compose up -d`)
3. Pasos numerados con bloques `redis-cli` ejecutables Y secciones "Abre `starter/main.py`" si aplica
4. Cada paso explica el concepto antes de mostrar el comando

## Formato de `starter/main.py` (código comentado)

```python
# ============================================
# PASO 1: Título del paso
# ============================================
print("--- Paso 1: Descripción ---")

# Explicación del concepto (por qué este comando)

# Descomenta las siguientes líneas:
# import ...
# r = redis.Redis(...)
# r.comando(...)
# print(...)
```

## Reglas

- Las prácticas NO tienen TODOs — el código comentado es la "solución"
- Sin carpeta `solution/`
- Los pasos redis-cli siempre muestran la salida esperada con `# →`
- La práctica debe poder completarse en 45-60 minutos
- Usar imagen `redis:8-alpine`, password `bootcamp2026`
- Mínimo 3 pasos, máximo 6 pasos
- El último paso limpia las claves creadas
