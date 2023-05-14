def SousMot(M,T,i):
    return M in T[i:]

def OccurMot(M,T):
  V=[]
  t=len(T)
  m=len(M)
  for i in range(0,t):
      if T[i:i+m]==M :
          V.append(i)
  return V
 

T="ABBBABCDBSHDSDABBWYQQBDABDSHDSAB"
M="ABB"
res =SousMot(M,T,15)
res1=SousMot(M,T,3)
print("TEST QUESTION 1 :",res,res1)
print('TEST QUESTION 2 :')
occ=OccurMot(M,T)
print(occ)
print("TEST QUESTION 3 :")


for i in range(0,len(occ)):
    print("occurance n°",i+1,"from:",occ[i],"to :",occ[i]+len(M)-1)
