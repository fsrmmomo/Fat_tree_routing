from routing.base import *


def ecmp_path_routing():
    G = gen_graph()
    asp_dict = get_all_shortest_k_paths(G)

    # print(asp_dict)
    for d in asp_dict.items():
        print(d)

    subnet_mapping = dict()
    for i in range(8):
        key = "access" + str(i)
        value = str(i) + ".0.0.0/8"
        subnet_mapping[key] = value


    save_res = []
    for i in range(8):
        for j in range(8):
            if i!=j:
                start = "access" + str(i)
                end = "access" + str(j)
                path = asp_dict[start][end]
                print(path)

                tmp = ""
                for node in path:
                    tmp += node + " "
                tmp += subnet_mapping[path[0]] + " "
                tmp += subnet_mapping[path[-1]] + " "
                save_res.append(tmp)

    plain_write("../../data/sp_result",save_res)

if __name__ == '__main__':
    ecmp_path_routing()
