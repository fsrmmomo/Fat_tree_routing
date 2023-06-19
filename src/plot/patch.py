from src.plot.draw import *


def polt_part_node():
    # y1 = [0.0344725, 0.0355577, 0.0371994, 0.0387749, 0.0400411, 0.0418726, 0.0434447, 0.0449468, 0.0466762, 0.0484507,
    #       0.0502383]
    # y2 = [0.0152808, 0.0161799, 0.0176459, 0.0190055, 0.0200451, 0.0211696, 0.0223614, 0.0242197, 0.025682, 0.0269276,
    #       0.0283505]
    # y3 = [0.0374691, 0.0385834, 0.0402525, 0.0418617, 0.0431633, 0.0451051, 0.0467367, 0.0481832, 0.0499542, 0.0518114,
    #       0.0536558]
    #
    # y11 = [i / y1[0] * 100 - 100 for i in y1[1:]]
    # y21 = [i / y2[0] * 100 - 100 for i in y2[1:]]
    # y31 = [i / y3[0] * 100 - 100 for i in y3[1:]]
    # draw_line(x=list(range(10)), y_list=[y11, y21, y31],
    #           label_list=["Total ARE", "Large Flow ARE", "Small Flow ARE"],
    #           xticks_label=[i for i in range(10, 110, 10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 9], ylimit=[0, 100],
    #           xlabel="Percentage of Servers Without Measurement Capability (%)", ylabel="ARE(%)",
    #           figsize=(8, 4.5), title="TM-SALFI ARE",
    #           save_name="TM-SALFI ARE1", no=0, istitle=True, log=False)
    # y11 = y1[1:]
    # y21 = y2[1:]
    # y31 = y3[1:]
    # draw_line(x=list(range(10)), y_list=[y11, y21, y31],
    #           label_list=["Total ARE", "Large Flow ARE", "Small Flow ARE"],
    #           xticks_label=[i for i in range(10, 110, 10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 9], ylimit=[0, 0.06],
    #           xlabel="Percentage of Servers Without Measurement Capability (%)", ylabel="ARE",
    #           figsize=(8, 4.5), title="TM-SALFI ARE",
    #           save_name="TM-SALFI ARE2", no=0, istitle=True, log=False)
    # y1 = [0.028160, 0.028708, 0.029177, 0.029927, 0.030683, 0.031262, 0.031757, 0.032502, 0.033227, 0.033649, 0.034436]
    # y2 = [0.000000, 0.007040, 0.017973, 0.028094, 0.035879, 0.046352, 0.062533, 0.072326, 0.083149, 0.092528, 0.105545]
    # y3 = [0.028245, 0.028774, 0.029211, 0.029932, 0.030667, 0.031216, 0.031664, 0.032381, 0.033075, 0.033470, 0.034220]
    # y11 = [i / y1[0] * 100 - 100 for i in y1[1:]]
    # # y21 = [i / y2[0] * 100 - 100 for i in y2[1:]]
    # y31 = [i / y3[0] * 100 - 100 for i in y3[1:]]
    #
    # draw_line(x=list(range(10)), y_list=[y11, y31],
    #           label_list=["Total ARE", "Small Flow ARE"],
    #           xticks_label=[i for i in range(10, 110, 10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 9], ylimit=[0, 100],
    #           xlabel="Percentage of Servers Without Measurement Capability (%)", ylabel="ARE(%)",
    #           figsize=(8, 4.5), title="TM-SALFM ARE",
    #           save_name="TM-SALFM ARE1", no=0, istitle=True, log=False)
    # y11 = y1[1:]
    # y21 = y2[1:]
    # y31 = y3[1:]
    # draw_line(x=list(range(10)), y_list=[y11, y21, y31],
    #           label_list=["Total ARE", "Large Flow ARE", "Small Flow ARE"],
    #           xticks_label=[i for i in range(10, 110, 10)], yticks_labels=None,
    #           color_list=color_list, marker_list=marker_list,
    #           xlimit=[0, 9], ylimit=[0, 0.11],
    #           xlabel="Percentage of Servers Without Measurement Capability (%)", ylabel="ARE",
    #           figsize=(8, 4.5), title="TM-SALFM ARE",
    #           save_name="TM-SALFM ARE2", no=0, istitle=True, log=False)

    y1 = [0.0344725, 0.0355577, 0.0371994, 0.0387749, 0.0400411, 0.0418726, 0.0434447, 0.0449468, 0.0466762, 0.0484507,
          0.0502383]
    y2 = [0.0152808, 0.0161799, 0.0176459, 0.0190055, 0.0200451, 0.0211696, 0.0223614, 0.0242197, 0.025682, 0.0269276,
          0.0283505]
    y3 = [0.0374691, 0.0385834, 0.0402525, 0.0418617, 0.0431633, 0.0451051, 0.0467367, 0.0481832, 0.0499542, 0.0518114,
          0.0536558]
    y4 = [0.028160, 0.028708, 0.029177, 0.029927, 0.030683, 0.031262, 0.031757, 0.032502, 0.033227, 0.033649, 0.034436]
    y5 = [0.000000, 0.007040, 0.017973, 0.028094, 0.035879, 0.046352, 0.062533, 0.072326, 0.083149, 0.092528, 0.105545]
    y6 = [0.028245, 0.028774, 0.029211, 0.029932, 0.030667, 0.031216, 0.031664, 0.032381, 0.033075, 0.033470, 0.034220]

    nnn = 6
    # draw_line(x=list(range(nnn)), y_list=[y1[1:nnn+1], y2[1:nnn+1], y3[1:nnn+1],y4[1:nnn+1],y5[1:nnn+1],y6[1:nnn+1]],
    #           label_list=["TM-SALFI Total ARE", "TM-SALFI Large Flow ARE", "TM-SALFI Small Flow ARE", "TM-SALFM Total ARE", "TM-SALFM Large Flow ARE", "TM-SALFM Small Flow ARE"],
    #           xticks_label=[i for i in range(10, 70, 10)], yticks_labels=None,
    #           color_list=['darkslategrey','teal','c','maroon','r','salmon'], marker_list=['o', 'D', 'x','o', 'D', 'x'],
    #           xlimit=[0, nnn-1], ylimit=[0, 0.08],
    #           xlabel="Percentage of Servers Without Measurement Capability (%)", ylabel="ARE",
    #           figsize=(8, 4.5), title="TM-SALFM ARE",
    #           save_name="ARE", no=0, istitle=True, log=False)
    draw_line(x=list(range(nnn)), y_list=[y2[1:nnn+1], y3[1:nnn+1],y5[1:nnn+1],y6[1:nnn+1]],
              label_list=["TM-SALFI large flow ARE", "TM-SALFI small flow ARE","TM-SALFM large flow ARE", "TM-SALFM small flow ARE"],
              xticks_label=[i for i in range(10, 70, 10)], yticks_labels=None,
              color_list=['darkslategrey','teal','maroon','r'], marker_list=['o', 'D','o', 'D'],
              xlimit=[0, nnn-1], ylimit=[0, 0.08],
              xlabel="Percentage of Servers Without Measurement Capability (%)", ylabel="ARE",
              figsize=(8, 4.5), title="Flow Size Measurement",
              save_name="ARE", no=0, istitle=True, log=False)

