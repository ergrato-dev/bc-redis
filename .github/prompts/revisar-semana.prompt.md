---
mode: agent
description: Revisa y valida que una semana del bootcamp cumpla todos los estándares de calidad del proyecto.
---

Revisa la semana ubicada en `${input:ruta:Ruta de la semana (ej: bootcamp/week-01-intro_redis_y_strings)}` y verifica que cumple todos los estándares del bootcamp.

## Checklist de validación

### Estructura de carpetas

- [ ] Existe `0-assets/` con al menos un SVG
- [ ] Existe `1-teoria/` con al menos 3 archivos .md
- [ ] Existe `2-practicas/` con al menos 2 prácticas
- [ ] Existe `3-proyecto/` con README, starter/ y tests
- [ ] Existe `4-recursos/` con ebooks-free/, videografia/, webgrafia/
- [ ] Existe `5-glosario/README.md`
- [ ] Existe `rubrica-evaluacion.md`
- [ ] NO existe `3-proyecto/solution/` (debe estar en .gitignore)

### Archivos de teoría

- [ ] Todos los .md tienen ≥ 150 líneas (`wc -l`)
- [ ] Todos siguen la estructura: Objetivos → Contenido → Recursos → Checklist
- [ ] Todos los ejemplos redis-cli incluyen salida esperada `# →`
- [ ] Todos los SVGs de 0-assets están referenciados en al menos un archivo de teoría
- [ ] No hay ASCII art — los diagramas usan SVGs

### Prácticas

- [ ] El código Python usa el formato "comentado para descomentar" (sin TODOs)
- [ ] Cada práctica tiene docker-compose.yml y redis.conf
- [ ] Las conexiones Redis leen variables de entorno
- [ ] Último paso de cada práctica limpia las claves

### Proyecto

- [ ] Las funciones tienen docstrings con Args, Returns, Examples
- [ ] Type hints en todos los parámetros
- [ ] Los TODOs indican qué comando Redis usar y los pasos
- [ ] Los tests usan `fakeredis.FakeRedis(decode_responses=True)`
- [ ] Hay al menos 3 tests por función pública
- [ ] El `if __name__ == "__main__"` funciona como demo

### Calidad general

- [ ] Documentación en español, código y claves en inglés
- [ ] Nomenclatura de claves: `objeto:subtipo:id`
- [ ] requirements.txt usa versiones exactas (sin `^`, `~`, `>=`)
- [ ] Los SVGs usan dark theme (#0f0f1a), color #DC382D, sans-serif, sin gradientes
- [ ] El README de la semana tiene distribución de 8h y navegación ← →

## Acción esperada

Para cada ítem que NO cumple: describe el problema y corrígelo directamente en el archivo correspondiente.
Al final reporta: cuántos ítems pasaron, cuántos se corrigieron y si queda algún pendiente.
