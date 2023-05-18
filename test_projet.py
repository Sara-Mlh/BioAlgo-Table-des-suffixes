import time
import random
import string
import matplotlib.pyplot as plt
import pandas as pd
#QUESTION 1 : TABLE DE SUFFIXES
def TABSUFF(chaine):
    indexes = []
    suffixes = []
    for i in range(len(chaine)):
        suffixes.append(chaine[i:])
        indexes.append(i)
    suffixes = sorted(suffixes) #suffixes contient les suffixes eux meme
    indexes.sort(key=lambda x: chaine[x:])  #indexes contient les indices des suffixes dans le texte
    return indexes, suffixes

#QUESTION 2 : RECHERCHE DU MOTIF 
def search_pattern(text, pattern):
    Tabsuffix = TABSUFF(text)[1]
    indexes = []
    for suffix in enumerate(Tabsuffix):
        if pattern == suffix[1][:len(pattern)]:
            index = len(text) - len(suffix[1])
            indexes.append(index)      #ajouer l occurence i a la liste indexes
    return indexes


#QUESTION 3 : HTR TABLE

def prefix_commun(word1, word2):
    l1 = len(word1)
    l2 = len(word2)
    i = 0
    long = ""
    while i < min(l1, l2) and word1[i] == word2[i]:
        long += word1[i]
        i += 1
    return long


def HTR(text):
    _, suffixes = TABSUFF(text)
    htr_table = []
    htr_len = []
    for i in range(1, len(suffixes)):
        suffix1 = suffixes[i]
        suffix2 = suffixes[i - 1]
        htr_table.append(prefix_commun(suffix1, suffix2))  # htr table contient les préfixes communs
        htr_len.append(len(prefix_commun(suffix1, suffix2)))  # htr len est la reel et qui contient le len des prefixes
    return htr_table, htr_len


#QUESTION 4: LONGEST REPEATED FACTORS
def longest_repeated_factors(text):
    _, htr = HTR(text)
    max_htr = max(htr)
    suffixes, _ = TABSUFF(text)
    factors = []
    # get the suffixes indexes of the max htr from the htr table
    for i in range(len(htr)):
        if htr[i] == max_htr:
            factor = text[suffixes[i]: suffixes[i] + max_htr]
            if factor not in factors:
                factors.append(factor)
    return factors


#QUESTION 5: FACTORS REPEATED AT LEAST 3 TIMES
def repeated_factors3(text):
    _, htr = HTR(text)
    suffixes, _ = TABSUFF(text)
    factors = []
    repeated_factors = []
    for i in range(len(htr)):
        if htr[i] >= 3:
            factor = text[suffixes[i]: suffixes[i] + htr[i]]
            factors.append(factor)
    for factor in factors:
        count = factors.count(factor)
        if count >= 3 and factor not in repeated_factors: # si le nombre de repetitions count est minimum 3 alors ajouter l elemnt a la liste des facteurs
            repeated_factors.append(factor)
    return repeated_factors


#QUESTION 6: INVERSE SUFFIX TABLE
def Inverse_TS(text):
    suffixes, _ = TABSUFF(text)
    inverse = [0] * len(suffixes)
    for i in range(len(suffixes)):
        index = suffixes[i]
        inverse[index] = i
    return inverse


#QUESTION 7: SHORTEST UNIQUE FACTOR
def Shortest_unique_factors(text):
    _, htr = HTR(text)
    suffixes, _ = TABSUFF(text)
    factors = []
    for i in range(1, len(htr)):
        factor = text[suffixes[i]: suffixes[i] + htr[i]]
        if htr[i] > 0 and text.count(factor) == 1:
            if not factors:
                factors.append(factor)
            else:
                if factor not in factors:
                    factors.append(factor)  # ajouter a la liste des facteurs uniques
    if factors:
        min_length = len(min(factors, key=len))  #la longeur minimale d'un facteur de la liste
        shortest = [factor for factor in factors if len(factor) == min_length]  #ajouter tout les elements qui ont la mm longeur minimale
        return shortest
    else:
        return []


