import random
import numpy as np
import matplotlib.pyplot as plt
np.set_printoptions(precision=4, suppress=True)
freq = random.randint(0,4)
t = np.arange(0, 10, 0.1)
ft = np.cos(freq*t*(2*np.pi))
fi = np.fft.fft(ft)  # 離散傅立葉轉換
# print('ft=', ft)
# print('fi=', fi)
print('freq=', freq)

plt.plot(t[range(int(len(t)/2))],ft[range(int(len(t)/2))],label="$y = 10 sin(f x)$", color="red", linewidth=2)
plt.plot(t[range(int(len(t)/2))],fi[range(int(len(t)/2))],label="ifft: y$", color="blue", linewidth=2)
plt.show()
 