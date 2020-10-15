"""problem configuration for lab5
Total 10 test cases

"""
SEED = 10
NUM_CASES = 15

ADD = 'add_operation'
RESET = 'reset_operation'
MULTIPLY = 'multiply_operation'
TRANSPOSE = 'transpose_operation'
OUTPUT = 'output_operation'


PROBLEM_SETTINGS = [
    # dict(
    #     w=50,
    #     n=30,
    #     m=30,
    #     op=[ADD, ADD, ADD, ADD, ADD, ADD, ADD, ADD, ADD,
    #         ADD, ADD, ADD, ADD, OUTPUT, OUTPUT, RESET]
    # ),
    # dict(
    #     w=100,
    #     n=500,
    #     m=500,
    #     op=[ADD, ADD, ADD, ADD, ADD, ADD, ADD, ADD, ADD,
    #         ADD, ADD, ADD, ADD, OUTPUT, OUTPUT, RESET]
    # ),
    dict(
        w=40,
        n=10,
        m=10,
        op=[ADD] * 5 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        w=40,
        n=100,
        m=100,
        op=[ADD] * 15 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        w=80,
        n=200,
        m=200,
        op=[ADD] * 20 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        w=100,
        n=500,
        m=500,
        op=[ADD] * 50 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        w=150,
        n=500,
        m=500,
        op=[ADD] * 50 + [RESET] * 2 + [OUTPUT] * 2
    ),
    dict(
        w=40,
        n=10,
        m=10,
        op=[ADD] + [RESET] + [TRANSPOSE] * 5 + [OUTPUT] * 2
    ),
    dict(
        w=40,
        n=100,
        m=100,
        op=[ADD] + [RESET] + [TRANSPOSE] * 20 + [OUTPUT] * 2
    ),
    dict(
        w=80,
        n=200,
        m=200,
        op=[ADD] + [RESET] + [TRANSPOSE] * 20 + [OUTPUT] * 2
    ),
    dict(
        w=100,
        n=500,
        m=500,
        op=[ADD] + [RESET] + [TRANSPOSE] * 50 + [OUTPUT] * 2
    ),
    dict(
        w=100,
        n=500,
        m=500,
        op=[ADD] + [RESET] + [TRANSPOSE] * 50 + [OUTPUT] * 2
    ),
    dict(
        w=40,
        n=10,
        m=10,
        op=[ADD]  + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 5
    ),
    dict(
        w=50,
        n=100,
        m=100,
        op=[ADD]  + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 20
    ),
    dict(
        w=100,
        n=100,
        m=100,
        op=[ADD] + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 50
    ),
    dict(
        w=100,
        n=500,
        m=500,
        op=[ADD] + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 50
    ),
    dict(
        w=200,
        n=500,
        m=500,
        op=[ADD] + [TRANSPOSE] + [OUTPUT] + [RESET] + [MULTIPLY] * 50
    ),
]
