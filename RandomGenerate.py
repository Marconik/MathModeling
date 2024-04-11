# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 00:10:17 2024

@author: mamin
"""

import numpy as np
import pandas as pd

N=3

RankList=np.zeros((6,6*N+20))
n=np.arange(1,6*N+21)
for i in range(6):
    RankList[i]=np.random.permutation(n)
    
dataframe=pd.DataFrame(RankList)

dataframe.to_csv("testdata.csv",index=False)