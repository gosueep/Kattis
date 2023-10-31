from math import sqrt, radians, cos, sin, degrees, acos, pi

def hypotenuse(dx, dy) -> float:
    return sqrt(dx**2 + dy**2)

class Point:
    PRECISION = 1e-9

    def __init__(self, x, y):
        self.x, self.y = x, y

    def distance(self, other: 'Point') -> float:
        return hypotenuse(self.x - other.x, self.y - other.y)

    def rotate(self, theta) -> 'Point':
        rad = radians(theta)
        
        # Rotation matrix to rotate around the origin
        return Point(self.x * cos(rad) - self.y * sin(rad),
                     self.x * sin(rad) + self.y * cos(rad))

    # translate = slide the point along Vector v
    def translate(self, v: 'Vector') -> 'Point':
        return Point(self.x + v.x, self.y + v.y)

    # angle between the three points, in radians
    # i.e., beyween line ab and bc
    def angle(self, b: 'Point', c: 'Point') -> float:
        vec1 = Vector.fromPoints(b, self)
        vec2 = Vector.fromPoints(b, c)

        return acos(vec1.dot(vec2) / sqrt(vec1.normSq() * vec2.normSq()))

    # the counter-clockwise test:
    # * self, b, c ==> is this a clockwise turn, or a CCW turn
    def ccw(self, b: 'Point', c: 'Point') -> bool:
        crossMag = Vector.fromPoints(self, b).cross(Vector.fromPoints(self, c))
        return crossMag > Point.PRECISION

    # does c lie on the line ab
    def colinear(self, a: 'Point', b: 'Point') -> bool:
        return abs(Vector.fromPoints(self, a).cross(Vector.fromPoints(self, b))) < Point.PRECISION
    
    # The "line" is ab -- I guess I could use a Line class if I did "toPoints" function
    def distanceToLine(self, a: 'Point', b: 'Point') -> float:
           ap = Vector.fromPoints(a, self)
           ab = Vector.fromPoints(a, b)

           u = ap.dot(ab) / ab.normSq()

           # c = a + u*ab
           c = Vector.scale(ab, u).translate(a)
           return self.distance(c)
        
    def __eq__(self, other: 'Point'):
        return (abs(self.x - other.x) < Point.PRECISION and
                abs(self.y - other.y) < Point.PRECISION)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return self.__str__()

class Line:
    PRECISION = 1e-9

    # represents the equation ax + by + c = 0
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    
    @staticmethod
    def fromPoints(p1: Point, p2: Point) -> 'Line':
        # detect vertical
        if abs(p1.x - p2.x) < Line.PRECISION:
            return Line(1, 0, -p1.x)

        a = - (p1.y - p2.y) / (p1.x - p2.x)
        b = 1.0
        c = - a * p1.x - p1.y
        return Line(a, b, c)
    
    @staticmethod
    def fromPointSlope(p: Point, m: float) -> 'Line':
        a = -m
        b = 1.0
        c = -((a * p.x) + (b * p.y))
        return Line(a, b, c)

    def isParallelTo(self, other: 'Line') -> bool:
        return abs(self.a - other.a) < Line.PRECISION and abs(self.b - other.b) < Line.PRECISION

    def isSameAs(self, other: 'Line') -> bool:
        return self.isParallelTo(other) and abs(self.c - other.c) < Line.PRECISION

    def intersectAt(self, other: 'Line') -> Point:
        if self.isParallelTo(other):
            return None
        
        # Solving the system of equations
        x = (other.b * self.c - self.b * other.c) / (other.a * self.b - self.a * other.b)
        y = 0

        if abs(self.b) > Line.PRECISION: # check for vertical line to avoid divide-by-zero
            y = -(self.a * x + self.c)
        else:
            y = -(other.a * x + other.c)

        return Point(x, y)

    def __eq__(self, other: 'Line'):
        return (abs(self.a - other.a) < Line.PRECISION and 
                abs(self.b - other.b) < Line.PRECISION and 
                abs(self.c - other.c) < Line.PRECISION)

    def __str__(self):
        return f"{self.a}x + {self.b}y + {self.c} = 0" 

