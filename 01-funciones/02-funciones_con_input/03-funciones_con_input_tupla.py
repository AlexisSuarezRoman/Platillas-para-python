# funcion con parametro de entrada tupla(input-*args) y sin datos retorno(output)
def funcion_comun(*datos_entrada):
     for elemento in datos_entrada:
          print(elemento)

# ejecucion de la funcion o llamado de funcion 
funcion_comun('parametro uno','parametro dos','parametro tres')
