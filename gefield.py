# coding utf-8
# 2019/05/01 21:00 ichiro

# モジュールをインポート
import numpy as np
import matplotlib.pyplot as plt
import math

# 定数
Q = (((0.0, 0.0), 10.0), ((5.0, -5.0), 5.0))    # 電荷 ((x, y), q)
TIMELIMIT = 20.0    # 打ち切り時間
RLIMIT = 0.1    # 距離の最低値
H = 0.01    # 時刻の刻み幅

t = 0.0 # 時刻

# 電荷をプロット
for qi in Q:
    plt.plot(qi[0][0], qi[0][1], ".")

# 初期値を入力
vx = float(input("初速度 V0 の X 成分："))
vy = float(input("初速度 V0 の Y 成分："))
x = float(input("初期位置 X："))
y = float(input("初期位置 Y："))

# グラフデータに初期値を追加
xlist = [x]
ylist = [y]

# シミュレーション開始
while t < TIMELIMIT:    # 打ち切り時間まで繰り返し
    t = t + H   # 時刻を更新
    rmin = float("inf") # 距離の最小値をリセット
    for qi in Q:
        rx = qi[0][0] - x
        ry = qi[0][1] - y
        r = math.sqrt(rx ** 2 + ry ** 2)    # 距離の計算
        if r < rmin:
            rmin = r    # 距離の最小値を更新
        vx += (rx / r / r / r * qi[1]) * H  # 速度の計算
        vy += (ry / r / r / r * qi[1]) * H
    x += vx * H     # 位置の計算
    y += vy * H
    xlist.append(x) # グラフデータの更新
    ylist.append(y)
    if rmin < RLIMIT:
        break   # 電荷に近づきすぎたら終了

# グラフを表示
plt.plot(xlist, ylist)  # プロット
plt.show()  # 表示
