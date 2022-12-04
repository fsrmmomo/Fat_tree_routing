import os
import pickle as pkl
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

def read_txt():
    data_dict = pkl_read("../../result/data_dict/output.pkl")
    print(data_dict)


def read_raw():
    read_file_dir = "../../result/DivSketch/"

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
    with open("../../result/data_dict/all.pkl","wb") as wf:
        pkl.dump(data_dict,wf)

def aggregation_data():
    """
    把每一层的数据合并算平均值
    :return:
    """
    with open("../../result/data_dict/all.pkl","rb") as rf:
        data_dict = pkl.load(rf)
    node_list = get_node_list()
    for k,s_dict in data_dict.items():
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
                new_dict[key][j] += s_dict[node][j]/down
        data_dict[k] = new_dict
    with open("../../result/data_dict/DivSketch.pkl","wb") as wf:
        pkl.dump(data_dict,wf)
    print(data_dict["ARE"])
    print(data_dict["HHD_ARE"])
    print(data_dict["HHD_F1"])


if __name__ == '__main__':
    # read_raw()
    # aggregation_data()
    read_txt()
