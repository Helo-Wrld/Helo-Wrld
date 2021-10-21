import sys
import time


def collatz(number):
    if a == -1:
        print(' ')
        print('Exiting Program', end='')
        time.sleep(1)
        print(' . ', end='')
        time.sleep(1)
        print('. ', end='')
        time.sleep(1)
        print('.', end='')
        sys.exit()
    elif a % 2 == 0:
        print(number // 2)
    elif a % 2 != 0:
        print(3 * number + 1)


while True:
    print('Enter a number: ', end='')
    a = int(input())
    collatz(a)
