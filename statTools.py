"""
work on:
lower_quartile
upper_quartile
variance
standard deviation
"""


def lower_quartile(num_list: list)->float:
    num_list.sort()
    return num_list[1]

