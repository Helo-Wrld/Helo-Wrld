import random
import sys
import os
import math

print("I am thinking of a number between 1 and 20.")
num = random.randint(1, 20)

# A loop that makes the player guess 5 times
for guess in range(1, 5):
    print("Take a guess:")
    b = int(input())
    if b > num:
        print("Too high try again.")
    elif b < num:
        print("Too low try again.")
    else:
        break

# The code past the loop if you went past the limit or got it right
if b == num:
    print("Good Job!")
    sys.exit()
else:
    print("No, the number I was thinking of was" + num)
