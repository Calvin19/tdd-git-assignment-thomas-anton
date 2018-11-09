"""
-----------------------------------------------------------------------------------------------------
Filename: statTools.py
Purpose: provide tools in order to find statistics: median, mode, lower quartile, and upper quartile

Author: Maglietta.T

Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
"""


def lower_quartile(num_list: list):
    """
    Finds the lower quartile in a list of integers

    :param num_list: list of integers to find the lower quartile of
    :return: the lower quartile of num_list
    """

    try:
        num_list.sort()  # sort the list or it will not be accurate
        key_index = len(num_list) // 4
        if len(num_list) % 4 == 2 or len(num_list) % 4 == 1:  # check for lists where the LQ is in the list
            return num_list[key_index]
        elif len(num_list) % 4 == 0:  # check if list is even
            num_1 = num_list[key_index]
            num_2 = num_list[key_index - 1]  # LQ found is an average of 2 numbers
            return (num_1 + num_2) / 2
        elif len(num_list) % 4 == 3:  # check if list is odd
            num_1 = num_list[key_index]
            num_2 = num_list[key_index + 1]
            return (num_1 + num_2) / 2  # LQ found is an average of 2 numbers
    except ValueError:
        print('Value Error')
        return ValueError
    except IndexError:
        print('Index Error')
        return IndexError


def upper_quartile(num_list):
    """
    Finds the upper quartile in a list of integers

    :param num_list: list of integers to find the upper quartile of
    :return: the upper quartile of num_list
    """
    num_list.sort()
    key_index = (len(num_list)-1) - (len(num_list)//4)
    if len(num_list) % 4 == 2 or len(num_list) % 4 == 1:  # check for lists where UQ is in list
        return num_list[key_index]
    elif len(num_list) % 4 == 0:  # check for lists where UQ is the average between to numbers
        num_1 = num_list[key_index]
        num_2 = num_list[key_index + 1]
        return (num_1 + num_2) / 2
    elif len(num_list) % 4 == 3:  # check for lists where UQ is the average between to numbers
        num_1 = num_list[key_index]
        num_2 = num_list[key_index - 1]
        return (num_1 + num_2) / 2


def median(num_list):
    num_list.sort()
    key_index = len(num_list) // 2
    if len(num_list) % 2 == 0:
        num_1 = num_list[key_index]
        num_2 = num_list[key_index - 1]
        return (num_1 + num_2) / 2
