class HistorialMantenimiento:
    def __init__(self, fecha, descripcion_servicio, kilometraje_en_servicio, costo, nombre_mecanico):
        self.__fecha = fecha
        self.__descripcion_servicio = descripcion_servicio
        self.__kilometraje_en_servicio = kilometraje_en_servicio
        self.__costo = costo
        self.__nombre_mecanico = nombre_mecanico

    # Métodos getter
    def get_fecha(self):
        return self.__fecha

    def get_descripcion_servicio(self):
        return self.__descripcion_servicio

    def get_kilometraje_en_servicio(self):
        return self.__kilometraje_en_servicio

    def get_costo(self):
        return self.__costo

    def get_nombre_mecanico(self):
        return self.__nombre_mecanico

    # Métodos setter
    def set_fecha(self, fecha):
        self.__fecha = fecha

    def set_descripcion_servicio(self, descripcion_servicio):
        self.__descripcion_servicio = descripcion_servicio

    def set_kilometraje_en_servicio(self, kilometraje_en_servicio):
        self.__kilometraje_en_servicio = kilometraje_en_servicio

    def set_costo(self, costo):
        self.__costo = costo

    def set_nombre_mecanico(self, nombre_mecanico):
        self.__nombre_mecanico = nombre_mecanico

    def __str__(self):
        return (f"Fecha: {self.__fecha}\n"
                f"Descripción del servicio: {self.__descripcion_servicio}\n"
                f"Kilometraje en servicio: {self.__kilometraje_en_servicio}\n"
                f"Costo: {self.__costo}\n"
                f"Nombre del mecánico: {self.__nombre_mecanico}")

