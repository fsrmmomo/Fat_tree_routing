import struct

trace_byte_size = 32

def read_dat():
    rf = '../../data/dat/time/20s/1.dat'

    x = 0
    with open(rf, 'rb') as f:
        bin_trace = f.read(trace_byte_size)

        while bin_trace:
            hex_trace = struct.unpack("BBBBHBBBBHBId", bin_trace)
            src_ip =int.from_bytes(hex_trace[0:4],'big')
            # print(src_ip)
            # print(hex_trace)
            # print(hex_trace[-2])
            bin_trace = f.read(trace_byte_size)
            x += 1
            if x > 100:
                break

if __name__ == '__main__':
    read_dat()