#!/usr/bin/env python

import sys
import re
import math
import numpy as np
from weightMatrixList import *

class ATGC:
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

atgc = ATGC()

zero = 10**-8


def myConSeq(con):
    seq = ["." for x in range(con.len)]
    w = con.weight
    column,row = np.where(w == 1.0)
    for x in range(column.shape[0]):
        i = column[x]
        j = row[x]
        seq[i] = atgc.list[j]
        con.sequence = "".join(seq)


def convertWeight(con):
    con.weight[con.weight == 0.0] = zero


def whereConSeq(con,seq):
    l = len(con.sequence)
    temp = 0
    t_seq = seq

    while(1):
        match = re.search(con.sequence,t_seq)
        if None == match:
            break

        conSeqStart = match.start()
        con.c_site.append(conSeqStart + temp)
        newSeqStart = conSeqStart + l
        temp = newSeqStart + temp
        t_seq = t_seq[newSeqStart:]


def frequency(seq):
    for key in atgc.freq.keys():
        atgc.freq[key] = seq.count(key)/len(seq)
    print(atgc.freq)

def logLikelihood(con,seq):
    for i in range(len(con.c_site)):
        m = 0.0
        site = con.c_site[i]
        p_seq = seq[site:site+con.len]

        for j in range(len(p_seq)):
            j_atgc = p_seq[j]
            f = np.dot(con.weight[j],atgc.dict[j_atgc].T)
            q = f/con.len
            p = atgc.freq[j_atgc]

            m += math.log((q*con.prob)/p)
            # m += math.log(q/p)


        con.score.append(m)
        con.i_site.append(site + con.intron)
    print(con.score)


def findSpliceSite(cons,seq):
    for con in cons:
        myConSeq(con)
        convertWeight(con)
        whereConSeq(con,seq)
        logLikelihood(con,seq)


if __name__ == '__main__':
    argvs = sys.argv
    argc = len(argvs)

    p_name = argvs[0].split("/")[-1]

    if (argc != 2):   # 引数が足りない場合は、その旨を表示
        print('Usage: %s input.fa'%(p_name))
        quit()         # プログラムの終了

    fi = open(argvs[1],'r')
    title = fi.readline()
    seq = fi.read().replace("\n","")
    fi.close()

    frequency(seq)
    findSpliceSite(con5,seq)
    # findSpliceSite(con3,seq)
