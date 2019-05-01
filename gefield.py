# coding utf-8
# 2019/05/01 21:00 ichiro

import numpy as np
import matplotlib.pyplot as plt
import math

Q = (((0.0, 0.0), 10.0), ((5.0, -5.0), 5.0))
TIMELIMIT = 20.0
RLIMIT = 0.1
H = 0.01

t = 0.0

for qi in Q:
    plt.plot(qi[0][0], qi[0][1], ".")

vx = float(input("初速度 V0 の X 成分："))
vy = float(input("初速度 V0 の Y 成分："))
x = float(input("初期位置 X："))
y = float(input("初期位置 Y："))

xlist = [x]
ylist = [y]

while t < TIMELIMIT:
    t = t + H
    rmin = float("inf")
    for qi in Q:
        rx = qi[0][0] - x
        ry = qi[0][1] - y
        r = math.sqrt(rx ** 2 + ry ** 2)
        if r < rmin:
            rmin = r
        vx += (rx / r / r / r * qi[1]) * H
        vy += (ry / r / r / r * qi[1]) * H
    x += vx * H
    y += vy * H
    xlist.append(x)
    ylist.append(y)
    if rmin < RLIMIT:
        break

plt.plot(xlist, ylist)
plt.show()
