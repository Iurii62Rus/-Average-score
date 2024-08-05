grades = [[1, 2, 3, 4, 0, 5], [4, 4, 3, 5], [3, 2, 5, 4, 1], [5, 5, 3, 4, 3], [5, 5, 4, 3, 3]]
students = ['Pablo Escobar', 'Grigory Rasputin', 'Yuri Kharlamov', 'Peter the First', 'Iiiigar']
def calculate_average(grades):
    return sum(grades) / len(grades)
averages = {}
for i, student in enumerate(students):
    if i < len(grades):
        averages[student] = calculate_average(grades[i])
    else:
        averages[student] = 0
print(averages)
