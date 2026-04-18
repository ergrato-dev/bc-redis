---
mode: agent
description: Crea un nuevo archivo de teoría para una semana del bootcamp Redis.
---

Crea el archivo de teoría **${input:archivo:Nombre del archivo (ej: 05-sorted-sets.md)}** en la carpeta `${input:ruta:Ruta de la carpeta 1-teoria (ej: bootcamp/week-03-hashes_y_sorted_sets/1-teoria)}`.

El tema a cubrir es: **${input:tema:Descripción del tema}**

## Estructura obligatoria

```markdown
# Título del Tema

## 🎯 Objetivos

- (3-5 objetivos de aprendizaje)

---

## 📋 Contenido

### 1. ...

### 2. ...

...

---

## 📚 Recursos Adicionales

---

## ✅ Checklist de Verificación
```

## Reglas de contenido

- **Mínimo 150 líneas**
- Todo ejemplo redis-cli incluye salida esperada: `# → RESULTADO`
- Secciones que describan arquitectura o flujos referencian un SVG en `../0-assets/`
- Explicaciones en español, código y claves Redis en inglés
- Nomenclatura de claves: `objeto:subtipo:id`
- Incluir complejidad Big-O cuando sea relevante
- Incluir al menos un caso de uso del mundo real por estructura de datos
- Comparar con alternativas cuando aplique (ej: List vs Stream, Hash vs String JSON)

## SVGs necesarios

Si el tema requiere un diagrama de arquitectura o comparación visual, crea también el SVG correspondiente en `../0-assets/NN-nombre.svg`:

- Dark theme (`#0f0f1a` background)
- Color principal Redis: `#DC382D`
- Fuente: Inter, Roboto o system-ui (sans-serif)
- Sin gradientes
- Vincularlo en el archivo de teoría con alt text accesible
