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


def mode(item_list):
    """
    Finds the mode of a list containing one data type

    :param item_list: list of items to find the mode of
    :return: the mode of the list
    """
    try:
        item_list.sort()
        max_occs = 0
        cur_occs = 0
        mode_list = []
        if not item_list:  # Check for empty list to return no mode
            return []
        prev_item = item_list[0]
        i = 0
        while i < len(item_list):  # use while since for
            if item_list[i] == prev_item:  # check if current item is the same as the last item
                cur_occs += 1
            else:
                if cur_occs > max_occs:  # check if there needs to be a new mode
                    max_occs = cur_occs
                    mode_list = [item_list[i - 1]]  # replace mode(s) with new mode
                elif cur_occs == max_occs:  # check if there is an/are additional mode(s)
                    mode_list.append(item_list[i - 1])  # add new mode to list
                cur_occs = 1  # reset occurrences since new item
            prev_item = item_list[i]
            i += 1
        if cur_occs > max_occs:  # if elif statement does mode checks for last set of items in list
            mode_list = [item_list[len(item_list) - 1]]
        elif cur_occs == max_occs:
            mode_list.append(item_list[i - 1])
        return mode_list
    except TypeError:
        raise TypeError('Must input a list that contains only 1 data type')
    except AttributeError:
        raise AttributeError('Must input a list')
