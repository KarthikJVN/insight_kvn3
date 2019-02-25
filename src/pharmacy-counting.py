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


import sys

global text_file
global out_file
#This is the default output file location.
out_file='./output/top_cost_drug.txt'

if(len(sys.argv)<2):
	print("ERROR: Require Filename")
	print("Format: python3 src/pharmacy-counting.py <input data file> <output data file>")
	sys.exit(-1)

try:
    text_file = open(sys.argv[1], 'r')
    print("INFO: Input File:", sys.argv[1])
    # Store configuration file values
except FileNotFoundError:
    print("ERROR: File does not exist the specified path.")
    sys.exit(-1)

try:
	out_file = sys.argv[2]
except IndexError:
	out_file='./output/top_cost_drug.txt'
	print("INFO: Taking Default Output file")

print("INFO: Output File:", out_file)

lines = text_file.read().split('\n')
text_file.close()

#TODO: Check for format
#print(lines[0].split(",")[0])
#id,prescriber_last_name,prescriber_first_name,drug_name,drug_cost
#if any(x in str for x in a):
   

drug_names = []
my_dict = {}

#For progress bar setting
#toolwidth = len(lines) 
#sys.stdout.write("[%s]" % (" " * toolbar_width))
#sys.stdout.flush()
#sys.stdout.write("\b" * (toolbar_width+1)) # return to start of line, after '['

for i in range(len(lines)):
     if i!=0:
         temp = lines[i].split(",")
         #temp = temp.decode('utf8').encode('utf-8')
         if len(temp) == 5:
             drug = temp[3]
             cost = temp[4]
         if len(temp) == 6:
             drug = temp[3] + "," + temp[4]
             cost = temp[5]
             
         drug_names.append(drug)
         
         if drug not in my_dict.keys():
             my_dict[drug] = float(cost)
         else:
             my_dict[drug] += float(cost)
         
         #for progress bar
         #sys.stdout.write("-")
         #sys.stdout.flush()

sys.stdout.write("\n")
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

with open(out_file, 'w') as output:
    
    header = "drug_name,num_prescriber,total_cost\n"
    output.write(header)
    
    for key, value in my_dict.items():
        count = drug_names.count(key)
        final_string = key + "," + str(count) + "," + str(value) + "\n"
#        A,2,300
#        C,2,3000
#        B,1,1500
        output.write(final_string)
