import os
import time

from creadorDeInstancias import CreadorDeInstancias
def main():
    # creador = CreadorDeInstancias()
    # creador.crear_instancia()

    # Crear carpteta de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    os.system('python tsp.py instancias/instancia_50.txt > resultados/outputTsp.txt')
    
    # empezar a contar el tiempo de ejecucion del nuevo modelo
    os.system('python nuevoModelo.py instancias/instancia_50.txt > resultados/outputNuevoModelo.txt')

    os.system('python modeloAdicional.py instancias/instancia_50.txt > resultados/outputModeloAdicional.txt')

if __name__ == '__main__':
    main()