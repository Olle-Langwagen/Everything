from wsgiref.validate import InputWrapper


firstNum = int(input("Pick your first number: "))
op = input("Pick an operator:")
secNum = int(input("Pick your second number: "))

if op == "+":
    print(firstNum + secNum)
elif op == "/":
    print(firstNum/secNum)
elif op == "-":
    print(firstNum - secNum)
elif op == "*":
    print(firstNum*secNum)
