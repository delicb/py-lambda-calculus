# Example of lambda calculus in Python

Basic idea is to only use functions that receive single parameter and
create boolean logic, numbering system and some utilities to show
capabilities.

Main reason for writing this was [Lambda Calculus from the Ground Up][1] from 
PyCon 2019 by David Beazley. Additional resource used is 
[A Tutorial Introduction to Lambda Calculus][2] by Raúl Rojas.


Main code is in `lambda_calculus.py`. There are tests in `test_lambda_calculus.py`
written using `pytest`.

Two functions are implemented to verify the rest of the system and using
[Y-combinator][3] implementation: fibonacci sequence and factorial. 


[1]: https://www.youtube.com/watch?v=pkCLMl0e_0k
[2]: https://personal.utdallas.edu/~gupta/courses/apl/lambda.pdf
[3]: https://en.wikipedia.org/wiki/Fixed-point_combinator#Y_combinator