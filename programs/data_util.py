import re

from file_util import load_sentences,Corpus

def parse_words(sentence_list):
    listed = []
    total = set()
    for sentence in sentence_list:
        new = re.sub(r'[^\w\s]','',sentence)
        new = new.split()
        listed.append(new)
        total |= set(listed[-1])
    return listed,total

def load_words(sep = '.',direc = None):
    sentences = load_sentences(sep,direc)
    listed,total = parse_words(sentences)
    return Corpus(listed=listed,total=total)

def load_pairs(sep = '.',direc = None):
    sentences = load_sentences(sep,direc)
    listed,_ = parse_words(sentences)
    pairs = []
    for row in listed:
         new = [(row[i-1] + ' ' + row[i]) for i in range(1,len(row))]
         pairs.append(new)
    return Corpus(listed=pairs)