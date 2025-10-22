import matplotlib.pyplot as plt
import csv

X = []
Y = []

with open('lab_1_test.csv', 'r') as datafile:
    plotting = csv.reader(datafile, delimiter=',')

    for rows in plotting:
        X.append(float(rows[5]))
        Y.append(float(rows[1]))

plt.plot(X, Y)
plt.title('Line Graph using CSV')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()