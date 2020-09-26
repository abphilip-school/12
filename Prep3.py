sum = 0
n = int(raw_input("How many terms? - "))
for a in range(2, n+2):
    term=0
    for b in range(1,a):
        term+=b
    sum+=term
print "Sum = ", sum
