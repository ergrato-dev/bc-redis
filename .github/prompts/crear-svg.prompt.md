---
mode: agent
description: Crea un diagrama SVG educativo para los 0-assets de una semana del bootcamp Redis.
---

Crea el SVG **${input:archivo:Nombre del archivo (ej: 05-pubsub-flow.svg)}** en `${input:ruta:Ruta de 0-assets (ej: bootcamp/week-05-pubsub/0-assets)}`.

El diagrama debe ilustrar: **${input:descripcion:Qué debe mostrar el diagrama}**

El SVG será vinculado en: **${input:referencia:Archivo de teoría que lo referencia (ej: 1-teoria/01-pubsub.md §3)}**

## Especificaciones visuales obligatorias

| Propiedad             | Valor                                               |
| --------------------- | --------------------------------------------------- |
| Background            | `#0f0f1a`                                           |
| Color principal Redis | `#DC382D`                                           |
| Texto principal       | `#ccccdd`                                           |
| Texto secundario      | `#888899`                                           |
| Bordes activos        | `#DC382D` stroke-width 2                            |
| Bordes neutros        | `#444466` stroke-width 1.5                          |
| Fuentes               | `Inter, Roboto, 'Open Sans', system-ui, sans-serif` |
| Gradientes            | ❌ No usar nunca                                    |
| Tamaño recomendado    | 800×420 o 800×480                                   |

## Tipos de diagramas frecuentes

- **Arquitectura**: cajas con flechas entre servicios/componentes
- **Flujo de mensajes**: líneas de tiempo (cliente izquierda, servidor derecha)
- **Comparación**: dos columnas con ❌ y ✅
- **Estructura de datos**: visualización de la estructura interna (ej: sorted set con scores)
- **Patrones**: cards con nombre, comando y caso de uso

## Reglas

- Incluir título en la parte superior (font-size 16, color `#DC382D`, font-weight 700)
- Incluir subtítulo descriptivo (font-size 11, color `#666688`)
- Todos los textos deben ser legibles con alto contraste sobre `#0f0f1a`
- Las flechas usan markers SVG con `<defs>`
- Leyenda en la parte inferior si el diagrama usa colores distintos
- El SVG debe ser autocontenido (sin imports externos)
- Revisar que no haya texto desbordado o sobrepuesto y que renderice 

## Después de crear el SVG

Añade la referencia en el archivo de teoría indicado:

```markdown
![Descripción accesible del diagrama](../0-assets/${archivo})
```
