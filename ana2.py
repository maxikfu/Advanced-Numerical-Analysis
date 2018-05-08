#ANA
import csv
import matplotlib.pyplot as plt
import numpy as np

#loading data for A
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

#loading data for B
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
print("B len",len(dataB_X))
print("A' len",len(derivativeA_X))
#
# removed_X = []
# reduced_B_X = []
# B_len = 0
# #while(B_len <= len(derivativeA_X)):
# for i,pointX in enumerate(dataB_X):
#     if(i == 0):
#         continue;
#     if(len(reduced_B_X) == len(derivativeA_X)):
#         break;
#     if( i == len(dataB_X)-1):
#         break;
#     if(dataB_X[i] > dataB_X[i-1] and dataB_X[i] < dataB_X[i+1] ):
#         removed_X.append(dataB_X[i])
#     else:
#         reduced_B_X.append(dataB_X[i])
#
# removed_Y = []
# reduced_B_Y = []
#
# for i,pointY in enumerate(dataB_Y):
#     if(i == 0):
#         continue;
#     if(len(reduced_B_Y) == len(derivativeA_Y)):
#         break;
#     if( i == len(dataB_Y)-1):
#         break;
#     if(dataB_Y[i] > dataB_Y[i-1] and dataB_Y[i] < dataB_Y[i+1] ):
#         removed_Y.append(dataB_Y[i])
#     else:
#         reduced_B_Y.append(dataB_Y[i])

# reducing number of points in function B
counter = 1
l = []
reduced_B_X = []
for pointX in dataB_X:
   l.append(pointX)
   if counter==5:
       reduced_B_X.append(np.mean(l))
       l=[]
       counter=0
   counter+=1
reduced_B_Y =[]
for pointY in dataB_Y:
   l.append(pointY)
   if counter==5:
       reduced_B_Y.append(np.mean(l))
       l=[]
       counter=0
   counter+=1
print('B len after reduction 5 avg',len(reduced_B_X))
#removing last 127 points so number of points in the functions A and B will be similar
reduced_B_X = reduced_B_X[:-127]
reduced_B_Y = reduced_B_Y[:-127]
print('B len after cutting',len(reduced_B_X))
#finding max min for function at X
max_norm_B_X =max(reduced_B_X)
min_norm_B_X = min(reduced_B_X)
max_norm_A_X =max(derivativeA_X)
min_norm_A_X = min(derivativeA_X)
#finding max min for functions at Y
max_norm_B_Y =max(reduced_B_Y)
min_norm_B_Y = min(reduced_B_Y)
max_norm_A_Y =max(derivativeA_Y)
min_norm_A_Y = min(derivativeA_Y)
#normalizing our functions so they will be between [0;1]
normalized_derivativeA_X=[]
normalized_reducedB_X=[]
normalized_derivativeA_Y=[]
normalized_reducedB_Y=[]
for a,b,c,d in zip(derivativeA_X,reduced_B_X,derivativeA_Y,reduced_B_Y):
    normalized_derivativeA_X.append((a-min_norm_A_X)/(max_norm_A_X-min_norm_A_X)) 
    normalized_reducedB_X.append((b-min_norm_B_X)/(max_norm_B_X-min_norm_B_X))
    normalized_derivativeA_Y.append((c-min_norm_A_Y)/(max_norm_A_Y-min_norm_A_Y)) 
    normalized_reducedB_Y.append((d-min_norm_B_Y)/(max_norm_B_Y-min_norm_B_Y))
#moving average for function B
k = 5 #number of neigbours we are avereging
# new_reduced_B_X = []
# for i in  range(0,len(normalized_reducedB_X)):
#     new_reduced_B_X.append(np.mean(normalized_reducedB_X[i:i+k]))
# normalized_reducedB_X = new_reduced_B_X
# new_reduced_B_Y = []
# for i in  range(0,len(normalized_reducedB_Y)):
#     new_reduced_B_Y.append(np.mean(normalized_reducedB_X[i:i+k]))
# normalized_reducedB_Y = new_reduced_B_Y

#comparing results
compareA_B_X = []

for i,j in zip(normalized_derivativeA_X,normalized_reducedB_X):
       compareA_B_X.append(i/j);
compareA_B_Y = []
for i,j in zip(normalized_derivativeA_Y,normalized_reducedB_Y):
       compareA_B_Y.append(i/j);

#ploting results
plt.figure(1)
plt.plot(normalized_derivativeA_X,label = 'derivA_X',color='blue',linewidth = 3)
plt.plot(normalized_reducedB_X,label='B_X',color='green',linewidth = 3)
#plt.plot(derivativeA_Y,label = 'derivA_Y',color='red',linewidth = 3)
plt.ylabel('Comparing X')
plt.legend()
plt.figure(2)
plt.plot(normalized_derivativeA_Y,label = 'derivA_Y',color='red',linewidth = 3)
plt.plot(normalized_reducedB_Y, label='B_Y',color='black',linewidth = 3)
plt.ylabel('Comparing Y')
plt.legend()
plt.figure(3)
plt.plot(compareA_B_X,label = 'compareA_B_X',color='blue')
plt.legend()
plt.figure(4)
plt.plot(compareA_B_Y,label = 'compareA_B_Y',color='black')
plt.legend()
plt.show()
