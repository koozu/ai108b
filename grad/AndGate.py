import gd2 as gd
import numpy as np
import math
from numpy.linalg import norm

def sig(t):
    return 1.0/(1.0+math.exp(-t))

def loss(p):
    dot = np.dot(i,p)
    print('o0={:.3f} o1={:.3f} o2={:.3f}'.format(dot[0],dot[1],dot[2]))
    return np.linalg.norm(dot-o, 2)

i = np.array([[0,1,1], [1,0,1], [1,1,1]])
o = [0, 0, 1]
p = [1.0, 0.0, 1.0]
p = gd.gradientDescendent(loss, p)
dot = np.dot(i,p)

ans = []
for j in dot:
    ans.append(sig(j))

print("ans = {}".format(ans))