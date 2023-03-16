from src.plot.draw import *

def plot_bar_cmp_sim1():
    # sim1-1
    draw_bar_cmp(x=[i+1 for i in range(10)], y_list=[[1 for i in range(10)] for _ in range(2)],
              label_list=['ST-MF', 'OPT'], xticks_label=[i+1 for i in range(10)], yticks_labels=None,
              color_list=color_list, marker_list=marker_list,
              xlimit=[0, 11], ylimit=[0,1.3],
              xlabel="资源种类数量", ylabel="Ratio",
              figsize=(8, 4.5), title="单任务下测量节点分配算法效果",
              save_name="4-sim-1-1", no=0, sci=False, log=False,ncols=2)

    # sim1-2-abcd
    draw_bar_cmp(x=[i+1 for i in range(10)], y_list=[[1 for i in range(10)] for _ in range(2)],
              label_list=['ST-MF', 'OPT'], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)], yticks_labels=None,
              color_list=color_list, marker_list=marker_list,
              xlimit=[0, 11], ylimit=[0,1.3],
              xlabel="网络资源总量", ylabel="Ratio",
              figsize=(8, 4.5), title="相同流量分布，相同资源分布下",
              save_name="4-sim-1-2-a", no=0, sci=False, log=False,ncols=2,istitle=False)
    draw_bar_cmp(x=[i+1 for i in range(10)], y_list=[[1 for i in range(10)] for _ in range(2)],
              label_list=['ST-MF', 'OPT'], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)], yticks_labels=None,
              color_list=color_list, marker_list=marker_list,
              xlimit=[0, 11], ylimit=[0,1.3],
              xlabel="网络资源总量", ylabel="Ratio",
              figsize=(8, 4.5), title="单任务下测量节点分配算法效果",
              save_name="4-sim-1-2-b", no=0, sci=False, log=False,ncols=2,istitle=False)
    draw_bar_cmp(x=[i+1 for i in range(10)], y_list=[[1 for i in range(10)] for _ in range(2)],
              label_list=['ST-MF', 'OPT'], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)], yticks_labels=None,
              color_list=color_list, marker_list=marker_list,
              xlimit=[0, 11], ylimit=[0,1.3],
              xlabel="网络资源总量", ylabel="Ratio",
              figsize=(8, 4.5), title="单任务下测量节点分配算法效果",
              save_name="4-sim-1-2-c", no=0, sci=False, log=False,ncols=2,istitle=False)
    draw_bar_cmp(x=[i+1 for i in range(10)], y_list=[[1 for i in range(10)] for _ in range(2)],
              label_list=['ST-MF', 'OPT'], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)], yticks_labels=None,
              color_list=color_list, marker_list=marker_list,
              xlimit=[0, 11], ylimit=[0,1.3],
              xlabel="网络资源总量", ylabel="Ratio",
              figsize=(8, 4.5), title="单任务下测量节点分配算法效果",
              save_name="4-sim-1-2-d", no=0, sci=False, log=False,ncols=2,istitle=False)
def plot_bar_cmp_sim2():
    data = pkl_read("../../result/cha4/ms")
    for d in data:
        for i,num in enumerate(d):
            d[i] = 1-num
    # draw_bar_no_cmp2(x=[i+1 for i in range(10)], y=data[0],
    #                 xlimit=[-1, 11], ylimit=[0, 9E-7], xticks_label=[i+1 for i in range(10)],
    #                 xlabel="任务数量", ylabel="1-Ratio",
    #                 figsize=(8, 4.5), title="多任务下测量节点分配算法效果",
    #                 save_name="4-sim-2-1", no=1, sci=True, log=False)

    draw_bar_no_cmp2(x=[i+1 for i in range(10)], y=data[1],
                    xlimit=[-1, 11], ylimit=[0, 9E-7], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)],
                    xlabel="网络资源总量", ylabel="1-Ratio",
                    figsize=(8, 4.5), title="多任务下测量节点分配算法效果",
                    save_name="4-sim-2-2-a", no=1, sci=True, log=False,istitle=False)
    draw_bar_no_cmp2(x=[i+1 for i in range(10)], y=data[2],
                    xlimit=[-1, 11], ylimit=[0, 9E-7], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)],
                    xlabel="网络资源总量", ylabel="1-Ratio",
                    figsize=(8, 4.5), title="多任务下测量节点分配算法效果",
                    save_name="4-sim-2-2-b", no=1, sci=True, log=False,istitle=False)
    draw_bar_no_cmp2(x=[i+1 for i in range(10)], y=data[3],
                    xlimit=[-1, 11], ylimit=[0, 2E-6], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)],
                    xlabel="网络资源总量", ylabel="1-Ratio",
                    figsize=(8, 4.5), title="多任务下测量节点分配算法效果",
                    save_name="4-sim-2-2-c", no=1, sci=True, log=False,istitle=False)
    draw_bar_no_cmp2(x=[i+1 for i in range(10)], y=data[4],
                    xlimit=[-1, 11], ylimit=[0, 2E-6], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)],
                    xlabel="网络资源总量", ylabel="1-Ratio",
                    figsize=(8, 4.5), title="多任务下测量节点分配算法效果",
                    save_name="4-sim-2-2-d", no=1, sci=True, log=False,istitle=False)

