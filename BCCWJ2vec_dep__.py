#=====================================================================================
#                       BCCWJ2vec_dep__.py
#                             by Ikko ota
#                             Last change 02 06 2017
#=====================================================================================

# 使い方: $python BCCWJ2vec_dep__.py
# BCCWJ2vec.pyと同じくグループのTFIDF比較だが、こちらではdep_gramを素性としてカウントする.
# すなわち、単語を素性とする代わりに、
# 文の語と語の全ての組み合わせを列挙し、それらを一文から抽出できる素性とする。

#-------------------------------------------------------------------------------------
#                        require
#-------------------------------------------------------------------------------------
import os
import sys
import glob
import numpy as np
import itertools
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
    with open(path,'r') as f:
        dep_words = []
        words = []
        for line in f:
            line = line.rstrip().split()
            if (not line) or ('ID' in line[0]):
                try:
                    dep_words.append(make_dep_feature(tuple(words)))
                except:
                    pass
                words = []
                continue
            else:
                words.append(line[2])
    return dep_words

def make_dep_feature(words):
    """
    N_C_2を組んで、それらを単語扱いにしてから返す。
    """
    if not words:
        return
    features = list(itertools.combinations(words,2))
    ans = []
    for feature in features:
        ans.append("".join(feature))
    return ans


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
    docs = [[d for d in doc if d ] for doc in docs if doc]
    docs = [' '.join([' '.join(d) for d in doc]) for doc in docs]
    features, terms = tfidf(docs)
    matrix = features.toarray()
    matrix = reduction(matrix)
    test,corp = matrix[-1],matrix[:-1]
    
    result = OrderedDict()
    for keys,corpus in zip(patterns,corp):
        similarity = 1 - cosine(test,corpus)
        result[keys] = similarity 

    sim = np.asarray([v for v in result.values()])
    np.save("dep_simis.npy",sim)
    print(sim)

#=====================================================================================
#                        END
#=====================================================================================
