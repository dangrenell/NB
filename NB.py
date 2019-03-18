import numpy as np
import pickle
import os
import glob


# This function counts all words in file from vocab dictionary and returns dictionary of the count
def make_dict(vocab_file, train_file):
    vocab_dict = {}
    # Add one to each word for Laplace smoothing
    with open(vocab_file, errors='ignore') as file:
        for row in file:
            row = row.strip('\n')
            vocab_dict[row] = 1
    # Ignore all errors
    with open(train_file, errors='ignore') as file:
        # Adds one for each word found in File
        for line in file:
            for word in line.split():
                try:
                    vocab_dict[word] += 1
                except KeyError:
                    pass
    # Returns Vocab dictionary with count of each word
    total_sum = sum(vocab_dict.values())
    vocab_dict = {k: v / total_sum for k, v in vocab_dict.items()}
    return vocab_dict


comedy_dict = make_dict('movie-review-HW2/aclImdb/imdb.vocab',
                        'small_corpus/small_corpus_train_comedy.txt')
action_dict = make_dict('movie-review-HW2/aclImdb/imdb.vocab',
                        'small_corpus/small_corpus_train_action.txt')


def fit(train_file_pos, train_file_neg, train_folder,
        vocab_file='movie-review-HW2/aclImdb/imdb.vocab'):
    '''
    Function that generates model parameters and saves them as pickles.
    Inputs:
     - train_file_pos is the big preprocessed file for positive examples
     - train_file_neg is the big preprocessed file for negative examples
     - train_folder is the folder of the individual .txt files, which is needed
        for calculating class counts
     - vocab_file is the file containing the vocabulary
     Outputs:
      - Three different pickles, all are dictionaries.
        (1) A dictionary with two keys, 'pos' and 'neg', and their respective
            class probabilities.
        (2) A dictionary whose keys are all the words in the vocab_file, and
            whose values are the probabilities of those words, calculated from
            train_file_pos
        (3) A dictionary whose keys are all the words in the vocab_file, and
            whose values are the probabilities of those words, calculated from
            train_file_pos
    '''
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


fit('train_pos.txt', 'train_neg.txt', 'movie-review-HW2/aclImdb/train')

positive_probs_test = pickle.load(open("pickle_jar/pos_probs.pickle", "rb"))

positive_probs_test['fun']

'''
note: work in log space
'''
