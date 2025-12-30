flag = True

while flag :
    print("1 - Addition \n2 - Subtraction \n3 - Multiplication \n4 - Division")
    try:
        n = int(input("Enter your choice : "))
    except ValueError:
        print("Please enter a valid number")
        continue

    if n == 1:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        print("Result : " , a+b)
        
    elif n == 2:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))

        print("Result : " , a-b)

    elif n == 3:
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        print("Result : " , a*b)

    elif n == 4 :
        a = int(input("Enter first number : "))
        b = int(input("Enter second number : "))
        if b != 0:
            print("Result : " , a/b)
        else:
            print("Can not divide by 0")
            
    else:
        print("Invalid choice")

    choice = input("Do you want to continue (y/n) ? :")
    if choice == 'n' or choice == 'N' :
        flag = False
        break
print("Thanks for using the calculator !!")
