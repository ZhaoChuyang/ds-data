import argparse
import sys
import os
import pathlib
from collections import deque


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--indir')
    parser.add_argument('--outdir')
    return parser.parse_args()


def gen_input(test_point):
    return int((test_point + 1) * 1e5)


def gen_output(n):
    queue = deque([i for i in range(1, n+1)])

    while len(queue) != 1:
        #print(len(queue))
        queue.popleft()
        top = queue[0]
        queue.append(top)
        queue.popleft()

    return queue[0]


def main():

    args = get_args()

    if not os.path.isdir(args.outdir):
        pathlib.Path(args.outdir).mkdir(exist_ok=True, parents=True)

    if not os.path.isdir(args.indir):
        pathlib.Path(args.indir).mkdir(exist_ok=True, parents=True)

    for case in range(10):
        n = gen_input(case)
        ans = gen_output(n)

        inpath = '%s/input%d.txt' % (args.indir, case)
        outpath = '%s/output%d.txt' % (args.outdir, case)

        with open(inpath, 'w') as fb:
            fb.write('%d\n' % n)

        with open(outpath, 'w') as fb:
            fb.write('%d\n' % ans)


if __name__ == '__main__':
    print(sys.argv)
    main()
