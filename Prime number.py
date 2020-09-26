#Prime or composite number
n=int(raw_input("Enter the number: "))
c=0
for i in range(2,n):
    if n%i==0:
        c=1
if c==1:
    print "Composite"
else:
    print "Prime"
