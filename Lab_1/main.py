import load_file
import analyze_file
import visual_file

stat_naming_mountain = []
stat_year_mountain = []
stat_count_death_mountain = []
stat_count_general_mountain = []
stat_reason_of_death = []

visualization_X = stat_naming_mountain
visualization_Y_1 = []
visualization_Y_2 = []
visualization_Y_3 = []

# Загрузка данных из файла
load_file.load_file(stat_naming_mountain, stat_year_mountain, stat_count_death_mountain, stat_count_general_mountain, stat_reason_of_death)

# Расчет процента смертности
visualization_Y_1 = analyze_file.mortality_calculator(stat_count_death_mountain, stat_count_general_mountain)
# Частота причин смерти на горах
visualization_Y_2 = analyze_file.reason_of_death_frequency(stat_reason_of_death)

# Визуализация графиков
visual_file.visual_file(visualization_X, visualization_Y_1, visualization_Y_2, stat_year_mountain)