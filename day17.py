#List comprehension
a = []
for x in range(1,11):
    a.append(x)
print(a)


b = [x for x in range(1,11)]
print(b)

c = []
for x in range(1,11):
    if x % 2 == 0:
        c.append(x) 
print(c)

d = [x for x in range(1,11) if x % 2 == 0]
print(d)

e = []
for x in range(1,4):
    for y in range(4,6):
        e.append((x,y))
print(e)
f = [(x,y) for x in range(1,4) for y in range(4,6)]
print(f)

f = {x for x in range(1,11)}
print(f)
g = {x:x**2 for x in range(1,11)}
print(g)
h = (x for x in range(1,11))
print(h)

def numbers():
    for x in range(1,11):
        if x % 2 == 0:
            yield x 
n = numbers()
print(type(n))
print(next(n))
print(next(n))
print(next(n))
print(n.__next__())
print(n.__next__())
print(next(n))

g = (x for x in range(1,11))
print(type(g))
print(g)
for i in g:
    print(i, end=' ')