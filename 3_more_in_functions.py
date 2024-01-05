# here we will discuss some more concepts about functions in python.....
# first we will create a function ....
# we will discuss here infinite arguments in the function.....

def student_name(*student):  # in this line the * sign shows the infinite argument
    for name in student:
        print("Student name is ", name)


student_name("Awais", "Honey", "Muzammil")
