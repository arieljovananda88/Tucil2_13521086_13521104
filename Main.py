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
Result=cp.closestPair(ListPoint)   
print(Result)
print('EucDistance count :',cp.count) 
RunTime = (time.time() - st)
print('Execution time:', RunTime, 'seconds') 
vis.visualizer(ListPoint,Result[1])
# for i in range(n) :
#     print(ListPoint[i])