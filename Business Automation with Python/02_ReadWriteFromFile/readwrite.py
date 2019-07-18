import os

def readcfg(config):
    items = []
    if os.path.isfile(config):
        cfile = open(config, 'r') # opening file in read mode 
        #reading it line by line 
        for line in cfile.readlines():
            items.append(parseconfigline(line)) # each line is parsed
        cfile.close()
    return items # results of parsed lines are returned
    #