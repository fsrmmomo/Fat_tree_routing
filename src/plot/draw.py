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
    assert len(x) == len(xticks_label)
    assert len(y_list) == len(label_list)
    assert len(y_list)<=len(marker_list)
    assert len(y_list)<=len(color_list)
    x_size = len(x)

    plt.figure(num=no, figsize=figsize, dpi=300)
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    # plt.rcParams['font.sans-serif'] = ['SimSun','Times New Roman']
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

    plt.xlabel(xlabel, fontdict=font1)
    plt.ylabel(ylabel, fontdict=font1)
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


def draw_line_no_cmp(x: list, y: list,  xticks_label: list,
               xlimit, ylimit, xlabel: str, ylabel: str,
              figsize: tuple, title: str,
              save_name: str, no: int,
              sci=False,log=False):

    assert len(x) == len(y)
    x_size = len(x)

    plt.figure(num=no, figsize=figsize, dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimSun','Times New Roman']

    # 修改刻度线向内 需在plot之前
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'

    plt.title(title, fontdict=font1)


    #使用对数曲线
    if log:
        plt.yscale('log')
    # plot 曲线
    plt.plot(x, y, color="g", marker="o")

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

    plt.xlabel(xlabel, fontdict=font1)
    plt.ylabel(ylabel, fontdict=font1)
    # plt.legend(prop=font1)
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
                  xlabel="Memory Usage (MB)", ylabel=ylabel,
                  figsize=(8, 4.5), title=title,
                  save_name=save_name, no=i,sci=sci,log=log)




def draw_bar_no_cmp(x: list, y: list, xticks_label: list,
                    xlimit, ylimit, xlabel: str, ylabel: str,
              figsize: tuple, title: str,
              save_name: str, no: int,
              sci=False,log=False):

    assert len(x) == len(xticks_label)
    x_size = len(x)

    plt.figure(num=no, figsize=figsize, dpi=300)
    plt.rcParams['font.sans-serif'] = ['SimSun','Times New Roman']
    # plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号(无用)
    # 修改刻度线向内 需在plot之前
    plt.rcParams['xtick.direction'] = 'in'
    plt.rcParams['ytick.direction'] = 'in'
    plt.title(title, fontdict=font1)

    # zorder=0 设置图层级别 不遮挡数据
    plt.grid(zorder=0)

    color_list = []
    color_list.extend(['g' for _ in range(8)])
    color_list.extend(['b' for _ in range(8)])
    color_list.extend(['c' for _ in range(4)])
    #使用对数曲线
    if log:
        plt.yscale('log')
    plt.bar(x, y, width=0.4, zorder=10,color = color_list)
        # plt.bar(x, y, color=color_list[i], label=label_list[i], marker=marker_list[i])

    plt.yticks(fontproperties='Times New Roman', size=18, ha="right")
    plt.xticks(ticks=np.linspace(x[0], x[-1], x_size), labels=xticks_label, fontproperties='Times New Roman',
               size=18, rotation=45)
    ax = plt.gca()

    # 设置文字和刻度的间距,防止左下角x和y重叠
    # ax.tick_params(axis="x", pad=10)
    # 设置纵坐标科学计数法
    if sci:
        ax.ticklabel_format(style='sci', scilimits=(0,0), axis='y',useMathText=True)
        print(mpl.rcParams['xtick.labelsize'])
        ax.get_yaxis().get_offset_text().set(va='bottom', ha='left',fontsize="large",
                                             fontproperties="stixgeneral",fontstyle="normal")

    plt.xlabel(xlabel, fontdict=font1)
    plt.ylabel(ylabel, fontdict=font1)

    # plt.legend(prop=font1)
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

# plot_bar():
def draw_error_bar(x: list, y_list: list,e_list:list, label_list: list, color_list: list,
              yticks_labels: list, xticks_label: list,
              marker_list: list, xlimit, ylimit, xlabel: str, ylabel: str,
              figsize: tuple, title: str,
              save_name: str, no: int,
              sci=False,log=False):
    assert len(x) == len(xticks_label)
    assert len(y_list) == len(label_list)
    assert len(y_list)<=len(marker_list)
    assert len(y_list)<=len(color_list)
    x_size = len(x)

    plt.figure(num=no, figsize=figsize, dpi=300)
    plt.rcParams['font.sans-serif'] = ['Times New Roman']
    # plt.rcParams['font.sans-serif'] = ['SimSun','Times New Roman']
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
        print(e_list[i])
        print(y)
        plt.errorbar(x,y,yerr=e_list[i],color=color_list[i],ecolor='b',ms=5,mfc='wheat',mec='salmon',capsize=3,
                     elinewidth=3,label=label_list[i], marker=marker_list[i])
        # plt.plot(x, y, color=color_list[i], label=label_list[i], marker=marker_list[i])

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

    plt.xlabel(xlabel, fontdict=font1)
    plt.ylabel(ylabel, fontdict=font1)
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

