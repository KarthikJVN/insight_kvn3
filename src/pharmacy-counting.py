# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 10:13:22 2019

"""
#Input
#id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
#1000000001,Smith,James,AMBIEN,100
#1000000002,Garcia,Maria,AMBIEN,200
#1000000003,Johnson,James,CHLORPROMAZINE,1000
#1000000004,Rodriguez,Maria,CHLORPROMAZINE,2000
#1000000005,Smith,David,BENZTROPINE MESYLATE,1500


#TODO: Check if the input is correct and if path exists. Throw error if the path does and also throw error if the file data format incorrect. 
import sys

global text_file

if(len(sys.argv)==1):
	print("ERROR: Require Filename")
	sys.exit(-1)

try:
    text_file = open(sys.argv[1], 'r')
    # Store configuration file values
except FileNotFoundError:
    print("ERROR: File does not exist the specified path.")
    sys.exit(-1)

#TODO: Check for format


#text_file = open("./input/itcont.txt", "r")

#TODO: Optimization  -  check for faster file read libraries. 
lines = text_file.read().split('\n')
text_file.close()


#TODO: Add comments in the code. DETAILED!!!
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

#TODO: This file location needs tobe generic. It should take from correct path store it in right path. The path variable needs to be automatically desciphered. 
with open('./output/top_cost_drug.txt', 'w') as output:
    
    header = "drug_name,num_prescriber,total_cost\n"
    output.write(header)
    
    for key, value in my_dict.items():
        count = drug_names.count(key)
        final_string = key + "," + str(count) + "," + str(value) + "\n"
#        A,2,300
#        C,2,3000
#        B,1,1500
        output.write(final_string)
