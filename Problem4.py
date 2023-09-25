class qe:
    def __init__(self):
        self.data=[]
    def enq(self,a):
        self.data.append(a)
    def deq(self):
        self.data=self.data[1:]
    def show(self):
        return self.data    
q=qe()
q.enq(32)
q.enq(43)
q.deq()
print(q.show())