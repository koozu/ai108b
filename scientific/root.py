import math

def root2(a,b,c):
    t = b*b - 4*a*c
    t2 = math.sqrt(t) if t>0 else complex(0,math.sqrt(abs(t)))
    return [(-b+t2)/(2*a), (-b-t2)/(2*a)]

print("root of x^2+1=", root2(1,0,1))
