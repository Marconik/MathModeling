#Compute the number of medals aff. to certain combination
import numpy as np
import math

class EvalScore:
    
    def __init__(self,ranklist):
        self.rk=ranklist
        self.totalnum=np.size(ranklist,1)
        self.teamnum=int((self.totalnum-20)/6)
        
    def DualList(self):
        #switch the rank and number
        A=np.zeros((6,self.totalnum)).tolist()
        for i in range(6):
            b=[0 for i in range(self.totalnum)]
            for j in range(self.totalnum):
                b[int(self.rk[i][j])-1]=j+1
            A[i]=b
        return np.array(A)
    
    def Localize(self,numberlist):
        #clear out the unexpected teammates
        A=self.DualList().tolist()
        B=np.zeros((6,6*(self.teamnum))).tolist()
        for i in range(6):
            b=[x for x in A[i] if x > 0 and x < 6*self.teamnum+1 or x in numberlist]
            B[i]=b
        return np.array(B)
    
    def scoreT(self,numberlist):
        #compute the scores per team
        A=self.Localize(numberlist).tolist()
        B=np.array(A)/6
        C=np.zeros((self.teamnum+1)).tolist()
        for i in range(6):
            for j in range(np.size(B,1)):
                x=math.floor(B[i][j])
                if x <= self.teamnum:
                    C[x-1]=C[x-1]+j
                else:
                    C[self.teamnum]=C[self.teamnum]+j
                    
        return np.array(C)
        
    def scoreP(self,numberlist):
        #compute the scores per person
        A=self.Localize(numberlist)
        C=np.zeros(6*(self.teamnum+1))
        for i in range(6):
            for j in range(6*(self.teamnum+1)):
                x=A[i][j]
                if x <= 6*self.teamnum:
                    C[x-1]=C[x-1]+j
                else:
                    y=np.where(numberlist==x)[0]+6*self.teamnum
                    C[y]=C[y]+j
                    
        return np.array(C)
    
    def medals(self,numberlist):
        #the total medal number
        A=self.Localize(numberlist)
        A1=A[0:6,0:3]
        t=0
        for i in range(6):
            for j in range(3):
                if A1[i][j]>6*self.teamnum:
                    t=t+1
        
        A2=self.scoreP(numberlist)
        B2=np.sort(np.unique(A2))[:3]
        C2=A2[6*self.teamnum:]
        for x in C2:
            if x in B2:
                t=t+1
                
        A3=self.scoreT(numberlist)
        B3=np.sort(np.unique(A3))[:3]
        if A3[-1] in B3:
            t=t+1
        return t
    
