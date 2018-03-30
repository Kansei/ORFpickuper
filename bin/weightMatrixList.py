import numpy as np

class Weight_matrix:
    def __init__(self,end,intron):
        self.end = int(end) #5or3
        self.intron = int(intron) #イントロンの始まり/終わり地点

    weight = [] #重み行列

w_5ss1 = Weight_matrix(5,1)
w_5ss1.weight = np.array([
[1,0,0,0],
[0,0,1,0],
[0.5,0,0,0.5],
[0.2,0.7,0,0.1],
])

w_3ss1 = Weight_matrix(3,2)
w_3ss1.weight = np.array([
[1,0,0,0],
[0,0,1,0],
[0.5,0,0,0.5],
[0.2,0.7,0,0.1],
])
