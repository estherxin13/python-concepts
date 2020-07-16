from random import *

# defining the characters in the password
char1="ABCDEFGHIJKLMNOPQRTUVWXYZ"
char2=char1.lower()
char3="!@#$%^&*()"
char4="0123456789"

def message():  # you have to define the function and then call it at the bottom
    print("Welcome to your random password generator!")
    print("Please select the length of each of your characters")
    print(userGen())

def userGen():    # asks the user for the input
    upper=int(input("Amount of upper case letters:"))
    lower=int(input("Amount of lower case letters:"))
    spec=int(input("Amount of special characters:"))
    num=int(input("Amount of numbers:"))
    return passGen(upper,lower,spec,num)     # prints the user's answer beside the thing

def passGen(upper,lower,spec,num): #if it is less than 6 letters, then you have to redo it
    new_password=""
    if (upper+lower+spec+num)<6:
        print("Please enter minimum 6 letters.")

    else:   # this is for everthing else
        for i in range(upper):  #checking if it is in range of the range indicated before and taking the number
            new_password+=choice(char1)   # += means that it is added a number to the variable
        for x in range(lower):
            new_password+=choice(char2)
        for y in range(spec):
            new_password+=choice(char3)
        for z in range(num):
            new_password+=choice(char4)

    pass_word=list(new_password) #puts it into a list
    shuff=shuffle(pass_word)  #shuffle around the letters
    new_pass="".join(pass_word)  #joins everything together
    return new_pass  #returns it

message()  # acc runs the message