#important problems
#1. print numbers from 1 to 10 
for x in range(1, 11):
    print(x, end=' ')
print('\n')

list = [4,3,5,2,5,2,9,1,7,4,6,8]
#2. print even numbers from 5 to 30 and above list
for x in range(5, 31):  
    if x % 2 == 0:
        print(x, end=' ')
print()
for x in list:
    if x % 2 == 0:
        print(x, end=' ')
print('\n')

#3. print odd numbers from 5 to 30 and above list
for x in range(5, 31):
    if x % 2 == 1:
        print(x, end=' ')
print()
for x in list:
    if x % 2 == 1:
        print(x, end=' ')
print('\n')

#4. print numbers divisible by 5 from 1 to 30 and above list
for x in range(1, 31):
    if x % 5 == 0:
        print(x, end=' ')
print()
for x in list:
    if x % 5 == 0:
        print(x, end=' ')
print('\n')
#5. print numbers divisible by both 5 and 7 from 1 to 100 and above list
for x in range(1, 101):
    if x % 5 == 0 and x % 7 == 0:
        print(x, end=' ')
print()
for x in list:
    if x % 5 == 0 and x % 7 == 0:
        print(x, end=' ')
print('\n')

#6. sum of numbers from 10 to 25 and above list
sum = 0
for x in range(10, 26):
    sum += x
print('Sum of numbers from 10 to 25 is: ', sum)
print()
sum = 0
for x in list:  
    sum += x 
print('Sum of numbers in given list is, ', sum)

#7. multiplication table of a number 
n = int(input('Enter a number for multiplication:  '))
for i in range(1, 11):
    print(f'{n} x {i} = {n * i}')
print()
#8. factorial 
n = int(input('Enter a number for factorial:  '))
product = 1 
for x in range(1, n + 1):
    product *= x 
print(f'Factorial of {n} is {product}')
#9. fibonacci 
n = int(input('Enter number of fibonacci terms:  '))
a = 0
b = 1
for x in range(n):
    print(a, end=' ')
    a, b = b, a+b 
print()
#10. reverse a string
string = input('Enter a string:  ')
rev = ''
for x in range(len(string)-1, -1, -1):
    rev += string[x]
print(f'Reverse of {string} is {rev}')

#11. count vowels in a string
s = input('Enter the string to count vowels:  ')
count = 0
for c in s:
    if c in 'aeiouAEIOU':
        count += 1 
print(f'Total vowels in the string is {count}')
#12. count z's and y's in a string
s = input('Enter the string to count z\'s and y\'s: ')
count = 0
for c in s:
    if c in 'zZyY':
        count += 1
print('Total z\'s and y\'s in given string is', count  )

#13. check whether a number is prime number or not 
n = int(input('Enter a number to check prime:  '))
if n < 2:
    print('Not Prime')
else:
    for x in range(2, int(n**0.5)+1):
        if n % x == 0:
            print('Not Prime')
            break
    else:
        print('Prime')