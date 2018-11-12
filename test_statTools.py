"""
----------------------------------------------------------
Filename: test_statTools.py
Purpose: test the functions in statTools file
Author: Anton Varabei Maglietta.T
Created: 11/9/18
----------------------------------------------------------
"""
import pytest
from statTools import *
ltest1 = []
ltest2 = [0]
ltest3 = [999999999]
ltest4 = [0, 999999]
ltest5 = [0, 0, 0]
ltest6 = [1, 1, 1]
ltest7 = [99999, 99999, 99999]
ltest8 = [0, 1, 2, 3, 4, 5, 6]
ltest9 = [6, 5, 4, 3, 2, 1, 0]
ltest10 = [0.05, 9.4, 7, 2, 1, 8, 0]
ltest11 = ["hello!", 6, "c", 9.2]
ltest12 = ["8", "2", "3.9"]

def testmean1():
    assert(mean(ltest1) == "Invalid Input, please try again!")


def testmean2():
    assert (mean(ltest2) == 0)


def testmean3():
    assert (mean(ltest3) == 999999999)


def testmean4():
    assert (mean(ltest4) == 499999.5)


def testmean5():
    assert (mean(ltest5) == 0)

def testmean6():
    assert (mean(ltest6) == 1)


def testmean7():
    assert (mean(ltest7) == 99999)


def testmean8():
    assert (mean(ltest8) == 3)


def testmean9():
    assert (mean(ltest9) == 3)


def testmean10():
    assert (round(mean(ltest10)) == 4)


def testmean11():
    assert(mean(ltest11) == "Invalid Input, please try again!")


def testmean12():
    assert(mean(ltest12) == "Invalid Input, please try again!")


def testrange1():
    assert (numrange(ltest1) == "Invalid Input, please try again!")


def testrange2():
    assert (numrange(ltest2) == 0)


def testrange3():
    assert (numrange(ltest3) == 0)


def testrange4():
    assert (numrange(ltest4) == 999999)


def testrange5():
    assert (numrange(ltest5) == 0)


def testrange6():
    assert (numrange(ltest6) == 0)


def testrange7():
    assert (numrange(ltest7) == 0)


def testrange8():
    assert (numrange(ltest8) == 6)


def testrange9():
    assert (numrange(ltest9) == 6)


def testrange10():
    assert (numrange(ltest10) == 9.4)


def testrange11():
    assert (numrange(ltest11) == "Invalid Input, please try again!")


def testrange12():
    assert (numrange(ltest12) == "Invalid Input, please try again!")


def testvari1():
  assert (variance(ltest1) == "Invalid Input, please try again!")


def testvari2():
  assert (variance(ltest2) == 0)


def testvari3():
  assert (variance(ltest5) == 0)


def testvari4():
  assert (variance(ltest6) == 0)


def testvari5():
  assert (variance(ltest8) == 4)


def testvari6():
  assert (round(variance(ltest10)) == 14)

def testsdv1():
  assert (round(standev(ltest1)) == "Invalid Input, please try again!")


def testsdv2():
  assert (round(standev(ltest2)) == 0)


def testsdv3():
  assert (round(standev(ltest5)) == 0)


def testsdv4():
  assert (round(standev(ltest6)) == 0)


def testsdv5():
  assert (round(standev(ltest8)) == 4)


def testsdv6():
  assert (round(standev(ltest10)) == 4)




test_list_1 = [1, 2, 3, 4]
test_list_2 = [1, 2, 3, 4, 5, 6]
test_list_3 = [1, 2, 3, 4, 5, 6, 7]
test_list_4 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test_list_5 = [1, 2, 3]
test_list_6 = [1, 2]
test_list_7 = [1]
test_empty_list = []
test_not_list = 'a'
test_str_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
# lower quartile tests


def test_lower_q_1():
    assert(lower_quartile(test_list_1) == 1.5)  # corner case -- LQ is the average of 2 numbers


def test_lower_q_2():
    assert(lower_quartile(test_list_2) == 2)  # general case -- returns item from index in list


def test_lower_q_3():
    assert (lower_quartile(test_list_3) == 2.5)  # corner case -- LQ is the average of 2 numbers


def test_lower_q_4():
    assert (lower_quartile(test_list_4) == 3)  # general case -- returns item from index in list


def test_lower_q_5():
    assert (lower_quartile(test_list_5) == 1.5)  # corner case -- list smaller than 4 items


