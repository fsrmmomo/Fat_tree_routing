from src.plot.draw import *
import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.cbook
import warnings

from matplotlib import font_manager

# from util.utils import *
from plot.param import *
from openpyxl import workbook, load_workbook

# with open("../../result/data_dict/data.xlsx","wb") as f:
#     pass
excel_ = load_workbook("../../result/data_dict/all_result_data.xlsx")

def plot_bar_cmp_sim1():
    # 流量识别准确率
    # sim1-1
    y1 = [0.9897, 0.992, 0.99, 0.9899]
    y2 = [0.9846, 0.9915, 0.9932, 0.9941]
    y3 = [0.9828, 0.9861, 0.9843, 0.9855]
    y4 = [0.9837, 0.9888, 0.9887, 0.9898]
    # y1 = [i*100 for i in y1]
    # y2 = [i*100 for i in y2]
    # y3 = [i*100 for i in y3]
    # y4 = [i*100 for i in y4]
    # y1 = [i*100 for i in y1]
    draw_bar_no_cmp3(x=[i + 1 for i in range(4)], y=y1,
                     xlimit=[0, 5], ylimit=[0, 1.1], xticks_label=["5%","10%","20%","30%"],
                     xlabel="大流比例", ylabel="ACC",
                     figsize=(6, 4.5), title="",
                     save_name="3-sim-1-1", no=1, sci=True, log=False, istitle=False)
    draw_bar_no_cmp3(x=[i + 1 for i in range(4)], y=y2,
                     xlimit=[0, 5], ylimit=[0, 1.1], xticks_label=["5%","10%","20%","30%"],
                     xlabel="大流比例", ylabel="Precision",
                     figsize=(6, 4.5), title="",
                     save_name="3-sim-1-2", no=1, sci=True, log=False, istitle=False)
    draw_bar_no_cmp3(x=[i + 1 for i in range(4)], y=y3,
                     xlimit=[0, 5], ylimit=[0, 1.1], xticks_label=["5%","10%","20%","30%"],
                     xlabel="大流比例", ylabel="Recall",
                     figsize=(6, 4.5), title="",
                     save_name="3-sim-1-3", no=1, sci=True, log=False, istitle=False)
    draw_bar_no_cmp3(x=[i + 1 for i in range(4)], y=y4,
                     xlimit=[0, 5], ylimit=[0, 1.1], xticks_label=["5%","10%","20%","30%"],
                     xlabel="大流比例", ylabel="F1",
                     figsize=(6, 4.5), title="",
                     save_name="3-sim-1-4", no=1, sci=True, log=False, istitle=False)
    # draw_bar_no_cmp2(x=[i + 1 for i in range(10)], y=data[0],
    #                  xlimit=[-1, 11], ylimit=[0, 2E-6], xticks_label=[i + 1 for i in range(10)],
    #                  xlabel="任务数量", ylabel="1-Ratio",
    #                  figsize=(8, 4.5), title="多任务下测量节点分配算法效果",
    #                  save_name="4-sim-2-1", no=1, sci=True, log=False)
    # draw_bar_cmp(x=[i + 1 for i in range(4)], y_list=[[1 for i in range(10)] for _ in range(2)],
    #              label_list=['ST-MF', 'OPT'], xticks_label=[i + 1 for i in range(10)], yticks_labels=None,
    #              color_list=color_list, marker_list=marker_list,
    #              xlimit=[0, 11], ylimit=[0, 1.3],
    #              xlabel="资源种类数量", ylabel="Ratio",
    #              figsize=(8, 4.5), title="单任务下测量节点分配算法效果",
    #              save_name="4-sim-1-1", no=0, sci=False, log=False, ncols=2)


if __name__ == '__main__':
    plot_bar_cmp_sim1()