import csv
import numpy as np
from collections import Counter
from random import randint


class NB:
    def __init__(self):

        # def text_file_to_list(self, file_name):
        #     """Converts the file to a list of words"""
        #     with open(file_name) as f:
        #         words = f.read().split()
        #     return words

        # def relative_freq_dict(self, words):
        #     """
        #     Creates a dictionary/counter with words as keys and counts as values.
        #     Normalizes the counts. Values now represent relative frequencies.
        #     """
        #     counts = Counter(words)

        #     total = sum(counts.values())
        #     for key in counts:
        #         counts[key] /= total

        #     return counts

        # def sentence_prob(self, text, model):
        #     """Calculates the product of the probabilities of the words in an input string given a model."""
        #     sentence_words = text.split()
        #     prob = 1
        #     for word in sentence_words:
        #         if word in model:
        #             prob *= model[word]
        #         else:
        #             prob *= .00001
        #     return prob


change

    def train(self, training_file, test_file, save_file):
        with open(training_file):
            probs = {}
            for i in training_file:
                probs[i]
