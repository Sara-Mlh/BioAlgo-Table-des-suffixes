def longest_common_prefix(s1,s2):
    i=0
    while i < len(s1) and i < len(s2) and s1[i]==s2[i]:
        i +=1
    return s1[:i]

print(longest_common_prefix("ACCATGT","ACCAGAC"))