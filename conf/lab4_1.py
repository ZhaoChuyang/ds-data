"""
Total 10 test cases.

N : The number of elements when initialize chain.
Q : The number of operations on chain.
OP : The chain operations of one test case.
"""

INSERT = "insert_operation"
DELETE = "delete_operation"
REVERSE = "reverse_operation"
QUERY = "query_operation"
OUTPUT = "output_operation"

SEED = 123
MAX_INT = 1e5

INPUT_DIR = 'data/exp4/prob1/input'

PROBLEM_SETTINGS = [
    dict(
        N=10,
        Q=10,
        OP=[INSERT, QUERY, OUTPUT],
    ),
    dict(
        N=100,
        Q=100,
        OP=[INSERT, QUERY, OUTPUT],
    ),
    dict(
        N=500,
        Q=1000,
        OP=[INSERT, QUERY, OUTPUT],
    ),
    dict(
        N=1000,
        Q=500,
        OP=[INSERT, QUERY, OUTPUT],
    ),
    dict(
        N=10,
        Q=10,
        OP=[INSERT, DELETE, QUERY, OUTPUT],
    ),
    dict(
        N=100,
        Q=100,
        OP=[INSERT, DELETE, QUERY, OUTPUT],
    ),
    dict(
        N=500,
        Q=1000,
        OP=[INSERT, DELETE, QUERY, OUTPUT],
    ),
    dict(
        N=1000,
        Q=500,
        OP=[INSERT, DELETE, QUERY, OUTPUT],
    ),
    dict(
        N=500,
        Q=1000,
        OP=[INSERT, DELETE, QUERY, REVERSE, OUTPUT],
    ),
    dict(
        N=1000,
        Q=500,
        OP=[INSERT, DELETE, QUERY, REVERSE, OUTPUT],
    ),
]
