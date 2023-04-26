class Employee():
    numEmployee = 0
    def __init__(self, name, bonus):
        self.name = name
        self.bonus = bonus
        self.payment = 0

    def __del__(self):
        Employee.numEmployee -= 1

    def hours(self, numHours):
        self.payment += numHours * self.bonus
        return "hours worked {}".format(numHours)

    def __str__(self):
        print ("se ha creado {}".format(self.name))

p1 = Employee("juan", 1.10)
p1.__str__()



