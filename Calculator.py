def Calculator(a):
    if a==1:
        try:
            x=int(input("Enter number 1:"))
            y=int(input("Enter number 2:"))
            print(x,"+",y,"=",x+y)
            a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
            Calculator(a)
        except Exception as e:
             print(str(type(e)),str(e))
             a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
             Calculator(a)
    elif a==2:
        try:
            x=int(input("Enter number 1:"))
            y=int(input("Enter number 2:"))
            print(x,"-",y,"=",x-y)
            a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
            Calculator(a)
        except Exception as e:
             print(str(type(e)),str(e))
             a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
             Calculator(a)
    elif a==3:
        try:
            x=int(input("Enter number 1:"))
            y=int(input("Enter number 2:"))
            print(x,"*",y,"=",x*y)
            a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
            Calculator(a)
        except Exception as e:
             print(str(type(e)),str(e))
             a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
             Calculator(a)
    elif a==4:
        try:
            x=int(input("Enter number 1:"))
            y=int(input("Enter number 2:"))
            print(x,"/",y,"=",x/y)
            a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
            Calculator(a)
        except Exception as e:
             print(str(e))
             a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
             Calculator(a)
    else:
        print("Please enter a correct number")
        a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
        Calculator(a)


a=int(input("Calculator \n Enter 1.ADDITION 2.SUBTRACTION 3.MULTIPLICATION 4.DIVISION:"))
Calculator(a)
