import csv

def load_file(arg_naming_mountain, arg_year_mountain, arg_count_death_mountain, arg_count_general_mountain, arg_reason_of_death):
    with open('analytics.csv', 'r', encoding='utf-8') as datafile:
        array = csv.reader(datafile, delimiter=',')
        for i, data in enumerate(array):
            if (i != 0):
                arg_naming_mountain.append(data[0])
                arg_year_mountain.append(int(data[1]))
                arg_count_death_mountain.append(float(data[2]))
                arg_count_general_mountain.append(float(data[3]))
                arg_reason_of_death.append(data[4])
