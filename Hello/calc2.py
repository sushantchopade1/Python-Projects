num1 = float(input("Enter 1st no."))
op = input("enter operator")
num2 = float(input("Enter 2nd no."))

if op == "+":
    print(num1 +num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("invalid operator")
