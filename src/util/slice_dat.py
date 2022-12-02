def read_ecmp_routing_and_get_mapping():
    """
    读取路由方案，并且根据路由方案切割流
    规则是只记录
    access i 到 access j 的流（j>i)
    短路由视为两个流
    :return:
    """

    routing = []
    with open("../../result/ecmp_result", 'r') as f:
        for line in f.readlines():
            tmp = line.split()
            if len(tmp) == 5:
                tmp = tmp[:3]
                i = int(tmp[0][-1])
                j = int(tmp[-1][-1])
                if j < i:
                    continue
                routing.append(tmp[:])
                routing.append(tmp[:])
            else:
                tmp = tmp[:5]
                i = int(tmp[0][-1])
                j = int(tmp[-1][-1])
                if j < i:
                    continue
                routing.append(tmp[:])

    switch_subflow_match_dict = dict()
    for i, p in enumerate(routing):
        for sw in p:
            if sw in switch_subflow_match_dict.keys():
                switch_subflow_match_dict[sw].append(i)
            else:
                switch_subflow_match_dict[sw] = [i]
    return switch_subflow_match_dict


def gen_sub_dat():
    """
    根据节点生成对应的dat文件
    :return:
    """

    node_list = []
    for i in range(1, 9):
        node_list.append("access" + str(i))
        node_list.append("merge" + str(i))
    for i in range(1, 5):
        node_list.append("core" + str(i))

    for i in range(10)


# print(s)

# for p in routing:
#     tmp =


if __name__ == '__main__':
    read_ecmp_routing_and_get_mapping()
