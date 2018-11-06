import pytest
from statTools import *


def lower_q_test_1():
    assert(lower_quartile([0, 50, 100, 150]) == 25)


def lower_q_test_2():
    assert(lower_quartile([0, 25, 50, 75, 100]) == 25)


def lower_q_test_3():
    assert (lower_quartile([0, 25, 50, 75, 100, 125, 150, 175, 200]) == 37.5)


lower_q_test_1()
lower_q_test_2()
lower_q_test_3()
