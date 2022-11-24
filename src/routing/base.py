from itertools import islice

from util.utils import *
import networkx as nx
from matplotlib import pyplot as plt


def gen_graph():
    '''
    读取topo文件，生成对应的图结构
    :return: G 图结构
    '''
    edge_list = plain_read("../../conf/topo")
    # print(edge_list)

    G = nx.Graph()
    for e in edge_list:
        e = e.split()
        G.add_edge(e[0], e[1], delay=1)
    # print(G.nodes)
    # print(G.edges)
    # plt.figure(figsize=(8,8))
    # nx.draw_networkx(G)
    # plt.show()
    return G


def get_all_shortest_path(G):
    asp = nx.all_pairs_dijkstra_path(G)

    asp_dict = dict()
    for p in asp:
        asp_dict[p[0]] = p[1]
    return asp_dict

def get_all_shortest_k_paths(G):
    '''
    获得所有节点对的最短路由，可能有多个，在同一个组为2个，在不同组为4个，因此只需要获得
    :param G:
    :return:
    '''

    # sp = nx.shortest_simple_paths(G, "access0", "access7", "delay")
    asp_dict = dict()
    for i in range(8):
        tmp = dict()
        start = "access" + str(i)

        for j in range(8):
            if i!=j:
                end = "access" + str(j)
                sps = []
                if i//2 == j//2:
                    sps = list(islice((nx.shortest_simple_paths(G, start, end, "delay")), 2))
                else:
                    sps = list(islice((nx.shortest_simple_paths(G, start, end, "delay")), 4))
                tmp[end] = sps

        asp_dict[start] = tmp
    # print(asp_dict)
    # for d in asp_dict.items():
    #     print(d)
if __name__ == '__main__':
    G = gen_graph()
    get_all_shortest_k_paths(G)
