# boolean algebra stuff
TRUE = lambda x: lambda y: x
FALSE = lambda x: lambda y: y
AND = lambda x: lambda y: x(y)(FALSE)
OR = lambda x: lambda y: x(TRUE)(y)
NOT = lambda x: x(FALSE)(TRUE)

# numbers, church representation
# number if always represented as "lambda f: lambda x: " and
# for number N function "f" is called N times
# e.g. for 2 it is f(f(x)), for zero no calls, just x is returned

# zero, base for all other numbers
ZERO = lambda f: lambda x: x

# successor, used later for generating other numbers
SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

# these are not strictly needed and we can only represent subset of them
# but they are useful for testing, so lets have at least some
ONE = SUCC(ZERO)
TWO = SUCC(ONE)
THREE = SUCC(TWO)
FOUR = SUCC(THREE)

# pair of numbers, lisp naming (cons, car, cdr)
CONS = lambda x: lambda y: lambda s: s(x)(y)
CAR = lambda x: x(TRUE)
CDR = lambda x: x(FALSE)

# we have successor, now with lists we can build predecessor
_T = lambda x: CONS(SUCC(CAR(x)))(CAR(x))
PRED = lambda x: CDR(x(_T)(CONS(ZERO)(ZERO)))

# arithmetic operations
ADD = lambda x: lambda y: x(SUCC)(y)
SUB = lambda x: lambda y: y(PRED)(x)
MUL = lambda x: lambda y: lambda f: y(x(f))

# comparison
ISZERO = lambda x: x(lambda f: FALSE)(TRUE)
GTE = lambda x: lambda y: ISZERO(x(PRED)(y))
LTE = lambda x: lambda y: ISZERO(y(PRED)(x))
EQ = lambda x: lambda y: AND(GTE(x)(y))(LTE(x)(y))
GT = lambda x: lambda y: AND(GTE(x)(y))(NOT(EQ(x)(y)))
LT = lambda x: lambda y: AND(LTE(x)(y))(NOT(EQ(x)(y)))


# support for recursion

# Y combinator
Y = lambda f: (lambda x: f(lambda z: x(x)(z)))(lambda x: f(lambda z: x(x)(z)))

# eager parameter evaluation workaround (not needed in lambda calculus)
# without this, python reports recursion limit problem (other eager-parameter-evaluation
# languages as well (probably, have not tried them))
LAZY_TRUE = lambda x: lambda y: x()
LAZY_FALSE = lambda x: lambda y: y()
LAZY_ISZERO = lambda x: x(lambda f: LAZY_FALSE)(LAZY_TRUE)
LAZY_LTE = lambda x: lambda y: LAZY_ISZERO(y(PRED)(x))

# factorial
_REC_FACT = lambda f: lambda n: LAZY_ISZERO(n)(lambda: ONE)(lambda: MUL(n)(f(PRED(n))))
FACT = Y(_REC_FACT)

# fibonacci sequence
_REC_FIB = lambda f: lambda n: LAZY_LTE(n)(TWO)(lambda: ONE)(lambda: ADD(f(PRED(n)))(f(PRED(PRED(n)))))
FIB = Y(_REC_FIB)