class CreadorDeInstancias:

    def __init__(self):
        self.cant_clientes = 5
        self.costo_repartidor = 5
        self.d_max = 5
        self.distancias = []
        self.refrigerados = []
        self.exclusivos = []
        self.filename = "instancia.txt"

    def crear_distancia(self, desde, hasta, distancia_repartidor, costo_camion):
        self.distancias.append(f"{desde} {hasta} {distancia_repartidor} {costo_camion}\n")

    def crear_instancia(self):
        self.crear_distancia(1,2,10,100)
        self.crear_distancia(1,3,10,100)
        self.crear_distancia(3,2,10,100)
        self.crear_distancia(1,4,1,10000)
        self.crear_distancia(2,5,1,10000)
        self.crear_distancia(3,5,1,10000)
        self.crear_distancia(2,4,1,10000)
        self.refrigerados = [1]
        self.exclusivos = [2]
        # abrimos el archivo de datos
        f = open(self.filename, "w")
        f.write(str(self.cant_clientes) + "\n")
        f.write(str(self.costo_repartidor) + "\n")
        f.write(str(self.d_max) + "\n")
        f.write(str(len(self.refrigerados)) + "\n")
        f.writelines([f"{x}\n" for x in self.refrigerados])
        f.write(str(len(self.exclusivos)) + "\n")
        f.writelines([f"{x}\n" for x in self.exclusivos])
        f.writelines(self.distancias)

        f.close()


def main():
    creador = CreadorDeInstancias()
    creador.crear_instancia()


if __name__ == '__main__':
    main()