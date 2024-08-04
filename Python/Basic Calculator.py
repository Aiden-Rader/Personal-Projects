
num1 = input("Enter a digit: ")
num2 = input("Enter some other digit: ")
calc = input("Choose what type of calculation you would like to use: ")

if calc == ('+'):
    result = float(num1) + float(num2)
    print(result)  

elif calc == ('-'):
    result = float(num1) - float(num2)
    print(result)

elif calc == ('/'):
    result = float(num1) / float(num2)
    print(result)

elif calc == ('*'):
    result = float(num1) * float(num2)
    print(result)

if result == 0:
    raise ZeroDivisionError





