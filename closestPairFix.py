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

def sortListX(lst):
    if len(lst) <= 1:
        return lst
    acuan = lst[0]
    left = []
    right = []
    for i in lst[1:]:
        if i.x < acuan.x:
            left.append(i)
        else:
            right.append(i)
    return sortListX(left) + [acuan] + sortListX(right)

def sortListY(lst):
    if len(lst) <= 1:
        return lst
    acuan = lst[0]
    left = []
    right = []
    for i in lst[1:]:
        if i.y < acuan.y:
            left.append(i)
        else:
            right.append(i)
    return sortListY(left) + [acuan] + sortListY(right)

def bruteForce(lst):
    minDistance = float('inf')
    pairTerdekat = None
    for i in range (len(lst)):
        for j in range(i+1, len(lst)):
            if distance(lst[i], lst[j]) < minDistance:
                minDistance = distance(lst[i], lst[j])
                pairTerdekat = (lst[i], lst[j])
    return pairTerdekat, minDistance

def findClosestPair(xSorted, ySorted):
    if len(xSorted) <= 3:
        return bruteForce(xSorted)
    middle = len(xSorted) // 2
    xLeft = xSorted[:middle]
    xRight = xSorted[middle:]
    middleXpoint = xSorted[middle]
    ySortedLeft = []
    ySortedRight = []
    for i in ySorted:
        if i.x < middleXpoint.x :
            ySortedLeft.append(i)
        else:
            ySortedRight.append(i)
    (leftClosestPair, leftMinDist) = findClosestPair(xLeft, ySortedLeft)
    (rightClosestPair, rightMinDist) = findClosestPair(xRight, ySortedRight)
    minDist = min(leftMinDist, rightMinDist)
    betweenHalves = []
    for i in ySorted:
        if abs(i.x - middleXpoint.x) < minDist:
            betweenHalves.append(i)
    closestPairBetween = None
    for i in range (len(betweenHalves)):
        for j in range(i+1, min(i+7, len(betweenHalves))):
            if distance(betweenHalves[i], betweenHalves[j]) < minDist:
                minDist = distance(betweenHalves[i], betweenHalves[j])
                closestPairBetween = (betweenHalves[i], betweenHalves[j])
    if closestPairBetween is not None:
        return closestPairBetween
    if leftMinDist < rightMinDist:
        return leftClosestPair
    else:
        return rightClosestPair




ListPoint=[]
n=int(input("Masukkan Jumlah Titik : "))

for i in range(n) :
    x=random.randint(0,9)
    y=random.randint(0,9)
    z=random.randint(0,9)
    ListPoint.append(Point(x,y,z))


for i in range(n):
    print(ListPoint[i])

#print(closestPair(ListPoint,n))
#print(len(ListPoint))
sortedListX = sortListX(ListPoint)
sortedListY = sortListY(ListPoint)


print("sorted on x axis")
for i in range(n) :
    print(sortedListX[i])


(p1, p2) = findClosestPair(sortedListX, sortedListY)
print(p1,p2)
print(distance(p1,p2))



#print("sorted on y axis")
#for i in range(n) :
    #print(sortedListY[i])
    

