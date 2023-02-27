import random
import math
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

count = 0
def generatePoints(row, col):
    matrix = [[random.uniform(0,100) for j in range(col)] for i in range(row)]
    return matrix

def distance(point1, point2):
    sum = 0
    for i in range(len(point1)):
        sum += ((point1[i] - point2[i]) ** 2)
    result = math.sqrt(sum)
    return result

def sortList(mat, axis):
    if len(mat) <= 1:
        return mat
    acuan = mat[0]
    left = []
    right = []
    for i in mat[1:]:
        if i[axis] < acuan[axis]:
            left.append(i)
        else:
            right.append(i)
    return sortList(left,axis) + [acuan] + sortList(right,axis)

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
        if abs(point[0] - midP[0])<minP :
            unsorted.append(point)
    
    sorted = sortList(unsorted, 1)
    
    for i in range(len(sorted)):
        j=i+1
        while j < len(sorted) and sorted[j][1]-sorted[i][1] < minP :
            tempMin=distance(sorted[i],sorted[j])
            count += 1
            if tempMin < minP:
                minP=tempMin
                cp=[sorted[i],sorted[j]]
            j+=1
            
    
    return minP,cp

def closestPair(List):
    global count
    count = 0
    if len(List)<2 :
        return None
    sorted = sortList(List, 0)
    
    return closestPairRec(sorted)

def visualizer(points, pair): #Visualisasi Grafik Titik-Titik
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    zs = [p[2] for p in points]
    ax.scatter(xs, ys, zs)
    
    if pair:
        x_pair = [pair[0][0], pair[1][0]]
        y_pair = [pair[0][1], pair[1][1]]
        z_pair = [pair[0][2], pair[1][2]]
        ax.scatter(x_pair, y_pair, z_pair, c='red',s=80) #Mengubah warna titik yang merupakan closestPair
    
    #Memberi Label
    ax.set_xlabel('X') 
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


row = int(input("Masukkan jumlah point: "))
col = int(input("Masukkan dimensi: "))
if col == 3:
    ListPoint = generatePoints(row,col)
    Result = closestPair(ListPoint)   
    print(Result)
    print('EucDistance count :', count)
    visualizer(ListPoint, Result[1])
else:
    ListPoint = generatePoints(row,col)
    Result = closestPair(ListPoint)   
    print(Result)
    print('EucDistance count :', count) 
