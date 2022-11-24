from  util.utils import *

def gen():
    '''
    生成交换机与id的对应文件
    :return:
    '''

    index = 1

    mapping_list = []
    s_list = []
    for i in range(4):
        s = "core" + str(i) + " "+ str(index)
        s_list.append(s)
        index += 1
    for i in range(8):
        s = "merge" + str(i) + " "+ str(index)
        s_list.append(s)
        index += 1
    for i in range(8):
        s = "access" + str(i) + " "+ str(index)
        s_list.append(s)
        index += 1

    plain_write("../../conf/mapping",s_list)

if __name__ == '__main__':
    gen()