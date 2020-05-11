#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
    if type(roman_string) is not str:
        return 0

    sum = 0
    for i in range(len(roman_string)):
        if i is (len(roman_string) - 1):
            sum += get_val(roman_string[i])
        else:
            if get_val(roman_string[i]) >= get_val(roman_string[i+1]):
                    sum += get_val(roman_string[i])
            else:
                    sum -= get_val(roman_string[i])
    return sum


def get_val(char):
        if char == 'I':
            return 1
        elif char == 'V':
            return 5
        elif char == 'X':
            return 10
        elif char == 'L':
            return 50
        elif char == 'C':
            return 100
        elif char == 'D':
            return 500
        elif char == 'M':
            return 1000
