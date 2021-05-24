# funcion anidada 
def funcion_envoltoria():
    print('codigo de la funcion envoltoria o wrapper')
    def funcion_a_envolver(): # ---> funcion anidada 
        print('codigo funcion anidada')
    funcion_a_envolver() # ---> llamado de la funcion anidada 

funcion_envoltoria()


