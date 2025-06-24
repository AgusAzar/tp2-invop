import os

from creadorDeInstancias import CreadorDeInstancias


def main():
    # creador = CreadorDeInstancias()
    # creador.crear_instancia()

    # Crear carpteta de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    
    os.system('python nuevoModelo.py instancias/instancia.txt 1 0 1 > instancias/outputNuevoModelo.txt')
    # os.system('python nuevoModelo.py 3_min/instancia_50_5.txt 0 0 1 > 3_min/outputNuevoModelo_dfs.txt')
    # os.system('python nuevoModelo.py 3_min/instancia_50_5.txt 2 0 1 > 3_min/outputNuevoModelo_bestT.txt')
    # os.system('python nuevoModelo.py 3_min/instancia_50_5.txt 3 0 1 > 3_min/outputNuevoModelo_bestT_alt.txt')
    
    os.system('python modeloAdicional.py instancias/instancia.txt 1 0 1 > instancias/outputModeloAdicional.txt')
    # os.system('python modeloAdicional.py 3_min/instancia_50_5.txt 0 0 1 > 3_min/outputModeloAdicional_dfs.txt')
    # os.system('python modeloAdicional.py 3_min/instancia_50_5.txt 2 0 1 > 3_min/outputModeloAdicional_bestT.txt')
    # os.system('python modeloAdicional.py 3_min/instancia_50_5.txt 3 0 1 > 3_min/outputModeloAdicional_bestT_alt.txt')


if __name__ == '__main__':
    main()