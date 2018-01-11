# fastaファイルを読み込み、指定された塩基数から塩基数までの塩基配列を取り出し、新たなfastaファイルを作る。

import sys

argvs = sys.argv
argc = len(argvs)

if (argc != 4):
    print('Usage: # python %s input.fa from(int) to(int)'% argvs[0])
    quit()

fi = open(argvs[1],'r')
title = fi.readline()
lines = fi.read().replace("\n","")
fi.close()



output = argvs[1].split("fa")[0]+"from_"+argvs[2]+"_to_"+argvs[3]+".fa"

fo = open(output,'w')

from_num = int(argvs[2]) - 1
to__num = int(argvs[3])

title_list = title.split(":")
title_list[4] = str(from_num)
title_list[5] = str(to__num)

for x in title_list:
    fo.write( x + ":")

num = to__num - from_num

extract = lines[from_num:to__num]

extract_list = [extract[i: i+60] for i in range(0, len(extract), 60)]

for x in extract_list:
    fo.write( x + "\n")

fo.close()
