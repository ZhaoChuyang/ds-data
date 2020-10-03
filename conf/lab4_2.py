from random import randint

SEED = 123
_MAX_CASE = 10

PROBLEM_SETTINGS = [
    dict(
        N=randint(10, 100),
        M=0,
    ),
    dict(
        N=randint(100, 500),
        M=0,
    ),
    dict(
        N=randint(500, 800),
        M=0,
    ),
    dict(
        N=randint(800, 1000),
        M=0,
    ),
    dict(
        N=randint(1000, 2000),
        M=0,
    ),
    dict(
        N=randint(10, 100),
        M=randint(10, 100),
    ),
    dict(
        N=randint(100, 500),
        M=randint(100, 500),
    ),
    dict(
        N=randint(500, 800),
        M=randint(500, 800),
    ),
    dict(
        N=randint(800, 1000),
        M=randint(800, 1000),
    ),
    dict(
        N=randint(1000, 2000),
        M=randint(1000, 2000),
    ),
]
