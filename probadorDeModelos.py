import os

from creadorDeInstancias import CreadorDeInstancias
def main():
    creador = CreadorDeInstancias()
    creador.crear_instancia()

    # Crear carpteta de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    os.system('python tsp.py instancia.txt > resultados/outputTsp.txt')
    os.system('python nuevoModelo.py instancia.txt > resultados/outputNuevoModelo.txt')
    os.system('python modeloAdicional.py instancia.txt > resultados/outputModeloAdicional.txt')

if __name__ == '__main__':
    main()