class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(" ")
        words = sorted(words, key=len)  # sorted uses a stable sort algorithm
        return " ".join(words).capitalize()
