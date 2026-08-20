#LINK: https://www.hackerrank.com/challenges/py-if-else/problem

#LINK: https://www.hackerrank.com/challenges/write-a-function/problem

#take n, if n from 1 to 7 print dayname else print invalid day number
#e.g. 1 - Sunday, 2 - Monday, 3 - Tuesday
n = int(input('Enter the day number'))
match n:
    case 1: print('Monday')