class Sample:
    def __init__(self):
        self.x=10
    def modify(self):
        self.x+=1
        
S1=Sample()
S2=Sample()
print('X in S1=',S1.x)
print('X in S2=',S2.x)
S1.modify()
print('X in S1=',S1.x)
print('X in S2=',S2.x)
