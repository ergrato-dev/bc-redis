---
mode: agent
description: Crea la estructura completa de una nueva semana del bootcamp Redis con todos sus archivos y carpetas.
---

Crea la estructura completa para la semana **${input:numero:Número de semana (ej: 02)}** del bootcamp Redis.

El tema principal es: **${input:tema:Tema principal (ej: listas-y-sets)}**
El título descriptivo es: **${input:titulo:Título para README (ej: Listas y Sets — Queues y Conjuntos)}**

Usa como referencia la semana 01 ya existente en `bootcamp/week-01-intro_redis_y_strings/`.

## Estructura a crear

```
bootcamp/week-${numero}-${tema}/
├── README.md
├── rubrica-evaluacion.md
├── 0-assets/              ← SVGs educativos (los necesarios para la teoría)
├── 1-teoria/              ← archivos .md (mínimo 150 líneas cada uno)
├── 2-practicas/
│   ├── practica-01-*/    ← ejercicio guiado (código comentado para descomentar)
│   └── practica-02-*/    ← ejercicio guiado (código comentado para descomentar)
├── 3-proyecto/            ← proyecto integrador (TODOs para implementar)
├── 4-recursos/
│   ├── ebooks-free/README.md
│   ├── videografia/README.md
│   └── webgrafia/README.md
└── 5-glosario/README.md
```

## Reglas

- Los archivos de teoría: mínimo 150 líneas, con secciones numeradas, ejemplos redis-cli con salida esperada, y referencias a SVGs
- Las prácticas usan código comentado para descomentar (NO TODOs)
- El proyecto usa TODOs con docstrings completos y tests con fakeredis
- Documentación en español, código y claves Redis en inglés
- Nomenclatura de claves: `objeto:subtipo:id` en lowercase
- Imágenes SVG: dark theme, color #DC382D, sans-serif, sin gradientes
- El README incluye: objetivos, distribución de 8h, links a contenido, entregables, navegación ← →
- La carpeta `solution/` del proyecto NO se crea (está en .gitignore)

Crea los archivos de forma secuencial. Empieza por el README.md de la semana y espera confirmación antes de continuar con cada carpeta.
