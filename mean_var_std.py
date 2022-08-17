import re
from statistics import variance
import numpy as np 

def Calculate(list):
   
   if len(list)>9:
    print("Out of Range")
   else : 
     a=np.reshape(list ,(3,3))
   mean=(np.mean(a,axis=0),np.mean(a,axis=1),np.mean(a))
   variance=(np.var(a, axis=0), np.var(a, axis=1), np.var(a))
   standard=(np.std(a, axis=0), np.std(a, axis=1), np.std(a))
   maximum=(np.max(a, axis=0), np.max(a, axis=1), np.max(a))
   minimum=(np.min(a,axis=0), np.min(a,axis=1), np.min(a))
   sum=(np.sum(a,axis=0), np.sum(a, axis=1), np.sum(a))

   Cal ={ 'Mean':[mean] ,'Variance':[variance],'Standard Deviation': [standard] , 'Maximum':[maximum], 'Minimum':[minimum], 'Sum':[sum]}
   return Cal
print(Calculate([1,3,4,6,7,9,9,5,6]))