import sys
import argparse
import os
from random import random, choice

from .utils import calculator


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input')
    parser.add_argument('--output')
    parser.add_argument('--ratio', type=float, default=0.3)
    return parser.parse_args()


def gen_data(num, maxval, ratio):
    a = [0] * num

    for i in range(num):
        a[i] = int(random() * maxval)

    lbrackets = 0

    for i in range(1, num-1):
        if random() <= ratio:
            if random() <= 0.4 and a[i-1]!='(':
                a.insert(i, '(')
                lbrackets += 1
            else:
                if lbrackets > 0:
                    a.insert(i, ')')
                    lbrackets -= 1

    for i in range(lbrackets):
        a.append(')')

    b = []
    b.append(a[0])

    for i in range(1, len(a)):
        if a[i-1] != '(' and a[i] != ')':
            ope = choice(['+', '-', '*', '/'])
            b.append(ope)
        b.append(a[i])

    for i in range(len(b)-1):
        if b[i] == '/' and b[i+1] == 0:
            b[i] = choice(['+', '-', '*'])
        if b[i] == '(' and b[i+1] == ')':
            b.insert(i+1, int(random() * maxval))

    i = 0
    while i < len(b)-2:
        #print('i: %d, len: %d' % (i, len(b)))
        if b[i] == '(' and b[i+2] == ')':
            b.pop(i+2)
            b.pop(i)
        i += 1

    return b


def gen_expression(a):
    s = ''
    for i in range(len(a)):
        s = s + '%s' % a[i]
    return s


def gen_answer(s):
    try:
        ans = eval(s)
    except Exception as e:
        return False
    else:
        return ans


def gen_input(args):

    if not os.path.isdir(args.input):
        os.mkdir(args.input)

    for i in range(10):
        path = '%s/input%d.txt' % (args.input, i)

        with open(path, 'w') as f:
            expnum = (i + 1) * 10
            f.write('%d\n' % expnum)

            for id in range(expnum):
                num = i * 45 + 50
                s = gen_expression(gen_data(num, 10, args.ratio))

                while gen_answer(s) == False:

                    s = gen_expression(gen_data(num, 10, args.ratio))

                f.write('%s\n' % s)


def gen_output(args):

    if not os.path.isdir(args.output):
        os.mkdir(args.output)

    for i in range(10):
        input_file = '%s/input%d.txt' % (args.input, i)

        with open(input_file, 'r') as in_fb:
            for idx, line in enumerate(in_fb):
                if idx != 0:
                    ans = eval(line)
                    output_file = '%s/output%d.txt' % (args.output, i)
                    with open(output_file, 'a') as out_fb:
                        out_fb.write('%.2f\n' % ans)


def main():
    args = get_args()
    gen_input(args)
    gen_output(args)


if __name__=='__main__':
    print(sys.argv)
    main()
