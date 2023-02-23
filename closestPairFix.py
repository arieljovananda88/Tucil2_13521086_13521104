import math
import random
class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def __repr__(self):
        return f'({self.x}, {self.y}, {self.z})'

def distance(Point1,Point2):
    return math.sqrt((Point2.x+Point1.x)**2 + (Point2.y+Point1.y)**2 + (Point2.z+Point1.z)**2)

def closestPair(List,n1):
    if n1<2 :
        return None
    if n1==2 :
        return distance(List[0],List[1])
    
    return
ListPoint=[]
n=int(input("Masukkan Jumlah Titik : "))

for i in range(n) :
    x=random.randint(0,9)
    y=random.randint(0,9)
    z=random.randint(0,9)
    ListPoint.append(Point(x,y,z))

print(closestPair(ListPoint,n))
for i in range(n) :
    print(ListPoint[i])