class Vector:
    PRECISION = 1e-9
    
    # x and y are *magnitudes*, not coordinates
    def __init__(self, x, y):
        self.x, self.y = x, y
    
    @staticmethod
    def fromPoints(a: Point, b: Point) -> 'Vector':
        return Vector(b.x - a.x, b.y - a.y)

    def scale(self, s: float) -> 'Vector':
        return Vector(self.x * s, self.y * s)

    def translate(self, p: Point) -> Point:
        return Point(p.x + self.x, p.y + self.y)

    def dot(self, b: 'Vector') -> float:
        return self.x * b.x + self.y * b.y
    
    # return the magnitude of the cross product
    def cross(self, b: 'Vector') -> float:
        return self.x * b.y - self.y * b.x

    def normSq(self):
        return self.x ** 2 + self.y ** 2
    
    def __eq__(self, other: 'Vector'):
        return (abs(self.x - other.x) < Vector.PRECISION and
                abs(self.y - other.y) < Vector.PRECISION)

    def __str__(self):
        return f"[{self.x} {self.y}]"

class Circle:
    PRECISION = 1e-9

    # Centered at Point c with radius r
    def __init__(self, c: Point, r: float):
        self.c, self.r = c, r
    
    # there's *two* possible circles defined by p1, p2, and radius r
    # this returns one of them
    @staticmethod
    def fromTwoPointsOnCircleAndRadius(p1: Point, p2: Point, r: float) -> 'Circle':
        d2 = (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y)
        det = r**2 / d2 - 0.25

        if det < 0.0:
            return None
        
        h = sqrt(det)
        c = Point(0, 0)
        c.x = (p1.x + p2.x) * 0.5 + (p1.y - p2.y) * h
        c.y = (p1.y + p2.y) * 0.5 + (p2.x - p1.x) * h

        return Circle(c, r)
   
    """
    returns:
       1 if inside
       0 if on the border
       -1 if outside
    """
    def containsPoint(self, p: Point) -> int:
        dx = p.x - self.c.x
        dy = p.y - self.c.y
        euc = dx**2 + dy**2
        rSq = self.r**2

        if abs(euc - rSq) < Circle.PRECISION: return 0
        if euc < rSq: return 1
        return -1

    def area(self) -> float:
        return self.r**2 * pi

    def diameter(self) -> float:
        return 2 * self.r

    def perimeter(self) -> float:
        return pi * self.diameter()

    def __eq__(self, other: 'Circle'):
        return (self.c == other.c and
                abs(self.r - other.r) < Circle.PRECISION)
    
    def __str__(self):
        return f'Circle(center={self.c}, radius={self.r})'

class Triangle:
    PRECISION = 1e-9

    def __init__(self, p1: Point, p2: Point, p3: Point):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
    
    @staticmethod
    def fromSideLengths(a: float, b: float, c: float) -> 'Triangle':
        if not Triangle.isValidTriangleFromLengths(a, b, c):
            return None

        # Fix p1 at the origin and p2 along the x-axis
        p1 = Point(0, 0)
        p2 = Point(a, 0)

        # Use the Law of Cosines to find the angle at p1
        angleAtP1 = acos((b**2 + a**2 - c**2) / (2*a*b))

        # Use the angle and side length b to find the coordinates of p3
        p3_x = b * cos(angleAtP1)
        p3_y = b * sin(angleAtP1)
        p3 = Point(p3_x, p3_y)

        return Triangle(p1, p2, p3)

    def edgeLengths(self) -> (float, float, float):
        a = self.p1.distance(self.p2)
        b = self.p1.distance(self.p3)
        c = self.p2.distance(self.p3)

        a, b, c = sorted([a, b, c])
        return (a, b, c)

    def isValid(self):
        return Triangle.isValidTriangleFromPoints(self.p1, self.p2, self.p3)
    
    @staticmethod
    def isValidTriangleFromPoints(p1: Point, p2: Point, p3: Point):
        a, b, c = Triangle.edgeLengths(Triangle(p1, p2, p3))
        return Triangle.isValidTriangleFromLengths(a, b, c)
    
    @staticmethod
    def isValidTriangleFromLengths(a: float, b: float, c: float):
        return (a + b > c and
                a + c > b and
                b + c > a)
    
    """
    is the triangle:
    * (R)ight
    * (E)quilateral
    * (I)soscales
    * (S)calene
    """
    def type(self) -> str:
        if not self.isValid():
            return None

        a, b, c = self.edgeLengths()
        
        # a == b == c --> Equilateral
        if abs(a - b) < Triangle.PRECISION and abs(b - c) < Triangle.PRECISION:
            return 'E'
        
        # satifies the pythagorean theorem --> right
        if abs((a**2 + b**2) - c**2) < Triangle.PRECISION:
            return 'R'

        # two side lengths match --> isoscales
        if abs(a - b) < Triangle.PRECISION or abs(b - c) < Triangle.PRECISION or abs(a - c) < Triangle.PRECISION:
            return 'I'

        return 'S'

    def perimeter(self) -> float:
        a, b, c = self.edgeLengths()
        return a + b + c

    def semiPerimeter(self) -> float:
        return self.perimeter() / 2

    def area(self) -> float:
        s = self.semiPerimeter()
        a, b, c = self.edgeLengths()
        return sqrt(s * (s - a) * (s - b) * (s - c))

    def __eq__(self, other: 'Triangle'):
        points_self = {self.p1, self.p2, self.p3}
        points_other = {other.p1, other.p2, other.p3}
        return points_self == points_other

    def __str__(self):
        return f'Triangle(p1={self.p1}, p2={self.p2}, p3={self.p3})'

