from classes import *

def main():
    cliente = Cliente(1,"uayeb")
    casa = Casa(2, 456, cliente)
    casa.info_casa()
    print(cliente.casas[0].numero)
    cliente.mis_metros_cuadrados(2)
    


if __name__ == "__main__":
    main()