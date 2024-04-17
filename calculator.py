def showOperations():

    print("OPERATIONS:")
    print("Choose 1 for addition")
    print("Choose 2 for subtraction")
    print("Choose 3 for multiplication")
    print("Choose 4 for division\n")

while(True):

    a=float(input("Enter first number: "))
    b=float(input("Enter second number: "))
    showOperations()
    select=int(input("Enter operation index: "))
    if select==1:
        print(f"Result: {a}+{b}= {a+b}\n")
        continue
    elif select==2:
        print(f"Result: {a}-{b}= {a-b}\n")
        continue
    elif select==3:
        print(f"Result: {a}*{b}= {a*b}\n")
        continue
    elif select==4:
        if b!=0:
            print(f"Result: {a}/{b}= {a/b}\n")
            continue
        else:
            print("Undefined")
            continue
    else:
        print("Invalid selection")
        continue
    

    
