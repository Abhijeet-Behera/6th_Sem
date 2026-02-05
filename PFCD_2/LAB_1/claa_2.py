
class Sample:
    x=10
    
    @classmethod
    def modify(cls):
        cls.x+=1
        
S1=Sample()
S2=Sample()
print('X in S1=',S1.x)
print('X in S2=',S2.x)
S1.modify()
print('X in S1=',S1.x)
print('X in S2=',S2.x)
