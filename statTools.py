"""
----------------------------------------------------------
Filename: statTools.py
Purpose: perform
Author: Anton Varabei, Maglietta.T
Created: 11/9/18
----------------------------------------------------------
"""
import math
def mean(alist):
    '''
    This function returns the mean of a given list of numbers
    :alist: a list of numbers
    :finalnum: the mean of the list of numbers is returned
    '''
    try:
        listclone = alist
        #make counter variable to hold our numbers before final
        numsum = 0
        for item in listclone:
            #hold the number of
            numsum = numsum + item
        finalnum = numsum / len(alist)
        return finalnum
    except:
        #if invalid inputs then return the exception message
        return "Invalid Input, please try again!"


def numrange(alist):
    '''
    This function returns the range of a given list of numbers
    :alist: a list of numbers
    :fRange: the range of a number set is returned
    '''
    try:
        #subtract minimum from maximum
        fRange = max(alist) - min(alist)
        return fRange
    except:
        # if invalid inputs then return the exception message
        return "Invalid Input, please try again!"

def variance(alist):
    '''
    This function finds the variance of a given list of numbers
    :alist: a list of numbers
    :returning: the variance of the given list
    '''
    try:
        #find the mean
        meanvar = mean(alist)
        numlist = []
        #fill the empty list with square differences
        for i in alist:
            squardiff = i-meanvar
            squardiff = squardiff * squardiff
            numlist.append(squardiff)
        #return the mean of the square differences to finally get variance
        return mean(numlist)
        # exceptions not required because they would have been caught in nestedfunctions
    except:
        return "Invalid Input, please try again!"


def standev(alist):
    '''
    This function gives the standard deviations of a list when called upon
    :alist: a list of numbers
    :returning: the standard deviation from a list's mean
    '''
    try:
        #call upon variance before modifying it to standard deviation
        sdv = variance(alist)
        sdv = math.sqrt(sdv)
        return sdv
        #exceptions not required because they would have been caught in nestedfunctions
    except:
        return "Invalid Input, please try again!"


def lower_quartile(num_list: list) -> float:
    """Finds the lower quartile in a list of integers

    :param num_list: list of integers to find the lower quartile of
    :return: float the lower quartile of num_list
    """

    try:
        exception_raiser = sum(num_list)  # force type error if not processing a list of ints
        num_list.sort()  # sort the list or it will not be accurate
        key_index = len(num_list)//4
        if len(num_list) % 4 == 2 or len(num_list) % 4 == 1:  # check for lists where the LQ is in the list
            return num_list[key_index]
        elif len(num_list) % 4 == 0:  # check if list is even
            num_1 = num_list[key_index]
            num_2 = num_list[key_index - 1]  # LQ found is an average of 2 numbers
            return (num_1 + num_2)/2
        elif len(num_list) % 4 == 3:  # check if list is odd
            num_1 = num_list[key_index]
            num_2 = num_list[key_index + 1]
            return (num_1 + num_2)/2  # LQ found is an average of 2 numbers
    except IndexError:
        raise IndexError('index is out of range')
    except TypeError:
        raise TypeError('a list of integers was not provided')
    except AttributeError:
        raise AttributeError('a list of integers was not provided')


def upper_quartile(num_list: list) -> float:
    """Finds the upper quartile in a list of integers

    :param num_list: list of integers to find the upper quartile of
    :return: float the upper quartile of num_list
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
            return (num_1 + num_2)/2
        elif len(num_list) % 4 == 3:  # check for lists where UQ is the average between to numbers
            num_1 = num_list[key_index]
            num_2 = num_list[key_index - 1]
            return (num_1 + num_2)/2
    except IndexError:
        raise IndexError('index is out of range')
    except TypeError:
        raise TypeError('a list of integers was not provided')
    except AttributeError:
        raise AttributeError('a list of integers was not provided')


def median(num_list: list) -> float:
    """Finds the median in a list of  integers

    :param num_list: list
    :return: float the median of num_list
    """
    try:
        exception_raiser = sum(num_list)  # force type error if not processing a list of ints
        num_list.sort()
        key_index = len(num_list)//2
        if len(num_list) % 2 == 0:  # check if median is average of two middle numbers
            num_1 = num_list[key_index]
            num_2 = num_list[key_index - 1]
            return (num_1 + num_2)/2
        if len(num_list) % 2 == 1:  # check if median is single middle number in list
            return num_list[key_index]
    except IndexError:
        raise IndexError('index is out of range')
    except TypeError:
        raise TypeError('a list of integers was not provided')
    except AttributeError:
        raise AttributeError('a list of integers was not provided')


def mode(item_list):
    """Finds the mode of a list containing one data type

    :param item_list: list of items to find the mode of
    :return: list the mode of item_list
    """
    try:
        item_list.sort()
        max_occs = 0  # most occurrences of a value in the list
        cur_occs = 0  # number of occurrences of the currently evaluated value
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
