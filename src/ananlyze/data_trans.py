import os
import pickle as pkl
import struct
from scipy import stats
from numpy.ma import mean
import numpy as np
from util.utils import *

file_num = 200
dat_num = 10
data_point_num = 10  # 容量级别 2，3,4,5,6，8,9,10,11
access_node = 8
merge_node = 8
core_node = 4


def get_node_list():
    node_list = []
    for i in range(1, 9):
        node_list.append("access" + str(i))
        node_list.append("merge" + str(i))
    for i in range(1, 5):
        node_list.append("core" + str(i))
    return node_list


def error_cul():
    #
    # read_file_dir = "../../result/TM-SALFI/"
    # all_dict = pkl_read("../../result/data_dict/all.pkl")
    # for k,v in all_dict.items():
    #     print(k)
    #     print(v)
    # print(all_dict)

    read_file_dir = "../../result/TM-SALFI/"

    node_list = get_node_list()

    data_dict = dict()

    for file in os.listdir(read_file_dir):
        data_dict[file] = dict()
        s_dict = data_dict[file]
        for file_no in range(10):
            s_dict[file_no] = dict()
            for node in node_list:
                s_dict[file_no][node] = [0 for _ in range(data_point_num)]

        read_file_name = read_file_dir + file
        print(read_file_name)
        x = [0 for _ in range(data_point_num)]
        with open(read_file_name, "r") as rf:
            for i in range(file_num):
                start = rf.readline()
                string = start.split("\\")[-1]
                node = string.split("-")[-1].split(".")[0]
                dat_file_no = int(string.split("-")[0])
                for j in range(data_point_num):
                    nums = float(rf.readline())
                    s_dict[dat_file_no][node][j] = nums
        # print(s_dict[0]["access1"])
        # print(s_dict)

    for k, s_dict in data_dict.items():
        tmp_dict = dict()
        for dat_file_no in range(dat_num):
            tmp_dict[dat_file_no] = dict()
            new_dict = tmp_dict[dat_file_no]
            new_dict["access"] = [0 for _ in range(data_point_num)]
            new_dict["merge"] = [0 for _ in range(data_point_num)]
            new_dict["core"] = [0 for _ in range(data_point_num)]
            # print(type(s_dict))
            for node in node_list:
                key = node[:-1]
                if key == "core":
                    down = 4
                else:
                    down = 8
                for j in range(data_point_num):
                    new_dict[key][j] += s_dict[dat_file_no][node][j] / down
        data_dict[k] = tmp_dict
        print(data_dict[k])
    # with open("../../result/data_dict/all.pkl", "wb") as wf:
    #     pkl.dump(data_dict, wf)

    error_data = dict()
    for k, s_dict in data_dict.items():
        error_data[k] = dict()
        new_dict = error_data[k]

        node_set = ["access", "merge", "core"]
        for node in node_set:
            new_dict[node] = []
            for i in range(data_point_num):
                datas = [s_dict[j][node][i] for j in range(dat_num)]
                new_dict[node].append(cul_up_and_down(datas, 0.95))
                # for file_no in range(dat_num):
        print(error_data[k])

    save_dict = dict()
    save_dict["TM-SALFI"] = error_data
    print(save_dict)
    pkl_write("../../result/data_dict/error_1.pkl", save_dict)


def cul_up_and_down(datas, Confidence=0.95):
    x = np.array(datas)
    return stats.t.interval(Confidence, len(datas) - 1, x.mean(), x.std())


def read_raw():
    read_file_dir = "../../result/TM-SALFI/"

    node_list = get_node_list()

    data_dict = dict()
    for file in os.listdir(read_file_dir):
        data_dict[file] = dict()
        s_dict = data_dict[file]
        for node in node_list:
            s_dict[node] = [0 for _ in range(data_point_num)]
        read_file_name = read_file_dir + file
        print(read_file_name)
        x = [0 for _ in range(data_point_num)]
        with open(read_file_name, "r") as rf:
            for i in range(file_num):
                start = rf.readline()
                string = start.split("\\")[-1]
                node = string.split("-")[-1].split(".")[0]
                for j in range(data_point_num):
                    nums = float(rf.readline())
                    s_dict[node][j] += nums / dat_num
        print(s_dict["access1"])
        print(s_dict)
    with open("../../result/data_dict/all.pkl", "wb") as wf:
        pkl.dump(data_dict, wf)