#QUESTION 8: SUPERMAXIMAL FACTORS
def find_supermaximal_repetitions(text):
    _, lcp = HTR(text)
    suffixes, _ = TABSUFF(text)
    n = len(text)
    repetitions = []
    for i in range(1, n):
        if i < len(lcp):  # Vérifier si l'indice est valide
            lcp_length = lcp[i]  # Longueur du préfixe commun avec le suffixe précédent
            suffix_i = suffixes[i]  # Indice du suffixe courant
            factor = text[suffix_i: suffix_i + lcp_length]  # Facteur correspondant au préfixe commun
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


#QUESTION 9: LONGEST COMMON FACTOR BETWEEN TWO WORDS
def Longest_common_factor(T1, T2):
    # Concatenate the texts with a unique separator
    concat_text = T1 + '#' + T2

    # Construct the suffix table for the concatenated text
    suffixes, _ = TABSUFF(concat_text)

    # Calculate the LCP table for the concatenated text
    _, lcp = HTR(concat_text)

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
word = "mississippi"
word1 ="rississippi"
pattern = "ssi"
ts,_= TABSUFF(word)
_,htr = HTR(word)

print("\nWord :",word)
print("\nPattern :",pattern)
print("\nThe suffix table of the word {} is : \n {}".format(word,ts))
print("\nThe pattern {} is in the positions : {}".format(pattern,search_pattern(word,pattern)))

print("\nTable htr of {} is :\n {} ".format(word,htr))

print("\nLongest factors of {} are: {}".format(word,longest_repeated_factors(word)))

print("\nThe factors that are repeated at least 3 times in the word {} are: {}".format(word,repeated_factors3(word)))

print("\nThe inverse of suffix table of the word {} is : \n {}".format(word,Inverse_TS(word)))
#print(mot[0:5])
print("\nThe shortest unique factors of the word {} are : {}".format(word,Shortest_unique_factors(word)))
print("\nThe super maximales of the word {} are : {}".format(word,find_supermaximal_repetitions(word)))
print("\nThe longest commun factor words {}  and {} are : {}".format(word,pattern,Longest_common_factor(word,word1)))

#Test de temps d execution
#Fonction qui genere un text d une taille donnée

def generate_text(size):
    return ''.join(random.choices(string.ascii_lowercase, k=size))

#Fonction qui calcule le temps d'éxecution
def measure_execution_time(func, text):
    start_time = time.time()
    result = func(text)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

text_sizes = [100, 200, 600, 1000, 2000, 5000]  # Tailles de texte variables à tester
execution_times_func1 = []
execution_times_func2 = []
execution_times_func3 = []
execution_times_func4 = []
execution_times_func5 = []
execution_times_func6 = []
execution_times_func7 = []

for size in text_sizes:
    # Générer le texte de taille 'size'
    text = generate_text(size)  # Remplacez cette fonction par celle qui génère vos textes

    # Mesurer le temps d'exécution pour chaque fonction
    time_func1 = measure_execution_time(TABSUFF, text)
    time_func2 = measure_execution_time(HTR, text)
    time_func3 = measure_execution_time(longest_repeated_factors, text)
    time_func4 = measure_execution_time(repeated_factors3, text)
    time_func5 = measure_execution_time(Inverse_TS, text)
    time_func6 = measure_execution_time(Shortest_unique_factors, text)
    time_func7 = measure_execution_time(find_supermaximal_repetitions, text)
    #time_func8= measure_execution_time(Longest_common_factor, text)
    # ...
    execution_times_func1.append(time_func1)
    execution_times_func2.append(time_func2)
    execution_times_func3.append(time_func3)
    execution_times_func4.append(time_func4)
    execution_times_func5.append(time_func5)
    execution_times_func6.append(time_func6)
    execution_times_func7.append(time_func7)


    # Afficher les temps d'exécution
    print(f"Taille du texte : {size}")
    print(f"Temps d'exécution de fonction1 : {time_func1} secondes")
    print(f"Temps d'exécution de fonction2 : {time_func2} secondes")
    print(f"Temps d'exécution de fonction3 : {time_func3} secondes")
    print(f"Temps d'exécution de fonction4 : {time_func4} secondes")
    print(f"Temps d'exécution de fonction5 : {time_func5} secondes")
    print(f"Temps d'exécution de fonction6 : {time_func6} secondes")
    print(f"Temps d'exécution de fonction7 : {time_func7} secondes")

