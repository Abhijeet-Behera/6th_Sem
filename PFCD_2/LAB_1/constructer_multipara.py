class Student:
    def __init__(self, redg, sec):
        self.name = "Abhijeet"
        self.age = 21
        self.mark = 90
        self.redg = redg  
        self.sec = sec    

    def talk(self):
        print('Name is', self.name)
        print('Age:', self.age)
        print('Mark:', self.mark)
        print('Registration:', self.redg)
        print('Section:', self.sec)


S1 = Student(2069, '2c1')
S1.talk()
