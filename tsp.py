import sys
#importamos el modulo cplex
import cplex

TOLERANCE =10e-6 

class InstanciaRecorridoMixto:
    def __init__(self):
        self.cant_clientes = 0
        self.costo_repartidor = 0
        self.d_max = 0
        self.refrigerados = []
        self.exclusivos = []
        self.distancias = []        
        self.costos = []        

    def leer_datos(self,filename):
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
            row = list(map(int,linea.split(' ')))
            self.distancias[row[0]-1][row[1]-1] = row[2]
            self.distancias[row[1]-1][row[0]-1] = row[2]
            self.costos[row[0]-1][row[1]-1] = row[3]
            self.costos[row[1]-1][row[0]-1] = row[3]
        
        # cerramos el archivo
        f.close()

def cargar_instancia():
    # El 1er parametro es el nombre del archivo de entrada
    # nombre_archivo = sys.argv[1].strip()
    nombre_archivo = "instancia.txt"
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
    nombres_x = [ f'x{i+1}{j+1}' for i in range(instancia.cant_clientes) for j in range(instancia.cant_clientes) ]
    
    coef_x = [ instancia.costos[i][j] for i in range(instancia.cant_clientes) for j in range(instancia.cant_clientes) ]
    coeficientes_funcion_objetivo = coef_x

    cant_variables = len(nombres_x)

    # Agregar las variables
    prob.variables.add(obj = coeficientes_funcion_objetivo,  types= ([prob.variables.type.binary] * cant_variables), names=nombres_x)

    nombres_u = [ f'u{i+1}' for i in range(instancia.cant_clientes) ]
    coef_u = [0] * instancia.cant_clientes

    prob.variables.add(obj = coef_u,  types= ([prob.variables.type.integer] * len(nombres_u)), names=nombres_u, ub=[instancia.cant_clientes -1] * len(nombres_u))


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

    deposito = 0

    # Visitar a todos los clientes una vez
    for i in range(instancia.cant_clientes):
        variables = [ f'x{i+1}{j+1}' for j in range(instancia.cant_clientes) ]
        prob.linear_constraints.add(lin_expr=[[variables, [1.0] * len(variables)]], senses=["E"], rhs=[1], names=[f'Visitar una sola vez cliente {i+1}'])

    #conservacion
    for i in range(instancia.cant_clientes):
        variables = [ x for j in range(instancia.cant_clientes) if j != i for x in [f'x{i+1}{j+1}', f'x{j+1}{i+1}']]
        prob.linear_constraints.add(lin_expr=[[variables, [1.0, -1.0] * len(variables)]], senses=["E"], rhs=[0], names=[f'Conservacion {i+1}'])
    
    #de tour
    prob.linear_constraints.add(lin_expr=[[["u1"],[1.0]]], senses=["E"], rhs=[0], names=["detour u1"])

    for i in range(instancia.cant_clientes):
        for j in range(instancia.cant_clientes):
            if i == deposito or j == deposito: continue
            if i != j:
                prob.linear_constraints.add(lin_expr=[[[f'u{i+1}',f'u{j+1}', f'x{i+1}{j+1}'],[1.0,-1.0,instancia.cant_clientes-1]]], senses=["L"], rhs=[instancia.cant_clientes-2], names=[f'detour x{i+1}{j+1}'])

    for i in range(instancia.cant_clientes):
        if i == deposito: continue
        prob.linear_constraints.add(lin_expr=[[[f'u{i+1}'], [1.0]]], senses=["G"], rhs=[1], names=[f"cota u{i+1}"])

    for i in range(instancia.cant_clientes):
        if i == deposito: continue
        prob.linear_constraints.add(lin_expr=[[[f'u{i+1}'], [1.0]]], senses=["L"], rhs=[instancia.cant_clientes-1], names=[f"cota u{i+1}"])


def armar_lp(prob, instancia):

    # Agregar las variables
    agregar_variables(prob, instancia)
   
    # Agregar las restricciones 
    agregar_restricciones(prob, instancia)

    # Setear el sentido del problema
    prob.objective.set_sense(prob.objective.sense.minimize)

    # Escribir el lp a archivo
    prob.write('recorridoMixto.lp')

def resolver_lp(prob):
    
    # Definir los parametros del solver
    #prob.parameters.mip.....
       
    # Resolver el lp
    prob.solve()

def mostrar_solucion(prob,instancia):
    
    # Obtener informacion de la solucion a traves de 'solution'
    
    # Tomar el estado de la resolucion
    status = prob.solution.get_status_string(status_code = prob.solution.get_status())
    
    # Tomar el valor del funcional
    valor_obj = prob.solution.get_objective_value()
    
    print('Funcion objetivo: ',valor_obj,'(' + str(status) + ')')
    
    # Tomar los valores de las variables
    x  = prob.solution.get_values()

    # Mostrar las variables con valor positivo (mayor que una tolerancia)
    vars = zip(prob.variables.get_names(), x)
    print(list(vars))

def main():
    
    # Lectura de datos desde el archivo de entrada
    instancia = cargar_instancia()
    
    # Definicion del problema de Cplex
    prob = cplex.Cplex()
    
    # Definicion del modelo
    armar_lp(prob,instancia)

    # Resolucion del modelo
    resolver_lp(prob)

    # Obtencion de la solucion
    mostrar_solucion(prob,instancia)

if __name__ == '__main__':
    main()