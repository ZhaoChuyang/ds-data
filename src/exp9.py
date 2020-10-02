import argparse
import sys
import os
import random
import pathlib

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cases', type=int)
    parser.add_argument('--outdir', help='relative to the project root folder(data-structure)')
    parser.add_argument('--indir', help='relative to the project root folder(data-structure)')
    parser.add_argument('--genout', help='whether generate output data', type=bool, default=False)
    parser.add_argument('--prob', help='choose problem', type=int)
    return parser.parse_args()


def get_tree(nodes):

    ratio = 0.2

    tree = [[-1, -1] for i in range(nodes+1)]  # index represents a tree's height, the root is always node 1

    height = 1
    node = 1

    can_left = set([1])
    can_right = set([1])

    for node in range(2, nodes+1):
        if len(can_right) == 0 or (len(can_left) > 0 and random.random() > 0.5):
            parent = random.choice(tuple(can_left))
            can_left.remove(parent)
            tree[parent][0] = node
            can_left.add(node)
            can_right.add(node)
        elif len(can_right) > 0:
            parent = random.choice(tuple(can_right))
            can_right.remove(parent)
            tree[parent][1] = node
            can_left.add(node)
            can_right.add(node)

    return tree


def get_pre_mid(tree):

    pre_list = []
    mid_list = []

    def get_pre(node):
        pre_list.append(node)
        if tree[node][0] != -1:
            get_pre(tree[node][0])
        if tree[node][1] != -1:
            get_pre(tree[node][1])

    def get_mid(node):
        if tree[node][0] != -1:
            get_mid(tree[node][0])
        mid_list.append(node)
        if tree[node][1] != -1:
            get_mid(tree[node][1])

    get_pre(1)
    get_mid(1)
    return pre_list, mid_list


def main():

    data_range = [10, 100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 10000]

    parser = get_args()
    cases = parser.cases
    indir = parser.indir
    prob = parser.prob

    if prob == 1:
        if not os.path.isdir(indir):
            pathlib.Path(indir).mkdir(parents=True, exist_ok=True)

        for case in range(cases):

            inpath = '%s/input%d.txt' % (indir, case)
            tree = get_tree(data_range[case])
            with open(inpath, 'w') as fp:
                fp.write(f'{data_range[case]}\n')
                for i in range(data_range[case]):
                    fp.write(f'{tree[i+1][0]} {tree[i+1][1]}\n')

    if prob == 2:
        if not os.path.isdir(indir):
            pathlib.Path(indir).mkdir(parents=True, exist_ok=True)

        for case in range(cases):

            inpath = '%s/input%d.txt' % (indir, case)
            tree = get_tree(data_range[case])
            prelist, midlist = get_pre_mid(tree)

            with open(inpath, 'w') as fp:
                fp.write(f'{data_range[case]}\n')
                for i in prelist:
                    fp.write('%d ' % i)
                fp.write('\n')
                for i in midlist:
                    fp.write('%d ' % i)


if __name__ == '__main__':
    print(sys.argv)
    main()
