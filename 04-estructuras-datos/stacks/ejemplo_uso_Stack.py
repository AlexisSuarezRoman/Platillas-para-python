# una lista es un ejemplo de stack(pila en español),
# es un tipo de dato LIFO(Last In Firt Out)
# El stack es un tipo de dato abstracto que se usa en muchos lenguajes 
# de programacion y cumple unas funciones especificas.
# sus metodos son append() en python o push() en otros lenguajes de programacion
# el cual agrega un elemento al final del stack,
# pop() el cual retira el ultimo elemento del stack.

# el siguiente es un ejerciocio que implemente el uso de un stack para 
# crear una funcion, la cual verifica que el orden de los signos 
# parentesis,corchetes y llaves se a correcto

def comprobar(cadena_caracteres):
    signos = {
        '(':')',
        '{':'}',
        '[':']',
    }
    ordenSignos = [] 


    for caracter in cadena_caracteres:
        if caracter in signos.keys():
            ordenSignos.append(signos[caracter])
            continue
        if ordenSignos and caracter in signos.values() and caracter != ordenSignos[-1]:
            return 'esta mal'
        if ordenSignos and caracter in signos.values() and caracter == ordenSignos[-1]:
            ordenSignos.pop()
            
    if ordenSignos:
        return 'esta mal'
    return 'esta bien'
                 
cadena1 = '[]{}()'
listasimbolos = comprobar(cadena1)
print(listasimbolos)
print('-----------------------------')
cadena1 = '[{](})'
listasimbolos = comprobar(cadena1)
print(listasimbolos)