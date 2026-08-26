#LINK: https://www.hackerrank.com/challenges/py-if-else/problem
if __name__ == '__main__':
    n = int(input().strip())
    if n % 2 == 1:
        print('Weird')
    elif n % 2 == 0 and 2 <= n <= 5:
        print('Not Weird')
    elif n % 2 == 0 and 6 <= n <= 20:
        print('Weird') 
    elif n % 2 == 0 and n > 20:
        print('Not Weird')

#LINK: https://www.hackerrank.com/challenges/write-a-function/problem
def is_leap(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False
    
#take n, if n from 1 to 7 print dayname, if > 7 print invalid day number
#e.g. 1 - Sunday, 2 - Monday, 3 - Tuesday
n = int(input('Enter the day number:  '))
match n:
    case 1: print('Sunday')
    case 2: print('Monday')
    case 3: print('Tuesday')
    case 4: print('Wednesday')
    case 5: print('Thursday')
    case 6: print('Friday')
    case 7: print('Saturday')
    case _: print('Invalid day number')
    