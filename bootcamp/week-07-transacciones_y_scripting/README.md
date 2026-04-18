# Semana 07 — Transacciones y Scripting Lua

Garantiza atomicidad con MULTI/EXEC y escribe operaciones complejas con scripts Lua registrados en Redis.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, el estudiante será capaz de:

- MULTI / EXEC / DISCARD: transacciones optimistas
- WATCH para detección de conflictos (CAS pattern)
- EVAL / EVALSHA: scripts Lua atómicos
- SCRIPT LOAD / SCRIPT EXISTS / SCRIPT FLUSH
- Casos de uso: rate limiting atómico, distributed locks

---

## 📋 Requisitos Previos

- Haber completado la [Semana 06](../week-06-streams/README.md)
- Tener el entorno Docker funcionando ([Setup](../../../docs/setup/README.md))

---

## 🗂️ Estructura de la Semana

```
week-07-transacciones_y_scripting/
├── README.md                 ← Este archivo
├── rubrica-evaluacion.md     ← Criterios de evaluación
├── 0-assets/                 ← SVGs y recursos visuales
├── 1-teoria/                 ← Material teórico (archivos .md)
├── 2-practicas/              ← Ejercicios guiados
├── 3-proyecto/               ← Proyecto integrador semanal
├── 4-recursos/               ← Ebooks, videos y webgrafía
└── 5-glosario/               ← Términos clave de la semana
```

---

## 📝 Contenidos

### Teoría (`1-teoria/`)

> _Por completar — usar el prompt `crear-teoria` para generar el contenido._

### Prácticas (`2-practicas/`)

> _Por completar — usar el prompt `crear-practica` para generar el contenido._

### Proyecto (`3-proyecto/`)

> _Por completar — usar el prompt `crear-proyecto` para generar el contenido._

---

## ⏱️ Distribución del Tiempo (8 horas)

| Actividad | Tiempo |
| --------- | ------ |
| Teoría    | 2 h    |
| Prácticas | 3.5 h  |
| Proyecto  | 2.5 h  |

---

## 📌 Entregables

- [ ] Ejercicios de práctica completados (descomentando el código starter)
- [ ] Proyecto integrador funcionando con Docker
- [ ] Todos los comandos redis-cli del material probados

---

## 🔗 Navegación

[← Semana 06](../week-06-streams/README.md) | [Semana 08 →](../week-08-pipelining_y_benchmarking/README.md)
