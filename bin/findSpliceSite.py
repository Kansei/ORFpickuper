#!/usr/bin/env python

import sys
import re
import math
import numpy as np
from matplotlib import pyplot as plt
from weightMatrixList import *

class Sequence:
    def __init__(self,name,seq):
        self.name = name
        self.seq = seq

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

def checkWeightMatrix(con):
    i = 0
    for row in con.weight:
        check = np.sum(row)
        # if(1.0 == check):
        #     print(row)
        # else:
        #     sys.stderr.write("This %d end WeightMatrix is wrong.\n"%(con.end))
        #     sys.stderr.write("%d row\n"%(i))
        # i += 1

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

def logLikelihood(con,seq,cut_score):
    for con_site in con.c_site:
        m = 0.0
        tmp_seq = seq[con_site:con_site + con.len]

        for sj in range(con.len):
            j_atgc = tmp_seq[sj]
            f = np.dot(con.weight[sj],gAtgc.dict[j_atgc].T)*100
            q = f/con.len
            p = gAtgc.freq[j_atgc]

            m += math.log(q/p)
            # m += math.log(q/p)

        m *= con.prob

        if m >= cut_score:
            # print(con.prob)
            con.score.append(m)
            con.i_site.append(con_site + con.intron)


def findSpliceSite(cons,seq, cut_score):
    for con in cons:
        # checkWeightMatrix(con)
        myConSeq(con)
        convertWeight(con)
        whereConSeq(con,seq)
        logLikelihood(con,seq,cut_score)


def pointScore(cons5,cons3):

    x_5, y_5 = joinListScore(cons5)
    x_3, y_3 = joinListScore(cons3)

    # printScoreAndSite(x_5,y_5)
    # printScoreAndSite(x_3,y_3)

    plt.scatter(x_5, y_5,label = '5 end')
    plt.scatter(x_3, y_3,label = '3 end')

    plt.xlabel('base-pair')
    plt.ylabel('score')

    plt.legend()
    plt.show()


def joinListScore(cons):
    x = []
    y = []

    for con in cons:
        x.extend(con.i_site)
        y.extend(con.score)

    return x,y

def printScoreAndSite(scores,sites):
    for score,site in scores,sites:
        print("==============")
        print("%d'end"%(con.end))
        print("score:%f"%(score))
        print("Intron Site:%f"%(site))

def divisionFileBySeq(file):
    file = fi.read().upper()
    tmp = file.split(">")[1:]
    Seq = [[] for _ in range(len(tmp))]

    for i,list in enumerate(tmp):
        file_list = list.split("\n")
        name = file_list[0]
        seq = "".join(file_list[1:])

        Seq[i] = Sequence(name, seq)

    return Seq

if __name__ == '__main__':

    argvs = sys.argv
    argc = len(argvs)

    pro_name = argvs[0].split("/")[-1]

    if (argc != 4):   # 引数が足りない場合は、その旨を表示
        print('Usage: %s input.fa cut_score(5) cut_score(3)'%(pro_name))
        quit()         # プログラムの終了

    fi = open(argvs[1],'r')

    Seq = divisionFileBySeq(fi)

    fi.close()

    # cut_score_5 = float(argvs[2])
    # cut_score_3 = float(argvs[3])
    #
    # frequency(seq)
    # findSpliceSite(con5,seq,cut_score_5)
    # findSpliceSite(con3,seq,cut_score_3)
    # pointScore(con5,con3)
