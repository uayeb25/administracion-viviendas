from classes import Cliente

class Casa:

    def __init__(self, numero, metrosConstruccion, cliente):
        self.numero = numero
        self.metrosConstruccion = metrosConstruccion
        self.cliente = cliente
        self.cliente.casas.append(self)
        print('Casa objeto instanciado')

    def info_casa(self):
        print( "La casa con numero {0}, tiene de duenio: {1}".format( self.numero , self.cliente.nombre ) )
    
    