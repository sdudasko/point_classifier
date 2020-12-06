from array import *
import matplotlib.pyplot as plt
import math
import random

from classifier import classifier

STATISTICS = {
    1: 0,
    3: 0,
    7: 0,
    15: 0
}

plt.plot([-150, 150], [0, 0])
plt.plot([-0, 0], [-150, 150])

def get_class_where_i_belong():
    pass


all_points = list()

for group in classifier.testing_groups:
    for point in classifier.testing_groups[group]:
        all_points.append(point)

def get_missing_points():
    matrix = list()
    for i in range(-10, 10):
        for j in range(-10, 10):
            matrix.append([i, j])
    random.shuffle(matrix)

    return matrix


def fill_missing_points():
    k = 1
    pts = get_missing_points()
    for i in range(-400, 400):
        p = (pts[i][0], pts[i][1])

        _classifier = classifier(STATISTICS)

        _classifier.create_and_classify_red_point(k)
        _classifier.create_and_classify_green_point(k)
        _classifier.create_and_classify_blue_point(k)
        _classifier.create_and_classify_purple_point(k)


fill_missing_points()
print(STATISTICS)

plt.show()
# plt.axis([-15, 15, -15, 15])
