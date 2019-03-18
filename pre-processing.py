# name of file: movie-review-BOW.NB
import glob
import os
import re
import pandas as pd

train_neg_path = 'movie-review-HW2/aclImdb/train/neg'
train_pos_path = 'movie-review-HW2/aclImdb/train/pos'
test_neg_path = 'movie-review-HW2/aclImdb/test/neg'
test_pos_path = 'movie-review-HW2/aclImdb/test/pos'


def single_file(file_to_write, file_path):
    """
    This function opens each text file, makes all of the text lower case,
    removes punctuation characters and HTML tags, and outputs a 'master file'
    with all of the text per class
    """
    with open(file_to_write, "w") as outfile:
        for filename in glob.glob(os.path.join(file_path, '*.txt')):
            with open(filename, 'r', errors='ignore') as f:
                for line in f:
                    line = str(line)
                    line = line.lower()
                    line = re.sub('<[^<]+?>', '', line)
                    line = line.strip('!"#$%&\'()*+,./:;<=>?@[\]^_`{|}~')
                    outfile.write(line)


def make_train_features(vocab_file='movie-review-HW2/aclImdb/imdb.vocab',
                        train_folder='movie-review-HW2/aclImdb/train',
                        write_file="train_features.pickle"):
    columns = ['label', 'file_name']
    with open(vocab_file, errors='ignore') as file:
        for row in file:
            row = row.strip('\n')
            columns.append(row)
    train_features_df = pd.DataFrame(columns=columns)

    with open(write_file, "w") as outfile:
        for filename in glob.glob(os.path.join(train_folder + '/pos', '*.txt'))[:5]:
            with open(filename, 'r', errors='ignore') as f:
                for line in f:
                    line = str(line)
                    line = line.lower()
                    line = re.sub('<[^<]+?>', '', line)
                    new_line = ''
                    for i in line:
                        if i not in '!"#$%&\'()*+,./:;<=>?@[\]^_`{|}~':
                            new_line += i
                    line = new_line
                    row_dict = {k: 1 for k in columns}
                    row_dict['labels'] = 1
                    row_dict['filename'] = filename
                    for word in line.split():
                        try:
                            row_dict[word] += 1
                        except KeyError:
                            pass
                    return pd.DataFrame.from_dict(row_dict)
                    '''
                    we are having an issue with creating a dataframe from a
                    dictionary when the dictionary values are all scalars
                    '''

    # return train_features_df


print(make_train_features())


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


single_file('train_neg.txt', train_neg_path)
single_file('train_pos.txt', train_pos_path)