text_sizes = [100, 200, 600, 1000, 2000, 5000]  # Variable text sizes to test

# Create a dictionary to store the execution times for each function
execution_times = {
    'Table suffixes TS': [],
    'Table HTR': [],
    'PlusLongsFacteursRépetes': [],
    'Repeated_Factors3': [],
    'Inverse TS': [],
    'Courts Facteurs uniques': [],
    'Repetitions Supermximales': []
}

# Iterate over each text size
for size in text_sizes:
    text = generate_text(size)  # Generate text of size 'size'

    # Measure the execution time for each function
    execution_times['Table suffixes TS'].append(measure_execution_time(TABSUFF, text))
    execution_times['Table HTR'].append(measure_execution_time(HTR, text))
    execution_times['PlusLongsFacteursRépetes'].append(measure_execution_time(longest_repeated_factors, text))
    execution_times['Repeated_Factors3'].append(measure_execution_time(repeated_factors3, text))
    execution_times['Inverse TS'].append(measure_execution_time(Inverse_TS, text))
    execution_times['Courts Facteurs uniques'].append(measure_execution_time(Shortest_unique_factors, text))
    execution_times['Repetitions Supermximales'].append(measure_execution_time(find_supermaximal_repetitions, text))

# Create a DataFrame for each function
df_TS = pd.DataFrame({'Taille du texte': text_sizes, 'Temps d\'exécution': execution_times['Table suffixes TS']})
df_HTR = pd.DataFrame({'Taille du texte': text_sizes, 'Temps d\'exécution': execution_times['Table HTR']})
df_PLF = pd.DataFrame({'Taille du texte': text_sizes, 'Temps d\'exécution': execution_times['PlusLongsFacteursRépetes']})
df_RF3 = pd.DataFrame({'Taille du texte': text_sizes, 'Temps d\'exécution': execution_times['Repeated_Factors3']})
df_ITS = pd.DataFrame({'Taille du texte': text_sizes, 'Temps d\'exécution': execution_times['Inverse TS']})
df_CFU = pd.DataFrame({'Taille du texte': text_sizes, 'Temps d\'exécution': execution_times['Courts Facteurs uniques']})
df_RSM = pd.DataFrame({'Taille du texte': text_sizes, 'Temps d\'exécution': execution_times['Repetitions Supermximales']})

# Print the DataFrames
print("Table suffixes TS:")
print(df_TS)

print("Table HTR:")
print(df_HTR)

print("PlusLongsFacteursRépetes:")
print(df_PLF)

print("Repeated_Factors3:")
print(df_RF3)

print("Inverse TS:")
print(df_ITS)

print("Courts Facteurs uniques:")
print(df_CFU)

print("Repetitions Supermximales:")
print(df_RSM)

#Le plot de comparaison

plt.plot(text_sizes, execution_times_func1, label='Table suffixes TS')
plt.plot(text_sizes, execution_times_func2, label='Table HTR')
plt.plot(text_sizes, execution_times_func3, label='PlusLongsFacteursRépetes')
plt.plot(text_sizes, execution_times_func4, label='Repeated_Factors3')
plt.plot(text_sizes, execution_times_func5, label='Inverse TS')
plt.plot(text_sizes, execution_times_func6, label='Courts Facteurs uniques')
plt.plot(text_sizes, execution_times_func7, label='Repetitions Supermximales')

plt.xlabel('Taille du texte')
plt.ylabel('Temps d\'exécution (secondes)')
plt.title('Comparaison des temps d\'exécution')
plt.legend()

plt.show()

