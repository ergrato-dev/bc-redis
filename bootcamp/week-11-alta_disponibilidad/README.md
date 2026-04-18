# Semana 11 — Alta Disponibilidad — Replicación, Sentinel y Cluster

Diseña arquitecturas Redis de alta disponibilidad con replicación, failover automático vía Sentinel y sharding con Cluster.

---

## 🎯 Objetivos de Aprendizaje

Al finalizar esta semana, el estudiante será capaz de:

- Replicación: REPLICAOF, replication lag, read replicas
- Redis Sentinel: setup, failover automático, client configuration
- Redis Cluster: hash slots, resharding, limitaciones de commands
- Monitoreo: comando INFO, métricas clave, RedisInsight
- Backup y recuperación: BGSAVE, BGREWRITEAOF, estrategias de migración

---

## 📋 Requisitos Previos

- Haber completado la [Semana 10](../week-10-redis_py_asincrono/README.md)
- Tener el entorno Docker funcionando ([Setup](../../../docs/setup/README.md))

---

## 🗂️ Estructura de la Semana

```
week-11-alta_disponibilidad/
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

[← Semana 10](../week-10-redis_py_asincrono/README.md) | [Semana 12 →](../week-12-produccion_y_proyecto_final/README.md)
