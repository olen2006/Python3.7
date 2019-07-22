import os, shutil,zipfile,time
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
        #for zipping
        zipf = startzip(options['dest'], options['type'])
        cmdfolder(zipf,options['origin'], options['dest'], options['type'], options['exclude'])
        if options['type'] == 'd':
            shutil.rmtree(options['origin'])
        endzip(zipf,options['type'])

def cmdfolder(zipf,origin,dest,opt,exc):
    for fld,sflds,fnames in os.walk(origin):
        #everything fls and sflds found in os.walk origin path is passed to func
        cmdfoldercore(zipf,fld,dest,opt,sflds,fnames,exc)


def cmdfoldercore(zipf,fld,dest,opt,sflds,fnames,exc):
    print('processing folder: ' + fld)
    cmdsubfolder(fld,opt,sflds) #part1
    cmdfiles(fld,dest,opt,fnames)

def cmdsubfolder(fld, opt,sflds):
    for sf in sflds:
        print('Processing subfolder: ' + sf + ' in ' + fld)

def cmdfiles(zipf,fld,dest,opt,fnames,exc):
    for fname in fnames:
        if not isexcluded(fname,exc):
            fn = os.path.join(fld,fname)
            if opt == 'c':
                filecopy(fname,fld,dest)
            elif opt == 'm':
                filemove(fname,fld,dest)
            elif opt == 'd':
                filedelete(fname,fld,dest)
            elif opt == 'z':
                filezip(zipf,fname,fld)

def filecopy(fname,fld,dest):
    fn = os.path.join(fld,fname)
    d = mergepaths(fld,dest)
    try:
        #check destination path and if not, then creat it.
        if not os.path.exists(d):
            os.makedirs(d)
        #copy files from origin to desitnation
        shutil.copy(fn,d)
    except err: #IOError as ioerr
        print('Error copying file: ' + fname + ' in ' + ' with exception ' + str(err))
    finally:
        print('Copied file: ' + fname + ' in ' + fld)

def filemove(fname,fld,dest):
    fn = os.path.join(fld,fname)
    d = mergepaths(fld,dest)
    try:
        #check destination path and if not, then creat it.
        if not os.path.exists(d):
            os.makedirs(d)
        #copy files from origin to desitnation
            shutil.move(fn,d)
    except ioerr: #IOError as ioerr
        print('Error moving file: ' + fname + ' in ' + ' with exception ' + str(ioerr))
    finally:
        print('Moved file: ' + fname + ' in ' + fld)

def filedelete(fname,fld,dest):
    fn = os.path.join(fld,fname)
    try:
        os.unlink(fn)
    except ioerr: #IOError as ioerr
        print('Error deleting file: ' + fname + ' in '  + fld)
    finally:
        print('Deleted file: ' + fname + ' in ' + fld)

#for zipping
def filezip(zipf,fname,fld):
    fn = os.path.join(fld,fname)
    try:
        zipf.write(fn)
    except:
        print('Error zipping file: ' + fname + ' in ' + fld)
    finally:
        print('Zipped file: ' + fname + ' in ' + fld)

#for zipping        
def adddttofilename(fname):
    datet = str(time.strftime("%Y%m%d - %H%M%S"))
    if '%%' in fname: 
        fname = fname.replace('%%', datet)
    return fname
#for zipping
def startzip(dest, opt):
	zipf = None
	if opt == 'z':
		zipf = zipfile.ZipFile(adddttofilename(dest), 'w', allowZip64=True)
	return zipf

#for zipping
def endzip(zipf, opt):
    if not zipf is None and opt == 'z':
        zipf.close()

#for excluding files with a specific extension 
def isexcluded(fname, excl):
    res = False
    lexc = excl.split(',')
    if len(lexc) > 0:
        if os.path.splitext(fname)[1] in lexc:
            res = True
    return res

#for ftp...
def ftpaction(opts):
    #todo...
	return

#for cfg script
def runall(): 
    cfg = os.path.splitext(os.path.basename('readwrite'))[0] + '.ini'
    items = readcfg(cfg)
    for item in items:
        if bool(item) is True:
            if item['type'] == 'f':
                ftpaction(item)
            else:
                fileaction(item)

#for cfg script
runall()

#cfg = os.path.splitext(os.path.basename('readwrite'))[0] + '.ini'
#fileaction(readcfg(cfg)[2]) #4 - delete option, 3 - move option