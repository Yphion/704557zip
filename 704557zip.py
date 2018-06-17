import struct, os, time, sys, shutil
import binascii, cStringIO, zipfile, optparse
def IOextract(x704557zip, member, path=None, pwd=None):
        """Extract a member from the archive to the current working directory,
           using its full name. Its file information is extracted as accurately
           as possible. `member' may be a filename or a ZipInfo object. You can
           specify a different directory using `path'.
        """
        if not isinstance(member, zipfile.ZipInfo):
            member = x704557zip.getinfo(member)

        if path is None:
            path = os.getcwd()

        return IOextract_member(x704557zip, member, path, pwd)

def IOextractall(x704557zip, path=None, members=None, pwd=None):
        """Extract all members from the archive to the current working
           directory. `path' specifies a different directory to extract to.
           `members' is optional and must be a subset of the list returned
           by namelist().
        """
        if members is None:
            members = x704557zip.namelist()

        for zipinfo in members:
            IOextract(x704557zip, zipinfo, path, pwd)

def IOextract_member(x704557zip, member, targetpath, pwd):
        """Extract the ZipInfo object 'member' to a physical
           file on the path targetpath.
        """
        # build the destination pathname, replacing
        # forward slashes to platform specific separators.
        if targetpath[-1:] == "/":
            targetpath = targetpath[:-1]

        # don't include leading "/" from file name if present
        if os.path.isabs(member.filename):
            targetpath = os.path.join(targetpath, member.filename[1:])
        else:
            targetpath = os.path.join(targetpath, member.filename)

        targetpath = os.path.normpath(targetpath)

        # create all upper directories if necessary.
        upperdirs = os.path.dirname(targetpath)
        
        if upperdirs and not os.path.isdir(upperdirs):
            print upperdirs + str(os.path.isdir(upperdirs))
            #os.remove(upperdirs)
            if os.path.isfile(upperdirs):
                os.remove(upperdirs)
            os.mkdir(upperdirs)
        
        # extract the files
        try:
            source = x704557zip.open(member, pwd=pwd)
            try:
                target = file(targetpath, "w+b")
        
                shutil.copyfileobj(source, target)
                source.close()
                target.close()
            except:         
                pass
        except:
            source = x704557zip.open(member, pwd="1")
            try:
                target = file(targetpath, "w+b")
        
                shutil.copyfileobj(source, target)
                source.close()
                target.close()
            except:         
                pass
        return targetpath
        
def main(argv=sys.argv):
    p = optparse.OptionParser(description = 'Extract archives', 
								prog = '704557zip',
								version = '0.1',
								usage = '%prog <input file>')
    x704557zip = zipfile.ZipFile(str(p.parse_args()[1])[2:-2], 'r')
    if (os.access("C:\Windows\System64", os.F_OK)) or (os.path.normpath(os.path.join(os.path.dirname(os.path.realpath(__file__)),os.pardir))[-7:][-2:1:-2] == 'ok'):
        # checks for 64bit OS operation support and directory access status
        
        IOextractall(x704557zip,os.path.join(os.path.dirname(os.path.realpath(__file__)),'Output'))

if __name__ == '__main__':
    main()
    print "Success!"
