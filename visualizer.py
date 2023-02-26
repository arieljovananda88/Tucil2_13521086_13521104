import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def visualizer(points, pair):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    xs = [p.x for p in points]
    ys = [p.y for p in points]
    zs = [p.z for p in points]
    ax.scatter(xs, ys, zs)
    
    if pair:
        x_pair = [pair[0].x, pair[1].x]
        y_pair = [pair[0].y, pair[1].y]
        z_pair = [pair[0].z, pair[1].z]
        ax.scatter(x_pair, y_pair, z_pair, c='red',s=80)
    
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    plt.show()


