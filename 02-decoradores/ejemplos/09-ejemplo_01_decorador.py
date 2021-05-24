def externa(funt):
    'instrucciones antes del wrapper'
    print('|-----------|')
    def interna():
        funt()
        print('|-----------|')
    return interna
    
@externa
def funcion_comun():
    print('texto')
    
funcion_comun()