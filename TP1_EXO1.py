def ssmot(s,l=3):
    ch=[]
    if(len(s)<l):
        print('error')
        return
    else :
        if(len(s)==l):
            print(s)
        else:
            for i in range(len(s)-l+1):
                print(s[i:i+l])
              
#question 2
        
def plus_long_pref(s1,s2):
    i=0
    minl=min(len(s1),len(s2))
    while((i<minl) and s1[i]==s2[i] ):
        i+=1
    print(s1[0:i])

#question 3

def prefixes(chaine):
    table=[]
    for i in range(len(chaine)):
        table.append(chaine[0:i+1])
    print(*table,sep='\n')


#question 4

def plus_long_pref2(ch1,ch2):
    prefixes1=prefixes(ch1)
    prefixes2=prefixes(ch2)
    n=min(len(ch1),len(ch2))
    for i in range(n,-1,-1):
        if(prefixes1[i]==prefixes2[i]):
            print(prefixes2[i])
        else:
            break


            

chaine='AGCAAACTTT'
m1='AGCTTCAGCA'
m2='AGCTTCAGCA'
#ssmot(chaine)
#plus_long_pref(chaine,m1)
prefixes(chaine)