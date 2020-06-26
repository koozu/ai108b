from net import Net
net = Net()

x = net.variable(1)
y = net.variable(2)
z = net.variable(3)
x2 = net.mul(x, x)  # x*x=x2
y2 = net.mul(y, y)  # y*y=y2
z2 = net.mul(z, z)  # z*z=z2
o1 = net.add(x2, y2)  # x2+y2=o1
o  = net.add(o1, z2)  # o1+z2=o
net.gradient_descendent()
print('x=', x.v, 'y=', y.v, 'z=', z.v)