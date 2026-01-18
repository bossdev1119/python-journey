import random 

x= random.randint(1,32)
print("\nWelcome to the guessing game!")
print("Computer thinking between 1 and 30 . You have 5 attempts to guess it.\n")
print("note: hints will be provided based on your guesses\n")  
# print(x)
user_input= int(input("Find the imposter : "))
attempt = 1
while user_input!=x and attempt<=5 :
    attempt +=1 
    
    if user_input<x :
        # print("too close")
        print("number is higher ")
        print("attempt no: ", attempt)
        user_input=int(input("try again: "))

    elif user_input> x :
        diff= abs(x - user_input)
        # print("getting closer ")
        print("number is lower ")
        print("attempt no: ", attempt)
        user_input=int(input("try again: "))

else :
    if user_input==x :
        print("\ncongratulations! you found the number ")
        print(f"you took {attempt} attempts to find the number\n")
        print(f"the number was {x}")
    else:
        print("\nsorry! you couldn't find the number ")
        print(f"the number was {x}")
        