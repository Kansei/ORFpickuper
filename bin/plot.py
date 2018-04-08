import json
import math
import numpy as np
from matplotlib import pyplot

class Plot:
    def __init__(self,l,score_cut,json_dict,num):
        self.l = l
        self.score_cut = score_cut
        self.json_dict = json_dict
        self.num = num

    def dot(self):
        # グラフの軸
        pyplot.xlabel('Query-base')
        pyplot.ylabel('Hit-base')

        for i in range(self.l):
            score = int(self.json_dict['BlastOutput2']['report']['results']['search']['hits'][self.num]['hsps'][i]['score'])
            if score >= self.score_cut:
                query_from = int(self.json_dict['BlastOutput2']['report']['results']['search']['hits'][self.num]['hsps'][i]['query_from'])
                query_to = int(self.json_dict['BlastOutput2']['report']['results']['search']['hits'][self.num]['hsps'][i]['query_to'])
                hit_from = int(self.json_dict['BlastOutput2']['report']['results']['search']['hits'][self.num]['hsps'][i]['hit_from'])
                hit_to = int(self.json_dict['BlastOutput2']['report']['results']['search']['hits'][self.num]['hsps'][i]['hit_to'])

                print("score:{}".format(score))
                print("query from:%d  query to:%d"%(query_from,query_to))
                print("hit from:%d    hit to:%d"%(hit_from,hit_to))
                print("=======================")

                pyplot.plot([query_from, query_to],[hit_from, hit_to],label="score:{}".format(score))

        pyplot.legend()
        pyplot.show()

    def score_rank(self):
        # グラフの軸
        pyplot.xlabel('Rank')
        pyplot.ylabel('Score')

        for i in range(self.l):
            score = int(self.json_dict['BlastOutput2']['report']['results']['search']['hits'][self.num]['hsps'][i]['score'])
            if score >= self.score_cut:
                pyplot.bar(i,score, color="royalblue")

        pyplot.show()
