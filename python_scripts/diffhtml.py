import difflib
import sys

fromfile = "C:/Users/WillC/Desktop/20160622/a.txt"
tofile = "C:/Users/WillC/Desktop/20160622/b.txt"
fromlines = open(fromfile, 'U').readlines()
tolines = open(tofile, 'U').readlines()
diff = difflib.HtmlDiff().make_file(fromlines,tolines,fromfile,tofile)


outfile = "C:/Users/WillC/Desktop/20160622/out.html"

# s=open(outfile,'w')
# s.write(diff)
# s.close()

from filecmp import dircmp
import filecmp

def print_diff_files(dcmp):
    for name in dcmp.diff_files:
        print "diff_file %s found in %s and %s" % (name, dcmp.left,
              dcmp.right)
    for sub_dcmp in dcmp.subdirs.values():
        print_diff_files(sub_dcmp)

frm=       'C:/Users/WillC/Desktop/20160622/bd'
to=        'C:/Users/WillC/Desktop/20160622/ad'

dcmp = dircmp(frm, to)
print_diff_files(dcmp)
totaldiff=''
for cfile in dcmp.common_files:
    fromfile=frm+'/'+cfile
    tofile=to+'/'+cfile
    if not filecmp.cmp(fromfile,tofile):
        print 'writing',fromfile,tofile
        fromlines = open(fromfile, 'U').readlines()
        tolines = open(tofile, 'U').readlines()
        totaldiff= totaldiff +'\n' + difflib.HtmlDiff().make_file(fromlines, tolines, fromfile, tofile)


# print filecmp.dircmp.common_files(frm , to)
outfile = "C:/Users/WillC/Desktop/20160622/total_diffs.html"
s=open(outfile,'w')
s.write(totaldiff)
s.close()

