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

    def add_vehicle(self, Vehicle):
        """
        Agrega un vehículo a la lista.

        :param vehicle: Objeto de tipo Vehicle.
        :type vehicle: Vehicle
        """
        self.vehicle_list.append(Vehicle)

    def find_vehicles_by_year(self, year, year_range):
        """
        Busca vehículos por su año de fabricación.

        :param year: Año de fabricación del vehículo.
        :type year: int
        :return: Lista de vehículos fabricados en el año especificado.
        :rtype: list
        """

        #Modifica la clase "Main", para que ahora el filtro por año permita buscar vehículos
        #que se encuentren en un rango de años. Actualiza el README.md con ejemplos de
        #cómo calcular la antigüedad de un vehículo.

        vehicles_by_year =  [vehicle for vehicle in self.vehicle_list if vehicle.year == year]
        vehicles_by_range = [vehicle for vehicle in self.vehicle_list if vehicle.year in year_range]

        if year:
            return vehicles_by_year
        else:
            return vehicles_by_range

    def print_vehicle_list(self):
        """
        Imprime la lista de vehículos con sus características.
        """
        for Vehicle in self.vehicle_list:
            print(f"Marca: {Vehicle.brand}, Modelo: {Vehicle.model}, Año: {Vehicle.year}")
