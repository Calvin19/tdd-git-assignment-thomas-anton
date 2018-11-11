"""
----------------------------------------------------------
Filename: statTools.py
Purpose: perform
Author: Anton Varabei
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
