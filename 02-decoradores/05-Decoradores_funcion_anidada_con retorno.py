# funcion anidada que tiene como parametro una funcion y 
# devuelve un objeto tipo funcion.
def funcion_envoltoria(funcion_parametro):
    print('codigo extra de la funcion envoltoria o wrapper')
    def funcion_a_envolver(): # ---> funcion anidada 
        funcion_parametro()# ---> llamado de la funcion parametro desde la funcion anidada
    return funcion_a_envolver # ---> retorna un objeto tipo funcion

def funcion_comun():
     print('codigo de la funcion comun')

variable_funcion = funcion_envoltoria(funcion_comun)
variable_funcion()

