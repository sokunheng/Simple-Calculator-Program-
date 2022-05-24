import os
import colorama
from colorama import Fore, Back, Style
colorama.init(autoreset=True)
os.system("cls")
"""
 => Old Version

operatr = [
    "         + = Addition",
    "         - = Subtraction",
    "         / = Division",
    "         * = Multiplication"
]
for row in operatr:
    print(row)
"""

print(f"{Fore.BLUE}======================================")
print(f"     {Fore.GREEN}Welcome To Calculaor Program.")
print(f"          {Fore.BLUE}+ {Fore.WHITE}= Addition")
print(f"          {Fore.GREEN}- {Fore.WHITE}= Subtraction")
print(f"          {Fore.MAGENTA}/ {Fore.WHITE}= Division ")
print(f"          {Fore.RED}* {Fore.WHITE}= Multiplication")
print(f"{Fore.BLUE}======================================")
print(f"{Fore.BLUE}=   {Fore.WHITE}Input your number to calculate {Fore.BLUE}  =")
print(f"{Fore.BLUE}======================================")

try:
    a = 1
    while a < 2:
        n1 = float(input("Input Number: "))
        op = input(f"Enter Operator: ")
        n2 = float(input(f"Input Number: "))
        if op == "+":
            re = n1 + n2
            print(f'Result {Fore.YELLOW}===> {Fore.WHITE}{re}')
            print(f"{Fore.BLUE}======================================")
        elif op == "-":
            re = n1 - n2
            print(f'Result {Fore.YELLOW}===> {Fore.WHITE}{re}')
            print(f"{Fore.BLUE}======================================")
        elif op == "*":
            re = n1 * n2
            print(f'Result {Fore.YELLOW}===> {Fore.WHITE}{re}')
            print(f"{Fore.BLUE}======================================")
        elif op == "/":
            re = n1 / n2
            print(f'Result {Fore.YELLOW}===> {Fore.WHITE}{re}')
            print(f"{Fore.BLUE}======================================")
        else:
            print(f"{Fore.RED}Invalid input! Please try again!")
            print(f"{Fore.BLUE}======================================")
except ValueError:
    print(f"{Fore.BLUE}======================================")
    print(f"{Fore.RED}Invalid input! Please try again!")
    print(f"{Fore.BLUE}======================================")
except ZeroDivisionError:
    print(f"{Fore.BLUE}======================================")
    print(f"{Fore.RED}Result is 0")
    print(f"{Fore.BLUE}======================================")
