# funcion con parametro de entrada key-value o 
# diccionario(input tipo **kwargs) y sin datos retorno(output)

def funcion_comun(**datos_entrada):
     for llave, valor in datos_entrada.items():
          print(llave + ': ' + valor)
     #NOTA: prestar especial cuidado a la sintaxis de diccionario.items()

# ejecucion de la funcion o llamado de funcion 
funcion_comun(uno='parametro uno',dos='parametro dos',tres='parametro tres')
