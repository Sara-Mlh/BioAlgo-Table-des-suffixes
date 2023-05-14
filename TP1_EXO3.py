def bord(mot):
    bords=[]
    for i in range(len(mot)):
        if(mot[:i]==mot[-i:]):
            bords.append(mot[:i])
    return bords

'''def Periode(mot):
    nb_p=[]
    mots_p=[]
    for i in range(len(mot)):
        end=i+1
        while(mot[i]==mot[end]):
            nb+=1
            end+=1
        nb_p.append(nb)
        mots_p.append(mot[i:end])'''



test ="aataata"
M="abcabdefeabcab"
tab_bords=bord(test)
print(tab_bords)
print(bord(M))

