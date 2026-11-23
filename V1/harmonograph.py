import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt

t = np.linspace(0, 40, 5000)

f1 = 3
f2 = 2
d = 0.02
p = 1.57

x = np.exp(-d * t) * np.sin(f1 * t + p)
y = np.exp(-d * t) * np.sin(f2 * t)

fig, ax = plt.subplots(figsize=(5,5))
fig.patch.set_facecolor('#0d1117')
ax.set_facecolor('#0d1117')

ax.plot(x, y, color='#39ff88', linewidth=2.5)
ax.axis('off')
ax.set_aspect('equal')

plt.savefig('avatar2.png', dpi=100, bbox_inches='tight', pad_inches=0)
plt.show()
