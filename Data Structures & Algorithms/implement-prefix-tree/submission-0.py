class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False 

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.root 

        for c in word:
            # does this char exists?
            if c not in curr.children:
                    curr.children[c] = TrieNode() # if not exists then make a TrieNode
            curr = curr.children[c] # if already exists then update the curr 
        curr.endOfWord = True # mark endOfWord as true 

    def search(self, word: str) -> bool:
        curr = self.root 

        for c in word:
            if c not in curr.children: 
                return False # if this char exists in tree
            # if it exists 
            curr = curr.children[c] # update the curr 
        return curr.endOfWord 

    def startsWith(self, prefix: str) -> bool:
        curr = self.root 

        for c in prefix: # go char by char in prefix 
            if c not in curr.children:
                return False 
            curr = curr.children[c]
        return True 
        