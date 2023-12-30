# dealing with numbers in python interpreter

# we can add numbers just as 5 + 5 and other arithmetic operations like this.

# for strings we can write them as " 4 " + " 5 ". these numbers will be considered as strings values.
# and these values will be concatenated and result will be 45.


# also we can use int(" 5 ") + int(" 6 ") this is actually type casting. converting from one datatype to other...

# Manipulating Strings

print('He said "Do not use abuse language..."\n')   # to print the narrated sentences with python...

print('I have '+ str(6) + " dollars.\n")              # we can concatenate strings and numbers in this way...
print('I have '+ str(6 + 37) + " dollars.\n")              # Also in this way...

print("hello: Awais\n".split(":"))                    # use to split the strings.....

print("My name is "+ "Awais: Honey: Muzammil\n".split(":")[1])     # use to split the values according to the index

# Lists in python

# these are like arrays but it contains multiple types of data.

a = ["Movies", 1 ," awais" , "Vassi", "computes"]           #list is declared and values are stored...
b = ["Movies", 1 ," awais" , "Vassi", "computes"][0]     # printing specific array index in the list..

print(a,"\n")
print(b,"\n")


# now we will discuss about the dictionaries....

dictionary = {"name" : "Awais", "major" : "Networking and machine learning" , "aim" : "software engineer"}  
                                        #in above we created dictionary
                                        # we associate a value to a key and then access that value with key very quickly
                                        # dictionaries are faster than lists bcz they are hashable...
                                     
print(dictionary["name"])               # printing value with specific key....
print(dictionary)                       # printing value with specific key....

# here we will try for variables...

name = "Hello Awais"                      # this is a string variable as we can see it contains character value.
splitted = name.split(" ")[0]             # this will print splitted first value in the name variable that is "Hello"...

nam = "Honey"
concat = splitted + nam                   # this will concatenate 2 strings and create a new one...

number = 1234                             # this is variable that contains the numeric values...
number2 = 12345

result = number * number2                 # we can perform all arithmetic operations like this... 

# builtin functions .........
#print function
print("Hi Awais")

#string function
str(232)                                  # this function is used to convert the value to string....

# integer function...........
int("72834")                              # this function converts the value to integer.....
                                          # many other functions like bool float are used for boolean and floating respectively....
# length function
arr = ["Awais", "Honey","Ahsan", "Muzammil", "Ismail", "Fahad"]
print(len(arr))
                                          # this will print the length of values array......
# sorted function....

arr1 = [1,2,4,3,2,1,2,45,46,3,23,5,3,23,3,43,43,2,32,3,23,23,34,0]

print(sorted(arr1))
