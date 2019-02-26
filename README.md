# Insight Datascience Challenge 2019  
Solution submitted by Karthik for the Insight datascience challenge

# Table of contents
1. [Overview](README.md#Overview)
1. [Directory Structure](README.md#Directory-Structure)
1. [Required Libraries](README.md#Required-Libraries)
1. [Instructions](README.md#Instructions)
1. [Expected Outputs](README.md#Expected-Output)
1. [Final Comments](README.md#Final-Comments)

# Overview
pharmacy-counting.py is the final code which prompts the user to specify the input and output file paths.



# Directory structure
The test large data set is not part of the repo. The user is required to download the tests suite in the correct location. 
The test_large is downloaded from [link](https://drive.google.com/file/d/1fxtTLR_Z5fTO-Y91BnKOQd6J0VC9gPO3/view)

The directory structure is similar to the one given in the question and is as follows-

     ├── README.md
     ├── input
     │   └── itcont.txt
     ├── insight_testsuite
     │   ├── run_tests.sh
     │   └── tests
     │       ├── test_1
     │       │   ├── input
     │       │   │   └── itcont.txt
     │       │   └── output
     │       │       └── top_cost_drug.txt
     │       └── test_large
     │           ├── input
     │           │   └── de_cc_data.txt.crdownload
     │           └── output
     ├── output
     │   └── top_cost_drug.txt
     ├── run.sh
     └── src
         └── pharmacy-counting.py


# Required Libraries
None


# Instructions
To run basic test case:
     bash run.sh

To run all test case:
     bash insight_testsuite/run_tests.sh

pharmacy-counting.py is the final code which needs to be run after specifying the input/output file paths appropriately.

# Expected Output 
The output expected is of the form as given in the question. As the code has been run on the entire test set, the output corresponding to the test set has been obtained.
