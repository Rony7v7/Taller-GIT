class Vehicle:
    def __init__(self, brand, model, year, kilometers, current_status, type_fuel, service_date, potencia):
        self.brand = brand
        self.model = model
        self.year = year
        self.kilometers = kilometers
        self.current_status = current_status
        self.type_fuel = type_fuel
        self.service_date = service_date
        self.potencia = potencia  
    
    def __str__(self):
        return f'{self.brand} {self.model} {self.year} {self.kilometers} {self.current_status} {self.type_fuel} {self.service_date} {self.potencia}HP'
    
    # Getters & Setters
    def get_brand(self):
        return self.brand
    
    def set_brand(self, brand):
        self.brand = brand

    def get_model(self):
        return self.model
    
    def set_model(self, model):
        self.model = model
    
    def get_year(self):
        return self.year
    
    def set_year(self, year):
        self.year = year
    
    def get_kilometers(self):
        return self.kilometers
    
    def set_kilometers(self, kilometers):
        self.kilometers = kilometers

    def get_current_status(self):
        return self.current_status
    
    def set_current_status(self, current_status):
        self.current_status = current_status

    def get_type_fuel(self):
        return self.type_fuel
    
    def set_type_fuel(self, type_fuel):
        self.type_fuel = type_fuel

    def get_potencia(self):
        return self.potencia
    
    def set_potencia(self, potencia):
        self.potencia = potencia

