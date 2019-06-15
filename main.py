from __future__ import print_function
from board import Board
from trie import Trie, add_words_from_file

def build_trie_from_filename(filename):
    root = Trie()
    add_words_from_file(root, filename)
    return root

root = build_trie_from_filename('dictionary.txt') #TODO(pickle this)

# score of alphabets from A-Z
score = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

def calc(word):
    return sum([score[ord(char) - ord('a')] for char in word])

print(sorted(list(set(Board(raw_input()).find_all_words(root))), key=calc, reverse=True))
