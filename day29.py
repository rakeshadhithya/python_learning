# # print(Z.__dict)          #Z is not defined
# print(object.__dict__)
# print()
# class A(object):    #remove object and see
#     pass 
# print(A.__str__)
# print(A.__repr__)
# print(A.__lt__)
# print()

# # Superclass
# class Vehicle:
#     def start(self):
#         print("Vehicle is starting")
#     def stop(self):
#         print("Vehicle is stopping")


# # 1. Single Inheritance
# class Car(Vehicle):
#     def drive(self):
#         print("Car is driving")


# # 2. Multilevel Inheritance
# class SportsCar(Car):
#     def race(self):
#         print("Sports car is racing")


# # 3. Hierarchical Inheritance
# class Bike(Vehicle):
#     def ride(self):
#         print("Bike is riding")


# # 4. Multiple Inheritance
# class Electric:
#     def charge(self):
#         print("Battery is charging")

# class ElectricCar(Vehicle, Electric):
#     def drive(self):
#         print("Electric car is driving")

# # 5. Hybrid Inheritance
# # Combination of multilevel + multiple inheritance
# class HybridCar(Car, Electric):
#     def hybrid_drive(self):
#         print("Hybrid car is driving")


# print('Vehicle') 
# v = Vehicle()
# v.start()       
# v.stop()       
# print()

# print("Single Inheritance:")
# c = Car()  
# c.start()  
# c.drive()   
# print()

# print("Multilevel Inheritance:")  
# s = SportsCar()
# s.start()   
# s.drive()   
# s.race()   
# print()

# print("Hierarchical Inheritance:") 
# b = Bike()
# b.start()    
# b.ride()    
# print()

# print("Multiple Inheritance:")      
# e = ElectricCar()
# e.start()    
# e.charge()    
# e.drive()    
# print()

# #mro
# print('MRO')                
# print(ElectricCar.mro())
# print(ElectricCar.__mro__)
# print()

# print("Hybrid Inheritance:") 
# h = HybridCar()
# h.start()        
# h.drive()      
# h.charge()      
# h.hybrid_drive()
# print()


# #super()
# class A:
#     def show(self):
#         print("A")

# class B(A):
#     def show(self):
#         super().show()  #here after B, C not A in mro
#         print("B")

# class C(A):
#     def show(self):
#         super().show()
#         print("C")

# class D(B, C):
#     def show(self):
#         super().show()
#         print("D")
# d = D()
# print(D.__mro__)
# d.show()

