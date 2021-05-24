# funcion con parametros de entrada(input) y sin datos retorno(output)
def funcion_comun(dato_entrada='parametro por defecto'):
     print(dato_entrada)

# llamado de funcion con parametro
funcion_comun('parametro')

# llamado de funcion usando el parametro por defecto
funcion_comun()

# NOTA IMPORTANTE: un parametro por defecto no debe temer otro parametro 
# sin defecto a su derecha, ya que genera error, por ejemplo:
# def funcion_comun(dato_entrada='parametro por defecto', segundo dato):