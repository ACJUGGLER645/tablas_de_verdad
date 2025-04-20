class GeneroMusical:
    def __init__(self, genero, ritmo, armonia):
        self.genero = genero
        self.ritmo = ritmo
        self.armonia = armonia

    def imprimir_genero_musical(self):
        print(f"El genero musical es {self.genero}")
        print(f"El ritmo es {self.ritmo}")
        print(f"La armonia es {self.armonia}")


primer_genero_musical = GeneroMusical("Vallenato", 16, 3.2)
segundo_genero_musical = GeneroMusical("Techno", 4, 4.24)


primer_genero_musical.imprimir_genero_musical()
segundo_genero_musical.imprimir_genero_musical()

print(primer_genero_musical.armonia)
