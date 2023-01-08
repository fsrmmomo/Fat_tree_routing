import hashlib
import math
from statistics import mean
import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb

ww = 1600
hh = 8
NN = 10000


class Hash:
    w = 1600
    h = 8
    array = None
    collision = 0
    nc = 0

    def __init__(self, w=1600, h=8):
        self.w = w
        self.h = h
        self.array = [[0 for _ in range(w)] for _ in range(h)]

    def insert(self, key):
        index = hash(key) % self.w
        for i in range(self.h):
            if self.array[i][index] == 0:
                self.array[i][index] = key
                self.nc += 1
                return
            if self.array[i][index] == key:
                # self.nc += 1
                return
        self.collision += 1

    def clear(self):
        self.array = [[0 for _ in range(self.w)] for _ in range(self.h)]
        self.collision = 0
        self.nc = 0

    def test_collision(self, n=10000, salt=""):
        c = []
        for x in range(10):
            self.clear()
            for i in range(n):
                self.insert(str(i))
            # print(self.nc/ n)
            # print(self.collision / n)
            c.append(self.collision / n)
        # print(self.nc / n)
        print(mean(c))
        return mean(c)


def cal(w=1600, h=8, N=10000):
    P = 1
    x = N / w
    for i in range(h + 1):
        P -= math.pow(math.e, -x) * (math.pow(x, i) / math.factorial(i))
    # print(P)
    return P


def cal2(w=1600, h=8, N=10000):
    y1 = 0
    y2 = 0
    y3 = 0
    x = N / w
    for i in range(h):
        y1 += h* PP(i)
    for i in range(h-1):
        y2 += x*PP(i)
    # y2 *= x
    # y2 = x * PP(h - 1)
    y3 = x

    cc = (y1 - y2 + y3 - h) * w
    print(cc / N)

    z1 = 1
    z2 = 1
    for i in range(h-1):
        z1 -= PP(i)
    z1 *= x

    for i in range(h):
        z2 -= PP(i)
    z2 *= h


    # print(z1)
    # print(z2)
    # print(z1-z2)
    # print((z1-z2)*w/N)
    return (z1-z2)*w/N


def coll_prob():
    pass


def cal3(w=1600, h=8, N=10000):
    P = 1
    p = 1/w
    for i in range(h+1):
        P -= comb(N,i)*math.pow(p,i)*math.pow(1-p,N-i)
    print(P)

def PP(i,w=1600, h=8, N=10000):
    x = NN / ww
    return math.pow(math.e, -x) * (math.pow(x, i) / math.factorial(i))


if __name__ == '__main__':
    # for i in range(10):
    #     print(hash(str(i)))

    hash1 = Hash(ww, hh)
    # hash1.test_collision(NN)
    # cal(ww, hh, NN)
    # cal2(ww, hh, NN)
    # cal3(ww, hh, NN)

    # nlist = [1000*i for i in range(1,11)]
    #
    # r_list = []
    # for n in nlist:
    #     r_list.append(hash1.test_collision(n)*100)

    # hash1.test_collision(ww*hh//10)
    # hash1.test_collision(ww*hh//100)
    # plt.figure(num=0, figsize=(8, 4.5), dpi=300)
    # ax = plt.gca()
    # # ax.ticklabel_format(style='sci', scilimits=(0, 0), axis='y', useMathText=True)
    # # plt.yscale('log')
    # for x, y in zip(nlist, r_list):
    #     ax.text(x, y, '%.2f' % y, fontdict={'fontsize': 14})
    # plt.ylim(0, 10)
    # plt.xlim(0, 11000)
    # plt.plot(nlist, r_list,marker="o")
    # plt.ylabel("collision percentage")
    # plt.xlabel("flow num")
    # plt.show()

    x = [0.01*(i+1) for i in range(1,50+1)]

    c1_r = []
    c2_r = []
    # for i in x:
    #     c1_r.append(cal(16000, 8, int(16000*8*i)))
    #     c2_r.append(cal2(16000, 8, int(16000*8*i)))

    ww = int(1E6)
    hh = 8
    NN = int(ww*hh*0.1)

    ww = int(1E5)
    hh = 1
    NN = int(ww*hh)
    # ww = 1600
    # hh = 8
    # NN = 6643
    print(cal(ww, hh, NN))
    print(cal2(ww, hh, NN))
    hash1 = Hash(ww, hh)
    hash1.test_collision(NN)
    # NN = int(ww*hh*0.01)
    # print(cal(ww, hh, NN))
    # print(cal2(ww, hh, NN))


    # cal(16000, 8, 16000*8//10)
    # cal(16000, 8, 16000*8//10)
    # cal(16000, 8, 16000*8//100)
