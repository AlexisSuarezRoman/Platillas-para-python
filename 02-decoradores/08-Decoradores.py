def funcion_envoltoria(funcion_parametro):
    print('codigo extra de la funcion envoltoria o wrapper')
    def funcion_a_envolver():
        funcion_parametro()
    return funcion_a_envolver

@funcion_envoltoria # aplicacion del decorador 
def funcion_comun():
     print('codigo de la funcion comun')

funcion_comun()

