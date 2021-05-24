# funcion anidada que tiene como parametro una funcion.
def funcion_envoltoria(funcion_parametro):
    print('codigo extra de la funcion envoltoria o wrapper')
    funcion_parametro() # ---> llamado de la funcion parametro desde la funcion wrapper
    def funcion_a_envolver(): # ---> funcion anidada 
        print('codigo funcion anidada')
        funcion_parametro() # ---> llamado de la funcion parametro desde la funcion anidada
    funcion_a_envolver() # ---> llamado de la funcion anidada 

def funcion_comun():
     print('codigo de la funcion comun')

funcion_envoltoria(funcion_comun)


