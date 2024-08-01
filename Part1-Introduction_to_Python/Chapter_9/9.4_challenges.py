universities = [
        ['California Institute of Technology', 2175, 37704],
        ['Harvard', 19627, 39848],
        ['Massachusetts Institute of Technology', 10566, 40732],
        ['Princeton', 7802, 37000],
        ['Rice', 5879, 35551],
        ['Stanford', 19535, 40569],
        ['Yale', 11701, 40500]
    ]

def enrollment_stats(list_universities):
    total_students = []
    total_tuition = []

    for university in list_universities:
        total_students.append(university[1])
        total_tuition.append(university[2])

    print(total_students)
    return total_students, total_tuition

def median(values):
    values.sort()

    if len(values) % 2 == 1:
        center_index = int(len(values) / 2)
        return values[center_index]
    else:
        left_center_index = (len(values) - 1) // 2
        right_center_index = (len(values) + 1) // 2
        return mean([[values[left_center_index]], values[right_center_index]])

def mean(values):
    return sum(values) / len(values)

total_students, total_tuition = enrollment_stats(universities)


print(total_students)
print(total_tuition)

print('******' * 6)
print(f"Total students: {sum(total_students)}")
print(f"Total tuition: {sum(total_tuition)}")


print(f"Student mean: {mean(total_students):.2f}")
print(f"Student median: {median(total_students)}")


print(f"Tuition mean: {mean(total_tuition):.2f}")
print(f"Tuition median: {median(total_tuition):.2f}")
