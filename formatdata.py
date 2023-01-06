import json
import csv
import numpy as np
from datetime import datetime
maxVal=0
maxIndex=0
checkLen=1
flow=1
i=0
while flow==1:
    
    try:
        checkLen=len(data['locations'][i])
        if checkLen > maxVal:
            maxVal=checkLen
            maxIndex=i
        i=i+1
    except:
        print('List length index:',i,' with max length:',maxVal,' at ',maxIndex)
        flow=0
        

listLen=i
locs=np.zeros((listLen,2))

for j in range(0,listLen):
    
    
    indStr=str(data['locations'][j])
    
    tup=indStr.rpartition("latitudeE7': ")
    tempStr=tup[2].split(',',1)[0]
    tempInt=int(tempStr)
    if tempInt>1800000000:
        tempInt=tempInt-4294967296
    tempInt=tempInt/(10**7)
    locs[j][0]=tempInt
    
    tup=indStr.rpartition("longitudeE7': ")
    tempStr=tup[2].split(',',1)[0]
    tempInt=int(tempStr)
    if tempInt>1800000000:
        tempInt=tempInt-4294967296
    tempInt=tempInt/(10**7)
    locs[j][1]=tempInt