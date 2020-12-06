import random
import math
import matplotlib.pyplot as plt

COLORS = ("red", "green", "blue", "purple")
COLORS_SHORT = ("R", "G", "B", "P")


class classifier:
    STATISTICS = []
    testing_groups = {}

    def __init__(self, STATISTICS):
        self.STATISTICS = STATISTICS

        self.testing_groups = {
            'R': [(-45, -44), (-41, -30), (-18, -24), (-25, -34), (-20, -14)],
            'G': [(45, -44), (41, -30), (18, -24), (25, -34), (20, -14)],
            'B': [(-45, 44), (-41, 30), (-18, 24), (-25, 34), (-20, 14)],
            'P': [(45, 44), (41, 30), (18, 24), (25, 34), (20, 14)],
        }

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


    def get_classification(self, p, k):
        distances = []
        for group in self.testing_groups:
            for feature in self.testing_groups[group]:
                euclidean_distances = math.sqrt((feature[0] - p[0]) ** 2 + (feature[1] - p[1]) ** 2)
                distances.append((euclidean_distances, group))

        distances = sorted(distances)[:k]

        freqRed = 0  # R
        freqGreen = 0  # G
        freqBlue = 0  # B
        freqPurple = 0  # P

        for distance in distances:
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

        x = random.randint(-50, 5)  # potom upravit o 2 desatinne miesta
        y = random.randint(-50, 5)  # potom upravit o 2 desatinne miesta
        p = (x, y)

        classification_index = self.get_classification(p, k)
        self.testing_groups[COLORS_SHORT[classification_index]].append(p)  # Pridavame to pola trenovacich
        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie

        # For statistics, we either increment by one if right our classification matches or zero
        self.STATISTICS[k] += (COLORS_SHORT[classification_index] == "R")

    def create_and_classify_green_point(self, k=3):

        x = random.randint(-5, 50)  # potom upravit o 2 desatinne miesta
        y = random.randint(-50, 5)  # potom upravit o 2 desatinne miesta
        p = (x, y)

        classification_index = self.get_classification(p, k)
        self.testing_groups[COLORS_SHORT[classification_index]].append(p)  # Pridavame to pola trenovacich
        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie

        # For statistics, we either increment by one if right our classification matches or zero
        self.STATISTICS[k] += (COLORS_SHORT[classification_index] == "G")

    def create_and_classify_blue_point(self, k=3):

        x = random.randint(-50, 5)  # potom upravit o 2 desatinne miesta
        y = random.randint(5, 50)  # potom upravit o 2 desatinne miesta
        p = (x, y)

        classification_index = self.get_classification(p, k)
        self.testing_groups[COLORS_SHORT[classification_index]].append(p)  # Pridavame to pola trenovacich
        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie

        # For statistics, we either increment by one if right our classification matches or zero
        self.STATISTICS[k] += (COLORS_SHORT[classification_index] == "B")

    def create_and_classify_purple_point(self, k=3):

        x = random.randint(-5, 50)  # potom upravit o 2 desatinne miesta
        y = random.randint(-5, 50)  # potom upravit o 2 desatinne miesta
        p = (x, y)

        classification_index = self.get_classification(p, k)
        self.testing_groups[COLORS_SHORT[classification_index]].append(p)  # Pridavame to pola trenovacich
        plt.plot(p[0], p[1], 'or', color=COLORS[classification_index])  # Pridame bod a dame ho do klasifikacie

        # For statistics, we either increment by one if right our classification matches or zero
        self.STATISTICS[k] += (COLORS_SHORT[classification_index] == "P")
