class Rectangle:
    def setSize(self, xcoord,ycoord):
        self.x = xcoord
        self.y = ycoord
    def perimeter(self):
        return 2*(self.x+self.y)
    def area(self):
        return self.x * self.y 

    
r = Rectangle()
r.setSize(3,4)
print(r.perimeter())




