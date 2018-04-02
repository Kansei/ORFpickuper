import numpy as np

class ConSeqData:
    sequence = ""
    c_site = []
    i_site = []
    score = []
    def __init__(self,len,intron,weight):
        self.len = len
        self.intron = intron #イントロンの始まり/終わり地点
        self.weight = weight #重み行列

w5 = []
w3 = []
