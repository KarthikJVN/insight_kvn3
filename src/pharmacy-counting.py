# -*- coding: utf-8 -*-

## This code has been tested on the entire 1.1 GB test data provided and it works consistently. 
## It also takes into account certain types of outlier cases where even the drug name has commas or numbers.


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


#text_file = open("de_cc_data.txt", "r")  # The corresponding input text file is opened
lines = text_file.read().split('\n') # The text within the file is split based on a new line and stored in variable "lines"
text_file.close() # The text file is closed


drug_names = [] # An empty list named "drug_names" is created to store the names of the drugs
my_dict = {}    # An empty dictionary named "my_dict is created"



## The for loop iterates throughout the contents of the text file and goes through every line

for i in range(len(lines)): # We iterate over each line 
     if i!=0:       # Makes sure that we iterate through the limits of the text file contents
         temp = lines[i].split(",")     # We split each line based on commas 
         if len(temp) == 5:     # If after splitting based on commas, there are only 5 fields/columns it implies that the text can be categorised accurately
             drug = temp[3]  # The drug name in the corresponding position is stored in variable "drug"
             cost = temp[4]  # The cost in the corresponding position is stored in variable "cost"

         elif len(temp) > 5:  # If the number of fields obtained after a comma based split is greater than 5, it means that the drug names may have a comma and need to be dealt with accordingly
             
             if '"' in temp[-2]:    # If "" is found at the position being tested for, it should be a part of the drug name
                 drug = (temp[-3] + "," + temp[-2])     # The drug name would be a combination of both fields obtained from their respective positions
             else:              # In case the field found is not enclosed in "" the usual process of assigning the cost and drug name separately is followed
                 drug = temp[-2]    # Drug name is stored in variable "drug"
             cost = temp[-1]        # Cost is stored in variable "cost"
            
         else:
             continue

         drug_names.append(drug)    # The drug names are appended to the list "drug_names" created earlier
         
         if drug not in my_dict.keys():  # The 'my_dict' dictionary is used to store costs according to drug names. , otherwise it sums with the previous cost.
             my_dict[drug] = float(cost)    # If the name isn't there in the dictionary already, it stores the cost with the key being the drug name.  
         else:
             my_dict[drug] += float(cost)   # If the name is already present in the dictionary, the cost is added to the previous cost for the same drug.






with open('top_cost_drug.txt', 'a') as output:  # The output generated is stored as "top_cost_drug.txt"
    
    header = "drug_name,num_prescriber,total_cost\n"    # The titles for the various fields in the output are stored as header
    output.write(header)    # Writes Header to output file
    
    for key, value in my_dict.items(): # We iterate through the "my_dict" dictionary
        count = drug_names.count(key)   # Count the number of occurrences of each drug name using the key values in "my_dict"
        final_string = key + "," + str(count) + "," + str(value) + "\n"  # Output has drug name, count and total cost
#        
        output.write(final_string)  # Writing final output

