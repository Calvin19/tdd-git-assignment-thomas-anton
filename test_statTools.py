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
test_list_5 = [1, 2, 3]
test_list_6 = [1, 2]
test_list_7 = [1]
test_list_8 = []
test_not_list = 'a'
test_str_list = ['a', 'b', 'c', 'd', 'e', 'f']
# lower quartile tests


def lower_q_test_1():
    assert(lower_quartile(test_list_1) == 1.5)  # corner case--LQ is the average of 2 numbers


def lower_q_test_2():
    assert(lower_quartile(test_list_2) == 2)  # general case--returns item from index in list


def lower_q_test_3():
    assert (lower_quartile(test_list_3) == 2.5)  # corner case--LQ is the average of 2 numbers


def lower_q_test_4():
    assert (lower_quartile(test_list_4) == 3)  # general case--returns item from index in list


def lower_q_test_5():
    assert (lower_quartile(test_list_5) == 1.5)


def lower_q_test_6():
    assert (lower_quartile(test_list_6) == 1)


def lower_q_test_7():
    assert (lower_quartile(test_list_7) == 1)


def lower_q_test_8():
    assert (lower_quartile(test_list_8) is IndexError)


def lower_q_test_9():
    assert (lower_quartile(test_not_list) is TypeError)


def lower_q_test_10():
    assert (lower_quartile(test_str_list) == '4')

# upper quartile tests


def upper_q_test_1():
    assert (upper_quartile(test_list_1) == 3.5)


def upper_q_test_2():
    assert (upper_quartile(test_list_2) == 5)


def upper_q_test_3():
    assert (upper_quartile(test_list_3) == 5.5)


def upper_q_test_4():
    assert (upper_quartile(test_list_4) == 7)


lower_q_test_1()
lower_q_test_2()
lower_q_test_3()
lower_q_test_4()
lower_q_test_5()
lower_q_test_6()
lower_q_test_7()
lower_q_test_8()
#lower_q_test_9()
#lower_q_test_10()


upper_q_test_1()
upper_q_test_2()
upper_q_test_3()
upper_q_test_4()
