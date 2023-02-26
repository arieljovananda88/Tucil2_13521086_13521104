import math

count =0;
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
    global count
    n=len(List)
    min=float('inf')
    cp=None
    
    for i in range(n):
        for j in range(i+1,n):
            temp=distance(List[i],List[j])
            count+=1
            if temp < min : 
                min=temp
                cp= [List[i],List[j]]
    return min , cp 

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
        

    
def closestPairRec(List):
    global count
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
    unsorted=[]
    for point in List:
        if abs(point.x-midP.x)<minP :
            unsorted.append(point)
    
    sorted = sortListY(unsorted)
    
    for i in range(len(sorted)):
        j=i+1
        while j < len(sorted) and sorted[j].y-sorted[i].y < minP :
            tempMin=distance(sorted[i],sorted[j])
            count+=1
            if tempMin < minP:
                minP=tempMin
                cp=[sorted[i],sorted[j]]
            j+=1
            
    # sortedZ=[]
    # for point in sorted :
    #     if abs(point.y-midP.y)<minP:
    #         sortedZ.append(point)
            
    # sortedZ.sort(key=lambda p: p.z)
    
    # for i in range(len(sortedZ)):
    #     j=j+1
    #     while j < len(sortedZ) and sortedZ[j].z-sortedZ[i].z < minP :
    #         tempMin2=distance(sortedZ[i],sortedZ[j])
    #         if tempMin2 < minP :
    #             minP=tempMin2
    #             cp= [sortedZ[i],sortedZ[j]]
    #         j+=1
    
    return minP,cp

def closestPair(List):
    global count
    count=0
    if len(List)<2 :
        return None
    List=sortListY(List)
    
    return closestPairRec(List)