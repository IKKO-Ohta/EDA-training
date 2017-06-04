#=====================================================================================
#                       BCCWJ2vec.py
#                             by Ikko ota
#                             Last change 02 06 2017
#=====================================================================================

# 使い方：python BCCWJ2Vec.py
# BCCWJ(6種類)の全組み合わせ(2^6-1=)63通りの全てについて、tf-idfによる類似度を求める。
# 次元削減の手法はLSIで、n=7で累積寄与率は100%ある。

#-------------------------------------------------------------------------------------
#                        require
#-------------------------------------------------------------------------------------

import os
import sys
import glob
import numpy as np
from collections import OrderedDict
from scipy.spatial.distance import cosine
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import TruncatedSVD
from sklearn.preprocessing import Normalizer

#-------------------------------------------------------------------------------------                                    
#                        defs                                                                               
#-------------------------------------------------------------------------------------  

def gen_patterns():
    cases =[]
    for a in range(2):
        for b in range(2):
            for c in range(2):
                for d in range(2):
                    for e in range(2):
                        for f in range(2):
                            cases.append((a,b,c,d,e,f))
    cases.pop(0) #(0,0,0,0,0,0)
    return cases

def grouping(cases,corpus_list):
    groups = []
    for case in cases:
        group = []
        for (i,flag) in enumerate(case):
            if flag == 1:
                group.append(corpus_list[i])
            else:
                continue
        groups.append(group)
    return groups

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

def reduction(x):
    '''
    dimensionality reduction using pca
    '''
    print("reductioning...","from: ",x.shape)
    svd = TruncatedSVD(n_components=7)
    x = svd.fit_transform(x)
    print("累積説明率:",sum(svd.explained_variance_ratio_))
    print("to:",x.shape)
    return x
#-------------------------------------------------------------------------------------                                    
#                        main                                                                                          
#-------------------------------------------------------------------------------------  

if __name__ == '__main__':
    # filenames
    OC = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/OC*.tree")
    OW = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/OW*.tree")
    OY = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/OY*.tree")
    PB = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/PB*.tree")
    PM = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/PM*.tree")
    PN = glob.glob("/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/corpus/2012/PN*.tree")
    TEST = "/mnt/mqs02/home/ikko/work/EDA_cutoff/resource/test/sakata-2017-02.tree"
    
    patterns = gen_patterns()
    corpus_paths = [OC,OW,OY,PB,PM,PN]
    groups = grouping(patterns,corpus_paths)

    docs = []
    for group in groups:
        words_by_group = []
        for files in group:
            words = []
            for file in files:
                w = EDAread(file)
                words.append(w)
            words = sum (words,[]) 
            words_by_group.append(words)
        words_by_group = sum(words_by_group,[])
        docs.append(words_by_group)

    testword = EDAread(TEST)
    docs.append(testword)
    docs = [' '.join(d) for d in docs]
    #features, terms = tf(docs)
    features, terms = tfidf(docs)
    matrix = features.toarray()
    matrix = reduction(matrix)
    test,corp = matrix[-1],matrix[:-1]
    
    result = OrderedDict()
    for keys,corpus in zip(patterns,corp):
        similarity = 1 - cosine(test,corpus)
        result[keys] = similarity 

    sim = np.asarray([v for v in result.values()])
    np.save("simis.npy",sim)
    print(sim)

#=====================================================================================
#                        END
#=====================================================================================
