from array import *
import matplotlib.pyplot as plt
import math


def classifyAPoint(points, p, k=3):
    '''
     This function finds the classification of p using
     k nearest neighbor algorithm. It assumes only two
     testing_groups and returns 0 if p belongs to group 0, else
      1 (belongs to group 1).

      Parameters -
          points: Dictionary of training points having two keys - 0 and 1
                   Each key have a list of training data points belong to that

          p : A tuple, test data point of the form (x,y)

          k : number of nearest neighbour to consider, default is 3
    '''

    distance = []
    for group in points:
        for feature in points[group]:
            # calculate the euclidean distance of p from training points
            euclidean_distance = math.sqrt((feature[0] - p[0]) ** 2 + (feature[1] - p[1]) ** 2)

            # Add a tuple of form (distance,group) in the distance list
            distance.append((euclidean_distance, group))

            # sort the distance list in ascending order
    # and select first k distances
    distance = sorted(distance)[:k]

    freq1 = 0  # frequency of group 0
    freq2 = 0  # frequency og group 1

    for d in distance:
        if d[1] == 0:
            freq1 += 1
        elif d[1] == 1:
            freq2 += 1

    return 0 if freq1 > freq2 else 1


testing_groups = {
    'R': [(-4.5, -4.4), (-4.1, -3), (-1.8, -2.4), (-2.5, -3.4), (-2, -1.4)],
    'G': [(4.5, -4.4), (4.1, -3), (1.8, -2.4), (2.5, -3.4), (2, -1.4)],
    'B': [(-4.5, 4.4), (-4.1, 3), (-1.8, 2.4), (-2.5, 3.4), (-2, 1.4)],
    'P': [(4.5, 4.4), (4.1, 3), (1.8, 2.4), (2.5, 3.4), (2, 1.4)],
}

plt.plot([-15, 15], [0, 0])
plt.plot([-0, 0], [-15, 15])

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

# plt.axis([-15, 15, -15, 15])


# testing point p(x,y)
p = (2.5, 7)
plt.plot(2.5, 7, 'or')
# Number of neighbours
k = 3

print("The value classified to unknown point is: {}". \
      format(classifyAPoint(testing_groups, p, k)))

plt.show()