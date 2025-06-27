import sys
# importamos el modulo cplex
import cplex

TOLERANCE = 10e-6


class InstanciaRecorridoMixto:
    def __init__(self):
        self.cant_clientes = 0
        self.costo_repartidor = 0
        self.d_max = 0
        self.refrigerados = []
        self.exclusivos = []
        self.distancias = []
        self.costos = []

    def leer_datos(self, filename):
        # abrimos el archivo de datos
        f = open(filename)

        # leemos la cantidad de clientes
        self.cant_clientes = int(f.readline())
        # leemos el costo por pedido del repartidor
        self.costo_repartidor = int(f.readline())
        # leemos la distamcia maxima del repartidor
        self.d_max = int(f.readline())

        # inicializamos distancias y costos con un valor muy grande (por si falta algun par en los datos)
        self.distancias = [[1000000 for _ in range(self.cant_clientes)] for _ in range(self.cant_clientes)]
        self.costos = [[1000000 for _ in range(self.cant_clientes)] for _ in range(self.cant_clientes)]

        # leemos la cantidad de refrigerados
        cantidad_refrigerados = int(f.readline())
        # leemos los clientes refrigerados
        for i in range(cantidad_refrigerados):
            self.refrigerados.append(int(f.readline()))

        # leemos la cantidad de exclusivos
        cantidad_exclusivos = int(f.readline())
        # leemos los clientes exclusivos
        for i in range(cantidad_exclusivos):
            self.exclusivos.append(int(f.readline()))

        # leemos las distancias y costos entre clientes
        lineas = f.readlines()
        for linea in lineas:
            row = list(map(int, linea.split(' ')))
            self.distancias[row[0] - 1][row[1] - 1] = row[2]
            self.distancias[row[1] - 1][row[0] - 1] = row[2]
            self.costos[row[0] - 1][row[1] - 1] = row[3]
            self.costos[row[1] - 1][row[0] - 1] = row[3]

        # cerramos el archivo
        f.close()


def cargar_instancia():
    # El 1er parametro es el nombre del archivo de entrada
    if len(sys.argv) < 2:
        nombre_archivo = "instancias/instancia_50.txt"
    else:
        nombre_archivo = sys.argv[1].strip()
    # Crea la instancia vacia
    instancia = InstanciaRecorridoMixto()
    # Llena la instancia con los datos del archivo de entrada 
    instancia.leer_datos(nombre_archivo)
    return instancia


def agregar_variables(prob, instancia):
    # Definir y agregar las variables:
    # metodo 'add' de 'variables', con parametros:
    # obj: costos de la funcion objetivo
    # lb: cotas inferiores
    # ub: cotas superiores
    # types: tipo de las variables
    # names: nombre (como van a aparecer en el archivo .lp)

    # Poner nombre a las variables y llenar coef_funcion_objetivo
    nombres_x = [f'x{i + 1}_{j + 1}' for i in range(instancia.cant_clientes) for j in range(instancia.cant_clientes) if i != j]
    nombres_r = [f'r{i + 1}_{j + 1}' for i in range(instancia.cant_clientes) for j in range(instancia.cant_clientes) if i != j]

    nombres = nombres_x + nombres_r

    coef_x = [instancia.costos[i][j] for i in range(instancia.cant_clientes) for j in range(instancia.cant_clientes) if i != j]
    coef_r = [instancia.costo_repartidor] * len(nombres_r)
    coeficientes_funcion_objetivo = coef_x + coef_r

    cant_variables = len(nombres)
    # Agregar las variables
    prob.variables.add(obj=coeficientes_funcion_objetivo, types=([prob.variables.type.binary] * cant_variables),
                       names=nombres)

    nombres_u = [f'u{i + 1}' for i in range(instancia.cant_clientes)]
    coef_u = [0] * instancia.cant_clientes

    prob.variables.add(obj=coef_u, types=([prob.variables.type.integer] * len(nombres_u)), names=nombres_u,
                       ub=[instancia.cant_clientes - 1] * len(nombres_u), lb=[0] * len(nombres_u))

    # Eleccion de depostio
    prob.variables.add(obj=[0] * instancia.cant_clientes,
                       types=([prob.variables.type.binary] * instancia.cant_clientes),
                       names=[f'd{i + 1}' for i in range(instancia.cant_clientes)])

    # Hacer 4 entregar por repartidor
    r_aux = [f'r{i + 1}' for i in range(instancia.cant_clientes)]
    prob.variables.add(obj=[0] * len(r_aux), types=[prob.variables.type.binary] * len(r_aux), names=r_aux)


