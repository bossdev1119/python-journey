print("multiplication table")
num = 1

while int(num) >0 :
    num =input("\nEnter a number (q to exit): ")
    if num!="q" :
        print("Boom! \n")
        for i in range(1, 11):
            print(f"{num} X {i} = {int(num) * i}")

    else :
        print("bye bye!")
        break

