import matplotlib.pyplot as plt
import random as rn
import numpy as np

def visual_file(arg_X, arg_Y_1, arg_Y_2, arg_year_mountain):
    current_X = []
    current_Y = []
    all_Y = []
    current_years = set(arg_year_mountain)
    current_set_X = set(arg_X)
    current_position_set_X = range(len(current_set_X))
    width = 0.25

    plt.figure(figsize = (14, 7))
    plt.gcf().canvas.manager.set_window_title('Анализ рисков в альпинизме: временные тенденции и факторы смерти')
    plt.subplot(1, 2, 1)

    for i in range(len(current_years)):
        current_X = []
        current_Y = []
        current_positions = []
        for j in range(len(arg_year_mountain)):
            if (list(current_years)[i] == arg_year_mountain[j]):
                current_X.append(arg_X[j])
                current_Y.append(float(arg_Y_1[j]))
                all_Y.append(float(arg_Y_1[j]))
                current_positions.append(list(current_set_X).index(arg_X[j]))
        offset = i * width
        shifted_positions = [pos + offset for pos in current_positions]

        plt.bar(shifted_positions, current_Y, width = width, color = (rn.random(), rn.random(), rn.random()), label = str(list(current_years)[i]) + ' г.')

    plt.title('Анализ рисков в альпинизме: временные тенденции')
    plt.xticks(ticks = current_position_set_X, labels = current_set_X, fontsize = 5, rotation = 45)
    plt.xlabel('Название горы')
    plt.yticks(np.arange(0, max(all_Y), 2.5))
    plt.ylabel('Процент смертности')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(list(arg_Y_2.keys()), list(arg_Y_2.values()))
    plt.title('Анализ рисков в альпинизме: факторы смерти')
    plt.xticks(fontsize = 5, rotation = 45)
    plt.xlabel('Причина смерти')
    plt.ylabel('Частота')

    plt.show()