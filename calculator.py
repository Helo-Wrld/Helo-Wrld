print("Enter first num: ")
x = input()
print("Enter operation sign: ")
sign = input()
print("Enter second num: ")
y = input()

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


