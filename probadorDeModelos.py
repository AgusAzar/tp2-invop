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
    start_time = time.time()
    os.system('python nuevoModelo.py instancias/instancia_50.txt > resultados/outputNuevoModelo.txt')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo de ejecucion del nuevo modelo: {elapsed_time:.2f} segundos")
    
    start_time = time.time()
    os.system('python modeloAdicional.py instancias/instancia_50.txt > resultados/outputModeloAdicional.txt')
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Tiempo de ejecucion del modelo adicional: {elapsed_time:.2f} segundos")

if __name__ == '__main__':
    main()