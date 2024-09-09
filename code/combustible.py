class combustible:
    COMBUSTIBLES_VALIDOS = ["Gasolina", "Diesel", "Eléctrico"]

    def __init__(self, marca, modelo, tipo_combustible):
        self.marca = marca
        self.modelo = modelo
        self.tipo_combustible = None  
        self.set_tipo_combustible(tipo_combustible)

    def set_tipo_combustible(self, tipo_combustible):
        if tipo_combustible not in Vehiculo.COMBUSTIBLES_VALIDOS:
            raise ValueError(f"Tipo de combustible inválido. Debe ser uno de {Vehiculo.COMBUSTIBLES_VALIDOS}.")
        self.tipo_combustible = tipo_combustible

    def __str__(self):
        return f"Vehiculo(marca={self.marca}, modelo={self.modelo}, combustible={self.tipo_combustible})"
