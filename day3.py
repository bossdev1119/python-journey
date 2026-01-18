#-----------------method 1-----------------

# x,y= map(int,input("Enter two numbers separated by space: ").split())
# math=input("Enter the operation (+, -, *, /): ")

# def add(a,b):
#     print("ans:",a+b)

# def subtract(a,b):
#     print("ans:",a-b)
    
# def multiply(a,b):
#     print("Tans:",a*b)

# def divide(a,b):
#     if b!=0:
#         print("ans:",a/b)
#     else:
#         print("Error! Division by zero.")

# if math=="+":
#     add(x,y) 
# elif math=="-":
#     subtract(x,y)
# elif math=="*":
#     multiply(x,y)       
# elif math=="/":
#     divide(x,y)
# else:
#     print("Invalid operation")
    

#-----------------method 2-----------------
def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return None
    return a/b

def get2number():
    while True :
        userInput= input("Enter 2 numbers with space : ").strip()
        if not userInput:
            print("input cannot be empty")
            continue

        piece = userInput.split()

        if len(piece)!=2 :
            print("you can enter only 2 numbers")
            continue
        try: 
            x= float(piece[0])
            y = float(piece[1])
            return x,y
        except ValueError:
            print("Enter valid numbers")

print('''  
    CALCULATOR
      
        1. Addition
        2. Subtraction
        3. Multiplication
        4. Division\n''')


while True:
    num = input("Choose operation: ")
    try:
        if int(num) in [1,2,3,4]:
            break
        else:
            print("oops ! you must enter an INTEGER(1-4) only\n")
    except ValueError:
        print("oops ! you must enter an INTEGER\n")

x,y = get2number()

if num=='1':
    print(f"ans : ",add(x,y))
elif num=='2':
    print("ans: " ,subtract(x,y))   
elif num=='3':
    print("ans : " ,multiply(x,y))       
elif num=='4':
    division = divide(x,y)
    if division is None:
        print("error ! division by zero ")
    else :
        print("ans : ", division)

    
