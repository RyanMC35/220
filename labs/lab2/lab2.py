"""

Ryan Campbell
lab2.py
Problem Description - Setting up a program, that will have a flexible number of input volumes that can
compute multiple outputs.
Certificate of Authenticity - I, Ryan Campbell, certify that this lab is entirely my own work.
"""


def means():
    number_value = eval(input("How many values?:"))
    rms_accum = 0
    harmonic_mean_accum = 0
    geometric_mean_accum = 1
    for i in range(number_value):
        user_input = eval(input("Enter the value"))
        squared_value = user_input * user_input
        rms_accum = squared_value + rms_accum
        reciprocal = 1 / user_input
        harmonic_mean_accum = reciprocal + harmonic_mean_accum
        geometric_mean_accum = user_input * geometric_mean_accum
    division_of_sum = rms_accum / number_value
    division_of_sum_final = division_of_sum ** (1/2)
    print("The Real-Mean-Square value is ", round(division_of_sum_final, 3))
    harmonic_mean_accum = number_value / harmonic_mean_accum
    print("The Harmonic mean value is ", round(harmonic_mean_accum, 3))
    geometric_mean_accum = geometric_mean_accum ** (1/number_value)
    print("The Geometric mean value is", round(geometric_mean_accum, 3))
