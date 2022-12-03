import matplotlib.pyplot as plt
import numpy as np
import matplotlib.cbook
import warnings

warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)
import matplotlib.pyplot as plt



font1 = {'family': 'Times New Roman',
        'weight': 'bold',
        'size': 20,
        }
font2 = {'family': 'SimHei',
        'weight': 'normal',
        'size': 20,
        }


def draw_line(x: list, y_list: list, label_list: list, color_list: list,
              marker_list:list ,xlimit, ylimit, xlabel: str, ylabel: str,
              figsize: tuple,
              save_name: str):
    plt.figure(figsize=figsize)
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # data_num = len(y_list)
    for i, y in enumerate(y_list):
        plt.plot(x, y, color=color_list[i], label=label_list[i],marker=marker_list[i])

    plt.yticks(fontproperties='Times New Roman', size=20)
    plt.xticks(fontproperties='Times New Roman', size=20)
    # plt.xlabel(xlabel,fontdict=font2)
    # plt.ylabel(ylabel,fontdict=font1)
    plt.xlabel(xlabel,fontsize=20)
    plt.ylabel(ylabel,fontdict=font1)
    plt.legend(fontsize=20)
    if xlimit is not None:
        plt.xlim(xlimit[0], xlimit[1])
    if ylimit is not None:
        plt.ylim(ylimit[0], ylimit[1])

    if save_name is not None:
        plt.savefig("../../result/figure/" + save_name)
    plt.show()


'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w',
if __name__ == '__main__':
    mem_list = [0.2 + 0.1 * i for i in range(10)]
    color_list = ['g', 'r', 'c', 'm', 'y', 'k', 'b', 'w']
    marker_list = ['o','D','x','+','v','^','*']
    draw_line(x=mem_list, y_list=[[0.05 * i for i in range(10)],[0.1 * i for i in range(10)]], label_list=["test1","test2"],
              color_list=color_list,marker_list=marker_list,
              xlimit=[0.2, 0.9], ylimit=[0, 0.5], xlabel="存储空间(MB)", ylabel="TESTY",
              figsize=(16, 9), save_name="test.png")
    if None:
        print(1)
