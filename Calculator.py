print("Calculaor program.")
operatr = [
    "+ = Addition",
    "- = Subtraction",
    "/ = Division",
    "* = Multiplication"
]
for row in operatr:
    print(row)
a = 1
while a <= 2:
    try:
        print("Calculator program")
        n1 = float(input(": "))
        s = input("Operator: ")
        n2 = float(input(": "))
        if s == "+":
            e1 = n1 + n2
            print(f"result: {e1}")
        elif s == "-":
            e2 = n1 - n2
            print(f"result: {e2}")
        elif s == "/":
            e3 = n1 / n2
            print(f"result: {e3}")
        elif s == "*":
            e4 = n1 * n2
            print(f"result: {e4}")
        elif s == "%":
            e = n1 % n2
            print(f"result: {e}")
        else:
            print("Invalid input!")
    except ZeroDivisionError:
        print("Number can not be 0.")
    except ValueError:
        print("Invalid value")
