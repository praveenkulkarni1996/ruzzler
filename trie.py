import unittest

class Trie(object):
    def __init__(self):
        self.done = False
        self.chars = {}


def add_word(node, chars):
    if chars == '':
        node.done = True
        return
    elif chars[0] not in node.chars:
        node.chars[chars[0]] = Trie()
    if len(chars) == 1:
        node.chars[chars[0]].done = True
        return
    else:
        add_word(node.chars[chars[0]], chars[1:])

def add_words_from_file(root, filename):
    with open(filename) as f:
        for word in f:
            add_word(root, word.strip())


def show_all_words(root):
    words = []
    def show_words(words, node, prefix):
        if node.done:
            words.append(''.join(prefix))
        for nextchar in node.chars:
            show_words(words, node.chars[nextchar], prefix + [nextchar])
        return words
    return show_words(words, root, [])

def add_multiple_words(root, words):
    for word in words:
        add_word(root, word)


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.root = Trie()


    def test_add_single_word(self):
        add_word(self.root, list('winter'))

    
    def test_show_single_word(self):
        add_word(self.root, list('winter'))
        self.assertEqual(show_all_words(self.root), ['winter'])


    def test_adding_words(self):
        words = {'win', 'winter', 'winters'}
        for word in words:
            add_word(self.root, word)
        self.assertEqual(set(show_all_words(self.root)), words)


    def test_adding_words2(self):
        words = {'summer', 'winter', 'monsoon'}
        for word in words:
            add_word(self.root, word)
        self.assertEqual(set(show_all_words(self.root)), words)


    def test_add_multiple_words_function(self):
        words = {'win', 'winter', 'winters'}
        add_multiple_words(self.root, list(words))
        self.assertEqual(set(show_all_words(self.root)), words)


    def test_add_multiple_words_function_part2(self):
        words = {'summer', 'winter', 'monsoon'}
        add_multiple_words(self.root, list(words))
        self.assertEqual(set(show_all_words(self.root)), words)

    def test_adding_words_from_file(self):
        words = {'summer', 'winter', 'win', 'winters'}
        add_words_from_file(self.root, 'testdict.txt')
        self.assertEqual(set(show_all_words(self.root)), words)

    def test_following_words(self):
        words = {'summer', 'winter'}
        add_multiple_words(self.root, list(words))
        self.assertEqual(len(self.root.chars), 2)
         
        

if __name__ == '__main__':
    unittest.main()
