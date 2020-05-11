#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None or len(a_dictionary) is 0:
        return None

    condition = True
    for person in a_dictionary:
        if condition:
            name = person
            score = a_dictionary[person]
            condition = False
        if a_dictionary[person] > score:
            score = a_dictionary[person]
            name = person
    return name
