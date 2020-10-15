import os


def main():
    for i in range(15):
        path_in = "/Users/chuyang/PythonProjects/data-structure/data/exp5/input/input" + str(i) + ".txt"
        path_out = "/Users/chuyang/PythonProjects/data-structure/data/exp5/output/output" + str(i) + ".txt"
        os.system("g++ -O2 -Wall -std=c++11 -o /Users/chuyang/Desktop/foo /Users/chuyang/Desktop/t3.cpp")
        os.system(f"/Users/chuyang/Desktop/foo {path_in} {path_out}")


if __name__ == '__main__':
    main()
