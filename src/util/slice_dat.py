import struct


def read_ecmp_routing_and_get_mapping():
    """
    读取路由方案，并且根据路由方案切割流
    规则是只记录
    access i 到 access j 的流（j>i)
    短路由视为两个流
    :return:
    """

    routing = []
    with open("../../result/routing/ecmp_result", 'r') as f:
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

    switch_to_subflow_match_dict = dict()
    subflow_to_switch_match_dict = dict()
    for i, p in enumerate(routing):
        for sw in p:
            if sw in switch_to_subflow_match_dict.keys():
                switch_to_subflow_match_dict[sw].append(i)
            else:
                switch_to_subflow_match_dict[sw] = [i]

        subflow_to_switch_match_dict[i] = []
        for sw in p:
            subflow_to_switch_match_dict[i].append(sw)
    print(subflow_to_switch_match_dict)
    print(switch_to_subflow_match_dict)
    return subflow_to_switch_match_dict


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

    read_file_dir = "../../data/dat/notime/20s/"
    write_file_dir = "../../data/dat/notime/slice/"
    trace_byte_size = 15
    x = 0
    sw_bin_list = dict()
    subflow_to_switch_match_dict = read_ecmp_routing_and_get_mapping()
    for i in range(10):
        print(i)
        read_file = read_file_dir + str(i) + ".dat"

        for sw in node_list:
            sw_bin_list[sw] = []

        with open(read_file, 'rb') as rf:
            bin_trace = rf.read(trace_byte_size)

            while bin_trace:
                # hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
                # src_ip =int.from_bytes(bin_trace[0:4],'big')
                hex_trace = struct.unpack("HBBBBHBBBBHB", bin_trace)
                src_ip = int.from_bytes(bin_trace[2:6], 'big')
                # print(src_ip)

                index = src_ip % len(subflow_to_switch_match_dict)
                for sw in subflow_to_switch_match_dict[index]:
                    sw_bin_list[sw].append(bin_trace)
                # print(hex_trace)
                # print(hex_trace[-2])
                bin_trace = rf.read(trace_byte_size)
                x += 1
                # if x > 100:
                #     break

        # 存储bintrace
        for sw in node_list:
            write_file = write_file_dir +str(i)+"-" +sw+".dat"
            with open(write_file,"wb") as wf:
                for bin in sw_bin_list[sw]:
                    wf.write(bin)

def gen_sub_dat_with_flag():
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

    # read_file_dir = "../../data/dat/flag_dat/20s/"
    # write_file_dir = "../../data/dat/flag_dat/slice/"
    read_file_dir = "../../data/dat/nodelay/20s1/"
    write_file_dir = "../../data/dat/nodelay/slice1/"
    trace_byte_size = 16
    x = 0
    sw_bin_list = dict()
    subflow_to_switch_match_dict = read_ecmp_routing_and_get_mapping()
    for i in range(10):
        print(i)
        read_file = read_file_dir + str(i) + ".dat"

        for sw in node_list:
            sw_bin_list[sw] = []

        with open(read_file, 'rb') as rf:
            bin_trace = rf.read(trace_byte_size)

            while bin_trace:
                hex_trace = struct.unpack("HBBBBHBBBBHBB", bin_trace)
                src_ip = int.from_bytes(bin_trace[2:6], 'big')

                index = src_ip % len(subflow_to_switch_match_dict)
                for sw in subflow_to_switch_match_dict[index]:
                    sw_bin_list[sw].append(bin_trace)
                # print(hex_trace)
                # print(hex_trace[-1])
                bin_trace = rf.read(trace_byte_size)
                x += 1
                # if x > 100:
                #     break

        # 存储bintrace
        for sw in node_list:
            write_file = write_file_dir +str(i)+"-" +sw+".dat"
            with open(write_file,"wb") as wf:
                for bin in sw_bin_list[sw]:
                    wf.write(bin)
# print(s)

# for p in routing:
#     tmp =


if __name__ == '__main__':
    # read_ecmp_routing_and_get_mapping()
    # gen_sub_dat()
    gen_sub_dat_with_flag()
