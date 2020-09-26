class  publications (object):
    def __init__(self,title,price):
        self.title= title
        self.price= price
    def getdata(self):
        self.title = raw_input("Enter title")
        self.price = int(raw_input("Enter price :- "))
    def putdata(self):
        print "Title is ", self.title
        print "Price is ", self.price
class Book(publications):
    def __init__(self,title, price,pageno):
        publications.__init__(self,title,price)
        self.pageno= pageno
    def getdata(self):                                                                                                                                                                                                                                                                                                                                                                                
        self.title = raw_input("Enter title")
        self.price = int(raw_input("Enter price :- "))
        self.pageno= int(raw_input("Enter page number"))
    def putdata(self):
        print "Title is ", self.title
        print "Price is ", self.price
        print "No: Page nos are", self.pageno
        
        
            
                    
