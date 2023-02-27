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

    #generate random point
    row = int(input("Masukkan jumlah point\t: "))
    col = int(input("Masukkan dimensi\t: "))
    if col == 3:
        stbf = time.time()
        ListPoint = cp.generatePoints(row,col)
        print(f"{Fore.RED}Pure Brute Force{Fore.WHITE}")
        Result1 = cp.bruteForce(ListPoint)
        print(Result1)
        print('EucDistance count\t:', cp.count)
        RunTime1 = (time.time() - stbf)
        print('Execution time\t\t:', RunTime1, 'seconds',"(ROG-G513qr)") 
        print(f"{Fore.RED}Divide and Conqeur{Fore.WHITE}")
        st = time.time()
        cp.count = 0
        Result = cp.closestPair(ListPoint)   
        print(Result)
        print('EucDistance count\t:', cp.count)
        RunTime = (time.time() - st)
        print('Execution time\t\t:', RunTime, 'seconds',"(ROG-G513qr)") 
        pil = str(input("Apakah ingin divisualisasikan? \nTekan tombol selain Y/y jika tidak\n"))
        if(pil == "Y" or pil == "y"):
             vis.visualizer(ListPoint, Result[1])
        else:
            return 0
    else:
        stbf = time.time()
        ListPoint = cp.generatePoints(row,col)
        print(f"{Fore.RED}Pure Brute Force{Fore.WHITE}")
        Result1 = cp.bruteForce(ListPoint)
        print(Result1)
        print('EucDistance count\t:', cp.count)
        RunTime1 = (time.time() - stbf)
        print('Execution time\t\t:', RunTime1, 'seconds',"(ROG-G513qr)") 
        print(f"{Fore.RED}Divide and Conqeur{Fore.WHITE}")
        st = time.time()
        cp.count = 0
        Result = cp.closestPair(ListPoint)   
        print(Result)
        print('EucDistance count\t:', cp.count)
        RunTime = (time.time() - st)
        print('Execution time\t\t:', RunTime, 'seconds',"(ROG-G513qr)")  
        return 0
        
main()