class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.casas = []

    def mis_metros_cuadrados(self, numero_casa):

        encontro = False
        for casa in self.casas:
            if casa.numero == numero_casa:
                encontro = True
                print("metros cuadrados de casa numero {0}: {1} mt2".format(numero_casa, casa.metrosConstruccion))
                break
        
        if not encontro:
            print("ID no encontrado")
        