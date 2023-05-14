def TABSUFF(chaine):
    tab=[]
    for i in range(1,len(chaine)):
       tab.append(chaine[i:len(chaine)+1])
    return tab


def PLFC(chaine1,chaine2):
    tabs1=TABSUFF(chaine1)
    tabs2=TABSUFF(chaine2)

    n=min(len(tabs1),len(tabs2))
    
    for i in range(n-1,0,-1):
        if tabs1[i]==tabs2[i]:
            return tabs1[i]

def isseq(s,mot):
    if s in mot:
        return True
    if(len(s)<=len(mot)):
     i=0
     j=0
     while(i<len(mot)-1 and j<len(s)-1):
        if mot[i]==s[j]:
            i=+1
            j=+1
        else:
            i=+1
     return j==len(s)
    #else:
        #return False

mot ='sara'
chaine1='saaaaaaaaaaaaaaraaa'
chaine2='saaaaaaaaaaaaaaraaaaahhhh'
print(TABSUFF(mot))
print('plfc:')
#print(PLFC(chaine1,chaine2))

#print[chaine2[len(chaine2)-1:0:-1]]

v1='aacttag'
v2='actg'
#print(isseq(v2,v1))