#!/usr/bin/python3
#calebbaraka79@gmail.com

def weight_average(my_list=[]):
    """Returns the weighted average of all integers tuple."""
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)

    avg = 0
    size = 0

    for tup in my_list:
        avg += (tup[0] * tup[1])
        size += tup[1]
    return (avg / size)
