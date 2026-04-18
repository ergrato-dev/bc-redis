#!/bin/sh
# seed.sh — carga datos de prueba para la Práctica 01
# Se ejecuta dentro del contenedor Redis

CLI="redis-cli -a bootcamp2026"

echo "Cargando datos de prueba..."

# Strings simples: usuarios
$CLI SET user:42:name "Alice"
$CLI SET user:43:name "Bob"
$CLI SET user:44:name "Carol"

# String con TTL: sesiones de usuario
$CLI SET session:user:1 "active" EX 3600
$CLI SET session:user:2 "active" EX 7200

# Contadores: vistas de artículos
$CLI SET article:1:views 142
$CLI SET article:2:views 89
$CLI SET article:3:views 317

# Flag de feature
$CLI SET feature:dark_mode:enabled "1"

echo "✓ Datos cargados: $(redis-cli -a bootcamp2026 DBSIZE) claves"
