# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:13:22 2019

@author: AdityaChanodia
"""
#Input
#id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
#1000000001,Smith,James,AMBIEN,100
#1000000002,Garcia,Maria,AMBIEN,200
#1000000003,Johnson,James,CHLORPROMAZINE,1000
#1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
#1000000005,Smith,David,BENZTROPINE MESYLATE,1500


text_file = open("itcont.txt", "r")
lines = text_file.read().split('\n')
text_file.close()

drug_names = []
my_dict = {}

for i in range(len(lines)):
     if i!=0:
         temp = lines[i].split(",")
         drug = temp[3]
         cost = temp[4]
         
         drug_names.append(drug)
         
         if drug not in my_dict.keys():
             my_dict[drug] = int(cost)
         else:
             my_dict[drug] += int(cost)
#initial = {}
#i = 1 {A:100}
#
#i =2 {A:300}
#
#i =3 {A:300, C:1000}
#
#i =4 {A:300, C:3000}
#
#i =5 {A:300, C:3000 B:1500}


with open('top_cost_drug.txt', 'a') as output:
    
    header = "drug_name,num_prescriber,total_cost\n"
    output.write(header)
    
    for key, value in my_dict.items():
        count = drug_names.count(key)
        final_string = key + "," + str(count) + "," + str(value) + "\n"
#        A,2,300
#        C,2,3000
#        B,1,1500
        output.write(final_string)
