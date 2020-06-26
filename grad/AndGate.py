import gd3 as gd
import numpy as np
import math
from numpy.linalg import norm

# x      y      z    
# 0*w1 + 0*w2 + 1*b = 0
# 0*w1 + 1*w2 + 1*b = 0
# 1*w1 + 0*w2 + 1*b = 0
# 1*w1 + 1*w2 + 1*b = 1

# sigmoid函式使輸入變成介於(1,0)之間的值，並且在輸入等於0時，輸出等於0.5，當輸入遠大於0，則輸出會一直貼近1，反之，則貼近0
def sig(t): 
    return 1.0/(1.0+math.exp(-t))

def loss(p):
    [w1,w2,b] = p
    o0 = sig(w1*0+w2*0+b) 
    o1 = sig(w1*0+w2*1+b)
    o2 = sig(w1*1+w2*0+b)
    o3 = sig(w1*1+w2*1+b)
    delta = np.array([o0-o[0], o1-o[1], o2-o[2], o3-o[3]]) # 將sigmoid之後的輸出減掉正確答案，去判斷與正確答案的距離
    print('o0={:.3f} o1={:.3f} o2={:.3f} o3={:.3f}'.format(o0,o1,o2,o3))
    return np.linalg.norm(delta, 2)  # 取範數，功用像是矩陣的長度

o = [0, 0, 0, 1]  # 正確答案
p = [2.0, 2.0, -5.0]  # p = [w1, w2, b]
p = gd.gradientDescendent(loss, p, max_loops=1000)

print("\n-------------------\n")
print("w1 = {:.3f}\tw2 = {:.3f}\tw3 = {:.3f}".format(p[0],p[1],p[2]))
o[0] = sig(p[0]*0+p[1]*0+p[2])
o[1] = sig(p[0]*0+p[1]*1+p[2])
o[2] = sig(p[0]*1+p[1]*0+p[2])
o[3] = sig(p[0]*1+p[1]*1+p[2])
print("\nsig(w1*0+w2*0+b) = {:.3f}\nsig(w1*0+w2*1+b) = {:.3f}\nsig(w1*1+w2*0+b) = {:.3f}\nsig(w1*1+w2*1+b) = {:.3f}".format(o[0],o[1],o[2],o[3]))
print("\n-------------------\n")
