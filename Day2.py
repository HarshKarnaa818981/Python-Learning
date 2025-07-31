name = print('What is ur Name?')
print('Hello harsha',name)
age = input('Enter your age:')
print(age)
print(type(age))
age = int(input('Enter your age:'))
print('Next year,youll be age',age+1) 

#Simple Calculator

num1 = float(input('Enetr first number: '))
num2 = float(input('Enter second number: '))
operation = input('Enter opertaion:(+,-,*,/)')
if operation == '+':
    result = num1+num2
elif operation == '-':
    result = num1-num2
elif operation == '*':
    result = num1*num2
elif operation == '/':
    if num2 !=0:
        result = num1/num2
else:
    print('Invalid operation')
    result = None  
print('Result:', result)
          