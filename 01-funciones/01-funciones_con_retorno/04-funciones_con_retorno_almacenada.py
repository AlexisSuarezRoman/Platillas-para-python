# funcion sin parametros de entrada(input) y con datos retorno(output)
def funcion_comun():
     return 'dato retorno'

# Almacenamiento de la funcion misma en una variable en memoria(ram)
variable_almacena_funcion = funcion_comun

# lo siguiente es equivalente a: print(funcion_comun())
print(variable_almacena_funcion())

