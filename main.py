# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 17:23:27 2024

@author: mamin
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 12:00:45 2024

@author: mamin
"""

import numpy as np
import pandas as pd

import CCT

import itertools

N=3

#Initialize dataset
RankList=np.zeros((6,6*N+20))

data=pd.read_csv("testdata.csv",header=0)
RankList=np.array(data.values[0::,0::])
TeamList=np.zeros((N,6))

for i in range(N):
    TeamList[i]=np.arange(6*i+1, 6*i+7)
TargTeam=np.array(range(6*N+1,6*N+21))

#Cut off the last 6 Numbers
IniSc=np.sum(RankList[::,6*N:6*N+20],axis=0)
IniSc2=np.sort(IniSc)
TargTeam2=[]
for x in TargTeam:
    if IniSc[x-6*N-1] not in IniSc2[-6::]:
        TargTeam2.append(x)

#Sommon the combinations and compute
A=CCT.EvalScore(RankList)
y=list(itertools.combinations(TargTeam2, 6))
r=[]
for x in y:
    r.append(A.medals(list(x)))

#Output
maxM=max(r)
rslt=[]
for i in range(np.size(r,0)):
    if r[i]==maxM:
        rslt.append(y[i])
with open("results.txt","w") as file:
    file.write("Max Medal amount: "+str(maxM)+'\n')
    file.write("Best Choice: "+str(rslt))
