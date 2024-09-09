class Vehiculo:
    COMBUSTIBLES_VALIDOS = ["Gasolina", "Diesel", "Eléctrico"]

    def __init__(self, marca, modelo, año, tipo_combustible):
        """
        Inicializa un vehículo con los atributos de marca, modelo, año y tipo de combustible.
        
        :param marca: Marca del vehículo.
        :param modelo: Modelo del vehículo.
        :param año: Año de fabricación del vehículo.
        :param tipo_combustible: Tipo de combustible del vehículo.
        """
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.tipo_combustible = None  
        self.set_tipo_combustible(tipo_combustible)

    def set_tipo_combustible(self, tipo_combustible):
        """
        Valida y establece el tipo de combustible del vehículo.
        
        :param tipo_combustible: Tipo de combustible a establecer.
        :raises ValueError: Si el tipo de combustible no es válido.
        """
        if tipo_combustible not in Vehiculo.COMBUSTIBLES_VALIDOS:
            raise ValueError(f"Tipo de combustible inválido. Debe ser uno de {Vehiculo.COMBUSTIBLES_VALIDOS}.")
        self.tipo_combustible = tipo_combustible

    def __str__(self):
        """
        Devuelve una representación en cadena del vehículo.
        """
        return f"Vehiculo(marca={self.marca}, modelo={self.modelo}, año={self.año}, combustible={self.tipo_combustible})"


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

    def find_vehicles_by_year(self, year):
        """
        Busca vehículos por su año de fabricación.

        :param year: Año de fabricación del vehículo.
        :type year: int
        :return: Lista de vehículos fabricados en el año especificado.
        :rtype: list
        """
        vehicles_by_year = [vehicle for vehicle in self.vehicle_list if vehicle.año == year]
        return vehicles_by_year

    def print_vehicle_list(self):
        """
        Imprime la lista de vehículos con sus características.
        """
        for vehicle in self.vehicle_list:
            print(f"Marca: {vehicle.marca}, Modelo: {vehicle.modelo}, Año: {vehicle.año}, Combustible: {vehicle.tipo_combustible}")

