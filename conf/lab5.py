"""problem configuration for lab5
Total 10 test cases

"""
SEED = 10
NUM_CASES = 5

ADD = 'add_operation'
RESET = 'reset_operation'
MULTIPLY = 'multiply_operation'
TRANSPOSE = 'transpose_operation'
OUTPUT = 'output_operation'

DENSE_ADD = 'dense_add_operation'
DENSE_MULTIPLY = 'dense_multiply_operation'
DENSE_RESET = 'dense_reset_operation'


PROBLEM_SETTINGS = [
    dict(
        dense=False,
        w=20,
        n=5,
        m=5,
        op=[ADD, TRANSPOSE, MULTIPLY, OUTPUT]
    ),
    dict(
        dense=False,
        w=40,
        n=10,
        m=10,
        op=[ADD] * 5 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=40,
        n=100,
        m=100,
        op=[ADD] * 15 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=80,
        n=200,
        m=200,
        op=[ADD] * 20 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=100,
        n=500,
        m=500,
        op=[ADD] * 50 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=150,
        n=500,
        m=500,
        op=[ADD] * 50 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=40,
        n=10,
        m=10,
        op=[ADD] + [RESET] + [TRANSPOSE] * 5 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=40,
        n=100,
        m=100,
        op=[ADD] + [RESET] + [TRANSPOSE] * 20 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=80,
        n=200,
        m=200,
        op=[ADD] + [RESET] + [TRANSPOSE] * 20 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=100,
        n=500,
        m=500,
        op=[ADD] + [RESET] + [TRANSPOSE] * 50 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=100,
        n=500,
        m=500,
        op=[ADD] + [RESET] + [TRANSPOSE] * 50 + [OUTPUT] * 2
    ),
    dict(
        dense=False,
        w=40,
        n=10,
        m=10,
        op=[ADD]  + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 5
    ),
    dict(
        dense=False,
        w=50,
        n=100,
        m=100,
        op=[ADD]  + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 20
    ),
    dict(
        dense=False,
        w=100,
        n=100,
        m=100,
        op=[ADD] + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 50
    ),
    dict(
        dense=False,
        w=100,
        n=500,
        m=500,
        op=[ADD] + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 50
    ),
    dict(
        dense=False,
        w=200,
        n=500,
        m=500,
        op=[ADD] + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 50
    ),
    dict(
        dense=True,
        w=20,
        n=5,
        m=5,
        op=[DENSE_ADD] * 1 + [DENSE_RESET] * 1 + [OUTPUT] *
        5 + [TRANSPOSE] * 1 + [DENSE_MULTIPLY] * 20
    ),
    dict(
        dense=True,
        w=20,
        n=20,
        m=20,
        op=[DENSE_ADD] * 1 + [DENSE_RESET] * 1 + [OUTPUT] *
        5 + [TRANSPOSE] * 1 + [DENSE_MULTIPLY] * 50
    ),
    dict(
        dense=True,
        w=40,
        n=40,
        m=40,
        op=[DENSE_ADD] * 1 + [DENSE_RESET] * 1 + [OUTPUT] *
        5 + [TRANSPOSE] * 1 + [DENSE_MULTIPLY] * 50
    ),
    dict(
        dense=True,
        w=80,
        n=80,
        m=80,
        op=[DENSE_ADD] * 1 + [DENSE_RESET] * 8 + [OUTPUT] *
        5 + [TRANSPOSE] * 1 + [DENSE_MULTIPLY] * 50
    ),
    dict(
        dense=True,
        w=100,
        n=100,
        m=100,
        op=[DENSE_ADD] * 1 + [DENSE_RESET] * 8 + [OUTPUT] *
        5 + [TRANSPOSE] * 1 + [DENSE_MULTIPLY] * 50
    ),
]
