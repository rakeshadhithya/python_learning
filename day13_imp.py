#while loop
n = 5 
#infinite loop : runs infinitely without end
# while n >= 0:      
#     print('Hi')
#     print('Bye') 
# print('Outside')

n = 5 
while n >= 0:
    print(n, end=' ')
    n -= 1 
print('Outside')

n = 5 
while n <= 10:
    print(n, end=' ')
    n += 1 
print('Outside')

n = 5
while n <= 10:
    if n == 7:
        n += 1
        continue 
    print(n, end=' ')
    n += 1
else:
    print('Loop Successful')

n = 5
while n >= 0:
    if n == 3:
        break 
    print(n, end=' ')
    n -= 1
else:
    print('Loop Successful')
print()

#print 1 to 10 with while loop
n = 1 
while n <= 10:
    print(n, end=' ')
    n += 1 
print()
#print even numbers from 1 to 10
n = 2
while n <= 10:
    print(n, end=' ')
    n += 2
print()
#print numbers divisible by both 5 and 7 from 1 to 500 
n = 1 
while n <= 500:
    if n % 5 == 0 and n % 7 == 0:
        print(n, end=' ')
    n += 1 
print()

#count digits
n = int(input('Enter the number to count digits:  '))
count = 0
while n > 0:
    n = n // 10 
    count += 1
print(f'Number of digits in the given number is: {count}')

#reverse a number
n = int(input('Enter number to reverse:  '))
temp = abs(n)
rev = 0
while temp > 0:
    last_digit = temp % 10 
    rev = rev*10 + last_digit 
    temp //= 10 
if n < 0:
    rev = -rev 
print(f'Reverse of the given number is {rev}')

#palindrome number 
n = int(input('Enter a number to check palindrome:  '))
temp = abs(n)
rev = 0
while temp > 0:
    last_digit = temp % 10 
    rev = rev*10 + last_digit 
    temp //= 10 
if n < 0:
    rev = -rev 
if rev == n:
    print('Palindrome')
else:
    print('Not a Palindrome')

#armstrong number
n = int(input('Enter a number to check armstrong number:  '))
total_digits = len(str(n)) 
sum = 0 
temp = n 
while temp > 0:
    last_digit = temp % 10 
    sum += last_digit ** total_digits 
    temp //= 10 
if n == sum:
    print('Armstrong Number')
else:
    print('Not a Armstrong Number')

#palindrome string wihout slicing, without built in function
s = input('Enter a string to check palindrome:  ')
# method1 = reverse and check
# rev = ''
# for x in range(len(s)-1, -1, -1):
#     rev += s[x]
# if s == rev:
#     print('Palindrome')
# else:
#     print('Not a Palindrome')
# method2 = two pointers
i, j = 0, len(s)-1 
while i <= j:
    if s[i] != s[j]:
        print('Not a palindrome')
        break 
    i += 1 
    j -= 1 
else:
    print('Palindrome')

