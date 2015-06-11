# Analyze data
from init import setup, is_banned
import os
import re
import operator
from collections import Counter, defaultdict
import sys
import pickle


if __name__ == '__main__':
    domain = sys.argv[1]
    stats_dir, texts_dir, _ = setup(domain)
    biplets = defaultdict(lambda: Counter())
    solos = defaultdict(lambda: Counter())
    for file_path in os.listdir(texts_dir):
        try:
            with open(texts_dir + file_path, 'r') as f:
                try:
                    # For every triplet of words estimate
                    # P(3rd word | 1st word and 2nd word) == 'how frequently the 3rd word occurs after 1st and 2nd'
                    # P(2nd word | 1st word)
                    # P(word) == 'how frequently `word` occurs overall'
                    for line in f.readlines():
                        # Heuristic not to count wiki headers and footers
                        if is_banned(line):
                            break
                        words = re.findall("[a-zа-яё]+|\.", line.lower())
                        for triple in [words[i:i+3] for i in range(len(words)-3)]:
                            biplets[tuple(triple[:-1])][triple[-1]] += 1
                        for tup in [words[i:i+2] for i in range(len(words)-2)]:
                            solos[tup[0]][tup[-1]] += 1
                except UnicodeDecodeError as e:
                    continue
        except IsADirectoryError as e:
            continue

    # We will use the following model for text generation: we take the first
    # word in a sentence randomly weighted from the overall word distribution.
    # Then, iteratively, we look at the previous 2 (or 1 in case of the 2nd word
    # in a sentence) words and take the most 'probable' word that we saw after them
    # (from the dict `most_frequent_biplets` or `most_frequent_solos` accordingly)
    most_frequent_biplets = {}
    most_frequent_solos = {}
    for (biplet, thirds_set) in biplets.items():
        most_frequent_biplets[biplet] = max(thirds_set.items(), key=operator.itemgetter(1))[0]
    for (solo, seconds_set) in solos.items():
        most_frequent_solos[solo] = max(seconds_set.items(), key=operator.itemgetter(1))[0]

    # Write out
    with open(stats_dir + 'biplets.p', 'wb') as f:
        pickle.dump(most_frequent_biplets, f)
    with open(stats_dir + 'solos.p', 'wb') as f:
        pickle.dump(most_frequent_solos, f)
