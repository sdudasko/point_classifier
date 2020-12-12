import random
import matplotlib.pyplot as plt

import config
from classifier import classifier

STATISTICS = {
    1: 0,
    3: 1,
    7: 1,
    15: 1
}

_classifier = classifier(STATISTICS)
all_points = list()

for group in classifier.testing_groups:
    for point in classifier.testing_groups[group]:
        all_points.append(point)


def get_missing_points():
    matrix = list()
    for i in range(-config.GENERATOR_RANGE, config.GENERATOR_RANGE):
        print(f"Getovanie radu: {i}")
        for j in range(-config.GENERATOR_RANGE, config.GENERATOR_RANGE):
            matrix.append([i, j])
    random.shuffle(matrix)

    return matrix

first_iteration = True
def fill_missing_points():
    global first_iteration
    pts = get_missing_points()

    _classifier = classifier(STATISTICS, False)

    for i in range(-2 * config.GENERATOR_RANGE ** 2, 2 * config.GENERATOR_RANGE ** 2):
        p = (pts[i][0], pts[i][1])
        print(f"Vyplnanie radu: {i}")
        if first_iteration:
            _classifier.classify_random(p, 1, True)
            first_iteration = False
        else:
            _classifier.classify_random(p, 1, False)


def fill_new_training_points():
    for k in [1, 3, 7, 15]:
        plt.plot([-config.GENERATOR_RANGE, config.GENERATOR_RANGE], [0, 0])
        plt.plot([-0, 0], [-config.GENERATOR_RANGE, config.GENERATOR_RANGE])
        plt.title(f'k = {k}')

        _classifier = classifier(STATISTICS)
        for x in range(config.NEW_POINTS_KVARTAL_COUNT):
            _classifier.create_and_classify_red_point(k)
            _classifier.create_and_classify_green_point(k)
            _classifier.create_and_classify_blue_point(k)
            _classifier.create_and_classify_purple_point(k)
        plt.show()


fill_new_training_points()
# fill_missing_points()
# plt.show()

def prettify_statistics():
    print(f"Number of points: {config.NEW_POINTS_KVARTAL_COUNT * 4 + 20}")
    for k_val in STATISTICS:
        print(f"k = {k_val}. Classified correctly: {STATISTICS[k_val] / (config.NEW_POINTS_KVARTAL_COUNT * 4) * 100}%")


prettify_statistics()
