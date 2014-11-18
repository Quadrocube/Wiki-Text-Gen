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
                    for line in f.readlines():
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
