import random as r

n = ['你', '我', '他']

def S():
    return N0() + VP()

def NP():
    return DET() + N2()

def VP():
    return V() + N1() + NP()

def N0():
    return n.pop(r.choice(range(len(n))))

def N1():
    return r.choice(n)

def N2():
    return r.choice(['麥香奶茶', '珍珠奶茶', '可樂', '雪碧', 'RedBull'])

def V():
    return r.choice(['請', '拿', '喝', '搶'])

def DET():
    return r.choice(['一瓶', '一罐', '一箱'])

print(S(),end='')
while(r.choice([0,1])==0) :
    print('又' + VP(),end='')

