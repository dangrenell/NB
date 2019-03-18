# name of file: movie-review-BOW.NB
import glob
import os
import re

train_neg_path = 'movie-review-HW2/aclImdb/train/neg'
train_pos_path = 'movie-review-HW2/aclImdb/train/pos'
test_neg_path = 'movie-review-HW2/aclImdb/test/neg'
test_pos_path = 'movie-review-HW2/aclImdb/test/pos'


def single_file(file_to_write, file_path):
    with open(file_to_write, "w") as outfile:
        for filename in glob.glob(os.path.join(file_path, '*.txt')):
            with open(filename, 'r', errors='ignore') as f:
                for line in f:
                    line = str(line)
                    line = line.lower()
                    line = re.sub('<[^<]+?>', '', line)
                    line = line.strip('!"#$%&\'()*+,./:;<=>?@[\]^_`{|}~')
                    outfile.write(line)
