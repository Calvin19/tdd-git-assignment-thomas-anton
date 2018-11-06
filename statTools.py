"""
work on:
lower_quartile
upper_quartile
median
mode
"""


def lower_quartile(num_list: list)->float:
    """
    median of lower half of list
    include median when searching in an odd sized list
    use nums before median when using an even sized list
    """
    num_list.sort()
    if len(num_list) % 4 == 2: #check for even sized lists where the LQ is in the list
        return num_list[len(num_list)//4]
    elif len(num_list) % 4 == 0: #check if list is even and LQ is found an average of 2 numbers
        num_1 = num_list[len(num_list)//4]
        num_2 = num_list[len(num_list)//4 - 1]
        return (num_1 + num_2)/2
    elif len(num_list) % 4 == 3:
        num_1 = num_list[len(num_list) // 4]
        num_2 = num_list[len(num_list) // 4 + 1]
        return (num_1 + num_2) / 2
