#!/usr/bin/env python

import sys
import json
import math
import numpy as np
from matplotlib import pyplot
from plot import Plot

if __name__ == '__main__':

    argvs = sys.argv  # コマンドライン引数を格納したリストの取得
    argc = len(argvs) # 引数の個数

    if (argc != 5):   # 引数が足りない場合は、その旨を表示
        print('Usage: # plotBlastn.py input.json dot/score num(int) cutting_score(int)')
        quit()         # プログラムの終了

    f = open(argvs[1], 'r')
    json_dict = json.load(f)

    plot_type = argvs[2]

    num = int(argvs[3])-1

    score_cut = int(argvs[4])

    #グラフタイトル
    hit_cs = json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['description'][0]['title']
    arr = argvs[1].split("/")
    title = arr[len(arr)-1].replace(".json"," ")+"Genome Graph\n"+hit_cs+"\n"
    pyplot.title(title)

    print(hit_cs)

    l = len(json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['hsps'])

    plot = Plot(l,score_cut,json_dict,num)

    if 'dot' == plot_type:
        plot.dot()
    elif 'score' == plot_type:
        plot.score_rank()
    else:
        print("Only dot or score")
        quit()

    f.close