def test_lower_q_6():
    assert (lower_quartile(test_list_6) == 1)  # corner case -- list smaller than 4 items


def test_lower_q_7():
    assert (lower_quartile(test_list_7) == 1)  # corner case -- list smaller than 4 items


def test_lower_q_empty_ls():  # unusual case --  empty list
    with pytest.raises(IndexError) as errmsg:
        lower_quartile(test_empty_list)
    assert ('index is out of range' == str(errmsg.value))


def test_lower_q_not_ls():  # unusual case -- not a list
    with pytest.raises(TypeError) as errmsg:
        lower_quartile(test_not_list)
    assert ('a list of integers was not provided' == str(errmsg.value))


def test_lower_q_str_ls():  # unusual case -- list of strings
    with pytest.raises(TypeError) as errmsg:
        lower_quartile(test_str_list)
    assert ('a list of integers was not provided' == str(errmsg.value))

# upper quartile tests


def test_upper_q_1():
    assert (upper_quartile(test_list_1) == 3.5)  # corner case -- LQ is the average of 2 numbers


def test_upper_q_2():
    assert (upper_quartile(test_list_2) == 5)  # general case -- returns item from index in list


def test_upper_q_3():
    assert (upper_quartile(test_list_3) == 5.5)  # corner case -- LQ is the average of 2 numbers


def test_upper_q_4():
    assert (upper_quartile(test_list_4) == 7)  # general case -- returns item from index in list


def test_upper_q_5():
    assert (upper_quartile(test_list_5) == 2.5)  # corner case -- LQ is the average of 2 numbers


def test_upper_q_6():
    assert (upper_quartile(test_list_6) == 2)  # corner case -- list smaller than 4 items


def test_upper_q_7():
    assert (upper_quartile(test_list_7) == 1)  # corner case -- list smaller than 4 items


def test_upper_q_empty_ls():  # unusual case -- empty list
    with pytest.raises(IndexError) as errmsg:
        upper_quartile(test_empty_list)
    assert ('index is out of range' == str(errmsg.value))


def test_upper_q_not_ls():  # unusual case -- not a list
    with pytest.raises(TypeError) as errmsg:
        upper_quartile(test_not_list)
    assert ('a list of integers was not provided' == str(errmsg.value))


def test_upper_q_str_ls():  # unusual case -- list of strings
    with pytest.raises(TypeError) as errmsg:
        upper_quartile(test_str_list)
    assert ('a list of integers was not provided' == str(errmsg.value))

# median tests


def test_median_1():
    assert (median(test_list_1) == 2.5)  # corner case -- median is the average of 2 numbers


def test_median_2():
    assert (median(test_list_3) == 4)  # general case -- returns item from index in list


def test_median_3():  # corner case -- list size is smaller than 2
    assert (median(test_list_7) == 1)


def test_median_empty_ls():  # unusual case -- empty list
    with pytest.raises(IndexError) as errmsg:
        median(test_empty_list)
    assert ('index is out of range' == str(errmsg.value))


def test_median_not_ls():  # unusual case -- not a list
    with pytest.raises(TypeError) as errmsg:
        median(test_not_list)
    assert ('a list of integers was not provided' == str(errmsg.value))


def test_median_str_ls():  # unusual case -- list of strings
    with pytest.raises(TypeError) as errmsg:
        median(test_str_list)
    assert ('a list of integers was not provided' == str(errmsg.value))

# mode tests, needs to use different lists


def test_mode_1():
    assert(mode([1, 1, 2]) == [1])  # general case -- has one mode


def test_mode_2():
    assert (mode([1, 1, 2, 2, 2]) == [2])  # general case -- has one mode


def test_mode_3():
    assert (mode([1]) == [1])  # general case -- has one mode


def test_mode_4():
    assert (mode([1, 1, 2, 2, 3]) == [1, 2])  # corner case has more than 1 mode


def test_mode_5():
    assert (mode([]) == [])  # corner case -- empty list has no mode


def test_mode_str_ls():  # list of strings can have mode
    assert (mode(['a', 'a', 'b']) == ['a'])


def test_mode_not_ls():  # unusual case -- not a list
    with pytest.raises(AttributeError) as errmsg:
        mode(1)
    assert ('Must input a list' == str(errmsg.value))


def test_mode_multi_type():  # unusual case -- needs to compare items of various data types
    with pytest.raises(TypeError) as errmsg:
        mode([1, 'a'])
    assert ('Must input a list that contains only 1 data type' == str(errmsg.value))