def agregar_restricciones(prob, instancia):
    # Agregar las restricciones ax <= (>= ==) b:
    # funcion 'add' de 'linear_constraints' con parametros:
    # lin_expr: lista de listas de [ind,val] de a
    # sense: lista de 'L', 'G' o 'E'
    # rhs: lista de los b
    # names: nombre (como van a aparecer en el archivo .lp)

    # Notar que cplex espera "una matriz de restricciones", es decir, una
    # lista de restricciones del tipo ax <= b, [ax <= b]. Por lo tanto, aun cuando
    # agreguemos una unica restriccion, tenemos que hacerlo como una lista de un unico
    # elemento.

    cant_clientes = instancia.cant_clientes

    # solo un deposito
    prob.linear_constraints.add(lin_expr=[[[f'd{i + 1}' for i in range(cant_clientes)], [1.0] * cant_clientes]],
                                senses=["E"], rhs=[1], names=["Solo un deposito"])

    # no visitar un cliente más de una vez

    for j in range(cant_clientes):
        variables = [f'x{i + 1}_{j + 1}' for i in range(cant_clientes) if i != j]
        prob.linear_constraints.add(lin_expr=[[variables, [1.0] * len(variables)]], senses=["L"], rhs=[1],
                                    names=[f'Visitar una sola vez cliente {j + 1}'])

    # no enviar a un repartidor a una distancia mayor a la maxima
    for i in range(cant_clientes):
        for j in range(cant_clientes):
            if i !=j:
                prob.linear_constraints.add(lin_expr=[[[f'r{i + 1}_{j + 1}'], [instancia.distancias[i][j]]]], senses=["L"],
                                        rhs=[instancia.d_max], names=[f'distancia maxima {i + 1} a {j + 1}'])

    # los repartidores deben de salir de lugares donde el camion frenó
    for i in range(cant_clientes):
        # if i == deposito: continue
        for j in range(cant_clientes):
            if i == j: continue
            variables = [f'x{k + 1}_{i + 1}' for k in range(cant_clientes) if k != i]
            valores = [1.0] * len(variables)
            variables.append(f'd{i + 1}')
            valores.append(1.0)
            variables.append(f'r{i + 1}_{j + 1}')
            valores.append(-1)
            prob.linear_constraints.add(lin_expr=[[variables, valores]], senses=["G"], rhs=[0],
                                        names=[f'r{i + 1}_{j + 1} sale desde cliente visitado'])

    # conservacion
    for i in range(cant_clientes):
        variables = [x for j in range(cant_clientes) if j != i for x in [f'x{i + 1}_{j + 1}', f'x{j + 1}_{i + 1}']]
        prob.linear_constraints.add(lin_expr=[[variables, [1.0, -1.0] * len(variables)]], senses=["E"], rhs=[0],
                                    names=[f'Conservacion {i + 1}'])

    # de tour
    for i in range(cant_clientes):
        prob.linear_constraints.add(lin_expr=[[[f'u{i + 1}', f'd{i + 1}'], [1.0, 1.0]]], senses=["G"], rhs=[1],
                                    names=[f"cota u{i + 1}"])

    for i in range(cant_clientes):
        prob.linear_constraints.add(lin_expr=[[[f'u{i + 1}', f'd{i + 1}'], [1.0, cant_clientes]]], senses=["L"],
                                    rhs=[cant_clientes], names=[f"cota u{i + 1}"])

    for i in range(cant_clientes):
        for j in range(cant_clientes):
            if i != j:
                prob.linear_constraints.add(
                    lin_expr=[[
                        [f'u{i + 1}', f'u{j + 1}', f'x{i + 1}_{j + 1}', f'd{i + 1}', f'd{j + 1}'],
                        [1.0, -1.0, cant_clientes - 1, -cant_clientes, -cant_clientes]]],
                    senses=["L"], rhs=[
                        cant_clientes - 2], names=[f'detour x{i + 1}{j + 1}'])

    # visitar a cada cliente
    for j in range(cant_clientes):
        # if j == deposito: continue
        variables = [var for k in range(cant_clientes) for var in [f'x{k + 1}_{j + 1}', f'r{k + 1}_{j + 1}'] if k != j ]
        variables.append(f'd{j + 1}')
        prob.linear_constraints.add(lin_expr=[[variables, [1.0] * len(variables)]], senses=["G"], rhs=[1.0],
                                    names=[f'Asegurarse de visitar cliente {j + 1}'])

    for i in range(cant_clientes):
        repartidores = [f'r{i + 1}_{j + 1}' for j in range(cant_clientes) if i != j]
        valores = [1 if j in instancia.refrigerados else 0 for j in range(cant_clientes) if i != j]
        prob.linear_constraints.add(lin_expr=[[repartidores, valores]], senses=["L"], rhs=[1.0],
                                    names=[f'maximo una entrega refrigerada desde {i + 1}'])

    # Restricciones adicionales por repartidor
    for i in range(cant_clientes):
        variables = [f'r{i + 1}_{j + 1}' for j in range(cant_clientes) if i != j]
        valores = [1.0] * len(variables)
        variables.append(f'r{i + 1}')
        valores.append(-4.0)
        prob.linear_constraints.add(lin_expr=[[variables, valores]], senses=["G"], rhs=[0.0],
                                    names=[f"Si un repartidor sale de {i + 1} debe hacer 4 entregas"])

        valores[-1] = -cant_clientes
        prob.linear_constraints.add(lin_expr=[[variables, valores]], senses=["L"], rhs=[0.0],
                                    names=[f"Si un repartidor sale de {i + 1} r{i + 1} debe valer 1"])

    for i in range(cant_clientes):
        if i in instancia.exclusivos:
            variables = [f'x{i + 1}_{j + 1}' for j in range(cant_clientes) if i != j]
            variables.append(f'd{i + 1}')
            valores = [1.0] * len(variables)
            prob.linear_constraints.add(lin_expr=[[variables, valores]], senses=["G"], rhs=[1],
                                        names=[f"El cliente {i + 1} requiere entrega"])


