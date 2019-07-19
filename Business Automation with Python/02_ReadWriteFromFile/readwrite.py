import os

def readcfg(config):
    items = []
    if os.path.isfile(config):
        cfile = open(config, 'r') # opening file in read mode 
        #reading it line by line 
        for line in cfile.readlines():
            items.append(parsecfgline(line)) # each line is parsed
        cfile.close()
    return items # results of parsed lines are returned
    
 #Creating function that parses each line 

def parsecfgline (line):
    #options kept in dictionary
    option = {}
    if '|' in line:
        opts = line.split('|')
        if len(opts) ==3:
               #separate and identify each option
            option['origin']=extcheck(opts[0],0)
            option['exclude']=extcheck(opts[0],1)
            option['dest']=opts[1]
            option['dest']=opts[2].replace('\n','')
    return option

#exclude files check        
def extcheck (opt,idx):
    res=''
    if ';' in opt:
        opts = opt.split(';')#separator
        if len(opts) == 2:
            res = opts[0] if idx == 0 else opts [1]
    elif idx == 0:
        res = opt
    return res

opts = readcfg(os.path.splitext(os.path.basename(__file__))[0] + '.ini')

for opt in opts:
    print(opt)

