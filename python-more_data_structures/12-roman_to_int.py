#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0

    roman_numerals = [
        ['M', 1000], ['D', 500], ['C', 100], ['L', 50],
        ['X', 10], ['V', 5], ['I', 1]
    ]
    result = 0
    previous_value = 0

    for symbol in roman_string:
        for numeral in roman_numerals:
            if symbol == numeral[0]:
                if previous_value == 0 or previous_value >= numeral[1]:
                    result += numeral[1]
                elif previous_value < numeral[1]:
                    result += numeral[1] - (previous_value * 2)

                previous_value = numeral[1]

    return result
