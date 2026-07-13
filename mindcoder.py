# print("hello world ")
# age = 18
# print(age)
# age = "four"
# print(age)
# name = "tilak"
# age = 19
# print("i am ", name,"i am",age,"year old")

# iery Sun Burst — infinity/lemniscate loop pattern
# ---------------------------------------------------
# Recreates the glowing double-loop "sun burst" effect from the screenshot:
# many concentric lemniscate (figure-eight / infinity) curves, layered with
# a yellow -> orange -> red gradient on a black background, continuously
# rotating so it runs forever.

# Requirements:
#     pip install matplotlib numpy


# import numpy as np
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# from matplotlib.colors import LinearSegmentedColormap

# # ---------- Figure / style setup ----------
# fig, ax = plt.subplots(figsize=(6, 8), facecolor="black")
# ax.set_facecolor("black")
# ax.set_xlim(-1.6, 1.6)
# ax.set_ylim(-1.6, 1.6)
# ax.set_aspect("equal")
# ax.axis("off")

# # Fiery colormap: yellow core -> orange -> deep red edges
# fire_cmap = LinearSegmentedColormap.from_list(
#     "fire", ["#fff6b0", "#ffd400", "#ff8c00", "#ff3b00", "#8c1400"]
# )

# N_LOOPS = 90          # number of nested curves (density of the "burst")
# POINTS = 800          # resolution of each curve
# t = np.linspace(0, 2 * np.pi, POINTS)

# lines = []
# for i in range(N_LOOPS):
#     frac = i / (N_LOOPS - 1)          # 0 -> 1 across the loops
#     color = fire_cmap(frac)
#     lw = 0.6 + 1.4 * (1 - abs(frac - 0.5) * 2)  # thicker near the middle
#     (ln,) = ax.plot([], [], color=color, linewidth=lw, alpha=0.85)
#     lines.append(ln)


# def lemniscate(scale, squash, phase, theta):
#     """
#     Vertical figure-eight ("infinity") curve, based on r^2 = cos(2*theta).
#     squash slightly flattens each loop so it reads as two "petals"
#     joined at the center, like the reference image.
#     phase rotates/twists this particular layer for the woven look.
#     """
#     r2 = np.cos(2 * theta)
#     r = np.sqrt(np.clip(r2, 0, None))
#     x = scale * r * np.cos(theta + phase)
#     y = scale * squash * r * np.sin(theta + phase)
#     # rotate the whole figure-eight 90 degrees so it stands vertically
#     x, y = -y, x
#     return x, y


# def init():
#     for ln in lines:
#         ln.set_data([], [])
#     return lines


# def animate(frame):
#     global_twist = frame * 0.01  # slow continuous rotation -> runs forever
#     for i, ln in enumerate(lines):
#         frac = i / (N_LOOPS - 1)
#         scale = 0.3 + 1.25 * frac              # loops grow outward
#         squash = 1.0                            # petal roundness
#         # each layer offset slightly in phase to build the "woven" glow
#         phase = global_twist + frac * 0.35 * np.sin(frame * 0.01 + i)
#         x, y = lemniscate(scale, squash, phase, t)
#         ln.set_data(x, y)
#     return lines


# ani = animation.FuncAnimation(
#     fig, animate, init_func=init, frames=None, interval=30, blit=True, cache_frame_data=False
# )

# plt.tight_layout()
# plt.show()

# To save an infinite-looking GIF instead of a live window, comment out
# plt.show() above and use something like:
#
# ani = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=30, blit=True)
# ani.save("fiery_sunburst.gif", writer="pillow", fps=30)