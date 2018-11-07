"""
----------------------------------------------------------
Filename: test_tatTools.py
Purpose: tests the functions in statTools.py

Author: Maglietta.T

Created: 31/10/2018
----------------------------------------------------------
"""

import pytest
from statTools import *


test_list_1 = [1, 2, 3, 4]
test_list_2 = [1, 2, 3, 4, 5, 6]
test_list_3 = [1, 2, 3, 4, 5, 6, 7]
test_list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# lower quartile tests


def lower_q_test_1():
    assert(lower_quartile(test_list_1) == 1.5)  # corner case--LQ is the average of 2 numbers


def lower_q_test_2():
    assert(lower_quartile(test_list_2) == 2)  # general case--returns item from index in list


def lower_q_test_3():
    assert (lower_quartile(test_list_3) == 2.5)  # corner case--LQ is the average of 2 numbers


def lower_q_test_4():
    assert (lower_quartile(test_list_4) == 3)  # general case--returns item from index in list

# upper quartile tests


def upper_q_test_1():
    assert (upper_quartile() == 5)


def upper_q_test_2():
    assert (upper_quartile() == 3)


lower_q_test_1()
lower_q_test_2()
lower_q_test_3()
lower_q_test_4()

#upper_q_test_1()
#upper_q_test_2()
