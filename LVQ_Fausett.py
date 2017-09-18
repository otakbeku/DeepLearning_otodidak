import numpy as np


def jarak(x, bobot):
    dist = 0
    for i in range(len(x)):
        dist += np.fabs(x[i] - bobot[i])
    return dist


# Training Vector
x = np.array([[1, 1, 0, 0], [0, 0, 0, 1], [0, 0, 1, 1], [1, 0, 0, 0], [0, 1, 1, 0]])
# Class
y = np.array([[1], [2], [2], [1], [1]])

# Bobot
w1 = [x[0], y[0]]
w2 = [x[1], y[1]]

a = 0.1
epoch = 200

for i in range(epoch):
    for xi in range(2, len(x)):
        d1 = jarak(x[xi], w1[0])
        d2 = jarak(x[xi], w2[0])

        if d1 < d2:
            if y[xi] == w1[1]:
                w1[0] = w1[0] + (np.dot(a, np.subtract(x[xi], w1[0])))
            else:
                w1[0] = w1[0] - (np.dot(a, np.subtract(x[xi], w1[0])))
        else:
            if y[xi] == w1[1]:
                w2[0] = w2[0] + (np.dot(a, np.subtract(x[xi], w1[0])))
            else:
                w2[0] = w2[0] - (np.dot(a, np.subtract(x[xi], w1[0])))

        a = a - 0.01
print(w1)
print(w2)
