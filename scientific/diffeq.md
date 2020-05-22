# diffeq
## code
```py
from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import C,V,R,t
V = Function('V')
sol = dsolve(Derivative(V(t), t)*C + V(t)/R,V(t))  # 根據克希荷夫電路定律我們求得電流於電容器所耗時間內產生的變化的微分方程
print('dsolve(Derivative(V(t), t)* + V/R,V(t))=', sol.doit())
```
## result
```
dsolve(Derivative(V(t), t)* + V/R,V(t))= Eq(V(t), exp((C1 - t/R)/C))
```