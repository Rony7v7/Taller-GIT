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

    def find_vehicles_by_year(self, year):
        """
        Busca vehículos por su año de fabricación.

        :param year: Año de fabricación del vehículo.
        :type year: int
        :return: Lista de vehículos fabricados en el año especificado.
        :rtype: list
        """
        vehicles_by_year = [Vehicle for Vehicle in self.vehicle_list if vehicle.year == year]
        return vehicles_by_year

    def imprimir_vehiculos(self):

        """
        Imprime la lista de vehículos con sus características.
        """

        if not self.vehiculos:
            print("No hay vehículos en la flota.")
            return
        
        for vehiculo in self.vehiculos:
            print(f"Marca: {vehiculo.marca}")
            print(f"Modelo: {vehiculo.modelo}")
            print(f"Año: {vehiculo.año}")
            print(f"Kilometraje: {vehiculo.kilometraje} km")
            print(f"Estado actual: {vehiculo.estado_actual}")
            print(f"Tipo de combustible: {vehiculo.tipo_combustible}")
            print("-" * 30)