def plot_bar_cmp_sim3():
    data = pkl_read("../../result/cha4/mm")
    print(data[0][0])
    print(data[0][1])
    print(data[0][2])
    print(data[0][3])
    print(data[1][0])
    print(data[1][1])
    print(data[1][2])
    print(data[1][3])
    # print(data[0])
    # print(data[2])
    # print(data[3])
    # sim3-1
    # draw_bar_cmp(x=[i+1 for i in range(10)], y_list=data[0],
    #           label_list=["MTMR-TR", "MTMR-RR","MTMR-Mix", 'OPT'], xticks_label=[i+1 for i in range(10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 11], ylimit=[0,1.5],
    #           xlabel="资源种类数量", ylabel="Ratio",
    #           figsize=(8, 4.5), title="多任务多资源下测量节点分配算法效果",
    #           save_name="4-sim-3-1", no=0, sci=False, log=False,ncols=2)

    # sim3-2-abcd

    # draw_bar_cmp(x=[i+1 for i in range(10)], y_list=data[1],
    #           label_list=["MTMR-TR", "MTMR-RR","MTMR-Mix", 'OPT'], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 11], ylimit=[0,1.5],
    #           xlabel="网络资源总量", ylabel="Ratio",
    #           figsize=(8, 4.5), title="相同流量分布，相同资源分布下",
    #           save_name="4-sim-3-2-a", no=0, sci=False, log=False,ncols=2,istitle=False)
    # draw_bar_cmp(x=[i+1 for i in range(10)], y_list=data[2],
    #           label_list=["MTMR-TR", "MTMR-RR","MTMR-Mix", 'OPT'], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 11], ylimit=[0,1.5],
    #           xlabel="网络资源总量", ylabel="Ratio",
    #           figsize=(8, 4.5), title="单任务下测量节点分配算法效果",
    #           save_name="4-sim-3-2-b", no=0, sci=False, log=False,ncols=2,istitle=False)
    # draw_bar_cmp(x=[i+1 for i in range(10)], y_list=data[3],
    #           label_list=["MTMR-TR", "MTMR-RR","MTMR-Mix", 'OPT'], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 11], ylimit=[0,1.5],
    #           xlabel="网络资源总量", ylabel="Ratio",
    #           figsize=(8, 4.5), title="单任务下测量节点分配算法效果",
    #           save_name="4-sim-3-2-c", no=0, sci=False, log=False,ncols=2,istitle=False)
    # draw_bar_cmp(x=[i+1 for i in range(10)], y_list=data[4],
    #           label_list=["MTMR-TR", "MTMR-RR","MTMR-Mix", 'OPT'], xticks_label=["%.1f"%((i+1)*0.2) for i in range(10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 11], ylimit=[0,1.5],
    #           xlabel="网络资源总量", ylabel="Ratio",
    #           figsize=(8, 4.5), title="单任务下测量节点分配算法效果",
    #           save_name="4-sim-3-2-d", no=0, sci=False, log=False,ncols=2,istitle=False)
if __name__ == '__main__':
    # plot_bar_cmp_sim2()
    plot_bar_cmp_sim3()