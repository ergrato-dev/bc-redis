# Semana 01 — Introducción a Redis y Strings

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, serás capaz de:

- Explicar qué es Redis, cómo funciona y cuándo usarlo
- Instalar y ejecutar Redis 8 con Docker y Docker Compose
- Navegar y operar redis-cli con fluidez
- Dominar todos los comandos de la estructura String
- Implementar patrones reales con strings: cache, contadores y flags con TTL

---

## 📚 Requisitos Previos

- Docker y Docker Compose instalados ([Bootcamp Docker](https://github.com/ergrato-dev/bc-docker))
- Terminal básica (bash/zsh)
- Sin conocimientos previos de Redis requeridos

---

## 🗂️ Estructura de la Semana

```
week-01-intro_redis_y_strings/
├── README.md                        ← este archivo
├── rubrica-evaluacion.md            ← criterios de evaluación
├── 0-assets/                        ← imágenes y diagramas SVG
├── 1-teoria/
│   ├── 01-que-es-redis.md           ← qué es Redis y cuándo usarlo
│   ├── 02-instalacion-con-docker.md ← entorno Docker con Redis 8
│   ├── 03-redis-cli.md              ← navegación y comandos esenciales
│   └── 04-strings.md                ← estructura String completa
├── 2-practicas/
│   ├── practica-01-primeros-pasos/  ← conexión, CLI y claves
│   └── practica-02-strings/         ← comandos String con python
├── 3-proyecto/                      ← mini blog cache (proyecto integrador)
├── 4-recursos/
│   ├── ebooks-free/
│   ├── videografia/
│   └── webgrafia/
└── 5-glosario/
    └── README.md
```

---

## 📝 Contenidos

### Teoría

| Archivo | Tema |
| ------- | ---- |
| [01 — ¿Qué es Redis?](1-teoria/01-que-es-redis.md) | Conceptos, casos de uso, Redis vs otras DBs |
| [02 — Instalación con Docker](1-teoria/02-instalacion-con-docker.md) | Docker Compose, redis.conf, RedisInsight |
| [03 — redis-cli](1-teoria/03-redis-cli.md) | Navegación, comandos esenciales, DEBUG |
| [04 — Strings](1-teoria/04-strings.md) | SET, GET, INCR, TTL, patrones comunes |

### Prácticas

| Ejercicio | Descripción |
| --------- | ----------- |
| [Práctica 01 — Primeros pasos](2-practicas/practica-01-primeros-pasos/README.md) | Conexión, exploración de claves, comandos básicos en redis-cli |
| [Práctica 02 — Strings con Python](2-practicas/practica-02-strings/README.md) | Comandos String desde redis-py: cache, contador y expiración |

### Proyecto

| Proyecto | Descripción |
| -------- | ----------- |
| [Mini Blog Cache](3-proyecto/README.md) | Sistema de cache de artículos con conteo de vistas y TTL |

---

## ⏱️ Distribución del Tiempo (8 horas)

| Actividad | Tiempo |
| --------- | ------ |
| Teoría (4 archivos) | 2 h |
| Práctica 01 — Primeros pasos | 1.5 h |
| Práctica 02 — Strings con Python | 2 h |
| Proyecto — Mini Blog Cache | 2.5 h |

---

## 📌 Entregables

- [ ] Práctica 01 completada y ejecutando sin errores
- [ ] Práctica 02 completada y ejecutando sin errores
- [ ] Proyecto Mini Blog Cache implementado (TODOs resueltos)
- [ ] Tests del proyecto pasando

---

## 🔗 Navegación

← No hay semana anterior | [Semana 02 →](../week-02-listas_y_sets/README.md)
