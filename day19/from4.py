#__all__ 
from physics import * 
from calculator import * 
from biology import * 

#all members of biology module
print(dna())     #dna information
print(genes())   #genes info
b = Biology()    #object of biology is created
print(b1)        #dna
print(b2)        #Protien
print()

#all members of physics module
print(newtonsfirst())
print(newtonssecond())
print(newtonsthird())
p = Physics() 
print(p1)
print(p2)
print()

#all members of calculator module
print(add(20,10))   #30
print(sub(20,10))   #20
print(mul(20,10))
print(div(20,10))
c = Calculator()
print(c1)
print(c2)

# change __all__ of calculator(__all__ = ['add', 'c1']) and check