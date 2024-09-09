# Code style Guidelines

Este documento define el estilo de codificación que seguiremos en el proyecto.

## 1. Nombres de Variables y Funciones

- **Variables**: Usar `snake_case` para las variables.
  - Ejemplo: `total_sales`, `customer_count`.
  
- **Funciones**: También usar `snake_case` para las funciones.
  - Ejemplo: `calculate_average()`, `get_data()`.

- **Clases**: Usar `PascalCase` para las clases.
  - Ejemplo: `Vehicle`, `MaintenanceHistory`.

## 2. Reglas de Indentación

- Usar usar **4 espacios** para la indentación.

## 3. Longitud Máxima de Líneas de Código

- La longitud máxima de una línea de código será de **80 caracteres**.
- Si una línea es muy larga, dividirla en varias líneas para mayor claridad.

## 4. Formato de Comentarios y Documentación

- Los comentarios deben ser claros, concisos y usados para explicar partes complejas del código.

### Comentarios de una sola línea
```python
# This is a single-line comment explaining the code below.
```

### Comentarios de varias líneas
```python
"""
  This is a multi-line comment that gives a detailed
  explanation of a block of code or a function.
"""
```

### Documentación de funciones

- Se recomienda documentar las funciones utilizando comentarios descriptivos.

```python
def calculate_average(numbers):
    """
    Calcula el promedio de una lista de números.
    
    :param numbers: Lista de números.
    :type numbers: list
    :return: El promedio calculado.
    :rtype: float
    """
    return sum(numbers) / len(numbers)
```

## 5. Buenas Prácticas

- Usar nombres descriptivos y significativos para variables y funciones.
- Evitar abreviaturas o nombres ambiguos.
- Seguir las convenciones del lenguaje Python para asegurar código legible y mantenible.
