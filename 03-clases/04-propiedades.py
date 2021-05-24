class Animal:
    
    def __init__(self,claseIn, especieIn, razaIn, precioIn):
        self.clase = claseIn
        self.especie = especieIn
        self.raza = razaIn
        self._precio = precioIn
    
    @property
    def precioSecreto(self):
        return self._precio
	
    @precioSecreto.setter
    def precioSecreto(self, nuevo_precio): 
        self._precio = nuevo_precio
    
    @precioSecreto.deleter
    def precioSecreto(self):
        del self._precio
    

dog = Animal('mamifero','perro',"labrador golden",100000 )
cat = Animal('mamifero','gato', 'criollito',5000)



print('------------------------------------')
print(dog.clase)
print(dog.especie)
print(dog.raza)
print(dog._precio)
print(dog.precioSecreto)
print('------------------------------------')
print(cat.clase)
print(cat.especie)
print(cat.raza)
print('------------------------------------')
print(dog.clase)
print(dog.especie)
print(dog.raza)