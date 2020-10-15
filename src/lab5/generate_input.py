import sys
import random

import numpy as np
from tqdm import tqdm

from ..utils.config import Config


_MAX_INT = 1e3
_DEVIATION = 1


class Matrix(object):
    pass


def set_seed(SEED):
    random.seed(SEED)


def reset_operation(fb, matrix):
    sentence = "1\n"
    fb.write(sentence)

    row_num = random.randint(
        matrix.row-10 if matrix.row - 10 > 0 else matrix.row, matrix.row+10)
    col_num = random.randint(
        matrix.col-10 if matrix.col - 10 > 0 else matrix.col, matrix.col+10)
    sentence = "%d %d\n" % (row_num, col_num)
    fb.write(sentence)

    matrix.row = row_num
    matrix.col = col_num
    mat = np.random.normal(0, _DEVIATION, size=(
        matrix.row, matrix.col)).astype(int).astype(str).tolist()
    mat = [" ".join(row) for row in mat]
    sentence = "\n".join(mat)
    fb.write(f"{sentence}\n")


def initialize_matrix(fb, matrix):
    mat = np.random.normal(0, _DEVIATION, size=(
        matrix.row, matrix.col)).astype(int).astype(str).tolist()
    mat = [" ".join(row) for row in mat]
    sentence = "\n".join(mat)
    fb.write(f"{sentence}\n")


def add_operation(fb, matrix, ratio=0.95):
    """
    Args:
        fb: file handler of the input test case
        ratio: probability generating valid data
        sparse_coef: coefficient to control the sparsity of the matrix Q
    """

    sentence = "3\n"
    fb.write(sentence)

    if random.random() < ratio:
        row_Q = matrix.row
        col_Q = matrix.col
    else:
        row_Q = random.randint(
            matrix.row - 10 if matrix.row - 10 > 0 else matrix.row, matrix.row + 10)
        col_Q = random.randint(
            matrix.col - 10 > 0 if matrix.col - 10 > 0 else matrix.col, matrix.col + 10)
    
    matrix.row = row_Q
    matrix.col = col_Q

    sentence = "%d %d\n" % (row_Q, col_Q)
    fb.write(sentence)

    num_non_zeros = random.randint(
        (row_Q * col_Q) // 1000 + 1, (row_Q * col_Q) // 1000 + 10)

    sentence = "%d\n" % num_non_zeros
    fb.write(sentence)

    items = []
    item_indices = []
    while num_non_zeros > 0:
        row = random.randint(1, row_Q)
        col = random.randint(1, col_Q)
        if (row, col) not in item_indices:
            item_indices.append((row, col))
            val = random.randint(1, 10)
            items.append((row, col, val))
            num_non_zeros -= 1
        
    items = sorted(items, key=lambda x: (x[0], x[1]))
    items = [" ".join(str(v) for v in r) for r in items]
    sentence = "\n".join(items)
    fb.write(f"{sentence}\n")

    # sentence = ""
    # mat = np.random.normal(0, _DEVIATION, size=(
    #     row_Q, col_Q)).astype(int).astype(str).tolist()
    # mat = [" ".join(row) for row in mat]
    # sentence = "\n".join(mat)
    



def transpose_operation(fb, matrix):
    temp = matrix.row
    matrix.row = matrix.col
    matrix.col = temp

    sentence = "5\n"
    fb.write(sentence)


def multiply_operation(fb, matrix, ratio=0.95):
    sentence = "2\n"
    fb.write(sentence)

    if random.random() < ratio:
        row_Q = matrix.row
        col_Q = matrix.col
    else:
        row_Q = random.randint(
            matrix.row - 10 if matrix.row - 10 > 0 else matrix.row, matrix.row + 10)
        col_Q = random.randint(
            matrix.col - 10 if matrix.col - 10 > 0 else matrix.col, matrix.col + 10)

    matrix.row = row_Q
    matrix.col = col_Q


    sentence = "%d %d\n" % (row_Q, col_Q)
    fb.write(sentence)

    num_non_zeros = random.randint(
        (row_Q * col_Q) // 1000 + 1, (row_Q * col_Q) // 1000 + 10)

    sentence = "%d\n" % num_non_zeros
    fb.write(sentence)

    items = []
    item_indices = []
    while num_non_zeros > 0:
        row = random.randint(1, row_Q)
        col = random.randint(1, col_Q)
        if (row, col) not in item_indices:
            item_indices.append((row, col))
            val = random.randint(1, 10)
            items.append((row, col, val))
            num_non_zeros -= 1
    
    items = sorted(items, key=lambda x: (x[0], x[1]))
    items = [" ".join(str(v) for v in r) for r in items]
    sentence = "\n".join(items)
    fb.write(f"{sentence}\n")

    # sentence = ""
    # mat = np.random.normal(0, _DEVIATION, size=(
    #     row_Q, col_Q)).astype(int).astype(str).tolist()
    # mat = [" ".join(row) for row in mat]
    # sentence = "\n".join(mat)

    # sentence = "%d %d\n" % (row_Q, col_Q)
    # fb.write(sentence)

    # sentence = ""
    # mat = np.random.normal(0, _DEVIATION, size=(
    #     row_Q, col_Q)).astype(int).astype(str).tolist()
    # mat = [" ".join(row) for row in mat]
    # sentence = "\n".join(mat)

    # fb.write(sentence)


def output_operation(fb, matrix):
    sentence = "4\n"
    fb.write(sentence)


def generate_input(path, settings):
    fb = open(path, 'w')

    num_row = settings['n']
    num_col = settings['m']
    num_op = settings['w']

    fb.write("%d\n" % num_op)

    matrix = Matrix()
    matrix.row = num_row
    matrix.col = num_col

    valid_operations = settings['op']
    for i in range(num_op):
        chosen_operation = random.choice(valid_operations)
        if i == 0:
            chosen_operation = "reset_operation"
        if chosen_operation == "reset_operation":
            matrix.row = num_row
            matrix.col = num_col
        globals()[chosen_operation](fb, matrix)

    fb.close()


def main():
    cfg = Config.fromfile('conf/lab5.py')
    set_seed(cfg.SEED)
    
    for case in tqdm(range(cfg.NUM_CASES)):
        input_filepath = 'data/exp5/input/input%d.txt' % case
        generate_input(input_filepath, cfg.PROBLEM_SETTINGS[case])



if __name__ == '__main__':
    print(sys.argv)
    main()
