print("Enter first num: ")
x = input()
print("Enter operation sign: ")
sign = input()
print("Will there be a second num: (y) or (n)")
v = input()
if v == 'y':
    
print("Enter second num: ")
y = input()

if x != int:
    print("Incorrect first num, try again")

if y != int:
    print("Incorrect second num, try again")

if sign == '+':
    print(x + y)
elif sign == '-':
    print(x - y)
elif sign == '/':
    print(x / y)
elif sign == '*':
    print(x * y)
elif sign == '^':
    print(x ** y)
elif sign == 'sqrt':
    print()
else:
    print("Incorrect operation value, try again")


