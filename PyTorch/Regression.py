import torch
import matplotlib.pyplot as plt
import torch.nn.functional as F

x = torch.unsqueeze(torch.linspace(-1, 1, 100), dim=1)  # size從(100)變(100,1)
y = x.pow(2) + 0.2*torch.rand(x.size())  # 加入一些噪音來模仿真實情況

plt.scatter(x.data.numpy(), y.data.numpy())
plt.ion()
plt.show()


class Net(torch.nn.Module):
    def __init__(self, n_feature, n_hidden, n_output):
        super(Net, self).__init__()
        self.hidden = torch.nn.Linear(n_feature, n_hidden)
        self.predict = torch.nn.Linear(n_hidden, n_output)

    def forward(self, x):
        x = F.relu(self.hidden(x))
        x = self.predict(x)
        return x


net = Net(n_feature=1, n_hidden=10, n_output=1)

optimizer = torch.optim.SGD(net.parameters(), lr=0.2)  # SGD是隨機梯度下降
loss_func = torch.nn.MSELoss()

for t in range(200):
    prediction = net(x)
    loss = loss_func(prediction, y)  # 計算兩者誤差平方的平均，平方會使偏離更多的值受到更嚴厲的懲罰
    optimizer.zero_grad()  # 清空當前梯度快取，否則之前的梯度會累加到當前的梯度
    loss.backward()  
    optimizer.step()

    if t % 5 == 0:
        plt.cla()
        plt.scatter(x.data.numpy(), y.data.numpy())
        plt.plot(x.data.numpy(), prediction.data.numpy(), 'r-', lw=5)
        plt.text(0.5, 0, 'Loss=%.4f' % loss.data.numpy(),
                 fontdict={'size': 20, 'color':  'red'})
        plt.pause(0.1)
