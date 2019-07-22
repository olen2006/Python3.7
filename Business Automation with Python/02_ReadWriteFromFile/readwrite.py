import os

def readcfg(config):
    items = []
    if os.path.isfile(config):
        cfile = open(config, 'r')
        for line in cfile.readlines():
            items.append(parsecfgline(line))
        cfile.close()
    return items

def parsecfgline(line):
    option = {}
    if '|' in line:
        opts = line.split('|')
        if len(opts) == 3:
            option['origin'] = extcheck(opts[0], 0)
            option['exclude'] = extcheck(opts[0], 1)
            option['dest'] = opts[1]
            option['type'] = opts[2].replace('\n', '')
    return option

def extcheck(opt, idx):
    res = ''
    if ';' in opt:
        opts = opt.split(';')
        if len(opts) == 2:
            res = opts[0] if idx == 0 else opts[1]
    elif idx == 0:
        res = opt
    return res

opts = readcfg(os.path.splitext(os.path.basename(__file__))[0] + '.ini')

for opt in opts:
    print(opt)