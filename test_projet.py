from collections import Counter

#QUESTION 1 : TABLE DE SUFFIXES
def TABSUFF(chaine):
    indexes=[]
    suffixes = []
    for i in range(len(chaine)):
       suffixes.append(chaine[i:])
       indexes.append(i)
    suffixes = sorted(suffixes)
    indexes.sort(key=lambda x: chaine[x:])
    return indexes,suffixes

#QUESTION 2 : RECHERCHE DU MOTIF 
def search_pattern(text,pattern):    
    _,Tabsuffix = TABSUFF(text)  
    indexes = []
    for i,suffix in enumerate(Tabsuffix):
        if pattern == suffix[:len(pattern)]:
            index = len(text) - len(suffix)
            indexes.append(index)
    return indexes

#QUESTION 3 : HTR TABLE

def prefix_commun(word1,word2):
    l1 = len(word1)
    l2 = len(word2)
    i = 0
    long = ""
    while i<min(l1,l2) and word1[i]==word2[i] :
        long += word1[i]
        i+=1
    return long  #word1[:i]

def HTR(text):
    _,suffixes = TABSUFF(text)
    htr_table = [] 
    htr_len = []
    for i in range(1,len(suffixes)):
        suffix1 = suffixes[i]
        suffix2 = suffixes[i-1]
        htr_table.append(prefix_commun(suffix1,suffix2)) #htr table contains strings of prefixes
        htr_len.append(len(prefix_commun(suffix1, suffix2))) # htr len is the real one and contain length of prefixes
    #htr_len.append(0)
    return htr_table,htr_len

#QUESTION 4 TS ET HTR

#LONGEST REPEATED FACTORS 
def longest_repeated_factors(text):
    _,htr = HTR(text)
    max_htr = max(htr)
    suffixes,_ = TABSUFF(text)
    factors = []
    #get the suffixes indexes of the max htr from the htr table
    for i in range(len(htr)) :
        if htr[i] == max_htr :
            factor = text[suffixes[i]: suffixes[i] + max_htr]
            if factor not in factors:
                factors.append(factor)
    return factors
#FACTORS REPEATED AT LEAST 3 TIMES
def repeated_factors3(text):
    _,htr = HTR(text)
    suffixes,_ = TABSUFF(text)
    factors = []
    repeated_factors= []
    #get the suffixes indexes from the htr table
    for i in range(len(htr)) :
        if htr[i] >= 2:
            factors.append(text[suffixes[i]:suffixes[i] + htr[i]])
    #save the factors that are repeated at least three times 
    for factor in factors :
        count = text.count(factor)
        if count >=3 and factor not in repeated_factors :
            repeated_factors.append(factor)      
    return repeated_factors
#QUESTION 5 INVERSE SUFFIX TABLE   
def Inverse_TS(text):
    suffixes,_ = TABSUFF(text)
    inverse = [0] * len(suffixes)
    for i in range(len(suffixes)):
        index = suffixes[i]
        inverse[index] = i
    return inverse

#QUESTION 6 SHORTEST FACTOR
def Shortest_unique_factors(text):
    _,htr = HTR(text)
    suffixes,_ = TABSUFF(text)
    factors = []
    for i in range(1,len(htr)):
        if htr[i] == 0 :
            factor = text[suffixes[i]:]
            if factor not in factors :
                factors.append(factor)
        '''if htr[i]>0 : 
            factor = text[suffixes[i]:suffixes[i] + htr[i]]
            if factors is None :
               factors.append(factor)
            else :
                if factor not in factors :
                    factors.append(factor)'''
    shortest = min(factors,key=len)
    return shortest        



#********************* TEST *************************
      #0123456789
mot = "AABBCZCAABBC"
mot1 = "AABBCZZZZ"
motif = "ABBC"
word ="saralynasaralychak"

print("The suffix table of the word {} is : \n {}".format(word,TABSUFF(word)))
#print("Le motif se trouve aux indices :",search_pattern(mot,motif))
# print("longest prefix :",prefix_commun(mot,mot1))

print("Table htr of {} is :\n {} ".format(word,HTR(word)))

print("Longest factors of {} are: {}".format(word,longest_repeated_factors(word)))

print("The factors that are repeated at least 3 times in the word {} are: {}".format(word,repeated_factors3(word)))

print("The inverse of suffix table of the word {} is : \n {}".format(word,Inverse_TS(word)))
#print(mot[0:5])
print("shirtest",Shortest_unique_factors(word))
#print('les indices sont :',search_pattern(mot,motif))