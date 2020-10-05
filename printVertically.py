class Solution:
    def printVertically(self, s: str) -> List[str]:

        words = s.strip().split(" ")
        num_words = len(words)

        len_words = {}
        for word in words:
            if word not in len_words:
                len_words[word] = len(word)

        max_len = max(len_words.values())
        words = [words[i].ljust(max_len, " ") for i in range(num_words)]

        vertical = ["".join([word[i] for word in words]).rstrip() for i in range(max_len)]
        return vertical
