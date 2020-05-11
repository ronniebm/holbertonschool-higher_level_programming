#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) is 0:
        return 0

    result = 0
    divisor = 0
    scores, weights = zip(*my_list)
    scores = list(scores)
    weights = list(weights)

    for i in range(len(weights)):
        result += scores[i] * weights[i]
        divisor += weights[i]
    return result / divisor
