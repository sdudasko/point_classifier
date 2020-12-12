import random
import math
import matplotlib.pyplot as plt
from random import randrange
import config

COLORS = ("red", "green", "blue", "purple")
COLORS_SHORT = ("R", "G", "B", "P")


class classifier:
    STATISTICS = []
    testing_groups = {}
    distances = []

    def __init__(self, STATISTICS, init_training_points = True):
        self.STATISTICS = STATISTICS

        if init_training_points:
            self.testing_groups = {
                'R': [(-4500, -4400), (-4100, -3000), (-1800, -2400), (-2500, -3400), (-2000, -1400)],
                'G': [(4500, -4400), (4100, -3000), (1800, -2400), (2500, -3400), (2000, -1400)],
                'B': [(-4500, 4400), (-4100, 3000), (-1800, 2400), (-2500, 3400), (-2000, 1400)],
                'P': [(4500, 4400), (4100, 3000), (1800, 2400), (2500, 3400), (2000, 1400)],
            }
            # Adding training points to map
            x_es = []
            y_es = []

            for red_point in self.testing_groups['R']:
                x_es.append(red_point[0])
                y_es.append(red_point[1])

            plt.plot(x_es, y_es, 'ro', color='red')

            x_es.clear()
            y_es.clear()

            for green_point in self.testing_groups['G']:
                x_es.append(green_point[0])
                y_es.append(green_point[1])
            plt.plot(x_es, y_es, 'ro', color='green')
            x_es.clear()
            y_es.clear()

            for blue_point in self.testing_groups['B']:
                x_es.append(blue_point[0])
                y_es.append(blue_point[1])
            plt.plot(x_es, y_es, 'ro', color='blue')
            x_es.clear()
            y_es.clear()

            for purple_point in self.testing_groups['P']:
                x_es.append(purple_point[0])
                y_es.append(purple_point[1])
            plt.plot(x_es, y_es, 'ro', color='purple')


    def get_classification(self, p, k, use_distances = False):

        if not use_distances:
            distances = []
            for group in self.testing_groups:
                for feature in self.testing_groups[group]:
                    pythagoras_formula = math.sqrt((feature[0] - p[0]) ** 2 + (feature[1] - p[1]) ** 2)
                    distances.append((pythagoras_formula, group))

            self.distances = sorted(distances)[:k]

        freqRed = 0
        freqGreen = 0
        freqBlue = 0
        freqPurple = 0

        for distance in self.distances:
            if distance[1] == "R":
                freqRed += 1
            elif distance[1] == "G":
                freqGreen += 1
            elif distance[1] == "B":
                freqBlue += 1
            elif distance[1] == "P":
                freqPurple += 1
            else:
                raise Exception("Unknown value")

        # Len taky helper, uz si nepamatam z prveho rocnika jak sa robim minimum a rozmyslat sa mi nad tym nechce
        frequencies = (freqRed, freqGreen, freqBlue, freqPurple)

        return frequencies.index(max(frequencies))

    def create_and_classify_red_point(self, k=3):

        if randrange(100) >= config.CHANCE_FOR_RANDOM_POINT:
            x = random.randint(-config.GENERATOR_RANGE, 500)
            y = random.randint(-config.GENERATOR_RANGE, 500)
            p = (x, y)
        else:
            x = random.randint(-config.GENERATOR_RANGE, config.GENERATOR_RANGE)
            y = random.randint(-config.GENERATOR_RANGE, config.GENERATOR_RANGE)
            p = (x, y)

        classification_index = self.get_classification(p, k)
        self.testing_groups[COLORS_SHORT[classification_index]].append(p)  # Pridavame to pola trenovacich
        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie

        # For statistics, we either increment by one if right our classification matches or zero
        self.STATISTICS[k] += (COLORS_SHORT[classification_index] == "R")

    def create_and_classify_green_point(self, k=3):

        if randrange(100) >= config.CHANCE_FOR_RANDOM_POINT:
            x = random.randint(-500, config.GENERATOR_RANGE)
            y = random.randint(-config.GENERATOR_RANGE, 500)
            p = (x, y)
        else:
            x = random.randint(-config.GENERATOR_RANGE, config.GENERATOR_RANGE)
            y = random.randint(-config.GENERATOR_RANGE, config.GENERATOR_RANGE)
            p = (x, y)

        classification_index = self.get_classification(p, k)
        self.testing_groups[COLORS_SHORT[classification_index]].append(p)  # Pridavame to pola trenovacich
        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie

        # For statistics, we either increment by one if right our classification matches or zero
        self.STATISTICS[k] += (COLORS_SHORT[classification_index] == "G")

    def create_and_classify_blue_point(self, k=3):

        if randrange(100) >= config.CHANCE_FOR_RANDOM_POINT:
            x = random.randint(-config.GENERATOR_RANGE, 500)
            y = random.randint(500, config.GENERATOR_RANGE)
            p = (x, y)
        else:
            x = random.randint(-config.GENERATOR_RANGE, config.GENERATOR_RANGE)
            y = random.randint(-config.GENERATOR_RANGE, config.GENERATOR_RANGE)
            p = (x, y)

        classification_index = self.get_classification(p, k)
        self.testing_groups[COLORS_SHORT[classification_index]].append(p)  # Pridavame to pola trenovacich
        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie

        # For statistics, we either increment by one if right our classification matches or zero
        self.STATISTICS[k] += (COLORS_SHORT[classification_index] == "B")

    def create_and_classify_purple_point(self, k=3):

        if randrange(100) >= config.CHANCE_FOR_RANDOM_POINT:
            x = random.randint(-500, config.GENERATOR_RANGE)
            y = random.randint(-500, config.GENERATOR_RANGE)
            p = (x, y)
        else:
            x = random.randint(-config.GENERATOR_RANGE, config.GENERATOR_RANGE)
            y = random.randint(-config.GENERATOR_RANGE, config.GENERATOR_RANGE)
            p = (x, y)

        classification_index = self.get_classification(p, k)
        self.testing_groups[COLORS_SHORT[classification_index]].append(p)  # Pridavame to pola trenovacich
        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie

        # For statistics, we either increment by one if right our classification matches or zero
        self.STATISTICS[k] += (COLORS_SHORT[classification_index] == "P")

    def classify_random(self, p, k, first_iteration = False):
        if first_iteration:
            classification_index = self.get_classification(p, k, False)
        else:
            classification_index = self.get_classification(p, k, True)

        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie