---
mode: agent
description: Audita las dependencias Python del bootcamp contra CVEs conocidos y genera un reporte con versiones pineadas seguras.
---

Realiza una auditoría de seguridad CVE para las dependencias Python ubicadas en:
`${input:ruta:Ruta del requirements.txt (ej: bootcamp/week-01-intro_redis_y_strings/3-proyecto/requirements.txt)}`

## Qué debes hacer

### 1. Leer el requirements.txt actual

Lee el archivo indicado e identifica:

- Paquetes con versiones pineadas exactas (`==`) ✅
- Paquetes con versiones flotantes (`>=`, `~=`, `^`, `*`) ❌

### 2. Verificar CVEs por paquete

Para cada paquete, consulta:

- **OSV (Open Source Vulnerabilities)**: https://osv.dev/list?ecosystem=PyPI&q={paquete}
- **PyPI Advisory Database**: https://pypi.org/project/{paquete}/#history
- **GitHub Security Advisories** si aplica

Busca vulnerabilidades de severidad **LOW, MODERATE, HIGH o CRITICAL**.

### 3. Verificar que las versiones pineadas son las últimas estables

Consulta https://pypi.org/pypi/{paquete}/json para obtener la `version` más reciente.

Compara con la versión pineada y reporta si hay una versión más nueva sin CVEs.

### 4. Generar el reporte

Produce un reporte con este formato:

```markdown
## Reporte de Auditoría CVE

Archivo: {ruta}
Fecha: {fecha actual}

### Resumen

| Paquete | Versión actual | CVEs activos | Versión recomendada | Acción |
| ------- | -------------- | ------------ | ------------------- | ------ |
| redis   | 5.2.1          | ✅ Ninguno   | 5.2.1               | OK     |
| ...     | ...            | ...          | ...                 | ...    |

### Estado General

- 🟢 APROBADO / 🔴 REQUIERE ACCIÓN

### Vulnerabilidades Encontradas (si hay)

...

### Dependencias con Versiones Flotantes (si hay)

...
```

### 5. Si hay problemas

Si encuentras CVEs activos o versiones flotantes:

1. Propone la versión corregida con pin exacto
2. Actualiza el `requirements.txt` con la versión segura
3. Explica brevemente el CVE y por qué la nueva versión lo resuelve

### 6. Si todo está limpio

Confirma que el `requirements.txt` cumple la política de seguridad del bootcamp:

- Todas las versiones son exactas (`==`)
- Ningún paquete tiene CVEs activos de severidad moderate o superior
- Las versiones están actualizadas o justificadas

## Herramientas de verificación recomendadas

```bash
# Verificar con pip-audit (instalar si no está disponible)
pip install pip-audit==2.9.0
pip-audit -r requirements.txt --format=json

# Verificar con safety
pip install safety==3.5.2
safety check -r requirements.txt
```

## Contexto del bootcamp

Stack base auditado el 18/04/2026:

- `redis==5.2.1` — sin CVEs activos ✅
- `fakeredis==2.35.1` — sin CVEs activos ✅
- `pytest==8.3.5` — sin CVEs activos ✅
- `pytest-asyncio==0.24.0` — sin CVEs activos ✅
- `python-dotenv==1.1.0` — sin CVEs activos ✅
- `FROM python:3.13-slim` — imagen Docker base con Python 3.13 ✅
