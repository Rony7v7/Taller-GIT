class Main:
    """
    Clase principal que gestiona una lista de vehículos.
    Permite agregar vehículos y buscarlos por año de fabricación.
    """

    def __init__(self):
        """
        Inicializa la lista de vehículos.
        """
        self.vehicle_list = []

    def add_vehicle(self, vehicle):
        """
        Agrega un vehículo a la lista.

        :param vehicle: Objeto de tipo Vehiculo.
        :type vehicle: Vehiculo
        """
        self.vehicle_list.append(vehicle)

    def find_vehicles_by_year(self, year, year_range,mayor_o_menor):
        """
        Busca vehículos por su año de fabricación.

        :param year: Año de fabricación del vehículo.
        :type year: int
        :param mayor_o_menor: Especifica si el filtro es para vehículos mayores o menores al año especificado.
        :type mayor_o_menor: str
        :return: Lista de vehículos que cumplen con el criterio de año.
        :rtype: list
        """
        vehicles_by_year = [vehicle for vehicle in self.vehicle_list if vehicle.año == year]
        return vehicles_by_year

        #Modifica la clase "Main", para que ahora el filtro por año permita buscar vehículos
        #que se encuentren en un rango de años. Actualiza el README.md con ejemplos de
        #cómo calcular la antigüedad de un vehículo.

        vehicles_by_year =  [vehicle for vehicle in self.vehicle_list if vehicle.year == year]
        vehicles_by_range = [vehicle for vehicle in self.vehicle_list if vehicle.year in year_range]

        if year:
            if mayor_o_menor == 'mayor':
                vehicles_by_year = [vehicle for vehicle in self.vehicle_list if vehicle.year > year]
            elif mayor_o_menor == 'menor':
                vehicles_by_year = [vehicle for vehicle in self.vehicle_list if vehicle.year < year]
            return vehicles_by_year
        else:
            return vehicles_by_range

    def imprimir_vehiculos(self):

        """
        Imprime la lista de vehículos con sus características.
        """

        if not self.vehicle_list:
            print("No hay vehículos en la flota.")
            return
        
        for vehiculo in self.vehicle_list:
            print(f"Marca: {vehiculo.marca}")
            print(f"Modelo: {vehiculo.modelo}")
            print(f"Año: {vehiculo.año}")
            print(f"Kilometraje: {vehiculo.kilometraje} km")
            print(f"Estado actual: {vehiculo.estado_actual}")
            print(f"Tipo de combustible: {vehiculo.tipo_combustible}")
            print(f"El color: {vehiculo.color}")
            print(f"El color: {vehiculo.potencia}")
            print("-" * 30)
            

        for vehicle in self.vehicle_list:
            print(f"Marca: {vehicle.marca}, Modelo: {vehicle.modelo}, Año: {vehicle.año}, Combustible: {vehicle.tipo_combustible}")
        for vehicle in self.vehicle_list:
            print(f"Marca: {vehicle.brand}, Modelo: {vehicle.model}, Año: {vehicle.year}")

