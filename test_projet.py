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

#QUESTION 3 : 

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
    indexsuff ,suffixes = TABSUFF(text)
    n = len(text)
    htr_table = []
    htr_len = []

    for i in range(1,n):
        suffix1 = suffixes[i]
        suffix2 = suffixes[i-1]
        htr_table.append(prefix_commun(suffix1,suffix2))
        htr_len.append(len(prefix_commun(suffix1, suffix2)))
    

    return htr_table,htr_len


#********************* TEST *************************
      #0123456789
mot = "AABBCZCAABBC"
mot1 = "AABBCZZZZ"
motif = "ABBC"
word ="banana"

print("Table des suffixes : \n",TABSUFF(word))
#print("Le motif se trouve aux indices :",search_pattern(mot,motif))
# print("longest prefix :",prefix_commun(mot,mot1))

print("Table htr : \n",HTR(word))


#print(mot[0:5])

#print('les indices sont :',search_pattern(mot,motif))