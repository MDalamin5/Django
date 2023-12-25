class Human(object):
    def eat(self):
        print('I can eat all days')
        

class Male(Human):
    def sleep(self):
        print('I can"t sleep whole day')
        

class Female(Human):
    def code(self):
        print('I can not code')
        
        
female_1 = Female()
female_1.code()
