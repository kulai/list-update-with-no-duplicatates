# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 15:48:51 2019
@author: Ashish Kulai
@program: update the data2 list with no duplicates entered by the data1 list.
"""

data1 = [6,25,20,6,9] # data from source
#data1 = [6,20,30,40,50,8,8,8,8]
data2 = [6,20,8,9] # database

print("length :: data1 ::",len(data1))
print("length :: data2 ::",len(data2))

# if list is empty enter the first element to the list
if len(data2) == 0:
    data2.append(data1[0])
    start = 1 # index has to be 1 coz first element has entered here
else:
    start = 0 

len1 = len(data1)
for i in range(start,len1):
   len2 = len(data2)
   print("\n\n-----------------------------------------")
   print("comapring with -> ",data1[i])
   for j in range(len2):
       print("comapring to -> ",data2[j])
       match = 0
       if data1[i] == data2[j]:
           print("update ::",data1[i])
           print("-----------------------------------------")
           match = 1
           break
   check = len2 - 1
   if j == check and match == 0 :    
       print("none of them match -> then -> insert ->",data1[i])
       print("-----------------------------------------")
       data2.append(data1[i]);
       
print("data1 :: ",data1)
print("data2 :: ",data2)

