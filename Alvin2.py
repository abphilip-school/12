import calendar;
a=2
while a<3:
    
    print"Enter 1 for calculator"
    print"Enter 2 for calendar"
    print"Enter 3 for pattern creator"
    print"Enter 4 to exit"
    a=input("")
    if a==1:
        print"Enter 1 for addition"
        print"Enter 2 for subtraction"
        print"Enter 3 for multiplication"
        print"Enter 4 for division"
        d=input("")
        if d==1:
            b=input("Enter the first number: ")
            c=input("Enter the second number: ")
            print b+c
        elif d==2:
            b=input("Enter the first number: ")
            c=input("Enter the second number: ")
            print b-c
        elif d==3:
            b=input("Enter the first number: ")
            c=input("Enter the second number: ")
            print b*c
        elif d==4:
            b=input("Enter the first number: ")
            c=input("Enter the second number: ")
            print "Division: ",
            print b/c
            print "Remainder: ",
            print b%c
        else:
            print"Wrong number"
    elif a==2:
        e=input("Enter the year: ")
        f=input("Enter the month: ")
        cal=calendar.month(e,f)
        print cal
    elif a==3:
        g=input("Enter the starting of the line loop")
        h=input("Enter the ending of the line loop")
        i=input("Enter the starting of the counting loop")
        j=input("Enter the ending of the counting loop")
        for k in range(g,h):
            for l in range(i,j):
                print l,
            print""
print "bye"
                