if __name__ == '__main__':
    # Point tests
    p1 = Point(1, 1)
    p2 = Point(0, 0)
    p3 = Point(2, 0)
    p4 = Point(10, 3)
    p5 = Point(2, 2)
    
    print('Distance should be the same:', p3.distance(p1) == p1.distance(p3))
    print('Rotating 10,3 around the origin by 180º should equal -10, -3:', p4.rotate(180) == Point(-10, -3))
    print('Angle of p1/p2/p3 is 45º:', round(degrees(p1.angle(p2, p3))) == 45)
    print('p1/p2/p3 is CCW:', p1.ccw(p2, p3))
    print('p1/p2/p5 are colinear:', p1.colinear(p2, p5))
    print('p1 distance from p2p3 is 1:', p1.distanceToLine(p2, p3) == 1.0)

    # Line tests
    l1 = Line.fromPoints(Point(0, 0), Point(1, 1))  # y = x
    l2 = Line.fromPoints(Point(-10, 10), Point(10, 10)) # y = 10

    print('Lines are not parallel:', not l1.isParallelTo(l2))
    print('L1 and L2 intersect at (10, 10)', l1.intersectAt(l2) == Point(10, 10))

    # Circle tests
    c1 = Circle(Point(1, 1), 3)
    inside = Point(0, 0)
    border = Point(4, 1)
    outside = Point(1, -3)

    print('Inside test:', c1.containsPoint(inside) == 1)
    print('Border test:', c1.containsPoint(border) == 0)
    print('Outside test:', c1.containsPoint(outside) == -1)

    secondBorder = Point(1, -2)
    radius = 3
    print('Same circle from two border points:', c1 == Circle.fromTwoPointsOnCircleAndRadius(secondBorder, border, radius))

    c2 = Circle(Point(0,0), 1)
    print('Area of c2 is pi:', abs(c2.area() - pi) < Circle.PRECISION)
    print('Diameter of c2 is 2:', c2.diameter() == 2)
    print('Perimeter of c2 is 2pi:', abs(c2.perimeter() - 2*pi) < Circle.PRECISION)

    # Triangle tests
    t1 = Triangle.fromSideLengths(3, 4, 5)
    t2 = Triangle(Point(0,0), Point(4, 0), Point(2, 4))
    t3 = Triangle.fromSideLengths(3, 3, 3)
    print('t1 is right:', t1.type() == 'R')
    print('t2 is isoscales:', t2.type() == 'I')
    print('t3 is equilateral:', t3.type() == 'E')
    print('t1s perimeter is 12:', t1.perimeter() == 12)
    print('t2s area is 8:', t2.area() == 8)




