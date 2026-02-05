class Student:
    def __init__(self):
        self.name="Abhijeet"
        self.age=21
        self.mark=90

    def talk(self):
        print('Name is',self.name)
        print(self.age)
        print(self.mark)
    
S1=Student()
S1.talk()