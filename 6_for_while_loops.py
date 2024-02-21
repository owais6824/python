# Here we will discuss loops
# for loop adn while loop
# loops are used when we are going to repeat the statements

# here is the example to dive in for and while loop

# For loop
print("For loop")
names = ["Awais", "Honey", "Muzammil", "Ahsan", "Javed", "Saqlain"]

for student in names:
    print("My name is ", student, " and I am Computer Science Student.")

# while Loop

run = True
num = 1

while run:
    if num == 100:
        run = False
    else:
        print(num)
        num += 1

