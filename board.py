import unittest

class Board(object):

    def __init__(self, board):
        if type(board) is list:
            self.board = board
        if type(board) is str and len(board) >= 16:
            self.init_from_string(board)
        elif type(board) is str:
            self.init_from_file(board)

    def init_from_string(self, boardstr):
        self.board = [list(row) for row in [boardstr[:4], boardstr[4:8], boardstr[8:12], boardstr[12:]]]

    def init_from_file(self, filename):
        with open(filename) as f:
            boardstr = f.readline().strip()
        self.init_from_string(boardstr)

    def get_neighbours(self, path, px, py):
        xs = {
         px - 1, px, px + 1}
        ys = {py - 1, py, py + 1}
        nbrs = ((x, y) for x in xs for y in ys if 0 <= x < 4 and 0 <= y < 4 and (x, y) not in path)
        return nbrs

    def build_words(self, node, path, hist):
        x, y = path[-1]
        nbrs = self.get_neighbours(path, x, y)
        words = [hist] if node.done else []
        for nx, ny in nbrs:
            char = self.board[nx][ny]
            if char not in node.chars:
                continue
            words += self.build_words(node.chars[char], path + [(nx, ny)], hist + char)
        return words

    def find_all_words(self, root):
        dimensions = [0, 1, 2, 3]
        words = []
        for x in dimensions:
            for y in dimensions:
                char = self.board[x][y]
                if char in root.chars:
                    words += self.build_words(root.chars[char], [(x, y)], char)
        return words


class TestBoard(unittest.TestCase):

    def setUp(self):
        import trie
        self.root = trie.Trie()
        self.board = Board([list('wint'), list('usre'), list('mmer'), list('oooo')])
        self.words = {'winter', 'summer', 'win', 'sure'}
        trie.add_multiple_words(self.root, list(self.words))

    def test_words_starting_with_w(self):
        char = self.board.board[0][0]
        found_words = self.board.build_words(self.root.chars[char], [(0, 0)], char)
        self.assertEqual(set(found_words), {'win', 'winter'})

    def test_words_starting_with_s(self):
        char = self.board.board[1][1]
        found_words = self.board.build_words(self.root.chars[char], [(1, 1)], char)
        self.assertEqual(set(found_words), {'summer'})

    def test_find_all_words(self):
        all_words = self.board.find_all_words(self.root)
        self.assertNotIn('sure', all_words)

    def test_init_from_file(self):
        self.board = Board('test_ruzzle.txt')
        testboard = [list('wint'), list('usre'), list('mmer'), list('oooo')]
        self.assertEqual(self.board.board, testboard)


if __name__ == '__main__':
    unittest.main()
# okay decompiling board.pyc
