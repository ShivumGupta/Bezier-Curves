import numpy as np
import matplotlib.pyplot as plt

def lerp(p1,p2,n):
    interpolated_points = [] #np.ndarray(n+1)

    xseparation = (p1[0] + p2[0]) / n
    yseparation = (p1[1] + p2[1]) / n

    initialx = p1[0]
    initialy = p1[1]
    print (interpolated_points)
    for i in range (n+1):
        newx = initialx+(i*xseparation)
        newy = initialy+(i*yseparation)
        interpolated_points.append([newx,newy])
        #interpolated_points.append([newx,newy])
        #interpolated_points[i] = [newx,newy]

    return interpolated_points

p1 = [0,0]
p2 = [10,10]
n = 50

points = lerp(p1,p2,n)
print (points)
plt.plot([points[i][0] for i in range (n+1)],[points[i][1] for i in range (n+1)],"o")
#plt.plot(points[:,0],points[:,1])
plt.show()

