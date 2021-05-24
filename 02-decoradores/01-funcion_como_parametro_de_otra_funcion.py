# funcion que tiene como parametro una funcion(input tipo funcion)
def funcion_envoltoria(funcion_parametro):
    print('codigo extra de la funcion envoltoria o wrapper')
    funcion_parametro()   

def funcion_comun():
     print('codigo de la funcion comun') 

funcion_envoltoria(funcion_comun)

# nota sobre desventaja: tendría que llamar la funcion wrapper y pasar como
# argumento a la funcion que deseo aplicar el wrapper. Esto tendría que 
# repetirlo las veces que aparezca llamada esta funcion en todo el codigo,
# lo cual puede ocurrir ser cientos de veces o mas. 