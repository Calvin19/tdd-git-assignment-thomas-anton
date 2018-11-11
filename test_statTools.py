"""
----------------------------------------------------------
Filename: test_statTools.py
Purpose: tests the functions in statTools file
Author: Anton Varabei
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
