import random

class c_radical():
    def __init__(self, VA, VB, VC):
        self.VA = VA
        self.VB = VB
        self.VC = VC
        
    def aleatoriza(self):
        self.RA = random.randint(self.VA, self.VB)
        print(self.RA)
    
    def guarda(self):
        if self.RA == self.VC:
            print(f'valor {self.VC} é o numero secreto!') 
        
a = c_radical(1,5, 2) 
print(a.VA,"<->",a.VB)

a.aleatoriza()
a.guarda()