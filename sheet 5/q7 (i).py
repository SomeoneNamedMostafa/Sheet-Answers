class Point2D:
    def __init__(self, x=0, y=0):  # initialize the point with x and y coordinates
        self.x = x  # Set the x-coordinate
        self.y = y  # Set the y-coordinate

    def __str__(self): # return a string representation of the point
        return f"({self.x}, {self.y})"

    def add(self, p): # adding another point to the current point
        self.x += p.x  # Add x-coordinates
        self.y += p.y  # Add y-coordinates

    def distance(self, p): # calculate distance to another point
        delta_x = self.x - p.x  # Difference in x-coordinates
        delta_y = self.y - p.y  # Difference in y-coordinates

        dist = (delta_x ** 2 + delta_y ** 2) ** 0.5  
        return dist


p1 = Point2D(1, 2)
p2 = Point2D(4, -2)

p2.add(p1)

print(p2)
print(p1.distance(p2))


print(p1.distance(p2))
