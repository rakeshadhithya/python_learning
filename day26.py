#class definition
class c1:
    def method1(self):
        pass 
    def method2(self):
        pass

#classes with same name
class c1:
    def greet(self):
        print('good morning') 
class c1:                         #same name
    def greet(self):
        print('hi')
class c1:
    def greet(self):
        print('hello')
c = c1()
c.greet()

#object creation and assigning variable
class c1:
    def greet(self):
        print('Hello')
c = c1() 
print(id(c))
print(type(c)) 


#Different ways of calling an menthod
class Display():
    def display(rakesh):
        print(rakesh)
d1 = Display() 
d2 = Display() 
d1.display()         #object.method
d2.display() 
Display.display(d1)  #Classname.method(object)
Display.display(d2)

#python objects are dynamic: varaibles can grow or shrink
class c1:
    def m1(self):
        print(self.x)
a = c1()
# a.m1()
a.x = 10
a.m1()
a.x = 20
a.m1()
del a.x
a.m1()



# Variables in Class 
#1. Static Variables
# creation
class Student:
    college = 'Malineni'
    # Student.department = 'CSE'  
    def m1(self):
        rollno = 1
        Student.rollno = 2       
age = 11 
Student.age = 22               
s = Student()
s.m1()
print(Student.__dict__)
print(s.__dict__)

#access
class Student:
    college = 'Malineni'
s = Student()
print(s.college)
print(Student.college)

#modification
class Student:
    college = 'Malineni'
    def __init__(self, rollno):
        self.rollno = rollno 
s1 = Student(1)
s2 = Student(2)
print(f'{s1.college}, {s1.rollno}')
print(f'{s2.college}, {s2.rollno}')
print()
s2.college = 'Laxmaiah'         #modify through object(creates instance variable)
print(f'{s1.college}, {s1.rollno}')
print(f'{s2.college}, {s2.rollno}')
del s2.college 
print()
Student.college = 'Laxmaiah'    #modify through class
print(f'{s1.college}, {s1.rollno}')
print(f'{s2.college}, {s2.rollno}')


#2. Instance variable (same prog as above)
class c1:
    def m1(self):
        print(self.x)
a = c1()
# a.m1()
a.x = 10
a.m1()
a.x = 20
a.m1()
del a.x
a.m1()


# Type of methods in class 
#1. Static Method: No first arg, not tied to class data and object data. helper method
class College:
    def m1(a,b,c):
        print(a,b,c)
    @staticmethod 
    def m2(a,b,c):
        print(a,b,c)
c = College() 
College.m1(1,2,3) 
# c.m1(4,5,6)
c.m1(4,5)
College.m2(10,20,30)
c.m2(40, 50, 60)

#2. Class method: first argument is class. tied to class data
class College:
    @classmethod 
    def m1(a, b, c):
        print(a, b, c)
c = College() 
College.m1(4, 5)
c.m1(6,7)          #class is pass even though called with object

#3. instance method: first argument is object. tied to object
class College:
    def m1(self, b):
        print(b) 
c = College()
c.m1(10)
College.m1(c, 20)
