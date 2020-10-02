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
    _n = [10, 100, 1000, 3000, 5000, 8000, 10000, 50000, 100000, 500000]
    _m = [20, 200, 2000, 6000, 10000, 16000, 20000, 100000, 200000, 1000000]
    n_op = 100
    return _n[case], _m[case]


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

    n, m = get_conf(case)
    graph = defaultdict(set)

    nodes = [i for i in range(1, n+1)]
    edges = set([])

    fb.write("%d %d\n" % (n, m))

    for i in range(m):
        if random() > 0.3 or len(edges) == 0:
            u = choice(nodes)
            v = choice(nodes)
            while v in graph[u] or u == v:
                u = choice(nodes)
                v = choice(nodes)
            fb.write("0 %d %d\n" % (u, v))
            add_edge(graph, u, v)
            edges.add((u,v))

        else:
            u, v = edges.pop()
            fb.write("1 %d %d\n" % (u, v))

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
