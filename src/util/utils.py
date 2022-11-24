import pickle as pkl


def pkl_write(filename, obj):
    with open(filename, 'wb') as f:
        pkl.dump(obj, f)


def pkl_read(filename):
    obj = None
    with open(filename, 'rb') as f:
        obj = pkl.load(f)
    return obj


def plain_write(filename, obj):
    with open(filename,'w') as f:
        if type(obj) == list:
            # f.writelines(obj)
            for o in obj:
                f.writelines(o)
                f.write("\n")
        else:
            f.write(obj)

def plain_read(filename):
    res = []
    with open(filename,'r') as f:
        for line in f.readlines():
            res.append(line)
    return res