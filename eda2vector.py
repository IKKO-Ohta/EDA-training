import os
import sys
import glob
import numpy as np
from scipy.spatial.distance import cosine
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer


def EDAread(path):
    '''
    return : EDAファイルに含まれている単語
    '''
    words = []
    with open(path,'r') as f:
        for line in f:
            if ('ID' in line) or (line == '\n'):
                continue
            else:
                line = line.rstrip().split(' ')
                words.append(line[2])
    return words

def tf(doc):
    vectorizer = CountVectorizer(token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(doc)
    terms = vectorizer.get_feature_names()
    return features, terms

def tfidf(docs):
    vectorizer = TfidfVectorizer(min_df=1, max_df=50, token_pattern=u'(?u)\\b\\w+\\b')
    features = vectorizer.fit_transform(docs)
    terms = vectorizer.get_feature_names()
    return features, terms

if __name__ == '__main__':
    files_path = glob.glob('../resource/corpus/*.tree')
    #['../resource/corpus/CWJ-train.tree', '../resource/corpus/EHJ-train.tree',
    # '../resource/corpus/JNL-train.tree', '../resource/corpus/NKN-test.tree',
    # '../resource/corpus/NKN-train.tree', '../resource/corpus/NPT-train.tree',
    # '../resource/corpus/RCP-train.tree']
    test_corpus_index = files_path.index('../resource/corpus/NKN-test.tree') #3。後でテスト分だけ抜くので
    docs = []

    for file_path in files_path:
        corpora = ' '.join(EDAread(file_path))
        docs.append(corpora)

    features, terms = tfidf(docs)
    print(terms)
    print(features.toarray())

    test_corpus = features.toarray()[test_corpus_index]
    trains_matrix = np.delete(features.toarray(),test_corpus_index,0)
    files_path.pop(test_corpus_index)

    result = {}
    for key,corpus in zip(files_path,trains_matrix):
        similarity =1 - cosine(test_corpus,corpus)
        result[key] = similarity
    
    for key,value in result.items():
        print(key,value)
