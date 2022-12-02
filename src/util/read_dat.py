import struct

trace_byte_size = 32

def read_dat():
    # rf = '../../data/dat/notime/slice/1-access1.dat'
    rf = '../../data/dat/time/20s/1.dat'

    x = 0
    src_set = dict()
    with open(rf, 'rb') as f:
        bin_trace = f.read(trace_byte_size)

        while bin_trace:
            hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
            src_ip =int.from_bytes(hex_trace[0:4],'big')
            # hex_trace = struct.unpack("HBBBBHBBBBHB", bin_trace)
            # src_ip =int.from_bytes(bin_trace[2:6],'big')
            src_set[src_ip] = []
            # print(src_ip)
            # print(hex_trace)
            print(hex_trace[-2])
            print(hex_trace[-1])
            bin_trace = f.read(trace_byte_size)
            x += 1
            if x > 100:
                break
        print(x)
        print(len(src_set))

if __name__ == '__main__':
    read_dat()