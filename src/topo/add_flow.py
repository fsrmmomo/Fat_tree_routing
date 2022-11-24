#!/usr/bin/python3
import os
import sys

with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        line = line[:-1]
        arr = line.split(' ')
        for i in range(len(arr)-3):
            out_port = "%c%c_%c%c" % (arr[i][0], arr[i][-1], arr[i+1][0], arr[i+1][-1])
            cmd = "docker exec %s ovs-ofctl add-flow br0 ip,nw_src=%s,nw_dst=%s,actions=output:%s" % (arr[i], arr[-2], arr[-1], out_port)
            print(cmd)
            os.system(cmd)
