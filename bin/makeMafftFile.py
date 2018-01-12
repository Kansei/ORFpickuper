#!/usr/bin/env python

# 複数のfastaファイルを結合し、一つのfastaファイルを作成する

import sys

argvs = sys.argv
argc = len(argvs)

if (argc < 4):
    print('Usage: # makeMafftFile.py output.fa input_1.fa input_2.fa (input_3.fa ...)')
    quit()

fo = open(argvs[1],'w')

for i in range(argc-2):
    fi = open(argvs[i+2],'r')
    reader = fi.read()
    fo.write(reader)
    fi.close()
