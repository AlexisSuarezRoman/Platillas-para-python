class Animal:
    
    def __init__(self,claseIn, especieIn, razaIn):
        self.clase = claseIn
        self.especie = especieIn
        self.raza = razaIn
    

dog = Animal('mamifero','perro',"labrador golden" )
cat = Animal('mamifero','gato', 'criollito')

cat.raza = 'egipcio'

print('------------------------------------')
print(dog.clase)
print(dog.especie)
print(dog.raza)
print('------------------------------------')
print(cat.clase)
print(cat.especie)
print(cat.raza)
print('------------------------------------')
print(dog.clase)
print(dog.especie)
print(dog.raza)