def TRUE(x):
    return lambda y: x
def FALSE(x):
    return lambda y: y

AND = lambda x: lambda y: x(y)(FALSE)
OR = lambda x: lambda y: x(TRUE)(y)
NOT = lambda x: x(FALSE)(TRUE)

ZERO = lambda f: lambda x: x
ONE = lambda f: lambda x: f(x)
TWO = lambda f: lambda x: f(f(x))
THREE = lambda f: lambda x: f(f(f(x)))
FOUR = lambda f: lambda x: f(f(f(f(x))))

SUCC = lambda n: lambda f: lambda x: f(n(f)(x))

CONS = lambda x: lambda y: lambda s: s(x)(y)
CAR = lambda x: x(TRUE)
CDR = lambda x: x(FALSE)

ISZERO = lambda x: x(lambda f: FALSE)(TRUE)

T = lambda x: CONS(SUCC(CAR(x)))(CAR(x))
PRED = lambda x: CDR(x(T)(CONS(ZERO)(ZERO)))

ADD = lambda x: lambda y: x(SUCC)(y)
SUB = lambda x: lambda y: y(PRED)(x)
MUL = lambda x: lambda y: lambda f: y(x(f))

GTE = lambda x: lambda y: ISZERO(x(PRED)(y))
LTE = lambda x: lambda y: ISZERO(y(PRED)(x))
EQ = lambda x: lambda y: AND(GTE(x)(y))(LTE(x)(y))
GT = lambda x: lambda y: AND(GTE(x)(y))(NOT(EQ(x)(y)))
LT = lambda x: lambda y: AND(LTE(x)(y))(NOT(EQ(x)(y)))


# python infinite recursion hacks
LAZY_TRUE = lambda x: lambda y: x()
LAZY_FALSE = lambda x: lambda y: y()
LAZY_ISZERO = lambda x: x(lambda f: LAZY_FALSE)(LAZY_TRUE)
FACT = lambda x: LAZY_ISZERO(x)\
                 (lambda: ONE)\
                 (lambda: MUL(x)(FACT(PRED(x))))



# Y combinator
Y = lambda f: (lambda x: f(lambda z: x(x)(z)))(lambda x: f(lambda z: x(x)(z)))
R = lambda f: lambda n: 1 if n == 0 else n*f(n-1)
R1 = lambda f: lambda n: LAZY_ISZERO(n)(lambda: ONE)(lambda: MUL(n)(f(PRED(n))))
# FACT1 = Y(R)
fact = Y(R)
FACT1 = Y(R1)

R2 = lambda f: lambda n: 1 if n <= 2 else f(n-1)+f(n-2)
fib = Y(R2)

R3 = lambda f: lambda n: LTE(n)(TWO)(lambda: ONE)(lambda: ADD(f(PRED(n))(f(SUB(n)(TWO)))))
FIB = Y(R3)


# debugging
incr = lambda x: x + 1
def show(x):
    print(x(incr)(0))

# assertions
assert ONE(incr)(0) == 1
assert EQ(ONE)(ONE) is TRUE
assert EQ(ONE)(TWO) is FALSE
assert ADD(ONE)(TWO)(incr)(0) == 3
assert SUB(THREE)(ONE)(incr)(0) == 2
assert MUL(TWO)(THREE)(incr)(0) == 6

# print(EQ(TWO)(TWO))
# print(GT(FOUR)(THREE))
# show(FACT(FOUR))
# print(fact(5))
show(FACT1(SUCC(FOUR)))
# print(fib(10))
# print(FIB(THREE)(incr)(0))
# print(LTE(TWO)(THREE)(lambda: 1)(lambda: 2))