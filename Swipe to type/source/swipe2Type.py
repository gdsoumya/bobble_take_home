from collections import defaultdict
import csv

# find length of LCS (Longest commin substring)
def lcs(X,Y): 
 
    m = len(X) 
    n = len(Y) 

    L = [[None]*(n+1) for i in range(0,m+1)] 
  
    for i in range(m+1): 
        for j in range(n+1): 
            if i == 0 or j == 0 : 
                L[i][j] = 0
            elif X[i-1] == Y[j-1]: 
                L[i][j] = L[i-1][j-1]+1
            else: 
                L[i][j] = max(L[i-1][j] , L[i][j-1]) 
  
    return L[m][n]  

# Load csv and sort words in order of popularity
def setupWordList(file):
    words={}
    wordList=[]
    with open(file, 'r') as file:
        reader = csv.reader(file)
        for word in reader:
            words[word[0]]=int(word[1])
            wordList.append(word[0])
    def sorting_func(w):
        return words[w]
    return (sorted(wordList, key= sorting_func, reverse= True), words)
    

if __name__ == "__main__":

    words, wordPop = setupWordList("EnglishDictionary.csv")
    inp = input()
    sug =  []
    for i in words :
        if i[0]==inp[0] and abs(len(i)-len(inp)) <3:
            sug.append([i,len(i)-lcs(i,inp)]) # appending no. of unmatched chars

    # sort depending on no. of unmatching chars and difference in length
    def sortLCS(l):
        return l[1] + 0.8*abs(len(inp)-len(l[0]))

    # sort depending on Popularity
    def sortPop(l):
        return wordPop[l[0]]

    res = sorted(sug, key= sortLCS)
    res = sorted(res[:20], key= sortPop, reverse=True)
    res = sorted(res[:10], key= sortLCS)
    
    print(", ".join([i[0] for i in res[:5]]))

