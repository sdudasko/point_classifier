from array import *
import matplotlib.pyplot as plt
import math
import random

COLORS = ("red", "green", "blue", "purple")
COLORS_SHORT = ("R", "G", "B", "P")

testing_groups = {
    'R': [(-45, -44), (-41, -30), (-18, -24), (-25, -34), (-20, -14)],
    'G': [(45, -44), (41, -30), (18, -24), (25, -34), (20, -14)],
    'B': [(-45, 44), (-41, 30), (-18, 24), (-25, 34), (-20, 14)],
    'P': [(45, 44), (41, 30), (18, 24), (25, 34), (20, 14)],
}

plt.plot([-150, 150], [0, 0])
plt.plot([-0, 0], [-150, 150])

x_es = []
y_es = []

for red_point in testing_groups['R']:
    x_es.append(red_point[0])
    y_es.append(red_point[1])
plt.plot(x_es, y_es, 'ro', color='red')
x_es.clear()
y_es.clear()

for green_point in testing_groups['G']:
    x_es.append(green_point[0])
    y_es.append(green_point[1])
plt.plot(x_es, y_es, 'ro', color='green')
x_es.clear()
y_es.clear()

for blue_point in testing_groups['B']:
    x_es.append(blue_point[0])
    y_es.append(blue_point[1])
plt.plot(x_es, y_es, 'ro', color='blue')
x_es.clear()
y_es.clear()

for purple_point in testing_groups['P']:
    x_es.append(purple_point[0])
    y_es.append(purple_point[1])
plt.plot(x_es, y_es, 'ro', color='purple')


def get_class_where_i_belong():
    pass


all_points = list()

for group in testing_groups:
    for point in testing_groups[group]:
        all_points.append(point)


def get_classification(p, k):
    distances = []
    for group in testing_groups:
        for feature in testing_groups[group]:
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

def create_and_classify_red_point(p, k = 3):
    global testing_groups

    # Dont make random variables please, I should have learned that from last assignment
    # x = random.randint(-50, 5)  # potom upravit o 2 desatinne miesta
    # y = random.randint(-50, 5)  # potom upravit o 2 desatinne miesta

    # Pridavame to pola trenovacich, je to dobre? pri 40k to bude krastne
    testing_groups[COLORS_SHORT[get_classification(p, k)]].append(p)

    # Zistujeme farbu, resp. klasifikaciu
    plt.plot(p[0], p[1], 'or', color=COLORS[get_classification(p, k)])


# plt.axis([-15, 15, -15, 15])

# Number of neighbours
k = 3

p = (5, 5)
create_and_classify_red_point(p, k)
p = (5, 10)
create_and_classify_red_point(p, k)
p = (5, 15)
create_and_classify_red_point(p, k)
p = (-5, 2)
create_and_classify_red_point(p, k)

plt.show()