def armar_lp(prob, instancia):
    # Agregar las variables
    agregar_variables(prob, instancia)

    # Agregar las restricciones 
    agregar_restricciones(prob, instancia)

    # Setear el sentido del problema
    prob.objective.set_sense(prob.objective.sense.minimize)

    # Escribir el lp a archivo
    prob.write('modeloAdicional.lp')


def resolver_lp(prob):
    # Definir los parametros del solver
    # prob.parameters.mip.....
    
    # Mostrar progreso detallado
    prob.parameters.mip.display.set(2)
    
    # Para que se vea en consola
    prob.set_log_stream(sys.stdout)

    # Resolver el lp
    prob.solve()


def mostrar_solucion(prob, instancia):
    # Obtener informacion de la solucion a traves de 'solution'

    # Tomar el estado de la resolucion
    status = prob.solution.get_status_string(status_code=prob.solution.get_status())

    # Tomar el valor del funcional
    valor_obj = prob.solution.get_objective_value()

    print('Funcion objetivo: ', valor_obj, '(' + str(status) + ')')

    # Tomar los valores de las variables
    x = prob.solution.get_values()

    # Mostrar las variables con valor positivo (mayor que una tolerancia)
    vars = zip(prob.variables.get_names(), x)
    for var, val in vars:
        if not val == 0:
            print(var, ": ", val)


def main():
    # Lectura de datos desde el archivo de entrada
    instancia = cargar_instancia()

    # Definicion del problema de Cplex
    prob = cplex.Cplex()

    # Definicion del modelo
    armar_lp(prob, instancia)

    # Resolucion del modelo
    resolver_lp(prob)

    # Obtencion de la solucion
    mostrar_solucion(prob, instancia)


if __name__ == '__main__':
    main()
