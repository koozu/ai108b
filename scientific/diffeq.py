from sympy import Function, dsolve, Eq, Derivative, sin, cos, symbols
from sympy.abc import C,V,R,t
V = Function('V')
sol = dsolve(Derivative(V(t), t)*C + V(t)/R,V(t))
print('dsolve(Derivative(V(t), t)* + V/R,V(t))=', sol.doit())