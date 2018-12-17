class rectangle(object):
    def __init__(self,width,height):
        self.width=width
        self.height=height
    def area(self):
        return self.width*self.height
    def perimeter(self):
        return(self.width+self.height)
rec1 = rectangle(50,60)
print(rec1.area())
