#single import
import calculator 

# members are not imported
#functions
# print(add(20,10))   #error, add is not there in current module
# print(sub(20,10))     #error, sub is not there in current module
# print(mul(20,10))     #error, mul is not there in current module
# print(div(20,10))     #error, div is not there in current module
#classes
# c = Calculator()      #error, Calculator class is not there in current module
#objects 
# print(c1)             #error, c1 is not there in current module
# print(c2)             #error, c2 is not there in current module

#module is imported
#functions
print(calculator.add(20,10))  #30
print(calculator.sub(20,10))  #10
print(calculator.mul(20,10))  #200
print(calculator.div(20,10))  #2.0
#classes
c = calculator.Calculator()
#objects 
print(calculator.c1)      #101
print(calculator.c2)      #201

 