#!/usr/bin/env python

import sys
import re
import math
import numpy as np
from matplotlib import pyplot
from weightMatrixList import *


class Atgc:
    list = ["A","T","G","C"]

    dict ={"A":np.array([[1.0,0.0,0.0,0.0]]),
        "T":np.array([[0.0,1.0,0.0,0.0]]),
        "G":np.array([[0.0,0.0,1.0,0.0]]),
        "C":np.array([[0.0,0.0,0.0,1.0]])
        }

    freq = {"A":0,
            "T":0,
            "G":0,
            "C":0
            }

gAtgc = Atgc()

g_zero = 10**-8


def myConSeq(con):
    seq = ["." for x in range(con.len)]
    w = con.weight
    column,row = np.where(w == 1.0)
    for x in range(column.shape[0]):
        i = column[x]
        j = row[x]
        seq[i] = gAtgc.list[j]
        con.sequence = "".join(seq)

def convertWeight(con):
    con.weight[con.weight == 0.0] = g_zero


def whereConSeq(con,seq):
    l = len(con.sequence)
    temp = 0
    tmp_seq = seq

    while(1):
        match = re.search(con.sequence,tmp_seq)
        if None == match:
            break

        conSeqSite = match.start()
        con.c_site.append(conSeqSite + temp)
        newSeqStart = conSeqSite + l
        tmp_seq = tmp_seq[newSeqStart:]
        temp = newSeqStart + temp

def frequency(seq):
    for key in gAtgc.freq.keys():
        gAtgc.freq[key] = seq.count(key)/len(seq)

def logLikelihood(con,seq):
    for con_site in con.c_site:
        m = 0.0
        tmp_seq = seq[con_site:con_site + con.len]

        for sj in range(len(tmp_seq)):
            j_atgc = tmp_seq[sj]
            q = np.dot(con.weight[sj],gAtgc.dict[j_atgc].T)

            # q = f/con.len
            p = gAtgc.freq[j_atgc]

            # m += math.log((q*con.prob)/p)
            m += math.log(q/p)

        con.score.append(m)
        con.i_site.append(con_site + con.intron)

def findSpliceSite(cons,seq):
    for con in cons:
        myConSeq(con)
        convertWeight(con)
        whereConSeq(con,seq)
        logLikelihood(con,seq)


def pointScore2(cons):

    x = []
    y = []

    for con in cons:
        x.extend(con.i_site)
        y.extend(con.score)

    pyplot.scatter(x, y,label = '%d end'%(cons[0].end))

    pyplot.xlabel('base-pair')
    pyplot.ylabel('score')

    pyplot.legend()
    pyplot.show()


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)

    pro_name = argvs[0].split("/")[-1]

    if (argc != 2):   # 引数が足りない場合は、その旨を表示
        print('Usage: %s input.fa'%(pro_name))
        quit()         # プログラムの終了

    fi = open(argvs[1],'r')
    title = fi.readline()
    seq = fi.read().replace("\n","")
    fi.close()

    frequency(seq)
    findSpliceSite(con5,seq)
    findSpliceSite(con3,seq)

    for con in con5:
        print(con.c_site)

    pointScore2(con5)
    pointScore2(con3)
