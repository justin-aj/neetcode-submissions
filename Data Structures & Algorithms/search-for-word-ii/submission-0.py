class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None  # store full word at the end node

class Solution:
    def findWords(self, board, words):
        # Build the trie
        root = TrieNode()
        for w in words:
            node = root
            for ch in w:
                if ch not in node.children:
                    node.children[ch] = TrieNode()
                node = node.children[ch]
            node.word = w  # store full word at the end node

        m, n = len(board), len(board[0])
        res = []

        def dfs(i, j, node):
            ch = board[i][j]
            if ch not in node.children:
                return

            child = node.children[ch]
            if child.word:
                res.append(child.word)
                child.word = None  # avoid duplicates

            board[i][j] = "#"  # mark visited
            for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
                if 0 <= x < m and 0 <= y < n and board[x][y] != "#":
                    dfs(x, y, child)
            board[i][j] = ch  # unmark

        for i in range(m):
            for j in range(n):
                dfs(i, j, root)

        return res
