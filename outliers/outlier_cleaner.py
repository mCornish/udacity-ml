#!/usr/bin/python3


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    import math
    coll = list(zip(predictions, ages, net_worths))

    with_errors = []
    for pred, age, worth in coll:
        error = abs(worth - pred)
        with_errors.append((age[0], worth[0], error[0]))

    sorted_errors = sorted(with_errors, key=lambda tup: tup[2])

    removal_count = math.floor(len(sorted_errors) * .1)
    new_len = len(sorted_errors) - removal_count
    
    cleaned_data = sorted_errors[0:new_len]

    return cleaned_data

