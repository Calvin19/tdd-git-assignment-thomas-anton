"""
-----------------------------------------------------------------------------------------------------
Filename: statTools.py
Purpose: provide tools in order to find statistics: median, mode, lower quartile, and upper quartile

Author: Maglietta.T

Created: 31/10/2018
-----------------------------------------------------------------------------------------------------
"""


def lower_quartile(num_list: list) -> float:
    """
    Finds the lower quartile in a list of integers

    :param num_list: list of integers to find the lower quartile of
    :return: the lower quartile of num_list
    """

    try:
        exception_raiser = sum(num_list)  # force type error if not processing a list of ints
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
    except IndexError:
        raise IndexError('index is out of range')
    except TypeError:
        raise TypeError('a list of integers was not provided')
    except AttributeError:
        raise AttributeError('a list of integers was not provided')


def upper_quartile(num_list: list) -> float:
    """
    Finds the upper quartile in a list of integers

    :param num_list: list of integers to find the upper quartile of
    :return: the upper quartile of num_list
    """
    try:
        exception_raiser = sum(num_list)  # force type error if not processing a list of ints
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
    except IndexError:
        raise IndexError('index is out of range')
    except TypeError:
        raise TypeError('a list of integers was not provided')
    except AttributeError:
        raise AttributeError('a list of integers was not provided')


def median(num_list: list) -> float:
    """
    Finds the median in a list of  integers
    :param num_list: list
    :return: the median of the list
    """
    try:
        exception_raiser = sum(num_list)  # force type error if not processing a list of ints
        num_list.sort()
        key_index = len(num_list) // 2
        if len(num_list) % 2 == 0:  # check if median is average of two middle numbers
            num_1 = num_list[key_index]
            num_2 = num_list[key_index - 1]
            return (num_1 + num_2) / 2
        if len(num_list) % 2 == 1:  # check if median is single middle number in list
            return num_list[key_index]
    except IndexError:
        raise IndexError('index is out of range')
    except TypeError:
        raise TypeError('a list of integers was not provided')
    except AttributeError:
        raise AttributeError('a list of integers was not provided')


def mode(num_list):
    num_list.sort()
    max_occs = 0
    cur_occs = 0
    mode_list = []
    if not num_list:
        return []
    prev_num = num_list[0]
    i = 0
    while i < len(num_list):
        if num_list[i] == prev_num:
            cur_occs += 1
        else:
            if cur_occs > max_occs:
                max_occs = cur_occs
                mode_list = [num_list[i - 1]]
            elif cur_occs == max_occs:
                mode_list.append(num_list[i-1])
            cur_occs = 1
        prev_num = num_list[i]
        print(cur_occs)
        i += 1
    if cur_occs > max_occs:
        mode_list = [num_list[len(num_list)-1]]
    elif cur_occs == max_occs:
        mode_list.append(num_list[i - 1])
    return mode_list
