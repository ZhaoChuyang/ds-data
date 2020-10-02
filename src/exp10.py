import sys
import os
import argparse
from random import random, choice
import pathlib
import string


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cases', type=int)
    parser.add_argument('--prob', type=int)
    parser.add_argument('--indir')
    parser.add_argument('--outdir')
    parser.add_argument('--genout', type=bool, default=False)
    return parser.parse_args()


def store_input(prob, indir, cases):

    if prob == 1:
        if not os.path.isdir(indir):
            pathlib.Path(indir).mkdir(parents=True, exist_ok=True)

        _n = [10, 100, 100, 500, 1000, 1000, 3000, 3000, 3000, 5000]
        _m = [10, 50, 50, 50, 50, 100, 100, 500, 1000, 1000]

        for case in range(cases):
            path = '%s/input%d.txt' % (indir, case)

            fb = open(path, "w")

            fb.write("%d\n" % _n[case])

            nums = []
            for i in range(_n[case]):
                nums.append(str(int(random() * 1000000) - 500000))

            s = ' '.join(nums)
            fb.write("%s\n" % s)

            fb.write("%d\n" % _m[case])
            cnt = 0
            heap = []

            while cnt < _m[case]-1:
                if random() > 0.5:
                    num = int(random() * 1000000) - 500000
                    heap.append(num)
                    fb.write("1 %d\n" % num)
                    cnt += 1
                elif len(heap) > 0:
                    num = min(heap)
                    heap.remove(num)
                    fb.write("2\n")
                    cnt += 1

            fb.write("3 %d\n" % _n[case])

            temp = []
            for i in range(_n[case]):
                temp.append(str(int(random() * 1000000) - 500000))
            s = ' '.join(temp)

            fb.write("%s\n" % s)
            fb.close()

    if prob == 2:
        if not os.path.isdir(indir):
            pathlib.Path(indir).mkdir(parents=True, exist_ok=True)

        letters = string.ascii_lowercase

        for case in range(cases):

            _slen = [10, 100, 1000, 5000, 10000, 50000, 100000, 500000, 800000, 1000000]

            path = "%s/input%d.txt" % (indir, case)

            fb = open(path, 'w')

            slen = _slen[case]
            s = ''
            for i in range(slen):
                c = choice(letters)
                s = '%s%s' % (s, c)
            fb.write("%s\n" % s)

            fb.close()


def main():
    args = get_args()
    indir = args.indir
    cases = args.cases
    prob = args.prob

    store_input(prob, indir, cases)


if __name__ == '__main__':
    print(sys.argv)
    main()
