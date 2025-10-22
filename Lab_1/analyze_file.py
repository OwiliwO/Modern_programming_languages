from collections import Counter

def mortality_calculator(arg_count_death_mountain, arg_count_general_mountain):
    arg_mortality = []
    for i in range(len(arg_count_death_mountain)):
        arg_mortality.append(arg_count_death_mountain[i] / arg_count_general_mountain[i] * 100)
    return arg_mortality

def reason_of_death_frequency(arg_reason_of_death):
    return Counter(arg_reason_of_death)