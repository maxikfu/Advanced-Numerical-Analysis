#ANA
import csv
import matplotlib.pyplot as plt
import numpy as np
with open('DERIV2D/DERIV2D_functionA_XY.csv','r') as fileA:
    csv_file = csv.reader(fileA, delimiter=',')
    dataA = []
    dataA_X =[]
    dataA_Y = []
    for line in csv_file:
        dataA_X.append(float(line[0]))
        dataA_Y.append(float(line[1]))
    dataA.append(dataA_X)
    dataA.append(dataA_Y)

with open('DERIV2D/DERIV2D_functionB_XY.csv','r') as fileB:
    csv_file = csv.reader(fileB, delimiter=',')
    dataB = []
    dataB_X =[]
    dataB_Y = []
    for line in csv_file:
        dataB_X.append(float(line[0]))
        dataB_Y.append(float(line[1]))
    dataB.append(dataB_X)
    dataB.append(dataB_Y)

#partial derivativs of A
derivativeA_X = []
i = 0
for i in range(0,len(dataA_X)-1):
    diff = dataA_X[i+1]-dataA_X[i]
    derivativeA_X.append(diff)
derivativeA_Y = []
i = 0
for i in range(0,len(dataA_X)-1):
    diff = dataA_Y[i+1]-dataA_Y[i]
    derivativeA_Y.append(diff)
derivativeA=[[i,j] for i,j in zip(derivativeA_X,derivativeA_Y)]
functionB = [[i,j] for i,j in zip(dataB_X,dataB_Y )]
#reducing number of points in function # B
counter = 1
l=[]
reduced_B_X = []
for pointX in dataB_X:
    l.append(pointX)
    if counter==5:
        reduced_B_X.append(np.mean(l))
        l=[]
        counter=0
    counter+=1
# print(len(dataB_X))
# print(len(derivativeA_X))
# print(float(len(dataB_X)/len(derivativeA_X)))
# print(len(reduced_B_X))
plt.figure(1)
plt.plot(derivativeA_X,label = 'derivA_X',color='blue',linewidth = 3)
plt.plot(derivativeA_Y,label = 'derivA_Y',color='red',linewidth = 3)
plt.ylabel('Deriv A')
plt.legend()
plt.figure(2)
plt.plot(reduced_B_X,label='B_X',color='green',linewidth = 3)
# plt.plot(dataB_Y, label='B_Y',color='black',linewidth = 3)
plt.ylabel('Function B')
plt.legend()
plt.show()
