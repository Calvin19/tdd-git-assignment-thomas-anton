"""
work on:
lower_quartile
upper_quartile
variance
standard deviation
"""


def lower_quartile(num_list: list)->float:
    """
    median of lower half of list
    include median when searching in an odd sized list
    use nums before median when using an even sized list
    """
    num_list.sort()
    if len(num_list) % 2 != 0:
        #if list is odd length
        num_list = num_list[0:len(num_list)//2 + 1]#takes first half of list

    return num_list


print(lower_quartile([1, 2, 3, 5, 7, 9, 10]))
