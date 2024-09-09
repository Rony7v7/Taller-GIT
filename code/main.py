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

        :param vehicle: Objeto de tipo Vehicle.
        :type vehicle: Vehicle
        """
        self.vehicle_list.append(vehicle)

    def find_vehicles_by_year(self, year, mayor_o_menor):
        """
        Busca vehículos por su año de fabricación.

        :param year: Año de fabricación del vehículo.
        :type year: int
        :param mayor_o_menor: Especifica si el filtro es para vehículos mayores o menores al año especificado.
        :type mayor_o_menor: str
        :return: Lista de vehículos que cumplen con el criterio de año.
        :rtype: list
        """
        if mayor_o_menor == 'mayor':
            vehicles_by_year = [vehicle for vehicle in self.vehicle_list if vehicle.year > year]
        elif mayor_o_menor == 'menor':
            vehicles_by_year = [vehicle for vehicle in self.vehicle_list if vehicle.year < year]
        else:
            raise ValueError("El parámetro 'mayor_o_menor' debe ser 'mayor' o 'menor'.")
        return vehicles_by_year

    def print_vehicle_list(self):
        """
        Imprime la lista de vehículos con sus características.
        """
        for vehicle in self.vehicle_list:
            print(f"Marca: {vehicle.brand}, Modelo: {vehicle.model}, Año: {vehicle.year}")

