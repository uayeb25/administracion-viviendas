class Cliente:
    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.casas = {}

    def mis_metros_cuadrados(self, numero_casa):

        print( self.casas[numero_casa].metrosConstruccion )
        