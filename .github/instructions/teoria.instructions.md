---
applyTo: "**/1-teoria/**/*.md"
---

# Instrucciones para archivos de Teoría

## Estructura obligatoria

Cada archivo de teoría DEBE seguir exactamente este orden de secciones:

```markdown
# Título del Tema

## 🎯 Objetivos

(lista de 3-5 bullets con lo que el estudiante aprenderá)

---

## 📋 Contenido

### 1. Primera sección

### 2. Segunda sección

...

### N. Última sección

---

## 📚 Recursos Adicionales

(lista de enlaces con descripción)

---

## ✅ Checklist de Verificación

(lista de preguntas que el estudiante debe poder responder)
```

## Reglas de contenido

- Mínimo **150 líneas** por archivo
- Todo ejemplo de `redis-cli` debe incluir la salida esperada con `# →`
- Los diagramas ASCII del tipo "arquitectura" deben reemplazarse por referencias a SVGs en `../0-assets/`
- Idioma: **español** para explicaciones, **inglés** para código y claves Redis
- Nomenclatura de claves: `objeto:subtipo:id` en lowercase con `:`
- Incluir complejidad algorítmica cuando sea relevante: `# O(log N)`

## Formato de ejemplos redis-cli

```bash
# Comentario explicativo en español
COMANDO CLAVE VALOR
# → SALIDA ESPERADA
```

## Assets SVG

Cada archivo de teoría que explique una arquitectura, flujo o comparación DEBE referenciar un SVG en `../0-assets/`:

```markdown
![Descripción accesible del diagrama](../0-assets/NN-nombre-descriptivo.svg)
```

Nombrar los SVGs como `NN-nombre-descriptivo.svg` (numerado, lowercase, guiones).
