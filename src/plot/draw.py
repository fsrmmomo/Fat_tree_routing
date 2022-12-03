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
    # 修改刻度线向内 需在plot之前
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    # ax.xaxis.set_ticks_position('bottom')
    # # 设置y坐标轴为左边框
    # ax.yaxis.set_ticks_position('left')

    for i, y in enumerate(y_list):
        plt.plot(x, y, color=color_list[i], label=label_list[i],marker=marker_list[i])

    # ha 参数防止坐标值重叠
    plt.yticks(fontproperties='Times New Roman', size=18,ha="right")
    # plt.xticks(fontproperties='Times New Roman', size=18,ha="left",)
    plt.xticks(fontproperties='Times New Roman', size=18)
    ax = plt.gca()

    #设置文字和刻度的间距
    ax.tick_params(axis="x",pad=10)
    # plt.margins(0.2)
    # plt.xlabel(xlabel,fontdict=font2)
    # plt.ylabel(ylabel,fontdict=font1)
    plt.xlabel(xlabel,fontsize=18)
    plt.ylabel(ylabel,fontdict=font1)

    # 修改刻度线向内
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    plt.legend(fontsize=20)
    plt.grid()
    if xlimit is not None:
        plt.xlim(xlimit[0], xlimit[1])
    if ylimit is not None:
        plt.ylim(ylimit[0], ylimit[1])
    plt.tight_layout()

    f = plt.gcf()
    plt.show()
    if save_name is not None:
        f.savefig("../../result/figure/" + save_name+".png", dpi=300)
        f.savefig("../../result/figure/" + save_name+".svg", dpi=300,format="svg")



'b', 'g', 'r', 'c', 'm', 'y', 'k', 'w',
if __name__ == '__main__':
    mem_list = [0.2 + 0.1 * i for i in range(10)]
    color_list = ['g', 'r', 'c', 'm', 'y', 'k', 'b', 'w']
    marker_list = ['o','D','x','+','v','^','*']
    draw_line(x=mem_list, y_list=[[0.05 * i for i in range(10)],[0.1 * i for i in range(10)]], label_list=["test1","test2"],
              color_list=color_list,marker_list=marker_list,
              xlimit=[0.2, 0.9], ylimit=[0, 0.5], xlabel="存储空间(MB)", ylabel="TESTY",
              figsize=(8, 4.5), save_name="test")

