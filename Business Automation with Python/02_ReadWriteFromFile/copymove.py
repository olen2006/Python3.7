import os, shutil

from readwrite import readcfg

#keeping part of the path from the origin path
#mergin path function is needed
def mergepaths (path1, path2):
    pieces = []
    parts1, tail1 = os.path.splitdrive(path1)
    parts2, tail2 = os.path.splitdrive(path2)
    result = path2
    parts1 = tail1.split('\\') if '\\' in tail1 else tail1.split('/')
    parts2 = tail2.split('\\') if '\\' in tail2 else tail2.split('/')
        for pitem in parts1:
            if pitem != '':
                if not pitem in parts2:
                    pieces.append(pitem)
        for piece in pieces:
            result = os.path.join(result,piece)
        return result

def fileaction(options):
    if len(options['type']) == 1:
        cmdfolder(options['origin'], options['dest'], options['type'])
        if options['type'] == 'd':
            shutil.rmtree(options['origin'])

def cmdfolder(origin,dest,opt):
    for fld,sflds,fnames in os.walk(origin):
        #everything fls and sflds found in os.walk origin path is passed to func
        cmdfoldercore(fld,dest,opt,sflds,fnames)

#part1
def cmdfoldercore(fld,dest,opt,sflds,fnames):
    print('processing folder: ' + fld)
    cmdsubfolder(fld,opt,sflds) #part1
    cmdfiles(fld,dest,opt,fnames)
#part1
def cmdsubfolder(fld, opt,sflds):
    for sf in sflds:
        print('Processing subfolder: ' + sf + ' in ' + fld)

def cmdfiles(fld,dest,opt,fnames):
    for fname in fnames:
        fn = os.path.join(fld,fname)
        if opt == 'c':
            filecopy(fname,fld,dest)
            elif opt == 'm':
                filemove(fname,fld,dest)
            elif opt == 'd':
                filedelete(fname,fld,dest)
def filecopy(fname,fld,dest):
    pass
    #...#









