import random
import string

capitalLetters=False
smallLetters=False
numbers=False
specialCharts=False

def ifCapitalLetters():
    global capitalLetters
    answer=input("Do you want to have in your password capital letters? (yes/no) \n")
    if answer.lower() == "yes":
        capitalLetters = True
        ifSmallLetters()
    elif answer.lower() == "no":
        ifSmallLetters()
    else:
        print("Provide correct answer!")
        ifCapitalLetters()
        
def ifSmallLetters():
    global smallLetters
    answer=input("Do you want to have in your password small letters? (yes/no) \n")
    if answer.lower() == "yes":
        smallLetters = True
        ifSmallLetters()
    elif answer.lower() == "no":
        ifSmallLetters()
    else:
        print("Provide correct answer!")
        ifSmallLetters()

def ifNumbers():
    print("numbers")

def ifSpecialCharts():
    print("Special Charts")

def generate_password():
    print("generate password")

while True:
    lenPassword = input("Type the length of password: ")
    try:
        lenPassword=int(lenPassword) 
    except:
        print("Error! Provide a number")
    else:
        lenPassword=int(lenPassword)
        if lenPassword <= 4:
            print("Error! Provide a number greater than 4")
        else:
            ifCapitalLetters()