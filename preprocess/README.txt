Table of Content
 
1. preProcess.py
This file contains source code in python to : (1) access and extract information from online directory; (2)reprocess the files and generate feature vectors, class labels and place labels. 

All methods are synchronized in a single source file. To run the code, one needs to be able to edit the source file by entering the target file address where one desire to output the result into. Steps are:
(1) generate three txt files in a distinguishable folder; file 1 is to store the word list, class label and place label for each article; file 2 is to store the attribute set for the feature vectors; file 3 is for storing ExistenceVector and FrequencyVector for each article.
(2) open the source file preProcess.py
(3)on top of the source code, locate below code:
 
wordlist = open("/Users/mengqizhou/Desktop/assignment1/wordlist.txt","w")#the file to write into
vectors = open("/Users/mengqizhou/Desktop/assignment1/vectors.txt","w")#the file to write into
attribute = open("/Users/mengqizhou/Desktop/assignment1/attribute.txt","w")#the file to write into"

(4)  replace /Users/mengqizhou/Desktop/assignment1/wordlist.txt with address of file 1; replace /Users/mengqizhou/Desktop/assignment1/vectors.txt with address of file 3; replace /Users/mengqizhou/Desktop/assignment1/attribute.txt with address of file 2. 
(5)Save the file.
(6) run preProcess.py in an IDE, such as Eclipse and Aptana Studio with Python system library newer than 2.7.

2. wordlist.txt
A sample file generated by running preProcess.py, including class label and place label for each article.

3. attribute.txt
A sample file generated by running preProcess.py, including attributes of feature vectors for every file, or a set of 1000 articles.

4.vectors.txt
A sample file, small part of what's generated by running preProcess.py, containing feature vectors for articles, including existence vector and frequency vector.
