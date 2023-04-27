import struct
import sys
import pickle as pkl


def time_dat_to_flag_dat_opt_opt():
    """
        将含时间戳的dat转换为不含时间戳但是包含大小流标记的dat数据，完美识别
        "BBBBHBBBBHBId"  to "HBBBBHBBBBHBB"
        :return:
        """

    # 0.5 一组进行切割，然后统计特征，进行识别
    read_file_dir = "../../data/dat/time/20s/"
    # write_file_dir = "../../data/dat/flag_dat/20s/"
    write_file_dir = "../../data/dat/nodelay/20s3/"
    big_key_dir = "../../data/dat/time/result1/"
    trace_byte_size = 32

    delay = 0.0
    for i in range(1):
        all_key = dict()
        print(i)
        T = 0.5
        t = T
        tmp_feature = dict()
        now_win = 0
        read_file = read_file_dir + str(i) + ".dat"

        # big_keys = dict()
        new_bin_list = []
        tmp_all = dict()
        tmp_big = dict()
        aa_big_key = dict()
        with open(read_file, 'rb') as rf:
            bin_trace = rf.read(trace_byte_size)
            while bin_trace:
                hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
                src_ip = int.from_bytes(bin_trace[0:4], 'big')
                # hex_trace = struct.unpack("HBBBBHBBBBHB", bin_trace)
                # src_ip = int.from_bytes(bin_trace[2:6], 'big')
                if src_ip in all_key.keys():
                    all_key[src_ip] += 1
                else:
                    all_key[src_ip] = 1
                bin_trace = rf.read(trace_byte_size)

            sort_list = []
            for k, v in all_key.items():
                sort_list.append([v, k])
            sort_list.sort(reverse=True)
            print(len(all_key))
            bb = len(all_key) // 15
            print(bb)
            print(sort_list[:bb])
            for tl in sort_list[:bb]:
                aa_big_key[tl[1]] = 0
            # return

        with open(read_file, 'rb') as rf:
            bin_trace = rf.read(trace_byte_size)

            while bin_trace:
                hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
                src_ip = int.from_bytes(bin_trace[0:4], 'big')
                # hex_trace = struct.unpack("HBBBBHBBBBHB", bin_trace)
                # src_ip = int.from_bytes(bin_trace[2:6], 'big')
                now_win += 1

                all_key[src_ip] = 0
                # all_key[src_ip] += 1

                tmp_all[src_ip] = 0

                if src_ip in aa_big_key:
                    flag = 1
                    tmp_big[src_ip] = 0
                else:
                    flag = 0

                new_bin = struct.pack("HBBBBHBBBBHBB", hex_trace[-2], bin_trace[0], bin_trace[1], bin_trace[2],
                                      bin_trace[3], hex_trace[4],
                                      bin_trace[5], bin_trace[6], bin_trace[7], bin_trace[8], hex_trace[9],
                                      hex_trace[-3], flag)
                # new_bin = struct.pack("HBBBBHBBBBHBB", hex_trace[0],  hex_trace[1], hex_trace[2],
                #                       hex_trace[3], hex_trace[4],
                #                       hex_trace[5], hex_trace[6], hex_trace[7], hex_trace[8],
                #                       hex_trace[9],hex_trace[10],hex_trace[11], flag)
                new_bin_list.append(new_bin)


                bin_trace = rf.read(trace_byte_size)

        print(len(all_key))
        write_file = write_file_dir + str(i) + ".dat"
        with open(write_file, "wb") as wf:
            for bin in new_bin_list:
                wf.write(bin)


