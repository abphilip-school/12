class employee:
    def __init__(self):
        self.e_no = raw_input("Employee number:")
        self.name = raw_input("Employee name:")
        self.add = raw_input("Address:")
        self.dept = raw_input("Department:")
    def display(self):
        print "Employee number:",self.e_no
        print "Employee name:",self.name
        print "Address:",self.add
        print "Department:",self.dept
class Manager(employee):
    def __init__(self):
        employee.__init__(self)
        self.emp_under = raw_input("Enter employees under the manager in the form of a list:")
    def display2(self):
        self.display()
        print "Employees under the manager:",self.emp_under
