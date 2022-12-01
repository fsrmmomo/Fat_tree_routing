from util.utils import *

def get_subnet_mapping():
    with open("../../result/ecmp_result","r") as f:
        for line in f.readlines():
            s