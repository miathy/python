class User:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.address = " "
    
    def setAdress(self, address):
        self.address = address
    
    def printUser(self):
        print('User details: ')
        print('Name: ' +self.name)
        print('Age: ' +self.age)
        print('Gender: ' +self.gender)
        print('Address: ' +self.address)