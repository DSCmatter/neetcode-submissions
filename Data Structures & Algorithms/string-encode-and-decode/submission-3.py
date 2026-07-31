class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res, i = [], 0 # ptr i to tell what position we are in 

        while i < len(s): # iterate and read strings till out of balance 
            j = i
            while s[j] != "#": # keep incrementing till we find # --> which means completing the word
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length]) # j at delimeter -- first char in string
            # above code will read the one word 

            i = j + 1 + length # go to next word 

        return res
