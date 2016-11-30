# Create a class that represents a cuboid:
# It should take its three sizes as constructor parameters (numbers)
# It should have a method called `getSurface` that returns the cuboid's surface
# It should have a method called `getVolume` that returns the cuboid's volume

class Cuboid():

    def __init__(self, a, b, c): # a, b, c parameters represent the sides of the cuboid
        self.a = a
        self.b = b
        self.c = c

    def getVolume(self):
        return self.a * self.b * self.c

    def getSurface(self):
        return ((self.a + self.b) * self.c + (self.a * self.b)) * 2

# c = Cuboid(1, 1, 3)
#
# print(c.getSurface())
