# Magical calculator

import re

print("My Magical Calculator")
print("Type 'quit' to exit\n")

previous = 0
run = True


def performath():

    global run
    global previous
    equation = input("Enter Equation: ")
    if equation == 'quit':
        run = False
    else:
        equation = re.sub('[a-zA-Z,.()" "@&#]','',equation)
        previous = eval(equation)
        print("You entered", previous)


while run:
    performath()
