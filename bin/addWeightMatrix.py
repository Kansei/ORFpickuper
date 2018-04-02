#!/usr/bin/env python

import sys

def myread(f):
    return f.readline().rstrip('\r\n')

if __name__ == '__main__':
    argvs = sys.argv  # コマンドライン引数を格納したリストの取得
    argc = len(argvs) # 引数の個数

    if(argc != 2):   # 引数が足りない場合は、その旨を表示
        print('Usage: # addWeightMatrix.py inputlist.txt')
        quit()         # プログラムの終了


    fr = open(argvs[1],'r')

    path = argvs[1].split("/")
    path = "/".join(path[:-1])

    fa = open("%s/weightMatrixList.py"%(path),'a')

    line = myread(fr)

    while line[0] == "#":
        line = fr.readline()

    while line:

        #読み込み
        len = myread(fr)
        end = myread(fr)
        intron = myread(fr)
        weight = [0 for i in range(int(len))]
        for i in range(int(len)):
            weight[i] = myread(fr)
        line = fr.readline()

        #書き込み
        fa.write("w%s.append(ConSeqData(%s,%s,\n"%(end,len,intron))
        fa.write("np.array([\n")
        for i in range(int(len)):
            fa.write("[%s],\n"%(weight[i]))
        fa.write("])\n")
        fa.write("))\n\n")

    fr.close
    fa.close
