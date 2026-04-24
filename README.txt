# Calculadora de Gastos Personales

Aplicación de consola en Python para registrar y analizar
gastos personales. Guarda los datos en JSON y muestra
resúmenes por categoría y por mes.

## Demo

Al ejecutar Python main.py verás:

----- Calculadora de Gastos -----
  1. Agregar gasto
  2. Ver todos los gastos
  3. Ver por categoría
  4. Resumen del mes
  5. Eliminar gasto
  6. Salir

## Características

- Agregar gastos con descripción, monto y categoría
- Ver todos los gastos ordenados por fecha
- Resumen visual por categoría con porcentajes
- Filtrar gastos del mes actual
- Eliminar gastos con confirmación
- Persistencia en JSON — los datos no se pierden al cerrar

## Instalación

# No requiere librerías externas — solo Python 3.10+
git clone https://github.com/Rinnendothir/calculadora-gastos.git
cd calculadora-gastos
Python main.py

## Estructura del proyecto

calculadora_gastos/
├── main.py          # Menús e interfaz de usuario
├── modelos.py       # Clases Gasto y GestorGastos
├── utilidades.py    # Funciones auxiliares de input
├── gastos.json      # Datos persistentes (se crea automáticamente)
└── README.txt

## Conceptos de Python aplicados

- Clases y POO: `Gasto`, `GestorGastos`
- Persistencia con JSON: guardar y cargar datos
- Manejo de errores: `try/except` en todas las operaciones
- List comprehensions para filtrar gastos
- Módulos propios: separación de responsabilidades
- `@classmethod` para crear objetos desde diccionarios

## Autor

**Veronika Koral**
GitHub: @Rinnendothir
https://github.com/Rinnendothir