print("Calculaor program.")
operatr = [
    "+ = Addition",
    "- = Subtraction",
    "/ = Division",
    "* = Multiplication"
]
for row in operatr:
    print(row)
try:
    a = 1
    while a < 2:
        n1 = float(input("Number: "))
        op = input("Enter Operator: ")
        n2 = float(input("Number: "))
        if op == "+":
            re = n1 + n2
            print(f'The result is {re}')
        elif op == "-":
            re = n1 - n2
            print(f'The result is {re}')
        elif op == "*":
            re = n1 * n2
            print(f'The result is {re}')
        elif op == "/":
            re = n1 / n2
            print(f'The result is {re}')
        else:
            print("Invalid input! Please try again.")
except ZeroDivisionError:
    print("The result is 0")
