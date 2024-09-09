from Vehicle import Vehicle
from HistorialMantenimiento import HistorialMantenimiento

class Main:
    """
    Esta clase representa el sistema principal para gestionar una lista de vehículos.
    Permite agregar vehículos a la lista y buscarlos por año.
    """

    def _init_(self):
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

    def buscar_vehiculo_por_anio(self, anio):
        """
        Busca y retorna los vehículos que fueron fabricados en un año específico.

        :param anio: Año de fabricación del vehículo a buscar.
        :type anio: int
        :return: Lista de vehículos que coinciden con el año dado.
        :rtype: list
        """
        vehiculos_encontrados = [vehiculo for vehiculo in self.vehiculos if vehiculo.anio == anio]
        return vehiculos_encontrados


def main():
    """
    Función principal para probar la funcionalidad de la clase Main.
    """
    sistema = Main()

    # Crear algunos vehículos de ejemplo
# Crear algunas instancias de vehículos con todos los argumentos necesarios
    vehiculo1 = Vehicle("Toyota", "Corolla", 2010, 100000, "Operativo", "Gasolina", "2023-01-01", "Blanco", 132)
    vehiculo2 = Vehicle("Ford", "Focus", 2015, 75000, "Operativo", "Diesel", "2022-05-15", "Negro", 150)
    vehiculo3 = Vehicle("Honda", "Civic", 2010, 120000, "Operativo", "Gasolina", "2023-06-12", "Rojo", 140)

    # Agregar vehículos al sistema
    sistema.agregar_vehiculo(vehiculo1)
    sistema.agregar_vehiculo(vehiculo2)
    sistema.agregar_vehiculo(vehiculo3)

    # Buscar vehículos del año 2015
    print("Vehículos del año 2015:")
    vehiculos_2015 = sistema.buscar_vehiculo_por_anio(2015)
    for vehiculo in vehiculos_2015:
        print(f"Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}")

    # Buscar vehículos del año 2020
    print("\nVehículos del año 2020:")
    vehiculos_2020 = sistema.buscar_vehiculo_por_anio(2020)
    for vehiculo in vehiculos_2020:
        print(f"Marca: {vehiculo.marca}, Modelo: {vehiculo.modelo}, Año: {vehiculo.anio}")


if __name__ == "__main__":
    main()
