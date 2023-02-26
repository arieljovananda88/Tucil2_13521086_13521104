import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

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

