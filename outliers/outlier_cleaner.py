#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10 percent of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    zipped_data = []
    ### your code goes here
    for pred, age, net_worth in zip(predictions, ages, net_worths):
        new_tuple = (age[0], net_worth[0],  abs(pred[0] - net_worth[0]))
        zipped_data.append(new_tuple)
    cleaned_data =sorted(zipped_data, key = lambda tup: tup[2])[9:]
    
    return cleaned_data

