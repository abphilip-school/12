class Person(object):
    def __init__(self,name,phone):
        self.name=name
        self.phone=phone
    def Input(self):
        self.name=raw_input("enter name   ")
        self.phone=raw_input("enter phone   ")
    def __del__(self):
        print "DESTRUCTORRRRRRR!!"
    def display(self):
        print "name = " ,self.name
        print "phone number : " ,self.phone
class Spouse(Person):
    def __init__(self,name,phone,sname,sphone):
        
        Person.__init__(self,name,phone)
        self.sname=sname
        self.sphone=sphone
    def Input(self):
        self.sname=raw_input("enter name   ")
        self.sphone=raw_input("enter phone   ")
    def display(self):
        print "name = " ,self.sname
        print "phone number : " ,self.sphone
class Clerk(Person):
    def __init__(self,name,phone):
        Person.__init__(self,name,phone)
    def Input(self):
        self.name=raw_input("enter name   ")
        self.phone=raw_input("enter phone   ")
    def display(self):
        print "name = " ,self.name
        print "phone number : " ,self.phone

        
        
        
