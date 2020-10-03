import os
import sys
import random
from ...utils.config import Config

_INT_RANGE = 10000

def generate_input(cfg: Config, case: int):
    fb = open("data/exp4/prob2/input/input%d.txt" % case, "w")
    settings = cfg.PROBLEM_SETTINGS[case]

    N, M = settings.N, settings.M
    sentence = "%d %d\n" % (N, M)
    fb.write(sentence)

    sentence = "\n"
    for _ in range(N):
        sentence = "%d %s" % (
            random.randint(-_INT_RANGE, _INT_RANGE), sentence)
    fb.write(sentence)

    sentence = "\n"
    for _ in range(M):
        sentence = "%d %s" % (
            random.randint(-_INT_RANGE, _INT_RANGE), sentence)
    fb.write(sentence)

    fb.close()

def main():
    print(sys.argv)
    cfg_path = 'conf/lab4_2.py'
    cfg = Config.fromfile(cfg_path)
    random.seed(cfg.SEED)

    for case in range(cfg._MAX_CASE):
        generate_input(cfg, case)

    


if __name__ == '__main__':
    main()
