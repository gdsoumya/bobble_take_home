from collections import defaultdict
import csv
import time

# Trie DS
class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode) #defaults to a TrieNode instance
        self.isLeaf = False
    def insert(self, word):
        node = self
        for w in word:
            node = node.children[w]
        node.isLeaf = True

    def search(self, word):
        node = self
        for w in word:
            if w in node.children:
                node = node.children[w]
            else:
                return []

        result = []
        self.traverse(node, list(word), result)
        return [''.join(r) for r in result]

    def traverse(self, root, prefix, result):
        if root.isLeaf:
            result.append(prefix[:]) #copy and append
        for c,n in root.children.items(): # iterrate over char and corresponding node
            prefix.append(c)
            self.traverse(n, prefix, result)
            prefix.pop(-1) #backtrack

# Load csv
def setupWordList(file):
    words={}
    with open(file, 'r') as file:
        reader = csv.reader(file)
        for word in reader:
            words[word[0]]=int(word[1])
    return words

# Create the Trie
def setupTrie(words):
    root = TrieNode()
    for w in words:
        root.insert(w)
    return root

# Main function
def startSmartSuggest(words, root):
    c=''
    st=''

    # sort depending on popularity
    def sortPop(w):
        return words[w]

    while True :
        c=input()[0]
        if c=='#':
            break
        start = time.perf_counter_ns() # start time
        st+=c
        res = root.search(st)
        sorted_lst = sorted(res, key= sortPop, reverse= True) # sort depending on popularity
        end = time.perf_counter_ns()  # end time
        elapsed = (end- start)/1000
        if res==[]:
            print("%-50s %4.3f%s" % ("No match Found !!",elapsed,"μs"))
            break
        else:
            if len(sorted_lst)<5:
                count=len(sorted_lst)
            else:
                count = 5
            sorted_lst=sorted_lst[:count]
            sorted_lst = ", ".join(sorted_lst)
            print("%-50s %4.3f %s" %(sorted_lst, elapsed,"μs"))
    print("Exiting")


if __name__ == "__main__":
    words = setupWordList("EnglishDictionary.csv")
    root = setupTrie(words)
    startSmartSuggest(words, root)
