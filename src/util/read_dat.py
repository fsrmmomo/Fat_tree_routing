import struct



def read_dat():
    """
    通用的读取dat文件的方法
    :return:
    """
    # rf = '../../data/dat/notime/slice/1-access1.dat'
    rf = '../../data/dat/flag_dat/slice/5-access1.dat'

    x = 0
    src_set = dict()
    trace_byte_size = 16
    with open(rf, 'rb') as f:
        bin_trace = f.read(trace_byte_size)

        while bin_trace:
            # hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
            # src_ip =int.from_bytes(hex_trace[0:4],'big')
            hex_trace = struct.unpack("HBBBBHBBBBHBB", bin_trace)
            src_ip =int.from_bytes(bin_trace[2:6],'big')
            src_set[src_ip] = []
            # print(src_ip)
            # print(hex_trace)
            bin_trace = f.read(trace_byte_size)
            x += 1
            # if x > 100:
            #     break
        print(x)
        print(len(src_set))
def read_dat2():
    """
    通用的读取dat文件的方法
    :return:
    """
    rf = '../../data/dat/notime/slice/1-access1.dat'
    # rf = '../../data/dat/flag_dat/slice/1-access1.dat'

    x = 0
    src_set = dict()
    trace_byte_size = 15
    with open(rf, 'rb') as f:
        bin_trace = f.read(trace_byte_size)

        while bin_trace:
            # hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
            # src_ip =int.from_bytes(hex_trace[0:4],'big')
            hex_trace = struct.unpack("HBBBBHBBBBHB", bin_trace)
            src_ip =int.from_bytes(bin_trace[2:6],'big')
            src_set[src_ip] = []
            # print(src_ip)
            # print(hex_trace)
            bin_trace = f.read(trace_byte_size)
            x += 1
            # if x > 100:
            #     break
        print(x)
        print(len(src_set))

if __name__ == '__main__':
    read_dat()
    # read_dat2()