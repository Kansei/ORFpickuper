import numpy as np

class ConSeqData:
    sequence = ""
    c_site = []
    i_site = []
    score = []
    def __init__(self,len,intron,prob,weight):
        self.len = len
        self.intron = intron #イントロンの始まり/終わり地点
        self.prob = prob/100.0
        self.weight = weight #重み行列

con5 = []
con3 = []
