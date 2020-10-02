import os
import sys
import random
from ..utils.config import Config

_MAX_INT = 1e5

def insert_operation(fb, chain: list):
    """insert element at specified index
    NOTE: You need to guarrantee the inserted position is not greater than the length of chain.
    The format of insert operation is "1 [index] [value]", i.e. insert [value] at [index].
    """
    length = len(chain)
    insert_idx = random.randint(0, length)
    insert_val = random.randint(0, _MAX_INT)
    chain.insert(insert_idx, insert_val)

    sentence = "1 %d %d\n" % (insert_idx, insert_val)
    fb.write(sentence)


def delete_operation(fb, chain: list, exist_ratio=0.7):
    """delete element by value
    NOTE:
    1. It is possible that the element to delete does not exist. You need to set the probability 
        whether the element exists.
    2. When dupilcate element exists, only delete the first one.
    """
    # element exists
    sentence = None
    if random.random() < 0.7 and not chain:
        element = random.choice(chain)
        chain.remove(element)
        sentence = "2 %d\n" % element
    else:
        element = random.randint(_MAX_INT+1, _MAX_INT+10000)
        assert not element in chain
        sentence = "2 %d\n" % element
    fb.write(sentence)


def query_operation(fb, chain: list):
    """find if specified element is in chain
    You donnot need to modify the chain.
    """
    element = random.randint(0, _MAX_INT)
    sentence = "4 %d\n" % element
    fb.write(sentence)


def reverse_operation(fb, chain: list):
    """reverse the chain
    You don't necessarily need to reverse the chain actually.
    """
    sentence = "3\n"
    fb.write(sentence)
    chain.reverse()


def output_operation(fb, chain: list):
    """output the xor sum of all elements in the chain
    f(chain) = \sum_{i=0}^{n}i^chain[i]
    """
    sentence = "5\n"
    fb.write(sentence)


def generate_input(cfg, case):
    fb = open("%s/input%d.txt" % (cfg.INPUT_DIR, case), "w")

    settings = cfg.PROBLEM_SETTINGS[case]
    # first line
    N, Q = settings.N, settings.Q
    sentence = "%d %d\n" % (N, Q)
    fb.write(sentence)

    chain = [random.randint(0, _MAX_INT) for _ in range(N)]
    sentence = ""
    for element in chain:
        sentence = "%s%d " % (sentence, element)
    sentence = "%s\n" % sentence
    fb.write(sentence)

    valid_operations = settings.OP
    for _ in range(Q):
        op = random.choice(valid_operations)
        globals()[op](fb, chain)

    fb.close()


def main():
    print(sys.argv)
    cfg_path = 'conf/lab4_1.py'
    cfg = Config.fromfile(cfg_path)
    random.seed(cfg.SEED)

    for case in range(10):
        generate_input(cfg, case)

if __name__ == '__main__':
    main()



    
    
    
