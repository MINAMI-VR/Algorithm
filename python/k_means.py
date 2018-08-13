import math
import random
import matplotlib.pyplot as plt


def clustering(data, center):
    group = [0] * len(data)
    difference = [float(0)] * len(data)

    while 1:
        i = 0
        while i < len(data):
            difference[i] = math.pow(data[i][0] - center[0][0], 2) + math.pow(data[i][1] - center[0][1], 2)
            group[i] = 0

            j = 1
            while j < len(center):
                if difference[i] > math.pow(data[i][0] - center[j][0], 2) + math.pow(data[i][1] - center[j][1], 2):
                    difference[i] = math.pow(data[i][0] - center[j][0], 2) + math.pow(data[i][1] - center[j][1], 2)
                    group[i] = j
                j += 1
            i += 1

        data_sum = [[0 for i in range(2)] for j in range(len(center))]
        n = [0] * len(center)

        i = 0
        while i < len(data):
            data_sum[group[i]][0] += data[i][0]
            data_sum[group[i]][1] += data[i][1]
            n[group[i]] += 1
            i += 1

        center_previous = [[0 for i in range(2)] for j in range(len(center))]

        i = 0
        while i < len(center):
            center_previous[i][0] = center[i][0]
            center_previous[i][1] = center[i][1]

            if n[i] > 0:
                center[i][0] = data_sum[i][0] / n[i]
                center[i][1] = data_sum[i][1] / n[i]
            i += 1

        if center == center_previous:
            return group


data = [[0 for i in range(2)] for j in range(random.randint(50, 100))]
center = [[0 for i in range(2)] for j in range(random.randint(3, 10))]
color = ["red", "green", "blue", "yellow", "black", "magenta", "cyan", "pink", "navy", "crimson"]

i = 0
while i < len(data):
    data[i][0] = random.randint(0, 100)
    data[i][1] = random.randint(0, 100)
    i += 1

i = 0
while i < len(center):
    center[i][0] = random.randint(0, 100)
    center[i][1] = random.randint(0, 100)
    i += 1

group = clustering(data, center)

x = [[] for i in range(len(center))]
y = [[] for i in range(len(center))]

i = 0
while i < len(data):
    x[group[i]].append(data[i][0])
    y[group[i]].append(data[i][1])
    i += 1

fig = plt.figure()

ax = fig.add_subplot(1, 1, 1)

i = 0
while i < len(center):
    ax.scatter(x[i], y[i], c=color[i])
    i += 1

ax.set_title('k means')
ax.set_xlabel('x')
ax.set_ylabel('y')

fig.show()
