algo1 = "DivSketch"
mem_list = [0.2 + 0.1 * i for i in range(10)]
color_list = ['g', 'r', 'c', 'm', 'y', 'k', 'b', 'w']
marker_list = ['o', 'D', 'x', '+', 'v', '^', '*']

node_set = {"access", "merge", "core"}

task_set = {"ARE", "CE", "HHD_ARE", "HHD_F1", "WMRE"}
algo_set = {algo1}
data_dict = dict()
cmp_dict = dict()
cmp_dict["ARE"] = [algo1,]
cmp_dict["CE"] = [algo1,]
cmp_dict["HHD_ARE"] = [algo1,]
cmp_dict["HHD_F1"] = [algo1,]
cmp_dict["WMRE"] = [algo1,]
xticks_label = ["%.1f" % i for i in mem_list]

# 加载result
data_dict_dir = "../../result/data_dict/"
# data_dict = dict()

data_point_num = 10
