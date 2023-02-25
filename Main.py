import random
import time
import ClosestPair as cp
import visualizer as vis

  
ListPoint=[]
n=int(input("Masukkan Jumlah Titik : "))
st = time.time()    

for i in range(n) :
    x=random.uniform(0,100)
    y=random.uniform(0,100)
    z=random.uniform(0,100)
    ListPoint.append(cp.Point(x,y,z))
print(cp.closestPair(ListPoint))
RunTime = time.time() - st
print('Execution time:', RunTime, 'seconds') 
print('EucDistance count :',cp.count) 
vis.visualizer(ListPoint)
# for i in range(n) :
#     print(ListPoint[i])