def time_dat_to_flag_dat_opt():
    """
    将含时间戳的dat转换为不含时间戳但是包含大小流标记的dat数据,完美无时延
    "BBBBHBBBBHBId"  to "HBBBBHBBBBHBB"
    :return:
    """

    # 0.5 一组进行切割，然后统计特征，进行识别
    read_file_dir = "../../data/dat/time/20s/"
    # write_file_dir = "../../data/dat/flag_dat/20s/"
    write_file_dir = "../../data/dat/nodelay/20s2/"
    big_key_dir = "../../data/dat/time/result1/"
    trace_byte_size = 32

    delay = 0.0
    for i in range(1):
        all_key = dict()
        print(i)
        T = 0.5
        t = T
        tmp_feature = dict()
        now_win = 0
        read_file = read_file_dir + str(i) + ".dat"
        big_key_file = big_key_dir + str(i) + ".pkl"

        with open(big_key_file, "rb") as f:
            all_big_keys = pkl.load(f)

        big_key_index = 0
        # big_keys = dict()
        big_keys = all_big_keys[big_key_index]
        print(len(big_keys))
        new_bin_list = []
        tmp_all = dict()
        tmp_big = dict()
        with open(read_file, 'rb') as rf:
            bin_trace = rf.read(trace_byte_size)

            while bin_trace:
                hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
                src_ip = int.from_bytes(bin_trace[0:4], 'big')
                # insert(bin_trace, tmp_feature, now_win)
                now_win += 1

                all_key[src_ip] = 0

                tmp_all[src_ip] = 0

                if src_ip in big_keys:
                    flag = 1
                    tmp_big[src_ip] = 0
                else:
                    flag = 0
                # new_bin = struct.pack("IHIHBIB", int.from_bytes(bin_trace[0:4], 'big'), hex_trace[4],
                #                       int.from_bytes(bin_trace[6:10], 'big'), hex_trace[-4], hex_trace[-3],
                #                       hex_trace[-2],
                #                       flag)
                new_bin = struct.pack("HBBBBHBBBBHBB", hex_trace[-2], bin_trace[0], bin_trace[1], bin_trace[2],
                                      bin_trace[3], hex_trace[4],
                                      bin_trace[5], bin_trace[6], bin_trace[7], bin_trace[8], hex_trace[9],
                                      hex_trace[-3], flag)
                new_bin_list.append(new_bin)
                # print(len(new_bin))
                if hex_trace[-1] > t + delay:
                    t = t + T

                    if big_key_index == 40 - 1:
                        break
                    big_keys.update(all_big_keys[big_key_index + 1])
                    # print(len(big_keys))
                    # print("tmp")
                    # print(len(tmp_all))
                    # print(len(tmp_big))
                    # print()

                    tmp_big.clear()
                    tmp_all.clear()

                    big_key_index += 1

                bin_trace = rf.read(trace_byte_size)
        print(len(big_keys))
        print(len(all_key))
        write_file = write_file_dir + str(i) + ".dat"
        with open(write_file, "wb") as wf:
            for bin in new_bin_list:
                wf.write(bin)


def time_dat_to_flag_dat():
    """
    将含时间戳的dat转换为不含时间戳但是包含大小流标记的dat数据
    "BBBBHBBBBHBId"  to "HBBBBHBBBBHBB"
    :return:
    """

    # 0.5 一组进行切割，然后统计特征，进行识别
    read_file_dir = "../../data/dat/time/20s/"
    # write_file_dir = "../../data/dat/flag_dat/20s/"
    write_file_dir = "../../data/dat/nodelay/20s1/"
    big_key_dir = "../../data/dat/time/result1/"
    trace_byte_size = 32

    delay = 0.0
    for i in range(1):
        all_key = dict()
        print(i)
        T = 0.5
        t = T
        tmp_feature = dict()
        now_win = 0
        read_file = read_file_dir + str(i) + ".dat"
        big_key_file = big_key_dir + str(i) + ".pkl"

        with open(big_key_file, "rb") as f:
            all_big_keys = pkl.load(f)

        big_key_index = 0
        # big_keys = all_big_keys[big_key_index]
        big_keys = dict()
        print(len(big_keys))
        new_bin_list = []
        tmp_all = dict()
        tmp_big = dict()
        with open(read_file, 'rb') as rf:
            bin_trace = rf.read(trace_byte_size)

            while bin_trace:
                hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
                src_ip = int.from_bytes(bin_trace[0:4], 'big')
                insert(bin_trace, tmp_feature, now_win)
                now_win += 1

                all_key[src_ip] = 0

                tmp_all[src_ip] = 0

                if src_ip in big_keys:
                    flag = 1
                    tmp_big[src_ip] = 0
                else:
                    flag = 0
                new_bin = struct.pack("IHIHBIB", int.from_bytes(bin_trace[0:4], 'big'), hex_trace[4],
                                      int.from_bytes(bin_trace[6:10], 'big'), hex_trace[-4], hex_trace[-3],
                                      hex_trace[-2],
                                      flag)
                new_bin = struct.pack("HBBBBHBBBBHBB", hex_trace[-2], bin_trace[0], bin_trace[1], bin_trace[2],
                                      bin_trace[3], hex_trace[4],
                                      bin_trace[5], bin_trace[6], bin_trace[7], bin_trace[8], hex_trace[9],
                                      hex_trace[-3], flag)
                new_bin_list.append(new_bin)
                # print(len(new_bin))
                if hex_trace[-1] > t + delay:
                    t = t + T

                    if big_key_index == 40:
                        break
                    big_keys.update(all_big_keys[big_key_index])
                    # print(len(big_keys))
                    # print("tmp")
                    # print(len(tmp_all))
                    # print(len(tmp_big))
                    # print()

                    tmp_big.clear()
                    tmp_all.clear()

                    big_key_index += 1

                bin_trace = rf.read(trace_byte_size)
        print(len(big_keys))
        print(len(all_key))
        write_file = write_file_dir + str(i) + ".dat"
        with open(write_file, "wb") as wf:
            for bin in new_bin_list:
                wf.write(bin)


