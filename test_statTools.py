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

# lower quartile tests


def lower_q_test_1():
    assert(lower_quartile([0, 50, 100, 150]) == 25)  # corner case--LQ is the average of 2 numbers


def lower_q_test_2():
    assert(lower_quartile([0, 25, 50, 75, 100, 125]) == 25)  # general case--returns item from index in list


def lower_q_test_3():
    assert (lower_quartile([0, 25, 50, 75, 100, 125, 150]) == 37.5)  # corner case--LQ is the average of 2 numbers


def lower_q_test_4():
    assert (lower_quartile([1, 2, 3, 4, 5, 6, 7, 8, 9]) == 3)  # general case--returns item from index in list


lower_q_test_1()
lower_q_test_2()
lower_q_test_3()
lower_q_test_4()
