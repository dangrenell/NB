import csv
import numpy as np
from collections import Counter
from random import randint
import pickle
import os
import glob


def make_dict(vocab_file, train_file):
    vocab_dict = {}
    with open(vocab_file, errors='ignore') as file:
        for row in file:
            row = row.strip('\n')
            vocab_dict[row] = 1
    with open(train_file, errors='ignore') as file:
        for line in file:
            for word in line.split():
                try:
                    vocab_dict[word] += 1
                except KeyError:
                    pass
    total_sum = sum(vocab_dict.values())
    vocab_dict = {k: v / total_sum for k, v in vocab_dict.items()}
    return vocab_dict


comedy_dict = make_dict('movie-review-HW2/aclImdb/imdb.vocab',
                        'small_corpus/small_corpus_train_comedy.txt')
action_dict = make_dict('movie-review-HW2/aclImdb/imdb.vocab',
                        'small_corpus/small_corpus_train_action.txt')


def fit(train_file_pos, train_file_neg, train_folder, vocab_file='movie-review-HW2/aclImdb/imdb.vocab'):
    class1_count = len(glob.glob(os.path.join(train_folder + '/pos', '*.txt')))
    class2_count = len(glob.glob(os.path.join(train_folder + '/neg', '*.txt')))
    class1_prob = class1_count / (class1_count + class2_count)
    class2_prob = class2_count / (class1_count + class2_count)
    class_dict = {'pos': class1_prob, 'neg': class2_prob}
    pos_dict = make_dict(vocab_file, train_file_pos)
    neg_dict = make_dict(vocab_file, train_file_neg)
    try:
        os.makedirs('pickle_jar')
    except FileExistsError:
        pass
    pickle.dump(class_dict, open("pickle_jar/class_prior_prob.pickle", "wb"))
    pickle.dump(pos_dict, open("pickle_jar/pos_probs.pickle", "wb"))
    pickle.dump(neg_dict, open("pickle_jar/neg_probs.pickle", "wb"))

    '''
    make dictionaries for each train file
    calculate class probabilities
    output as pickles (3)
    '''


fit('train_pos.txt', 'train_neg.txt', 'movie-review-HW2/aclImdb/train')
#
positive_probs_test = pickle.load(open("pickle_jar/pos_probs.pickle", "rb"))

positive_probs_test['fun']

# csv.DictReader()
'''
read vocabulary in as a dictionary with values set to 1
for word in file:
    dict[word]+=1

normalize dict values by sum of dict values

class priors?

note: work in log space

'''
