import pytest
from statTools import *


def lower_q_test_1():
    assert(lower_quartile() == 0)


def lower_q_test_2():
    assert(lower_quartile() == 1)


lower_q_test_1()
lower_q_test_2()
