# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import traceback


"""
Convert the png or jpg whose size larger than the Specified(default is 50*1024) to webp
the have two parameter.The first argument is the directory ，the files in this directory will be converted
The Second parameter is the Specified Size ,and files larger than this size will be converted.
"""

def startWebp(soure_dir,size):
    """
    Convert the png or jpg whose size larger than the Specified(default is 50*1024) to webp
    :param soure_dir: the dir for png or jpg
    :param size: the Specified size
    :return:
    """
    webp_dir_50 = "./webp_50"
    webp_dir_75 = "./webp_75"
    webp_dir_95 = "./webp_95"
    webp_dir_lossless = "./webp_lossless"
    list_webp_dir = [webp_dir_50, webp_dir_75, webp_dir_95, webp_dir_lossless]

    for str in list_webp_dir:
        print "rm "
        os.system("rm -rf %s" % str)
        os.system("mkdir %s" % str)

    cwebp = "./cwebp"
    if(not os.path.isfile(cwebp)):
        cwebp = "cwebp"

    for f in os.listdir(soure_dir):
        if f[-4:] == ".png" or f[-4:] == ".jpg":
            if 6 < len(f) and f.endswith(".9.png"):
                print "NinePatch:",f
                continue
            if os.path.getsize(os.path.join(soure_dir, f)) < size:
                print "the file less than default:",f,os.path.getsize(os.path.join(soure_dir, f)),"   defaultSize:",size
                continue
            print f, len(f)
            qList = ["50", "75", "95"]
            for q in qList:
                print q, ":", list_webp_dir[qList.index(q)]
                command = cwebp+" -m 6 -q " + q + " " +f+ " -o " + \
                          os.path.abspath(list_webp_dir[qList.index(q)] + '/' +f[0:-4] + ".webp")
                subprocess.call(command, shell=True)
            commandlossless = cwebp+" -m 6 -q 100 " + "-lossless" + " " + f + " -o " + \
                              os.path.abspath(list_webp_dir[3] + '/' +f[0:-4] + ".webp")
            subprocess.call(commandlossless, shell=True)



if __name__ == "__main__":
    size = 50*1024
    if len(sys.argv) > 1:
        soure_dir = sys.argv[1]
        if len(sys.argv) > 2:
            try:
                size = float(sys.argv[2])*1024
            except ValueError, e:
                print "warn: The second argument must be a number"
                traceback.print_exc()
    else:
        print "error: please input the soure dir"
        sys.exit(1)
    startWebp(soure_dir,size)
