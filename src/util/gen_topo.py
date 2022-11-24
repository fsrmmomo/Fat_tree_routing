from util.utils import *

def gen_topo():
    edge_list = []

    for i in range(8):
        a = i - 1
        b = i
        if i % 2 == 0:
            a = i
            b = i + 1
        edge_list.append("access" + str(i) + " " + "merge" + str(a))
        edge_list.append("access" + str(i) + " " + "merge" + str(b))

    for i in range(8):
        a = 2
        b = 3
        if i % 2 == 0:
            a = 0
            b = 1
        edge_list.append("merge" + str(i) + " " + "core" + str(a))
        edge_list.append("merge" + str(i) + " " + "core" + str(b))


    for e in edge_list:
        print(e)
    plain_write("../../conf/topo",edge_list)


if __name__ == '__main__':
    gen_topo()