def aggregation_data():
    """
    把每一层的数据合并算平均值
    :return:
    """
    with open("../../result/data_dict/all.pkl", "rb") as rf:
        data_dict = pkl.load(rf)
    node_list = get_node_list()
    for k, s_dict in data_dict.items():
        new_dict = dict()
        new_dict["access"] = [0 for _ in range(data_point_num)]
        new_dict["merge"] = [0 for _ in range(data_point_num)]
        new_dict["core"] = [0 for _ in range(data_point_num)]
        print(type(s_dict))
        for node in node_list:
            key = node[:-1]
            if key == "core":
                down = 4
            else:
                down = 8
            for j in range(data_point_num):
                new_dict[key][j] += s_dict[node][j] / down
        data_dict[k] = new_dict
    with open("../../result/data_dict/TM-SALFI.pkl", "wb") as wf:
        pkl.dump(data_dict, wf)
    print(data_dict["ARE"])
    print(data_dict["HHD_ARE"])
    print(data_dict["HHD_F1"])


def count_num():
    """
    统计每个节点流的数目和包的数目
    :return:
    """
    node_list = get_node_list()
    read_dir = "../../data/dat/flag_dat/slice/"

    flow_count_per_node_dict = dict()
    pkt_count_per_node_dict = dict()
    for node in node_list:
        flow_count_per_node_dict[node] = 0
        pkt_count_per_node_dict[node] = 0

    trace_byte_size = 16
    for file in os.listdir(read_dir):
        print(file)
        s = file.split(".")[0]
        # dat_id = s.split("-")[0]
        node = s.split("-")[1]

        flow_id = dict()
        pkt_count = 0
        with open(read_dir + file, "rb") as rf:
            bin_trace = rf.read(trace_byte_size)
            while bin_trace:
                pkt_count += 1
                src_ip = int.from_bytes(bin_trace[2:6], 'big')
                flow_id[src_ip] = 0
                bin_trace = rf.read(trace_byte_size)

        flow_count_per_node_dict[node] += int(len(flow_id) / dat_num)
        pkt_count_per_node_dict[node] += int(pkt_count / dat_num)
        # print(node)
        # print(pkt_count)
    print(flow_count_per_node_dict)
    print(pkt_count_per_node_dict)
    pkl_write("../../result/data_dict/flow_count_per_node_dict.pkl", flow_count_per_node_dict)
    pkl_write("../../result/data_dict/pkt_count_per_node_dict", pkt_count_per_node_dict)

    # print(dat_id)
    # print(node)


def get_CDF():
    """
    统计十个dat数据的CDF曲线，最后计算一个平均值
    :return:
    """
    read_dir = "../../data/dat/flag_dat/20s/"
    files = os.listdir(read_dir)
    cdf_data_list = []
    for file in files:
        print(file)
        x = 0
        src_set = dict()
        trace_byte_size = 16
        with open(read_dir + file, 'rb') as f:
            bin_trace = f.read(trace_byte_size)

            while bin_trace:
                x += 1
                src_ip = int.from_bytes(bin_trace[2:6], 'big')
                if src_ip in src_set.keys():
                    src_set[src_ip] += 1
                else:
                    src_set[src_ip] = 1
                bin_trace = f.read(trace_byte_size)
        flow_list = []
        for k, v in src_set.items():
            # flow_list.append([k, v])
            flow_list.append(v)
        flow_list.sort(reverse=True)
        cdf_list = [0]
        sum = 0
        for i in range(len(flow_list)):
            sum += flow_list[i]
            cdf_list.append(sum / x)

        indexs = [int(i / 100 * len(flow_list)) for i in range(101)]

        percent_cdf_list = []
        for index in indexs:
            percent_cdf_list.append(cdf_list[index])
        print(percent_cdf_list)

        cdf_data_list.append(percent_cdf_list)

    cdf_data = []

    print(len(cdf_data_list))
    for i in range(101):
        cdf_data.append(mean([cdf_data_list[j][i] for j in range(10)]))
    print(cdf_data)
    pkl_write("../../result/data_dict/cdf_data.pkl", cdf_data)


def get_kw_cmp():
    read_file_dir = "../../result/result2/"
    files = os.listdir(read_file_dir)
    data_dict = dict()
    data_dict["2"] = []
    data_dict["4"] = []
    data_dict["8"] = []
    k_list = ["2", "4", "8"]
    ratio_list = [1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]

    for k in k_list:
        read_file_name = read_file_dir + "ARE" + k
        with open(read_file_name, "r") as rf:
            tmp = [[] for _ in range(7)]
            for i in range(10):
                start = rf.readline()
                for j in range(7):
                    nums = float(rf.readline())
                    # tmp.append(nums)
                    tmp[j].append(nums)
            print(tmp)
            avr = []
            for j in range(7):
                avr.append(mean(tmp[j]))
            print(avr)
            data_dict[k] = avr
    print(data_dict)
    pkl_write("../../result/data_dict/kw_cmp.pkl",data_dict)

if __name__ == '__main__':
    # read_raw()
    aggregation_data()
    # count_num()
    # get_CDF()
    # error_cul()
    # get_kw_cmp()