def plot_ovs_througput():
    ovs = [7031046, 12147309, 15255833, 15314143, 15415806, 15338417, 15249433]
    y1 = [4589658, 9080572, 12976244, 15331200, 15376621, 15273061, 15368014]
    y2 = [5468704, 8847788, 13174371, 15172765, 15072722, 15211493, 15224551]
    es = [4903647, 8819947, 12796050, 14887745, 15175457, 15248267, 15523233]

    s1 = 18743725
    s2 = 29868006
    s1 = 7031046 * s1 // (7031046+s1)
    s2 = 7031046 * s2 // (7031046+s2)

    print(s1)
    print(s2)

    y3 = []
    y4 = []

    x = ovs[0]
    y = y1[0]
    z1 = (s1 - y)/(x-y)
    x = ovs[0]
    y = y2[0]
    z2 = (s2 - y)/(x-y)
    print(z1)
    print(z2)
    # return

    for i in range(7):
        x = ovs[i]

        y = y1[i]
        y3.append(int(y1[i]+z1*(x-y)))

        y= y2[i]
        y4.append(int(y2[i]+z2*(x-y)))

    # y = [ovs, y1, y2, es]
    y = [ovs, y1, y2, y3,y4]
    for l in y:
        for i, n in enumerate(l):
            l[i] = n / (1 << 20)
        print(l)
    draw_line(x=list(range(7)), y_list=y,
              label_list=["OVS", "OVS w/ TM-SALFI(w/ ringbuffer)", "OVS w/ TM-SALFM(w/ ringbuffer)", "OVS w/ TM-SALFI(w/o ringbuffer)", "OVS w/ TM-SALFM(w/o ringbuffer)"],
              xticks_label=[i for i in range(1, 8)], yticks_labels=None,
              color_list=['g','darkslategrey','maroon','teal','r'], marker_list=['x','o','o', 'D', 'D'],
              xlimit=[0, 6], ylimit=None,
              xlabel="# threads", ylabel="Througput (Mpps)",
              figsize=(8, 4.5), title="OVS Througput",
              save_name="OVS Througput", no=0, istitle=True, log=False)


