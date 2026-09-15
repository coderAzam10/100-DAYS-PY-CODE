# first program in python
#print("Hello, World!")

# if we want to print lot of things with new line with a sinle print we can use like this 
# print("Hello, World!\n Hello, Nitesh!\nHello, Nawab!\nHello, World!\nHello,azam!\n ")

# string concatenation
#print("hello " + "Shaikh")

#input fxn 
# unlike print fxn we use input fxn for taking input from user in print fxn it will print the value but in input fxn it will take the value from user and store it in variable
#input("What is your name? ")
#  now we will give the input in the terminal and 
# it will store the value in variable and we can use that variable for further use
#we can also use input fxn with print fxn like this
# print("Hello "  + input("what is your name?!"))
 
#variables are used to store the value in python we can use any name for variable
#  but it should not start with number and
# it should not contain any special character except underscore(_) ,
#  it should not start with number and it should not be a keyword in python

# we can use len() fxn to find the length of string or any variable which is string type in python
#name = "azam shaikh"
#print(len(name))
#it will print the length of the string which is 11 in this case


# name = "azam"
# print(name)
# name = "jack"
# print(name)
#  after changing the value of same  variable name it will print the new value of variable name which is jack in this case

# (print(len(input("what is your name?!"))))
# also we can use this too

# username = input("what is your name?!")
# length = len(username)  
# print(length) 
# this is how we can store the value of input in variable and then we can use that variable for further use


# we can solve some problem using python like this

# let say glass1 = "milk "
# and glass2 = "water"

# how can we switch out the liquid ?

# in this case we can use a temporary variable to store the value
# of glass1 and then we can assign the value of glass2 to glass1 and then we can assign the value of temporary variable to glass2

# lets say glass 3 = glass1
# glass1 = glass2
# glass2 = glass3
# this is how we can switch the value of two variables using a temporary variable

# Band name Generator
print("Welcome to the band Name Generator.")

city = input("What is the name of the city you grew up in ?\n")
pet = input("What is the name of your pet ?\n")

print("Your band name could be " + city + " " + pet)









