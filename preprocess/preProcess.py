from __future__ import print_function 
import urllib2
import HTMLParser
import sys
h=HTMLParser.HTMLParser( )

NumOfArticle = 0 #total number of articles
Places = []#create places attribute for article
articleClass = [] # an array recording topics of each article 

wordlist = open("/Users/mengqizhou/Desktop/assignment1/wordlist.txt","w")#the file to write into
vectors = open("/Users/mengqizhou/Desktop/assignment1/vectors.txt","w")#the file to write into
attribute = open("/Users/mengqizhou/Desktop/assignment1/attribute.txt","w")#the file to write into

for it in range(0,10): 
    
    address = "http://www.cse.ohio-state.edu/~srini/674/public/reuters/reut2-00"+str(it)+".sgm"           
    content = urllib2.urlopen(address).read()
    topics_end = 0
    topics_position = 0
    last_topics = content.rfind('</TOPICS>')  #get index for last <TOPICS> so the loop knows when to stop
        
            #loop through every article
    FrequencyVector = [] #create a list of frequency vector for every article in subset
    ExistenceVector = []#create a list of existence vector for every article in subset
    Attributes = [] #create a list of attributes corresponding to the feature vector in subset
    vocabulary = {}#a dictionary recording word and frequency for the whole  subset
    NumInSubset = 0
    ini = NumOfArticle
    initialNumber = []
    lastNumber = []
    while (topics_end != last_topics) :
        initialNumber.append(ini)

                
                #located the article
        topics_position = content.find('<TOPICS>', topics_end)
        topics_end = content.find('</TOPICS>', topics_position)
        data = content[topics_position + 8: topics_end]
                
                #extract topics
        d_end = 0
        d_position = 0
        last_d = data.rfind('</D>')
        topic =[] 
        while(d_end != last_d) :
            d_position = data.find('<D>', d_end)
            d_end = data.find('</D>', d_position)
            Da_ta = data[d_position + 3: d_end]
            topic.append(Da_ta)
        articleClass.append(topic)
        
        #extract place
        place_position = content.find('<PLACES>', topics_end)
        place_end = content.find('</PLACES>', place_position)
        place = content[place_position + 8: place_end]
        p_end = 0
        p_position = 0
        last_p = place.rfind('</D>')
        places =[]
        while(p_end != last_p) :
            p_position = place.find('<D>', p_end)
            p_end = place.find('</D>', p_position)
            Data = place[p_position + 3: p_end]
            places.append(Data)
        Places.append(places)
      
                #extract the body     
        body_position = content.find('<BODY>', topics_end)
        body_end = content.find('</BODY>', body_position)
        if body_position>0:
            
            data = content[body_position + 6: body_end]
        
            
                #count word frequency of the article
                #below code is copied and modified from "http://www.yasyf.com//coding/simple-python-word-frequency-count/"
            words_to_ignore = ["were","there", "still", "have","will", "over","don't","well","talk","take","soon","best","said","been","that","what","with","this","would","from","your","which","while","these"]
            things_to_strip = [".",",","?",")","(","\"",":",";","'s", "/"]
            words_min_size = 4   
            words = data.lower().split()
            wordcount = {}
            for word in words:
                for thing in things_to_strip:
                    if thing in word:
                        word = word.replace(thing,"")
                if word not in words_to_ignore and len(word) >= words_min_size:
                    if word in wordcount:
                        wordcount[word] += 1
                    else:
                        wordcount[word] = 1
                    
                    #update featurevector, existence featurevector attribute and vocabulary using wordcount  
            temp = wordcount.copy()
            Words = []     
            for word in temp:
                if wordcount[word]<=1:
                    del wordcount[word]
                        #add new word into attribute array
                else:
                    Words.append(word)
                    if word not in Attributes: #new attribute
                        Attributes.append(word)
                        vocabulary[word] = wordcount[word]
                                #updating the previous feature vectors by adding append 0 
                        for k in range(0,NumInSubset):
                            FrequencyVector[k].append(0)
                            ExistenceVector[k].append(0)
                    else: 
                        vocabulary[word] += wordcount[word]
                    
                    #update wordFrequency in the sequence of Attributes
            wordFrequency = [] 
            wordExistence = []
            for word in Attributes:
                if word in wordcount:
                    wordFrequency.append(wordcount[word])
                    wordExistence.append(1)
                else:
                    wordFrequency.append(0)
                    wordExistence.append(0)
                            
                    #updating feature vector by appending wordFrequency
            FrequencyVector.append(wordFrequency)     
            #update existence vecotr by appending wordExistence
            ExistenceVector.append(wordExistence)
            
            print ("Article Number = ",NumOfArticle, file = wordlist)
            print ("word list = ", Words, file = wordlist)
            print ("class =", articleClass[NumOfArticle], file = wordlist)
            print ("place= ", Places[NumOfArticle], file = wordlist)
            
            NumInSubset += 1   
            NumOfArticle += 1
         
    print ("for article",ini," to ", NumOfArticle-1, file = attribute)
    print ("attributes = ", Attributes, file = attribute) 
    print("for article",ini," to ", NumOfArticle-1, file = vectors)
    
    for i in range(ini,NumOfArticle):
        print ("Article Number = ", i, file = vectors)
        print ("existence Vector = ", ExistenceVector [i-ini], file = vectors)
        print ("frequency vector = ", FrequencyVector[i-ini], file = vectors)
 
          
        
   