def plot_cpu_througput():
    # draw_bar_no_cmp(x=list(range(3)), y=[18743725 / (1 << 20), 29868006 / (1 << 20), 12886181 / (1 << 20)],
    #                 xlimit=[-1, 3], ylimit=[0, 32], xticks_label=["TM-SALFI", "TM-SALFM", "ES-Sketch"],
    #                 xlabel="", ylabel="Througput (Mpps)",
    #                 figsize=(9, 4.5), title="CPU Througput",
    #                 save_name="CPU Througput", no=0, sci=False, istitle=True, log=False)
    draw_bar_no_cmp(x=list(range(2)), y=[18743725 / (1 << 20), 29868006 / (1 << 20)],
                    xlimit=[-1, 2], ylimit=[0, 32], xticks_label=["TM-SALFI", "TM-SALFM"],
                    xlabel="", ylabel="Througput (Mpps)",
                    figsize=(9, 4.5), title="CPU Througput",
                    save_name="CPU Througput", no=0, sci=False, istitle=True, log=False)


def plot_FCM():
    # y1 = [2.24506,0.110436,0.053602,0.032409,0.020777,0.015247,0.011726,0.008735,0.008335]
    y2 = [0.266668, 0.111499, 0.0546132, 0.0328845, 0.021197, 0.015441, 0.0117294, 0.0095585, 0.0071838]
    y3 = [0.279744, 0.092865, 0.036217, 0.016989, 0.009888, 0.005736, 0.003861, 0.002912, 0.002411]
    y4 = [0.745675, 0.294256, 0.130666, 0.068580, 0.039870, 0.027187, 0.020761, 0.013534, 0.009774]
    draw_line(x=list(range(9)), y_list=[y2, y3, y4],
              label_list=["TM-SALFI w FCM (2-Tree)", "TM-SALFI w FCM (3-Tree)", "TM-SALFI w CM (3-Array)"],
              xticks_label=["%.1f" % i for i in mem_list][:9], yticks_labels=None,
              color_list=color_list, marker_list=marker_list,
              xlimit=[0, 8], ylimit=None,
              xlabel="Total Memory (MB)", ylabel="ARE",
              figsize=(8, 4.5), title="Flow Size Measurement",
              save_name="FCM ARE", no=0, istitle=True, log=True)


def plot_loss():
    y1 = [0.299602, 0.134841, 0.073425, 0.044674, 0.027930, 0.020366, 0.014433, 0.011582, 0.008377]
    y2 = [0.306874, 0.155692, 0.098091, 0.069540, 0.053232, 0.045244, 0.039014, 0.035697, 0.032587]
    y3 = [0.319386, 0.185655, 0.132522, 0.105399, 0.089653, 0.081919, 0.075323, 0.071045, 0.067013]
    y4 = [0.342807, 0.226445, 0.181412, 0.156417, 0.140465, 0.133623, 0.126287, 0.121463, 0.118710]
    y5 = [0.369005, 0.271264, 0.226821, 0.206007, 0.192383, 0.182920, 0.176126, 0.172612, 0.167858]
    draw_line(x=list(range(9)), y_list=[y1, y2, y3, y4, y5],
              label_list=["0%", "2%", "5%", "10%", "15%"],
              xticks_label=["%.1f" % i for i in mem_list][:9], yticks_labels=None,
              color_list=color_list, marker_list=marker_list,
              xlimit=[0, 8], ylimit=[0,0.4],
              xlabel="Total Memory (MB)", ylabel="ARE",
              figsize=(8, 4.5), title="Effect of Packet Loss Rate on FSM",
              save_name="TM-SALFM Loss Effect", no=0, istitle=True, log=False)

def plot_extra():
    draw_bar_no_cmp(x=list(range(3)), y=[8352, 7816, 7190],
                    xlimit=[-1, 3], ylimit=[0,9000], xticks_label=["Access", "Merge", "Core"],
                    xlabel="Node", ylabel="Packets",
                    figsize=(9, 4.5), title="Extra Packets of TM-SALFM",
                    save_name="TM-SALFM Extra Packets", no=0, sci=False, istitle=True, log=False)

if __name__ == '__main__':
    # polt_part_node()
    # plot_ovs_througput()
    # plot_cpu_througput()
    # plot_FCM()
    # plot_loss()
    plot_extra()
