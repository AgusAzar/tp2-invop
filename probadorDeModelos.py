import os

from creadorDeInstancias import CreadorDeInstancias


def main():
    # creador = CreadorDeInstancias()
    # creador.crear_instancia()

    # Crear carpteta de resultados si no existe
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    for instancia in os.listdir('resultados_exp/exp 3/instancias'):
        print(instancia)
        isntancia_name = instancia.split('.')[0]
        os.system(f'python nuevoModelo.py "resultados_exp/exp 3/instancias/{instancia}" 1 0 > resultados/outputNuevoModelo_{isntancia_name}.txt')
        os.system(f'python modeloAdicionalRequeridos.py "resultados_exp/exp 3/instancias/{instancia}" 0 0 > resultados/outputAdicionalRequeridos_{isntancia_name}.txt')


if __name__ == '__main__':
    main()
