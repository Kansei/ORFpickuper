import sys
import json
import math
import numpy as np
from matplotlib import pyplot

def dot_plot(l, score_cut):
    # グラフの軸
    pyplot.xlabel('Query-base')
    pyplot.ylabel('Hit-base')

    for i in range(l):
        score = int(json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['hsps'][i]['score'])
        if score >= score_cut:
            query_from = int(json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['hsps'][i]['query_from'])
            query_to = int(json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['hsps'][i]['query_to'])
            hit_from = int(json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['hsps'][i]['hit_from'])
            hit_to = int(json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['hsps'][i]['hit_to'])
            print("===============")
            print(score)
            print(query_to)
            print(query_from)
            print(hit_to)
            print(hit_from)
            pyplot.plot([query_from, query_to],[hit_from, hit_to], color="royalblue")

    pyplot.show()

def score_rank_plot(l, score_cut):
    # グラフの軸
    pyplot.xlabel('Rank')
    pyplot.ylabel('Score')

    for i in range(l):
        score = int(json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['hsps'][i]['score'])
        if score >= score_cut:
            pyplot.bar(i,score, color="royalblue")

    pyplot.show()


argvs = sys.argv  # コマンドライン引数を格納したリストの取得
argc = len(argvs) # 引数の個数

if (argc < 4):   # 引数が足りない場合は、その旨を表示
    print('Usage: # python %s input-file dot/score num (score)'% argvs[0])
    quit()         # プログラムの終了

f = open(argvs[1], 'r')
json_dict = json.load(f)

plot_type = argvs[2]

num = int(argvs[3])-1

score_cut = 0
if len(argvs) == 5:
    score_cut = int(argvs[4])

#グラフタイトル
hit_cs = json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['description'][0]['title']
arr = argvs[1].split("/")
title = arr[len(arr)-1].replace(".json"," ")+"Genome Graph\n"+hit_cs+"\n"
pyplot.title(title)

l = len(json_dict['BlastOutput2']['report']['results']['search']['hits'][num]['hsps'])

if 'dot' == plot_type:
    dot_plot(l, score_cut)
elif 'score' == plot_type:
    score_rank_plot(l, score_cut)
else:
    print("Only dot or score")
    quit()

f.close