def plot_error_bar(task, ylimit: list, title_patter: str,sci=False,log=False ):
    cmp_list = cmp_dict[task]
    label_list = cmp_list
    for i, node in enumerate(node_set):
        y_list = []
        e_list = []

        for algo in cmp_list:

            yt_list = data_dict[algo][task][node][:data_point_num]
            et_list = error_dict[algo][task][node][:data_point_num]
            # et_list.append(error_dict[algo][task][node][:data_point_num])
            # print(error_dict[algo][task][node][:data_point_num])
            # print(et_list)
            et_list = [[yt_list[x]- et_list[x][0] for x in range(data_point_num)], [et_list[x][1]-yt_list[x] for x in range(data_point_num)]]
            # print(et_list)
            y_list.append(yt_list)
            e_list.append(et_list)
        # et_list = [[et_list[x][0] for x in range(data_point_num)], [et_list[x][1] for x in range(data_point_num)]]
        # title = "Heavy Hitter Detection on " + node.capitalize() + " Node"
        title = title_patter + " on " + node.capitalize() + " Node"
        save_name = task + "_" + node + "_error"
        if task == "CE":
            ylabel = "RE"
        else:
            ylabel = task
        print(e_list)
        draw_error_bar(x=list(range(data_point_num)), y_list=y_list,e_list=e_list,
                  label_list=label_list, xticks_label=xticks_label, yticks_labels=None,
                  color_list=color_list, marker_list=marker_list,
                  xlimit=[0, data_point_num - 1], ylimit=ylimit,
                  xlabel="Memory Usage (MB)", ylabel=ylabel,
                  figsize=(8, 4.5), title=title,
                  save_name=save_name, no=i,sci=sci,log=log)

def get_node_list():
    node_list = []
    for i in range(1, 9):
        node_list.append("access" + str(i))
    for i in range(1, 9):
        node_list.append("merge" + str(i))
    for i in range(1, 5):
        node_list.append("core" + str(i))
    return node_list

def plot_statistics_error_bar():

    global data_dict,error_dict
    data_dict = pkl_read("../../result/data_dict/all_data.pkl")
    error_dict = pkl_read("../../result/data_dict/all_error.pkl")

    plot_error_bar("ARE", ylimit=[0, 2], title_patter="Flow Size Measurement")
    # plot_error_bar("HHD_ARE", ylimit=[0, 0.03], title_patter="Heavy Hitter Detection")
    # plot_error_bar("HHD_F1", ylimit=[0.9, 1], title_patter="Heavy Hitter Detection")
    # plot_error_bar("CE", ylimit=[0.00001,0.1], title_patter="Cardinality Estimation",log=True)
    # plot_error_bar("CE", ylimit=[0,0.1], title_patter="Cardinality Estimation",log=False)
    # plot_error_bar("WMRE", ylimit=[0.0001,2], title_patter="Flow Size Distribution Estimation",log=True)

def plot_statistics():
    # global data_dict
    # for algo in algo_set:
    #     data_dict[algo] = pkl_read(data_dict_dir + algo + ".pkl")
    # data_dict.update(pkl_read("../../result/data_dict/output.pkl"))
    # print(data_dict.keys())
    # data_dict["TM-SALFM"] = data_dict["ServerCount Sketch"]
    # data_dict.pop("ServerCount Sketch")
    # print(data_dict.keys())
    #
    #
    #
    # pkl_write("../../result/data_dict/all_data.pkl", data_dict)
    global data_dict
    data_dict = pkl_read("../../result/data_dict/all_data.pkl")




    plot_linear("ARE", ylimit=[0, 2], title_patter="Flow Size Measurement")
    plot_linear("HHD_ARE", ylimit=[0, 0.03], title_patter="Heavy Hitter Detection")
    plot_linear("HHD_F1", ylimit=[0.9, 1], title_patter="Heavy Hitter Detection")
    plot_linear("CE", ylimit=[0.00001,0.1], title_patter="Cardinality Estimation",log=True)
    plot_linear("CE", ylimit=[0,0.1], title_patter="Cardinality Estimation",log=False)
    plot_linear("WMRE", ylimit=[0.0001,2], title_patter="Flow Size Distribution Estimation",log=True)