for it in range(10,22):      
    address = "http://www.cse.ohio-state.edu/~srini/674/public/reuters/reut2-0"+str(it)+".sgm"           
    content = urllib2.urlopen(address).read()
    topics_end = 0
    topics_position = 0
    last_topics = content.rfind('<TOPICS>')  #get index for last <TOPICS> so the loop knows when to stop
        
            #loop through every article
    FrequencyVector = [] #create a list of frequency vector for every article in subset
    ExistenceVector = []#create a list of existence vector for every article in subset
    Attributes = [] #create a list of attributes corresponding to the feature vector in subset
    vocabulary = {}#a dictionary recording word and frequency for the whole  subset
    NumInSubset = 0
    ini = NumOfArticle
    while (topics_position != last_topics) :
                
                #located the article
        topics_position = content.find('<TOPICS>', topics_end)
        topics_end = content.find('</TOPICS>', topics_position)
        data = content[topics_position + 8: topics_end]
                
                #extract topics
        d_end = 0
        d_position = 0
        last_d = data.rfind('</D>')
        topic =[] 
        while(d_end != last_d) :
            d_position = data.find('<D>', d_end)
            d_end = data.find('</D>', d_position)
            Da_ta = data[d_position + 3: d_end]
            topic.append(Da_ta)
        articleClass.append(topic)
        
        #extract place
        place_position = content.find('<PLACES>', topics_end)
        place_end = content.find('</PLACES>', place_position)
        place = content[place_position + 8: place_end]
        p_end = 0
        p_position = 0
        last_p = place.rfind('</D>')
        places =[]
        while(p_end != last_p) :
            p_position = place.find('<D>', p_end)
            p_end = place.find('</D>', p_position)
            Data = place[p_position + 3: p_end]
            places.append(Data)
        Places.append(places)
      
                #extract the body     
        body_position = content.find('<BODY>', topics_end)
        body_end = content.find('</BODY>', body_position)
        if body_position>0:
            data = content[body_position + 6: body_end]
        
            
                #count word frequency of the article
                #below code is copied and modified from "http://www.yasyf.com//coding/simple-python-word-frequency-count/"
            words_to_ignore = ["were","there", "still", "have","will", "over","don't","well","talk","take","soon","best","said","been","that","what","with","this","would","from","your","which","while","these"]
            things_to_strip = [".",",","?",")","(","\"",":",";","'s", "/"]
            words_min_size = 4   
            words = data.lower().split()
            wordcount = {}
            for word in words:
                for thing in things_to_strip:
                    if thing in word:
                        word = word.replace(thing,"")
                if word not in words_to_ignore and len(word) >= words_min_size:
                    if word in wordcount:
                        wordcount[word] += 1
                    else:
                        wordcount[word] = 1
                    
                    #update featurevector, existence featurevector attribute and vocabulary using wordcount  
            temp = wordcount.copy()
            Words = []     
            for word in temp:
                if wordcount[word]<=1:
                    del wordcount[word]
                        #add new word into attribute array
                else:
                    Words.append(word)
                    if word not in Attributes: #new attribute
                        Attributes.append(word)
                        vocabulary[word] = wordcount[word]
                                #updating the previous feature vectors by adding append 0 
                        for k in range(0,NumInSubset):
                            FrequencyVector[k].append(0)
                            ExistenceVector[k].append(0)
                    else: 
                        vocabulary[word] += wordcount[word]
                    
                    #update wordFrequency in the sequence of Attributes
            wordFrequency = [] 
            wordExistence = []
            for word in Attributes:
                if word in wordcount:
                    wordFrequency.append(wordcount[word])
                    wordExistence.append(1)
                else:
                    wordFrequency.append(0)
                    wordExistence.append(0)
                            
                    #updating feature vector by appending wordFrequency
            FrequencyVector.append(wordFrequency)     
            #update existence vecotr by appending wordExistence
            ExistenceVector.append(wordExistence)
            
            print ("Article Number = ",NumOfArticle, file = wordlist)
            print ("word list = ", Words, file = wordlist)
            print ("class =", articleClass[NumOfArticle], file = wordlist)
            print ("place= ", Places[NumOfArticle], file = wordlist)
            
            NumInSubset += 1   
            NumOfArticle += 1
         
    print ("for article",ini," to ", NumOfArticle-1, file = attribute)
    print ("attributes = ", Attributes, file = attribute) 
    print("for article",ini," to ", NumOfArticle-1, file = vectors)
    for i in range(ini,NumOfArticle):
        print ("Article Number = ", i, file = vectors)
        print ("existence Vector = ", ExistenceVector [i-ini], file = vectors)
        print ("frequency vector = ", FrequencyVector[i-ini], file = vectors)



