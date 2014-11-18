# Generate text
from init import setup
import pickle
import sys
import random

if __name__ == '__main__':
    domain = sys.argv[1]
    stats_dir, _, _ = setup(domain)
    biplets = {}
    solos = {}
    with open(stats_dir + 'biplets.p', 'rb') as f:
        biplets = pickle.load(f)
    with open(stats_dir + 'solos.p', 'rb') as f:
        solos = pickle.load(f)

    words = list(solos.keys())
    TEXT_LINES_COUNT = 100
    for line_num in range(TEXT_LINES_COUNT):
        word_count = 2
        first_word = random.choice(words)
        second_word = solos[first_word]
        print(first_word.capitalize(), end="")
        while(second_word != '.' and word_count < 10):
            print(" {}".format(second_word), end="")
            third_word = biplets.get((first_word, second_word), '.')
            first_word, second_word = second_word, third_word
            word_count += 1
        print(".")
