import os

from creadorDeInstancias import CreadorDeInstancias


def main():
    # creador = CreadorDeInstancias()
    # creador.crear_instancia()

    # Crear carpteta de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    for instancia in os.listdir('instancias'):
        instancia_size = instancia.split('.')[0].split('_')[1]
        os.system(f'python nuevoModelo.py instancias/{instancia} 1 0 > resultados/outputNuevoModelo_{instancia_size}_default.txt')
        os.system(f'python nuevoModelo.py instancias/{instancia} 0 0 > resultados/outputNuevoModelo_{instancia_size}_dfs.txt')
        os.system(f'python nuevoModelo.py instancias/{instancia} 0 2 > resultados/outputNuevoModelo_{instancia_size}_dfs_raizA.txt')

if __name__ == '__main__':
    main()