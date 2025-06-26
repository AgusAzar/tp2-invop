import os

from creadorDeInstancias import CreadorDeInstancias


def main():
    # creador = CreadorDeInstancias()
    # creador.crear_instancia()

    # Crear carpteta de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')

    os.system('python nuevoModelo.py instancias/instancia.txt 1 0 > instancias/outputNuevoModelo_default.txt')
    # os.system('python nuevoModelo.py instancias/instancia.txt 0 0 > instancias/outputNuevoModelo_dfs.txt')
    # os.system('python nuevoModelo.py instancias/instancia.txt 0 2 > instancias/outputNuevoModelo_dfs_raizA.txt')

if __name__ == '__main__':
    main()