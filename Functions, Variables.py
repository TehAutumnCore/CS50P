#print("hello, world")    #print is a function, and ("hello, world") is an argument to the function

# input("What's your name?")
# print("hello, world")

#ask user for their name
# name = input("What's your name? ")
#say hello to the user
# print("hello, " + name + "!")

#python documentation: docs.python.org         /3/library/functions.html
# documentation for the print function: print(*objects, sep=' ',end='\n', file=sys.stdout, flush=False)
#sep is short for seperator, \n is short for new line, end is short for line ending
#this means print will end every line with ' '

#say hello to user
# print("hello, \"friend\"")      #escaping characters, \ lets the computer know they're literal quotes

#say hello to user
# print(f"hello, {name}")   #f string, short for format string

#python documention: docs.python.org/3/library/stdtypes.html#string-methods
#documentation for strings

name = input("What's your name? ").strip().title()
# name = name.strip() #removes whitespace from string, .strip is a method that removes from the left and the right but not inbetween
# name = name.capitalize() #capitalizes the first letter
# name = name.strip().title()
# name = name.title() #capitalizes the first letter in each word
print(f"hello, {name}")   #f string, short for format string
