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
    row = int(input("Masukkan jumlah point: "))
    col = int(input("Masukkan dimensi: "))
    if col == 3:
        st = time.time() 
        ListPoint = cp.generatePoints(row,col)
        Result = cp.closestPair(ListPoint)   
        print(Result)
        print('EucDistance count :', cp.count)
        RunTime = (time.time() - st)
        print('Execution time\t\t:', RunTime, 'seconds',"(ROG-G513qr)") 
        pil = str(input("Apakah ingin divisualisasikan? \nTekan tombol selain Y/y jika tidak\n"))
        if(pil == "Y" or pil == "y"):
             vis.visualizer(ListPoint, Result[1])
        else:
            return 0
    else:
        st = time.time() 
        ListPoint = cp.generatePoints(row,col)
        Result = cp.closestPair(ListPoint)   
        print(Result)
        print('EucDistance count :', cp.count) 
        RunTime = (time.time() - st)
        print('Execution time\t\t:', RunTime, 'seconds',"(ROG-G513qr)") 
        return 0
        
main()