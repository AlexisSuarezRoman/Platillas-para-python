# funcion que tiene como parametro una funcion(input tipo funcion)
def funcion_envoltoria(funcion_parametro):
    print('codigo extra de la funcion envoltoria o wrapper')
    funcion_parametro()   

def funcion_comun():
     print('codigo de la funcion comun') 

variable_con_una_funcion = funcion_comun
funcion_envoltoria(variable_con_una_funcion)
# nota sobre desventaja: tendria que crear una variable por cada 
# funcion a la que desee inyectarle el codigo extra, adicionalmente debo 
# llamar la funcion que la envuelve y esto debo hacerlo las veces que
# aparezca la funcion en el todo el codigo


