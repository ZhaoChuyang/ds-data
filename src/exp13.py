import sys
import os
import argparse
from collections import defaultdict
from random import random, choice
import pathlib


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--cases', type=int, default=10)
    parser.add_argument('--indir')
    parser.add_argument('--outdir')
    return parser.parse_args()


def get_conf(case):
    _n = [10, 100, 300, 300, 500, 500, 500, 1000, 1000, 1000]
    _m = [20, 200, 10000, 20000, 20000, 80000, 100000, 100000, 200000, 200000]
    n_op = [1, 2, 10, 20, 20, 20, 20, 20, 20, 20]
    return _n[case], _m[case], n_op[case]


def add_edge(graph, u, v):
    graph[u].add(v)
    graph[v].add(u)


def remove_edge(graph, u, v):
    graph[u].remove(v)
    graph[v].remove(u)


def dfs(graph, vis, n, step=0):
    vis[n] = 1
    for neighbor in graph[n]:
        if vis[neighbor] != 1:
            try:
                dfs(graph, vis, neighbor, step+1)
            except RecursionError:
                print(step)


def get_graph(case, indir):

    if not os.path.isdir(indir):
        pathlib.Path(indir).mkdir(parents=True, exist_ok=True)

    inpath = "%s/input%d.txt" % (indir, case)
    fb = open(inpath, "w")

    n, m, op = get_conf(case)
    graph = defaultdict(set)

    nodes = [i for i in range(1, n+1)]
    edges = set([])

    fb.write("%d %d %d\n" % (n, m, op))

    for i in range(m):
        u = choice(nodes)
        v = choice(nodes)
        w = int(random()*100)-50
        while v in graph[u] or u == v:
            u = choice(nodes)
            v = choice(nodes)
        fb.write("%d %d %d\n" % (u, v, w))
        add_edge(graph, u, v)
        edges.add((u,v))

    for i in range(op):
        v = choice([i for i in range(n)])
        fb.write("%d\n" % v)

    # s = choice(nodes)
    # vis = [0] * (n+10)
    # dfs(graph, vis, s)
    # ans = []
    #
    # for index, it in enumerate(vis):
    #     if it != 0:
    #         ans.append(index)
    # t = choice(ans)
    #
    # print("%d %d" % (s, t))

    fb.close()
    return graph


def main():
    args = get_args()
    indir = args.indir
    cases = args.cases
    for i in range(cases):
        get_graph(i, indir)


if __name__ == '__main__':
    print(sys.argv)
    main()
