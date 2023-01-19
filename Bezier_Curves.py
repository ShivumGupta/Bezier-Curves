import numpy as np
import matplotlib.pyplot as plt

def lerp(p1,p2,n):
    interpolated_points = np.ndarray((n+1,2))
    steps = 1/n
    
    for i in range (n+1):
        t = i*steps
        interpolated_points[i] = np.multiply((1-t),p1) + np.multiply(t,p2)

    return interpolated_points

def quadratic_Bezier(p1,p2,p3,n):
    interpolated_points = np.ndarray((n+1,2))
    lerp1 = lerp (p1,p2,n)
    lerp2 = lerp (p2,p3,n)

    for i in range (n+1):
        lerp_of_lerps = lerp(lerp1[i],lerp2[i],n)[i]
        interpolated_points[i] = [lerp_of_lerps[0],lerp_of_lerps[1]]

    return interpolated_points

p1 = [0,0]
p2 = [100,170]
p3 = [150,920]
n = 50

points = lerp(p1,p2,n)
points2 = lerp(p2,p3,n)
qpoints = quadratic_Bezier(p1,p2,p3,n)
#plt.plot(points[:,0],points[:,1],"--")
#plt.plot(points2[:,0],points2[:,1],"--")
#plt.plot(qpoints[:,0],qpoints[:,1],"-")

cols = ["tab:blue","tab:orange","tab:red","tab:green","tab:pink"]

for i in range (1,6):
    qpoints = quadratic_Bezier(p1,np.multiply(p2,i),p3,n)
    plt.plot(qpoints[:,0],qpoints[:,1],"-",color=cols[i-1])
    plt.scatter(np.multiply(p2,i)[0],np.multiply(p2,i)[1],color=cols[i-1])
plt.show()

#print (qpoints)
