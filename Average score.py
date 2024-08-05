grades = [[1, 2, 3, 4, 0, 5], [4, 4, 3, 5], [3, 2, 5, 4, 1], [5, 5, 3, 4, 3], [5, 5, 4, 3, 3]]
students = ['Pablo Escobar', 'Grigory Rasputin', 'Yuri Kharlamov', 'Peter the First', 'Iiiigar']
def calculate_average(grades):
    return sum(grades) / len(grades)
averages = {}
sorted_students = sorted(students)

for student in sorted_students:
    if student in students:
        index = students.index(student)
        averages[student] = calculate_average(grades[index])
    else:
        averages[student] = 0
print(averages)
