def addition(a,b):
    return a+b

def subtraction(a,b):
    return a-b

def multiplication(a,b):
    return a*b

def division(a,b):
    if b==0:
        return ValueError("Cannot divide by zero")
    return a/b


print('Simple Calculator')
number1 = float(input('Enter first number:'))
number2 = float(input("Enter second number:"))
action = input("Enter operation (+,-,*,/):")

if action =='+':
    result = addition(number1,number2)
elif action == '-':
    result = subtraction(number1, number2)
elif action == '*':
    result = multiplication(number1, number2)
elif action =='/':
    result = division(number1,number2)
else:
    rresult = 'invalid operation!'

print(f"The result is:{result}")
