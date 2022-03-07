# Code for a Word Ladder Graph using buckets

from adjacency_list import Graph

def buildGraph(wordFile):
    d = {} # Dictionary to store buckets & words
    g = Graph() # Graph to create the Word Ladder
    wfile = open(wordFile,'r')
    # Create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:] # Forms bucket tags from words
            if bucket in d: # If the word matches a bucket tag, put it in bucket word list
                d[bucket].append(word)
            else: # Otherwise, create a new bucket & put that word in a list
                d[bucket] = [word]
    # Add vertices and edges for words in the same bucket
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1,word2)
    return g