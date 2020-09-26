def over(a,b):
    l1=len(a)
    l2=len(b)
    for i in range(l1):
        for j in range(l2):
            if a[i] == b[j]:
                return True
    else:
        return False
a= list(raw_input("Enter the List1: "))
b= list(raw_input("Enter the List2: "))
c= over(a,b)
if c == True:
    print "True"
else:
    print "False"
