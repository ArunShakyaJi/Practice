a = input("Enter the first number: ")
opeartor = input("Enter the operator (+, -, *, /): ")
b = input("Enter the second number: ")

if opeartor == "+":
    result = float(a) + float(b)
elif opeartor == "-":
    result = float(a) - float(b)
elif opeartor == "*":
    result = float(a) * float(b)
elif opeartor == "/":
    if float(b) == 0:
        result = "Error: Division by zero is not allowed."
    else:
        result = float(a) / float(b)

print("The result of {} {} {} is {}".format(a, opeartor, b, result))
