#       0  1  2  3  4
list = [4, 3, 2, 5, 6]
#print elements in list with for each loop
for x in list:  
    print(x, end=' ')
print()
print()
#print elements in list with index based for loop
for x in range(len(list)):    #0 1 2 3 4
    print(list[x], end=' ')
print()
print()
#skip printing even numbers in list
for x in list:
    if x % 2 == 0:
        continue 
    print(x, end=' ')
print()
print()
#skip printing odd numbers in list
for x in list:
    if x % 2 == 1:
        continue 
    print(x, end=' ')
print()
print()
#when number 2 comes stop printing  
for x in list:
    if x == 2:
        break 
    print(x, end=' ')
print()
print()
#when first odd number comes stop printing
for x in list:
    if x % 2 == 1:
        break 
    print(x, end=' ')
print()
print()
#print numbers from 1 to 10, when all numbers are printed, print 'All numbers printed'
for x in range(1, 11):
    print(x, end=' ')
else:
    print('All numbers are printed')
print()
print()
#print numbers from 1 to 10, skipping even numbers, when all numbers are printed, print 'All numbers printed'
for x in range(1, 11):
    if x % 2 == 0:
        continue 
    print(x, end=' ')
else:
    print('All numbers are printed')
print()
print()
#print numbers from 10 to 1, when 5 comes stop printing, when all numbers are print, print 'All numbers printed'
for x in range(10, 0, -1):
    if x == 5:
        break
    print(x, end=' ')
else:
    print('All numbers are printed')