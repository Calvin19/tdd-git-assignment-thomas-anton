"""
work on:
lower_quartile
upper_quartile
median
mode
"""


def lower_quartile(num_list: list) -> float:
    """
    -median of lower half of list
    -include median when searching in an odd sized list
    -use nums before median when using an even sized list
    """
    num_list.sort()  # sort the list or it will not be accurate
    key_index = len(num_list) // 4
    if len(num_list) % 4 == 2 or len(num_list) % 4 == 1:  # check for lists where the LQ is in the list
        return num_list[key_index]
    elif len(num_list) % 4 == 0:  # check if list is even
        num_1 = num_list[key_index]
        num_2 = num_list[key_index - 1]  # LQ found is an average of 2 numbers
        return (num_1 + num_2) / 2
    elif len(num_list) % 4 == 3:  # check if list is even
        num_1 = num_list[key_index]
        num_2 = num_list[key_index + 1]
        return (num_1 + num_2) / 2  # LQ found is an average of 2 numbers
