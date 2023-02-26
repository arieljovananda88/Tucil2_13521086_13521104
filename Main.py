import random
import time
import ClosestPair as cp
import visualizer as vis
from colorama import Fore
def main():
    #SplashScreen
    print(f"""{Fore.GREEN}
     ██████╗██╗      ██████╗ ███████╗███████╗███████╗████████╗    ██████╗  █████╗ ██╗██████╗     ██████╗       ██████╗ 
    ██╔════╝██║     ██╔═══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝    ██╔══██╗██╔══██╗██║██╔══██╗    ╚════██╗      ██╔══██╗
    ██║     ██║     ██║   ██║███████╗█████╗  ███████╗   ██║       ██████╔╝███████║██║██████╔╝     █████╔╝█████╗██║  ██║
    ██║     ██║     ██║   ██║╚════██║██╔══╝  ╚════██║   ██║       ██╔═══╝ ██╔══██║██║██╔══██╗     ╚═══██╗╚════╝██║  ██║
    ╚██████╗███████╗╚██████╔╝███████║███████╗███████║   ██║       ██║     ██║  ██║██║██║  ██║    ██████╔╝      ██████╔╝
     ╚═════╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝       ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝    ╚═════╝       ╚═════╝ 
                                                                                                                    
        {Fore.WHITE}  """)  

    input(f"Press {Fore.RED}Enter{Fore.WHITE} to start...\n")
    ListPoint=[]
    n=int(input("Masukkan Jumlah Titik\t: "))
    st = time.time()    

    #generate random point
    for i in range(n) :
        x=random.uniform(0,100)
        y=random.uniform(0,100)
        z=random.uniform(0,100)
        ListPoint.append(cp.Point(x,y,z))
    Result=cp.closestPair(ListPoint)   
    print(Result)
    print('EuclideanDistance count\t:',cp.count) 
    RunTime = (time.time() - st)
    print('Execution time\t\t:', RunTime, 'seconds') 
    vis.visualizer(ListPoint,Result[1])
    # for i in range(n) :
    #     print(ListPoint[i])
main()