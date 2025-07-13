# Task:
# Given four points A, B, C, and D in 3D space, compute the angle between two planes: ABC & BCD

# Approach:
# 1. Compute vectors:AB = B - A & BC = C - B & CD = D - C

# 2. Get normal vectors (perpendicular to each plane):  Normal1 = AB × BC &  Normal2 = CD × BC

# 3. Compute the angle between the two normals using the dot product formula:
#    cos(θ) = (Normal1 • Normal2) / (|Normal1| * |Normal2|)

# Input Format:
# Four lines, each with 3 float values representing a point in 3D (x y z)

# Output Format:
# A single line with the angle (in degrees) between the two planes, rounded to 2 decimal places.



import math

class Points(object):
    def __init__(self, x, y, z):
        self.x=x
        self.y=y
        self.z=z

    def __sub__(self, no):
        return points(self.x-no.x,self.y-no.y,self.z-no.z)

    def dot(self, no):
        return self.x*no.x + self.y*no.y + self.z*no.z

    def cross(self, no):
        
        x= self.y *no.z - self.z *no.y
        y=-1*(self.x *no.z - self.z* no.x)
        z=self.x *no.y -self.y *no.x
        return points(x,y,z)
 
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)


if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))


# Sample Input:
# 0 4 5
# 1 7 6
# 0 5 9
# 1 7 2

# Sample Output:
# 8.19
