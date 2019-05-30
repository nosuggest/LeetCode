class tire():
    def __init__(self):
        self.children = {}
        self.isWord = False

class WordDictionary(object):
    def __init__(self):
        self.root = tire()

    def addWord(self,word):
        node = self.root

        for c in word:
            if c not in node.children:
                node.children[c] = tire()
            node = node.children[c]
        node.isWord=True

    def search(self,word):

        def dfs(node,i =0):
            if i == len(word):
                return node.isWord
            if word[i] =='.':
                return any([dfs(key,i+1) for key in node.children.values()])
            if word[i] in node.children:
                return dfs(node.children[word[i]],i+1)
                    #return True
            return False
        node = self.root
        return dfs(node,0)
