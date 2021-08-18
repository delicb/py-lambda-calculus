from .lambda_calculus import *


# testing utils, pure python, no lambda calculus
def to_int(num):
    return num(lambda x: x+1)(0)

def from_int(n):
    cur = ZERO
    for _ in range(n):
        cur = SUCC(cur)
    return cur


# tests

def test_true():
    assert TRUE(1)(2) == 1

def test_false():
    assert FALSE(1)(2) == 2

def test_and():
    assert AND(TRUE)(TRUE) is TRUE
    assert AND(TRUE)(FALSE) is FALSE
    assert AND(FALSE)(TRUE) is FALSE
    assert AND(FALSE)(FALSE) is FALSE


def test_or():
    assert OR(TRUE)(TRUE) is TRUE
    assert OR(TRUE)(FALSE) is TRUE
    assert OR(FALSE)(TRUE) is TRUE
    assert OR(FALSE)(FALSE) is FALSE

def test_not():
    assert NOT(TRUE) is FALSE
    assert NOT(FALSE) is TRUE

def test_zero():
    assert to_int(ZERO) == 0

def test_succ():
    cur = ZERO
    for i in range(1, 10):
        cur = SUCC(cur)
        assert to_int(cur) == i

def test_cons():
    pair = CONS(ONE)(TWO)
    assert to_int(pair(TRUE)) == 1
    assert to_int(pair(FALSE)) == 2


def test_car_cdr():
    pair = CONS(TWO)(THREE)
    assert to_int(CAR(pair)) == 2
    assert to_int(CDR(pair)) == 3

def test_pred():
    assert to_int(PRED(FOUR)) == 3
    assert to_int(PRED(THREE)) == 2
    assert to_int(PRED(TWO)) == 1
    assert to_int(PRED(ONE)) == 0
    assert to_int(PRED(ZERO)) == 0

def test_add():
    assert to_int(ADD(ONE)(TWO)) == 3
    assert to_int(ADD(ZERO)(ZERO)) == 0
    assert to_int(ADD(ZERO)(THREE)) == 3

def test_sub():
    assert to_int(SUB(TWO)(ONE)) == 1
    assert to_int(SUB(ONE)(ONE)) == 0
    assert to_int(SUB(ZERO)(ZERO)) == 0
    # no negative numbers
    #assert to_int(SUB((ONE)(TWO))) == 0

def test_mul():
    assert to_int(MUL(ONE)(TWO)) == 2
    assert to_int(MUL(TWO)(TWO)) == 4
    assert to_int(MUL(ZERO)(ONE)) == 0
    assert to_int(MUL(TWO)(ZERO)) == 0

def test_iszero():
    assert ISZERO(ZERO) is TRUE
    assert ISZERO(ONE) is FALSE
    assert ISZERO(TWO) is FALSE

def test_gte():
    assert GTE(ONE)(ONE) is TRUE
    assert GTE(TWO)(ONE) is TRUE
    assert GTE(ONE)(TWO) is FALSE

def test_lte():
    assert LTE(ONE)(ONE) is TRUE
    assert LTE(ONE)(TWO) is TRUE
    assert LTE(TWO)(ONE) is FALSE

def test_eq():
    assert EQ(ONE)(ONE) is TRUE
    assert EQ(ZERO)(ZERO) is TRUE
    assert EQ(ONE)(ZERO) is FALSE
    assert EQ(ZERO)(ONE) is FALSE

def test_gt():
    assert GT(TWO)(ONE) is TRUE
    assert GT(ONE)(ONE) is FALSE
    assert GT(ONE)(TWO) is FALSE

def test_lt():
    assert LT(ONE)(TWO) is TRUE
    assert LT(ONE)(ONE) is FALSE
    assert LT(TWO)(ONE) is FALSE

def test_fact():
    assert to_int(FACT(THREE)) == 6

def test_fib():
    assert to_int(FIB(ONE)) == 1
    assert to_int(FIB(TWO)) == 1
    assert to_int(FIB(THREE)) == 2
    assert to_int(FIB(FOUR)) == 3
    # same as previous lines, but not predefined number, so generating them from int
    assert to_int(FIB(from_int(5))) == 5
    assert to_int(FIB(from_int(6))) == 8
    assert to_int(FIB(from_int(7))) == 13
    assert to_int(FIB(from_int(8))) == 21
    assert to_int(FIB(from_int(9))) == 34
    assert to_int(FIB(from_int(10))) == 55
