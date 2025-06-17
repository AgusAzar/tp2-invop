import os

from creadorDeInstancias import CreadorDeInstancias
def main():
    creador = CreadorDeInstancias()
    creador.crear_instancia()

    os.system('python tsp.py instancia.txt > outputTsp.txt')
    os.system('python nuevoModelo.py instancia.txt > outputNuevoModelo.txt')
    os.system('python modeloAdicional.py instancia.txt > outputModeloAdicional.txt')

if __name__ == '__main__':
    main()