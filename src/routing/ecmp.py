from routing.base import *


def ecmp_path_routing():
    '''
    使用ecmp规则计算每个流的大小，但是这里只是简单实现，通过观察发现实际上是每个子流的均分
    :return:
    '''
    G = gen_graph()
    asp_dict = get_all_shortest_k_paths(G)

    # print(asp_dict)
    for d in asp_dict.items():
        print(d)

    subnet_mapping = dict()
    for i in range(1,9):
        key = "access" + str(i)
        value = str(i) + ".0.0.0/8"
        subnet_mapping[key] = value

    save_res = []
    for i in range(1,9):
        for j in range(1,9):
            if i!=j:
                start = "access" + str(i)
                end = "access" + str(j)
                paths = asp_dict[start][end]
                n = len(paths)
                assert (n==2 or n==4)
                if n == 2:
                    for k,path in enumerate(paths):
                        tmp = ""
                        for node in path:
                            tmp += node + " "
                        tmp += str(i) + "." + str(k*128) + ".0.0/9"+" "
                        tmp += subnet_mapping[path[-1]] + " "
                        save_res.append(tmp)
                elif n==4:
                    for k,path in enumerate(paths):
                        tmp = ""
                        for node in path:
                            tmp += node + " "
                        tmp += str(i) + "." + str(k*64) + ".0.0/10"+" "
                        tmp += subnet_mapping[path[-1]]
                        save_res.append(tmp)
    plain_write("../../result/routing/ecmp_result", save_res)


if __name__ == '__main__':
    ecmp_path_routing()
