"""
Ryan Campbell
lab8.py
Problem Description -
I Ryan Campbell certify this assignment is entirely my own work.

"""


def weighted_average(in_file_name, out_file_name):
    opened_input_file = open(in_file_name, "r")
    opened_output_file = open(out_file_name, "w")
    number_of_students_grades = 0
    class_average = 0
    for line in opened_input_file.readlines():
        name_numbers = line.split(":")
        name_student = name_numbers[0]
        numbers_ = name_numbers[1]
        split_numbers = (numbers_.strip()).split(" ")
        number_of_numbers = len(split_numbers)
        total_weight = 0
        for i in range(0, number_of_numbers, 2):
            weight_ = split_numbers[i]
            total_weight = eval(weight_) + total_weight
        if total_weight == 100:
            total_grade = 0
            for i in range(0, number_of_numbers, 2):
                partial_grade = eval(split_numbers[i]) * eval(split_numbers[i + 1])
                total_grade = partial_grade + total_grade
            final_grade = total_grade / 100
            class_average = final_grade + class_average
            number_of_students_grades = 1 + number_of_students_grades
            print(name_student + "'s".lstrip(), "average:", round(final_grade, 1), file=opened_output_file)
        elif total_weight > 100:
            print(name_student + "'s", "average:", "Error: The weights are more than 100.", file=opened_output_file)
        elif total_weight < 100:
            print(name_student + "'s", "average:", "Error: The weights are less than 100.", file=opened_output_file)
    print("Class average:", class_average / number_of_students_grades, file=opened_output_file)
    opened_input_file.close()
    opened_output_file.close()


if __name__ == '__main__':
    weighted_average("graded.txt", "avg.txt")
