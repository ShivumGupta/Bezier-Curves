import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation

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

def cubic_Bezier(p1,p2,p3,p4,n):
    interpolated_points = np.ndarray((n+1,2))
    qB1 = quadratic_Bezier (p1,p2,p3,n)
    qB2 = quadratic_Bezier (p2,p3,p4,n)

    for i in range (n+1):
        lerp_of_quadratics = lerp(qB1[i],qB2[i],n)[i]
        interpolated_points[i] = [lerp_of_quadratics[0],lerp_of_quadratics[1]]

    return interpolated_points


p1 = [10,10]
p2 = [100,170]
p3 = [150,920]
p4 = [200,7]
n = 50

# qpoints = quadratic_Bezier(p1,p2,p3,n)
# plt.plot(qpoints[:,0],qpoints[:,1],"-")

# cpoints = cubic_Bezier(p1,p2,p3,p4,n)
# plt.plot(cpoints[:,0],cpoints[:,1],"-")

# cols = ["tab:blue","tab:orange","tab:red","tab:green","tab:pink"]

lerp_points = lerp(p1,p2,n)
draw = lerp_points

fig = plt.figure()
ax = plt.axes(xlim=(0,1.1*max(draw[:,0])), ylim=(0,1.1*max(draw[:,1])))
line, = ax.plot([],[],"-")
ax.scatter([p1[0],p2[0]],[p1[1],p2[1]],color="gray")
points = ax.scatter(p1[0],p1[1],color="black")

def update(i):
    to_draw = draw[:i]
    xpoints = to_draw[:,0]
    ypoints = to_draw[:,1]
    line.set_xdata (xpoints)
    line.set_ydata (ypoints)
    points.set_offsets([to_draw[-1][0],to_draw[-1][1]])
    return line,

anim = animation.FuncAnimation(fig, update, interval=100,blit=False,frames=np.arange(1,n+2,1),repeat=False)
plt.show()