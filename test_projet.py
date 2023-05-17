from collections import Counter
import re

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

#QUESTION 6 SHORTEST UNIQUE FACTOR
def Shortest_unique_factors(text):
    _,htr = HTR(text)
    suffixes,_ = TABSUFF(text)
    factors = []
    for i in range(1,len(htr)):
        factor = text[suffixes[i]:suffixes[i] + htr[i]]
        if htr[i]> 0 and len(re.findall(f'(?={factor})', text)) == 1 : 
            if factors is None :
               factors.append(factor)
            else :
                if factor not in factors :
                    factors.append(factor)
    min_length = len(min(factors, key=len))
    shortest = [factor for factor in factors if len(factor) == min_length]
    return shortest
#QUESTION 7 SUPERMAXIMAL FACTOR
def find_supermaximal_repetitions(text):
    _, lcp = HTR(text)  # Fonction pour construire les tables LCP et suffixes
    suffixes,_=TABSUFF(text)
    n = len(text)
    repetitions = []
    for i in range(1, n):
        if i < len(lcp):  # Vérifier si l'indice est valide
            lcp_length = lcp[i]  # Longueur du préfixe commun avec le suffixe précédent
            suffix_i = suffixes[i]  # Indice du suffixe courant
            factor = text[suffix_i:suffix_i + lcp_length]  # Facteur correspondant au préfixe commun
            repetition_count = text.count(factor)
            if repetition_count > 1:
                is_supermaximal = True
                for j in range(1, len(factor) + 1):
                    if text.count(factor[:j]) > repetition_count:
                        is_supermaximal = False
                        break
                if is_supermaximal:
                    repetitions.append(factor)
    return repetitions

#QUESTION 8 LONGEST COMMUN FACTOR BETWEEN TWO WORDS
def Longest_common_factor(T1, T2):
    # Concatenate the texts with a unique separator
    concat_text = T1 + '#' + T2

    # Construct the suffix table for the concatenated text
    suffixes, _ = TABSUFF(concat_text)

    # Calculate the LCP table for the concatenated text
    _,lcp = HTR(concat_text)

    max_lcp = 0  # Maximum LCP value
    common_suffix_index = -1  # Index of the common suffix in the concatenated text

    # Find the maximum LCP value between suffixes from different texts
    for i in range(1, len(lcp)):
        if (suffixes[i] < len(T1) and suffixes[i - 1] > len(T1)) or (suffixes[i] > len(T1) and suffixes[i - 1] < len(T1)):
            if lcp[i] > max_lcp:
                max_lcp = lcp[i]
                common_suffix_index = i

    if common_suffix_index == -1:
        return None  # No common factor found

    # Extract the longest common factor from the concatenated text
    longest_common_factor = concat_text[suffixes[common_suffix_index]: suffixes[common_suffix_index] + max_lcp]

    return longest_common_factor

#********************* TEST *************************
      #0123456789
mot = "AABBCZCAABBC"
mot1 = "AABBCZZZZ"
motif = "ABBC"
word ="saralynalynasara"
pattern = "sara"

print("The suffix table of the word {} is : \n {}".format(word,TABSUFF(word)))
print("The pattern {} is in the positions : {}".format(pattern,search_pattern(word,pattern)))
# print("longest prefix :",prefix_commun(mot,mot1))

print("Table htr of {} is :\n {} ".format(word,HTR(word)))

print("Longest factors of {} are: {}".format(word,longest_repeated_factors(word)))

print("The factors that are repeated at least 3 times in the word {} are: {}".format(word,repeated_factors3(word)))

print("The inverse of suffix table of the word {} is : \n {}".format(word,Inverse_TS(word)))
#print(mot[0:5])
#print("The shortest unique factors of the word {} are : {}".format(word,Shortest_unique_factors(word)))
#print('les indices sont :',search_pattern(mot,motif))
print("The super maximales of the word {} are : {}".format(word,find_supermaximal_repetitions(word)))
print("The longest commun factor words {}  and {} are : {}".format(word,pattern,Longest_common_factor(word,pattern)))