from classes import *

def main():
    cliente = Cliente(1,"uayeb")
    casa = Casa(2, 456, cliente)
    casa.info_casa()
    


if __name__ == "__main__":
    main()