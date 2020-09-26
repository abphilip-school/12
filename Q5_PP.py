class students:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def readdata(self):
        self.name = raw_input('enter name')
        self.age = int(raw_input('enter age'))
    def display(self):
        print str(self.name)
        print str(self.age)
class pstudent(students):
    def __init__(self,name,age,hrs):
        students.__init__(self,name,age)
        self.hrs=hrs
    def readdata1(self):
        self.readdata()
        self.hrs=int(raw_input("enter no of hrs"))
    def display1(self):
        self.display()
        print str(self.hrs)

    
    