def dat_to_feature():
    """
     0.5s 一组进行切割，然后统计特征，在识别服务器进行识别
    :return:
    """
    read_file_dir = "../../data/dat/time/20s/"
    write_file_dir = "../../data/dat/time/feature/"
    trace_byte_size = 32

    for i in range(10):
        print(i)
        T = 0.5
        t = T
        tmp_feature = dict()
        features = []
        now_win = 0
        allpkts = 0
        allbytes = 0
        read_file = read_file_dir + str(i) + ".dat"

        all_feature = []
        with open(read_file, 'rb') as rf:
            bin_trace = rf.read(trace_byte_size)

            while bin_trace:
                hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
                insert(bin_trace, tmp_feature, now_win)
                now_win += 1
                allpkts += 1
                allbytes += hex_trace[-2]

                if hex_trace[-1] > t:

                    t += T
                    features.append(tmp_feature)
                    sort_list = []
                    for k, v in tmp_feature.items():
                        sort_list.append([k, v[0]])
                        v = f_to_instance(v, allbytes, allpkts)
                        tmp_feature[k] = v
                        if k == 253:
                            print(v[0])
                            print(tmp_feature[k][0])

                    sort_list.sort(reverse=True, key=lambda x: x[1])
                    print(sort_list[:100][0])
                    break
                    all_feature.append(tmp_feature)
                    tmp_feature = dict()

                    allpkts = 0
                    allbytes = 0
                    now_win = 0
                bin_trace = rf.read(trace_byte_size)

        write_file = write_file_dir + str(i) + ".pkl"
        # with open(write_file, "wb") as wf:
        #     print(len(all_feature))
        #     pkl.dump(all_feature, wf)
        # all_feature.clear()


#               0     1     2           3           4           5              6          7                 8         9         10      11          12      13
# feature = [总Bytes,包数, max bytes , min bytes, aver bytes, start windows,end win, windows size, time win size,  max twin, min twin, aver twin,dst port, src port]

def f_to_instance(f, all_bytes, all_pkts):
    """
    格式转换
    :param f:
    :param all_bytes:
    :param all_pkts:
    :return:
    """
    feature = f[:7]
    feature.append(f[6] - f[5])
    feature.append(f[8] - f[7])
    feature.append(f[9])
    feature.append(f[10])
    feature.append(f[11])

    feature.append(f[12])
    feature.append(f[13])

    feature[0] /= all_bytes
    feature[1] /= all_pkts
    feature[5] /= all_pkts
    feature[6] /= all_pkts
    feature[7] /= all_pkts

    return feature


#               0     1     2           3           4           5           6           7           8         9         10      11
# feature = [总Bytes,包数, max bytes , min bytes, aver bytes, start windows,end win, start time, end time, max twin, min twin, aver twin]
def read_pkl():
    read_file = "../../data/dat/time/feature/0.pkl"

    with open(read_file, "rb") as rf:
        all_feature = pkl.load(rf)[0]
        print(all_feature[253])


def insert(bin_trace, tmp_feature, now_win):
    hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
    key = int.from_bytes(bin_trace[0:4], 'big')
    length = hex_trace[-2]
    now_time = hex_trace[-1]

    if key in tmp_feature.keys():
        last_feature = tmp_feature[key]
        last_feature[0] += length
        last_feature[1] += 1
        last_feature[2] = max(last_feature[2], length)
        last_feature[3] = min(last_feature[3], length)
        last_feature[4] = ((last_feature[4] * (last_feature[1] - 1)) + length) / last_feature[1]
        last_feature[6] = now_win
        twin = now_time - last_feature[8]
        last_feature[8] = now_time
        last_feature[9] = max(twin, last_feature[9])
        last_feature[10] = min(twin, last_feature[10])
        last_feature[11] = ((last_feature[11] * (last_feature[1] - 2)) + twin) / (last_feature[1] - 1)
    else:
        # last_feature = [0 for _ in range(12)]
        last_feature = [0 for _ in range(14)]
        last_feature[0] += length
        last_feature[1] += 1
        last_feature[2] = length
        last_feature[3] = length
        last_feature[4] = length
        last_feature[5] = now_win
        last_feature[6] = now_win
        last_feature[7] = now_time
        last_feature[8] = now_time
        last_feature[10] = sys.maxsize

        last_feature[12] = int(hex_trace[4])
        last_feature[13] = int(hex_trace[9])
        tmp_feature[key] = last_feature


if __name__ == '__main__':
    # dat_to_feature()
    # read_pkl()
    time_dat_to_flag_dat_opt_opt()
    # time_dat_to_flag_dat_opt()
    # time_dat_to_flag_dat()
