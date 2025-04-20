class Auto:
    def __init__(self, modelo, marca, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año
    
    def mostrar_info(self):
        print(f"El modelo del carro es {self.modelo}, la marca es {self.marca} del año {self.año}")


primer_carro = Auto("Iberica","Susuki",2016)
primer_carro.mostrar_info()