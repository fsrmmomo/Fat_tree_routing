import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np
import matplotlib.cbook
import warnings

from matplotlib import font_manager

from util.utils import *
from plot.param import *

warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt

font1 = {'family': 'Times New Roman',
         'weight': 'normal',
         'size': 20,
         }
font2 = {'family': 'SimSun',
         'weight': 'normal',
         'size': 20,
         }

figure_no = 1


def draw_line(x: list, y_list: list, label_list: list, color_list: list,
              yticks_labels: list, xticks_label: list,
              marker_list: list, xlimit, ylimit, xlabel: str, ylabel: str,
              figsize: tuple, title: str,
              save_name: str, no: int,
              sci=False,log=False):
    print(len(x))
    print(len(xticks_label))
    assert len(x) == len(xticks_label)
    assert len(y_list) == len(label_list)
    assert len(y_list)<=len(marker_list)
    assert len(y_list)<=len(color_list)
    x_size = len(x)

    plt.figure(num=no, figsize=figsize, dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimSun','Times New Roman']
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号(无用)

    # 修改刻度线向内 需在plot之前
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    plt.title(title, fontdict=font1)

    #使用对数曲线
    if log:
        plt.yscale('log')
    # plot 曲线
    for i, y in enumerate(y_list):
        plt.plot(x, y, color=color_list[i], label=label_list[i], marker=marker_list[i])

    plt.yticks(fontproperties='Times New Roman', size=18, ha="right")
    plt.xticks(ticks=np.linspace(x[0], x[-1], x_size), labels=xticks_label, fontproperties='Times New Roman', size=18)

    ax = plt.gca()
    # 设置文字和刻度的间距,防止左下角x和y重叠
    ax.tick_params(axis="x", pad=10)

    # 设置纵坐标科学计数法
    if sci:
        ax.ticklabel_format(style='sci', scilimits=(0,0), axis='y',useMathText=True)
        print(mpl.rcParams['xtick.labelsize'])
        ax.get_yaxis().get_offset_text().set(va='bottom', ha='left',fontsize="large",
                                             fontproperties="stixgeneral",fontstyle="normal")




    plt.xlabel(xlabel, fontsize=18)
    plt.ylabel(ylabel, fontdict=font1)

    # 修改刻度线向内
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    plt.legend(prop=font1)
    plt.grid()
    if xlimit is not None:
        plt.xlim(xlimit[0], xlimit[1])
    if ylimit is not None:
        plt.ylim(ylimit[0], ylimit[1])
    plt.tight_layout()

    f = plt.gcf()
    plt.show()
    if save_name is not None:
        f.savefig("../../result/figure/" + save_name + ".jpg", dpi=300)
        f.savefig("../../result/figure/" + save_name + ".svg", dpi=300, format="svg")


def plot_linear(task, ylimit: list, title_patter: str,sci=False,log=False ):
    # task = "HHD_F1"
    cmp_list = cmp_dict[task]
    label_list = cmp_list
    for i, node in enumerate(node_set):
        y_list = []

        for algo in cmp_list:

            y_list.append(data_dict[algo][task][node][:data_point_num])
        # title = "Heavy Hitter Detection on " + node.capitalize() + " Node"
        title = title_patter + " on " + node.capitalize() + " Node"
        save_name = task + "_" + node
        if task == "CE":
            ylabel = "RE"
        else:
            ylabel = task
        draw_line(x=list(range(data_point_num)), y_list=y_list,
                  label_list=label_list, xticks_label=xticks_label, yticks_labels=None,
                  color_list=color_list, marker_list=marker_list,
                  xlimit=[0, data_point_num - 1], ylimit=ylimit,
                  xlabel="存储空间(MB)", ylabel=ylabel,
                  figsize=(8, 4.5), title=title,
                  save_name=save_name, no=i,sci=sci,log=log)


if __name__ == '__main__':

    for algo in algo_set:
        global data_dict
        data_dict[algo] = pkl_read(data_dict_dir + algo + ".pkl")
    data_dict.update(pkl_read("../../result/data_dict/output.pkl"))

    for k,v in data_dict.items():
        print(k)
        print(v)
        # print(data_dict[algo])
    # print(data_dict)
    # plot_linear("ARE", ylimit=[0, 2], title_patter="Flow Size Measurement")
    # plot_linear("HHD_ARE", ylimit=[0, 0.03], title_patter="Heavy Hitter Detection")
    # plot_linear("HHD_F1", ylimit=[0.9, 1], title_patter="Heavy Hitter Detection")
    # plot_linear("CE", ylimit=[0,0.05], title_patter="Cardinality Estimation",sci=False)
    plot_linear("WMRE", ylimit=[0,2], title_patter="Flow Size Distribution Estimation",log=True)
