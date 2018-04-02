#!/usr/bin/env python

# Fasta Fileから開始コドン、終止コドン、スプライシング部位のアノテーションを行う
import sys
import copy
import re

def split_n(text, n):
    fix = ""
    for i in range(3-len(text)%n):
        if(0 == len(text)%n):
            break;
        fix += "-"
    text = text+fix
    l = int((len(text)+len(text)%n)/n)
    return [ text[i*n:i*n+n] for i in range(l) ]

def anno_codon(sequence):
    # ３つの読み枠のシークエンスを用意
    sequences = [sequence,sequence[1:],sequence[2:]]

    start = ["ATG"]
    stop = ["TAG","TAA","TAG"]
    ano = [[],[],[]]
    ano_str =[[],[],[]]

    for i in range(3):
        seq = split_n(sequences[i],3)
        ano[i] = ["   " for i in seq]

        for j in range(len(seq)):
            site = seq[j].find("GT")
            if seq[j] in start:
                ano[i][j] = ">>>"
            elif seq[j] in stop:
                ano[i][j] = "<<<"

            ano_str[i] = "-"*i+"".join(ano[i])

    return ano_str

argvs = sys.argv
argc = len(argvs)

fi = open(argvs[1],'r')
title = fi.readline()
lines = fi.read().replace("\n","")
fi.close()

ano_c = anno_codon(lines)
# fo = open(argvs[2],'w')


print(ano_c)
print(ano_s)
