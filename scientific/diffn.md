# diffn
## code
```py
from math import *

step = 0.05  # 取近似值時會產生誤差，所以讓x離遠一點，但我還是不懂為什麼影響這麼大
def df(f, x, h=step):
    return (f(x+h)-f(x-h))/(2*h)

def dfn(f, x, n, h=step):
    if (n == 0): return f(x)
    if (n == 1): return df(f,x,h)
    return (dfn(f, x+h, n-1) - dfn(f, x-h, n-1))/(2*h)

print('df(sin, pi/4)=', df(sin, pi/4))

for i in range(10):
    print('dfn(sin,', i, 'pi/4)=', dfn(cos, pi/4, i))
```
## result
```
df(sin, pi/4)= 0.7068121901873392
dfn(sin, 0 pi/4)= 0.7071067811865476
dfn(sin, 1 pi/4)= -0.7068121901873392
dfn(sin, 2 pi/4)= -0.7065177219190422
dfn(sin, 3 pi/4)= 0.7062233763303061
dfn(sin, 4 pi/4)= 0.7059291533706435
dfn(sin, 5 pi/4)= -0.7056350529111022
dfn(sin, 6 pi/4)= -0.7053410749913169
dfn(sin, 7 pi/4)= 0.705047190630026
dfn(sin, 8 pi/4)= 0.7047534111848108
dfn(sin, 9 pi/4)= -0.7044487770890839
```