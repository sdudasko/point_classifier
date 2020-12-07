from array import *
import matplotlib.pyplot as plt
import math
import random
from classifier import classifier
import config

STATISTICS = {
    1: 0,
    3: 0,
    7: 0,
    15: 0
}

_classifier = classifier(STATISTICS)

def get_class_where_i_belong():
    pass


all_points = list()

for group in classifier.testing_groups:
    for point in classifier.testing_groups[group]:
        all_points.append(point)


def get_missing_points():
    matrix = list()
    for i in range(-config.GENERATOR_RANGE, config.GENERATOR_RANGE):
        for j in range(-config.GENERATOR_RANGE, config.GENERATOR_RANGE):
            matrix.append([i, j])
    random.shuffle(matrix)

    return matrix


def fill_missing_points():
    pts = get_missing_points()
    for i in range(-2 * config.GENERATOR_RANGE ** 2, 2 * config.GENERATOR_RANGE ** 2):
        p = (pts[i][0], pts[i][1])

        _classifier = classifier(STATISTICS)
        _classifier.classify_random(p, 1)


def fill_new_training_points():
    # for k in [1, 3, 7, 15]:
    for k in [3]:
        plt.plot([-config.GENERATOR_RANGE, config.GENERATOR_RANGE], [0, 0])
        plt.plot([-0, 0], [-config.GENERATOR_RANGE, config.GENERATOR_RANGE])
        plt.title(f'k = {k}')

        for x in range(config.NEW_POINTS_KVARTAL_COUNT):
            _classifier.create_and_classify_red_point(k)
            _classifier.create_and_classify_green_point(k)
            _classifier.create_and_classify_blue_point(k)
            _classifier.create_and_classify_purple_point(k)
        plt.show()


fill_new_training_points()
fill_missing_points()
plt.show()

def prettify_statistics():
    for k_val in STATISTICS:
        if k_val == 3:
            print(f"{_classifier.STATISTICS[k_val]} / {_classifier.STATISTICS[k_val] / (config.NEW_POINTS_KVARTAL_COUNT * 4)}")
            print(STATISTICS[k_val] / (config.NEW_POINTS_KVARTAL_COUNT * 4) * 100)


prettify_statistics()

# plt.show()
# plt.axis([-15, 15, -15, 15])
