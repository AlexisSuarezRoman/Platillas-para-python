# funcion sin parametros de entrada(input) y con datos retorno(output)
def funcion_comun():
     return 'primer dato','segundo dato','tercer dato','cuarto dato','quinto dato','sexto dato'

# almacenamiento del valor de retorno de la funcion en variables individuales
primer_dato, *resto_datos, ultimo_dato = funcion_comun()

#impresion variables individuales
print(primer_dato)
print(resto_datos)
print(ultimo_dato)


