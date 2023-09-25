class st:
    def __init__(self):
        self.data=[]
    def push(self,a):
        self.data.append(a)
    def pop(self):
        self.data=self.data[:-1]
    def show(self):
        return self.data    
s=st()
s.push(32)
s.push(43)
s.pop()
print(s.show())
            
        