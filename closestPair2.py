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
    return math.sqrt((Point2.x-Point1.x)**2 + (Point2.y-Point1.y)**2 + (Point2.z-Point1.z)**2)
def bruteForce(List):
    n=len(List)
    min=float('inf')
    cp=None
    
    for i in range(n):
        for j in range(i+1,n):
            temp=distance(List[i],List[j])
            if temp < min : 
                min=temp
                cp= [List[i],List[j]]
    return min , cp            
        

    
def closestPairRec(List):
    n=len(List)
    if n<=3 : 
        return bruteForce(List)
    
    mid= n//2
    midP=List[mid]
    
    left_p=List[:mid]
    right_p=List[mid:]
    
    min_l,cp_l=closestPairRec(left_p)   
    min_r,cp_r=closestPairRec(right_p)
    
    minP=min(min_l,min_r)
    cp=cp_r if min_r<min_l else cp_l
    sorted=[]
    for point in List:
        if abs(point.x-midP.x)<minP :
            sorted.append(point)
    
    sorted.sort(key=lambda p:p.y)
    
    for i in range(len(sorted)):
        j=i+1
        while j < len(sorted) and sorted[j].y-sorted[i].y < minP :
            tempMin=distance(sorted[i],sorted[j])
            if tempMin < minP:
                minP=tempMin
                cp=[sorted[i],sorted[j]]
            j+=1
    return minP,cp

def closestPair(List):
    if len(List)<2 :
        return None
    List.sort(key=lambda p: p.x)
    
    return closestPairRec(List)
    
    
ListPoint=[]
n=int(input("Masukkan Jumlah Titik : "))

for i in range(n) :
    x=random.randint(0,9)
    y=random.randint(0,9)
    z=random.randint(0,9)
    ListPoint.append(Point(x,y,z))

print(closestPair(ListPoint))
for i in range(n) :
    print(ListPoint[i])