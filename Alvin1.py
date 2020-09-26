al = raw_input("Enter the String: ")
a = al.lower()
b = len(a)
s = ""

for i in range(0,b):
    if a[i] == 'a':
        s = s+'1'
    elif a[i] == 'e':
        s = s+'2'
    elif a[i] == 'i':
        s = s+'3'
    elif a[i] == 'o':
        s = s+'4'
    elif a[i] == 'u':
        s = s+'5'
    else:
        s = s+a[i].upper()

print s       
