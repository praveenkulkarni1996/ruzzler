from trie import *
from board import *

def build_trie_from_filename(filename):
    root = Trie()
    add_words_from_file(root, filename)
    return root

root = build_trie_from_filename('dictionary.txt')
print sorted(list(set(Board(raw_input()).find_all_words(root))), key=len)
