

class Polygons:
    def __init__(self,num_sides):
        self.num_sides=num_sides
    def get_side_lenghts(self):
        for side_number in range(self.num_sides):
            self.get_side_lenghts().append(input(f"Enter tge lenght of side {side_number}"))
    def perimeter(self):
        return sum(self.side_lenghts)
class Triangle(Polygons):
    def __init__(self):
        super().__init__(3)
        self.get_side_lenghts()

class Rectangle(Polygons):
    def __init__(self):
        super().__init__(4)
        self.get_side_lenghts()

class Pentagon(Polygons):
    def __init__(self):
        super().__init__(5)
        self.get_side_lenghts()
class Hexagon(Polygons):
    def __init__(self):
        super().__init__(6)
        self.get_side_lenghts()

Shape = input("Enter Shape:")
if Shape.upper()=="TRAIANGLE":
    s=Triangle()
elif Shape.upper()=="RECTANGLE":
    s=Rectangle()
elif Shape.upper()=="PENTAGON":
    s=Pentagon()
elif Shape.upper()=="HEXAGON":
    s=Hexagon()
else:
    print("invalid Shape")
s.get_side_lenghts()
s.perimeter = s.get_perimeter()
print("\nshape=", shape)
print("\nPerimeter=",s.perimeter)
print("\nPerimeter=",s.perimeter)
print("\nPerimeter=",s.perimeter)