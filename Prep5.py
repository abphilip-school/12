n=int(raw_input("Enter no of days: "))
y=365.25
m=float(y/12)
w=7
Y=int(n/y)
M=int(n/m)-Y*12
W=int(n/w-(Y*365.25/7 +((M*365.25)/(12*7))))
N=int(n-(Y*365.25 + M*(365.25/12) + W*7))
print Y, "Years"
print M, "Months"
print W, "Weeks"
print N, "Days"