def plot_flow_and_pkt_count():
    flow_count_dict = pkl_read("../../result/data_dict/flow_count_per_node_dict.pkl")
    pkt_count_dict = pkl_read("../../result/data_dict/pkt_count_per_node_dict")

    flow_count_list = []
    pkt_count_list = []
    xticks_label = []
    node_list = get_node_list()
    for node in node_list:
        flow_count_list.append(flow_count_dict[node])
        pkt_count_list.append(pkt_count_dict[node])
    print(len(xticks_label))
    draw_bar_no_cmp(x=list(range(20)), y=flow_count_list,
                    xlimit=[-1, 20], ylimit=[0,90000],xticks_label=node_list,
                    xlabel="Node Name", ylabel="Number of Flows",
                    figsize=(9, 4.5), title="Number of Flows on Each Node",
                    save_name="Flows_Number", no=1, sci=True, log=False)

    draw_bar_no_cmp(x=list(range(20)), y=pkt_count_list,
                    xlimit=[-1, 20], ylimit=[0,500000],xticks_label=node_list,
                    xlabel="Node Name", ylabel="Number of Packets",
                    figsize=(9, 4.5), title="Number of Packets on Each Node",
                    save_name="Packets_Number", no=1, sci=True, log=False)


def plot_CDF():
    cdf_list = pkl_read("../../result/data_dict/cdf_data.pkl")
    # plot_linear("Percentage", ylimit=[0.0001, 2], title_patter="Cumulative Distribution Function", log=True)

    draw_line_no_cmp(x=list(range(0,101,5)), y=[int(cdf_list[i]*100) for i in range(0,101,5)],
                     xticks_label=[i for i in range(0,101,5)],
              xlimit=[0, 100], ylimit=[0,100],
              xlabel="Percentage of Top Flow(%)", ylabel="Percentage of Packets(%)",
              figsize=(8, 4.5), title="Cumulative Distribution Function of Flow Size",
              save_name="CDF", no=1, sci=False, log=False)


def get_all_data():
    global data_dict
    data_dict["TM-SALFI"] = pkl_read("../../result/data_dict/TM-SALFI.pkl")
    data_dict.update(pkl_read("../../result/data_dict/output_10.pkl"))

    print(data_dict.keys())
    data_dict["TM-SALFM"] = data_dict["ServerCount Sketch"]
    data_dict.pop("ServerCount Sketch")
    global error_dict
    error_dict = pkl_read("../../result/data_dict/error_1.pkl")
    error_dict.update(pkl_read("../../result/data_dict/confidence_interval.pkl"))
    error_dict["TM-SALFM"] = error_dict["ServerCount Sketch"]
    error_dict.pop("ServerCount Sketch")
    print(error_dict.keys())
    pkl_write("../../result/data_dict/all_data.pkl", data_dict)
    pkl_write("../../result/data_dict/all_error.pkl", error_dict)

if __name__ == '__main__':

    # global data_dict
    # for algo in algo_set:
    #     data_dict[algo] = pkl_read(data_dict_dir + algo + ".pkl")
    # data_dict.update(pkl_read("../../result/data_dict/output.pkl"))

    # for k,v in data_dict.items():
    #     print(k)
    #     print(v)
    # print(data_dict[algo])
    # print(data_dict)
    # plot_linear("ARE", ylimit=[0, 2], title_patter="Flow Size Measurement")
    # plot_linear("HHD_ARE", ylimit=[0, 0.03], title_patter="Heavy Hitter Detection")
    # plot_linear("HHD_F1", ylimit=[0.9, 1], title_patter="Heavy Hitter Detection")
    # plot_linear("CE", ylimit=[0.00001,0.1], title_patter="Cardinality Estimation",log=True)
    # plot_linear("CE", ylimit=[0,0.1], title_patter="Cardinality Estimation",log=False)
    # plot_linear("WMRE", ylimit=[0.0001,2], title_patter="Flow Size Distribution Estimation",log=True)

    # plot_flow_and_pkt_count()
    plot_statistics()
    # plot_statistics_error_bar()
