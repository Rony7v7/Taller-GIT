En el archivo README.md se establecerá que el formato de los mensajes de los commits deberá seguir la estructura: "Tipo de commit": "Título del commit". Ambos componentes, el tipo y el título, son obligatorios para garantizar claridad y consistencia en el historial del repositorio.

Tipo de commit: Este campo indicará la naturaleza del cambio realizado. Algunos ejemplos de tipos comunes son:

feat (nueva funcionalidad),
develop (desarrollo),
fix (corrección de errores),
docs (cambios en la documentación),
style (formato y estilo de código que no afecta la lógica),
refactor (cambios en el código que no corrigen errores ni añaden características).

Título del commit: Es una breve descripción concisa de la acción realizada, enfocándose en lo que se cambió, agregó o corrigió. 


# Sistema de Gestión de Vehículos

Este proyecto forma parte del desarrollo de un sistema de gestión de vehículos, cuyo objetivo es gestionar el inventario de una flota vehicular. Cada estudiante, dividido en roles específicos, contribuye a la creación de clases y funcionalidades que permiten registrar, buscar y mantener información detallada sobre los vehículos.

## Funcionalidades Principales

### 1. Registro de Vehículos
El sistema permite almacenar información detallada de los vehículos, incluyendo:
- Marca
- Modelo
- Año de fabricación
- Historial de mantenimiento

### 2. Búsqueda de Vehículos
Se ha implementado una funcionalidad para buscar vehículos en el inventario según su año de fabricación. Es posible buscar:
- Vehículos fabricados en un año específico.
- Vehículos fabricados antes o después de un año dado.

**Ejemplo de uso del filtro por año**:
```python
# Buscar vehículos fabricados después del año 2010
resultado = buscar_vehiculos_por_año(2010, 'despues')
```

### 3. Cálculo de la Antigüedad de un Vehículo
Se ha añadido la capacidad de calcular la antigüedad de un vehículo basado en su año de fabricación.

**Ejemplo de cálculo de antigüedad**:
```python
# Calcular la antigüedad de un vehículo fabricado en 2015
antiguedad = calcular_antiguedad_vehiculo(2015)
print(f'La antigüedad del vehículo es de {antiguedad} años.')
```

### 4. Nuevos Atributos: Color y Potencia
El proyecto ha sido ampliado para incluir nuevas características que mejoran el detalle de la información vehicular:

- **Color**: Se ha añadido el atributo `color` a la clase `Vehiculo`, con sus métodos getter y setter.
- **Potencia**: Se ha incorporado el atributo `potencia` (caballos de fuerza) a la clase `Vehiculo`, con sus respectivos getter y setter.

**Ejemplo de uso de los nuevos atributos**:
```python
# Crear un vehículo con color y potencia
mi_vehiculo = Vehiculo(marca="Toyota", modelo="Corolla", año=2020, color="Rojo", potencia=150)

# Obtener y modificar el color
print(mi_vehiculo.get_color())  # Salida: Rojo
mi_vehiculo.set_color("Azul")

# Obtener y modificar la potencia
print(mi_vehiculo.get_potencia())  # Salida: 150
mi_vehiculo.set_potencia(180)
```

## Colaboración y Control de Versiones
Este proyecto fomenta la colaboración a través del uso de Git para el control de versiones, incluyendo el uso de ramas para desarrollo paralelo y la resolución de conflictos.

- Cada desarrollador debe seguir el formato establecido para los mensajes de los commits, descrito a continuación:
  - Tipo de commit: "feat", "fix", "docs", etc.
  - Descripción concisa del cambio realizado.
