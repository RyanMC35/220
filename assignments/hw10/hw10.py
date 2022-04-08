"""
Name: Ryan Campbell
hw10.py
Problem: to create computation functions without while loops
and to create classes that can be used to create graphics.
Certification of Authenticity: I, Ryan Campbell, certify this assignment
is entirely my own work.
<include one of the following>
I certify that this assignment is entirely my own work.
I certify that this assignment is my own work, but I discussed it with: <Name(s)>


"""
import graphics
from face import Face


def fibonacci(n):
    sequence = []
    numbers_in_sequence = 0
    if n < 1:
        return None
    while numbers_in_sequence != n:
        if numbers_in_sequence == 0:
            sequence.append(1)
            numbers_in_sequence = numbers_in_sequence + 1
        if numbers_in_sequence == 1:
            sequence.append(1)
            numbers_in_sequence = numbers_in_sequence + 1
        if numbers_in_sequence > 1:
            number = sequence[numbers_in_sequence - 1] + sequence[numbers_in_sequence - 2]
            sequence.append(number)
            numbers_in_sequence = numbers_in_sequence + 1
    return sequence[n-1]


def double_investment(principle, rate):
    total = principle
    years = 0
    while total <= (principle * 2):
        total = total * (1 + rate)
        years = years + 1
    return years


def syracuse(num):
    number = num
    sequence = []
    while number != 1:
        if number % 2 == 1:
            sequence.append(int(number))
            number = 3 * number + 1
        if number % 2 == 0:
            sequence.append(int(number))
            number = (number / 2)
    sequence.append(int(number))
    return sequence


def goldbach(n):
    if (n > 2) and (n % 2) == 0:
        all_numbers = []
        number = 1
        while number < n:
            all_numbers.append(number)
            number += 1

        # above this fine
        i = 0
        list_of_primes = []
        while i < len(all_numbers):
            num = 2
            value = True
            while num < (int(all_numbers[i])) and value:
                is_not_prime = all_numbers[i] % num
                if is_not_prime == 0 and num != all_numbers[i]:
                    value = False
                    num += 1
                else:
                    value = True
                    num += 1
            if value:
                list_of_primes.append(all_numbers[i])
            i += 1

        # below this is fine
        j = 0
        while j < len(list_of_primes):
            i = 0
            while i < len(list_of_primes) - 1:
                if list_of_primes[j] + list_of_primes[i] == n:
                    return [list_of_primes[i], list_of_primes[j]]
                else:
                    i += 1
            j += 1
    return None


def face():
    win = graphics.GraphWin("Face", 500, 500)
    win.setCoords(10, 10, 0, 0)
    the_face = Face(win, graphics.Point(5, 5), 2)
    win.getMouse()

    the_face.shock()
    win.getMouse()
    win.close()

