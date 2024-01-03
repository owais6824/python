# here we will discuss about the functions in python...
# we will discuss different function cases and there exxamples accordingly...

# now we will create a function with name basic .....

# here is the simple syntax for function in python...

def basic():            # def is the keyword used to create a function in python and the basic is its name
    print("We are creating a simple function in python")
    print("This is the function without any argument.....")

# to call our function we will just type its name ....
basic()

# Now we will create a function with arguments in it....
# And see how it works....

# this is the function to perform addition.....
def add_num(num1, num2):
    result = num1 + num2
    print(result)

add_num(23, 34)

# now the function for subtraction....

def subtract_num(num2, num3):
    subtract = num2 - num3
    print(subtract)

subtract_num(450, 340)

# now we will take input from user and then multiply them....
def mutl_num(n1, n2):
    multiply = n1 * n2
    print(multiply)

mutl_num(int(input("Enter first number : ")), int(input("Enter second number : ")))

# for dividing the number
def div_num(nu1, nu2):
    divide = nu1 / nu2
    print(divide)
div_num(int(input("Enter first number to divide : ")), int(input("Enter second number to divide : ")))


# now we will use default arguments in the function
def default_arg(name = "Awais", age = 21):
    print("Hey, I am ", name , " and my age is", age)

default_arg()

# now have some look about the arguments with keywords...
# let us ahave some case that we want to make the argument null...
# here is how we can with keyword...

def keyword_arg(name , age ):
    print("Hey, I am ", name, " and my age is", age)

keyword_arg(None, 21)

