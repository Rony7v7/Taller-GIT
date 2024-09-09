from Vehicle import Vehicle
from HistorialMantenimiento import HistorialMantenimiento


class Main:
    """
    Esta clase representa el sistema principal para gestionar una lista de vehículos.
    Permite agregar vehículos a la lista y buscarlos por año.
    """

    def __init__(self):
        """
        Inicializa la clase Main con una lista vacía de vehículos.
        """
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        """
        Agrega un vehículo a la lista de vehículos.

        :param vehiculo: Instancia de la clase Vehicle que representa un vehículo.
        :type vehiculo: Vehicle
        """
        self.vehiculos.append(vehiculo)

    def find_vehicles_by_year(self, year, year_range, mayor_o_menor):
        """
        Busca vehículos por su año de fabricación.

        :param year: Año de fabricación del vehículo.
        :type year: int
        :param mayor_o_menor: Especifica si el filtro es para vehículos mayores o menores al año especificado.
        :type mayor_o_menor: str
        :return: Lista de vehículos que cumplen con el criterio de año.
        :rtype: list
        """
        vehicles_by_year = [
            vehicle for vehicle in self.vehiculos if vehicle.year == year
        ]
        vehicles_by_range = [
            vehicle for vehicle in self.vehiculos if vehicle.year in year_range
        ]

        if year:
            if mayor_o_menor == "mayor":
                vehicles_by_year = [
                    vehicle for vehicle in self.vehiculos if vehicle.year > year
                ]
            elif mayor_o_menor == "menor":
                vehicles_by_year = [
                    vehicle for vehicle in self.vehiculos if vehicle.year < year
                ]
            return vehicles_by_year
        else:
            return vehicles_by_range

    def imprimir_vehiculos(self):
        """
        Imprime la lista de vehículos con sus características.
        """

        if not self.vehiculos:
            print("No hay vehículos en la flota.")
            return

        for vehiculo in self.vehiculos:
            print(f"Marca: {vehiculo.brand}")
            print(f"Modelo: {vehiculo.model}")
            print(f"Año: {vehiculo.year}")
            print(f"Kilometraje: {vehiculo.kilometers} km")
            print(f"Estado actual: {vehiculo.current_status}")
            print(f"Tipo de combustible: {vehiculo.type_fuel}")
            print(f"El color: {vehiculo.color}")
            print(f"El color: {vehiculo.potencia}")
            print("-" * 30)


def main():
    """
    Función principal para probar la funcionalidad de la clase Main.
    """
    sistema = Main()

    # Crear algunos vehículos de ejemplo
    # Crear algunas instancias de vehículos con todos los argumentos necesarios
    vehiculo1 = Vehicle(
        "Toyota",
        "Corolla",
        2010,
        100000,
        "Operativo",
        "Gasolina",
        "2023-01-01",
        "Blanco",
        132,
    )
    vehiculo2 = Vehicle(
        "Ford", "Focus", 2015, 75000, "Operativo", "Diesel", "2022-05-15", "Negro", 150
    )
    vehiculo3 = Vehicle(
        "Honda",
        "Civic",
        2010,
        120000,
        "Operativo",
        "Gasolina",
        "2023-06-12",
        "Rojo",
        140,
    )

    # Agregar vehículos al sistema
    sistema.agregar_vehiculo(vehiculo1)
    sistema.agregar_vehiculo(vehiculo2)
    sistema.agregar_vehiculo(vehiculo3)

    # Buscar vehículos del año 2015
    print("Vehículos del año 2015:")
    vehiculos_2015 = sistema.find_vehicles_by_year(2015, (2015, 2017), 0)
    for vehiculo in vehiculos_2015:
        print(vehiculo)

    # Buscar vehículos del año 2020
    print("\nVehículos del año 2020:")
    vehiculos_2020 = sistema.find_vehicles_by_year(2020, (2015, 2017), 0)
    for vehiculo in vehiculos_2020:
        print(vehiculo)

    sistema.imprimir_vehiculos()


if __name__ == "__main__":
    main()
