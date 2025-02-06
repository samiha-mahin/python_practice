n1 = float(input("Enter first number: "))
n2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == '+':
    print("result:", {n1 + n2})
elif operation == '-':
    print("result:",{n1 - n2})
elif operation == '*':
    print("result:" ,{n1 * n2})
elif operation == '/':
    if n2 != 0:
        print("result: ",{n1/n2})
    else:
        print("Division by zero is not allowed")
else:
    print("Invalid operation")