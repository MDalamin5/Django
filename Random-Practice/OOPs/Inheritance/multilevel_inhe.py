from other_class import MyClass

class Fater:
    def __init__(self) -> None:
        self.name = 'Badrul Islam'
        self.phone_no = '018xxxxxx'
        print('this is parrent constructor')
        
    def bike(self):
        print('This is my bike')
        print(4 + 5)
    
    def dog(self):
        print('Base class also have dog method')
        

class Son(Fater, MyClass):
        
    def car(self):
        print('i buy this biek')
        
    # def dog(self, name):
    #     print('you are in son class')
    #     return super().dog(name)
    
    
    # def dog(self):
    #     print('you are in son class')
        
        
alamin = Son()
# alamin.bike()
# alamin.dog('Al Amin')
# alamin.bike()
# alamin.dog()
MyClass.dog(alamin)
print(Son.mro())
