class Traiangle:
    def __init__(self, side1, side2, side3):
        self.side1=side1
        self.side2=side2
        self.side3=side3
        number_of_sides = 3
        def check_angles(self):
            return (self.side1 + self.side2 + self.side3) == 180
        side1=int(input("Enter side1:"))
        side2 =int(input("Enter side1:"))
        side3 =int(input("Enter side1:"))
        my_traingle=Traiangle(side1,side2,side3)
        print(my_traingle.number_of_sides)
        print(my_traingle.check_angles())