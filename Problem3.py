class shopping_cart:
    def __init__(self):
        self.l={}
    def add(self,item,price):
        self.l.update({item:price})
    def remove(self,item):
        del self.l[item]
    def cal(self):
        sum=0
        for x in self.l.values():
            sum=sum+x
        return sum
sc=shopping_cart()
sc.add("Banana",122)
sc.add("Apple",544)
sc.remove("Apple")
print(sc.cal())                

