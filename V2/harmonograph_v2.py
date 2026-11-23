import numpy as np
import matplotlib; matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

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

ax.axis('off')
ax.set_aspect('equal')

line, = ax.plot([], [], color='#39ff88', linewidth=2.5)
ax.set_xlim(-1.1, 1.1)
ax.set_ylim(-1.1, 1.1)

total_frames = 100
fps = 30

def update(frame):
    idx = int((frame + 1) / total_frames * len(x))
    line.set_data(x[:idx], y[:idx])

    return (line,)

anim = FuncAnimation(fig, update, frames=total_frames, interval=1000/fps, blit = True)

anim.save('harmonograph_anim.gif', writer=PillowWriter(fps=fps), dpi = 100)

print("Done!")
