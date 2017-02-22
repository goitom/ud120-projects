#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    ### your code goes here
    cleaned_data = [a_i - b_i for a_i, b_i in zip(predictions, net_worths)]
    
    
    return cleaned_data

