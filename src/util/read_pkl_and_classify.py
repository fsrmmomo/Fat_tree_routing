import errno
import os
import socket
import struct
import _pickle as cPickle
from sklearn.model_selection import train_test_split

from argparse import ArgumentParser
from collections import namedtuple
from typing import List, Dict
# from path_utils import get_prj_root
from datetime import datetime
import numpy as np
import joblib
from sklearn.ensemble import RandomForestClassifier  # 训练模型
import pandas as pd
import time
import threading
import pickle as pkl

model = None




def load_model():
    # 加载模型
    model_file_name = "../data/model/0.5s/random_forest0.01.pkl"
    with open(model_file_name, "rb") as fp:
        try:
            predict_model = cPickle.load(fp)
        except EOFError:
            print("模型为空")
    global model
    model = predict_model


def load_pkl():
    """
    加载feature并识别
    :return:
    """
    read_file_dir = "./feature/"
    write_file_dir = "./result/"
    for i in range(10):
        read_file = read_file_dir + str(i) + ".pkl"
        all_feature = []
        all_result = []
        with open(read_file,'rb') as rf:
            all_feature = pkl.load(rf)
        for d in all_feature:
            key_list = []
            feature_list = []
            x  = 0
            for k,v in d.items():
                key_list.append(k)
                feature_list.append(v)
                # if k==253:
                #     print(x)
                # x += 1
                # if x>300:
                #     break
            result_list = model.predict(feature_list)

            big_key = dict()
            for index,r in enumerate(result_list):
                if r == 1:
                    # print("big")
                    # print(key_list[index])
                    # print(feature_list[index][0])
                    big_key[key_list[index]] = 0
                # else:
                #     print("small")
                #     print(feature_list[index][0])
            print(len(big_key))
            print(len(key_list))
            print()
            all_result.append(big_key)

        write_file = write_file_dir + str(i) + ".pkl"
        with open(write_file,"wb") as wf:
            pkl.dump(all_result,wf)

def read_pkl():
    read_file = "./feature/0.pkl"

    with open(read_file,"rb") as rf:
        all_feature = pkl.load(rf)[0]
        print(all_feature[253])

if __name__ == '__main__':
    read_pkl()
    load_model()
    load_pkl()
