vowels = {}
vowels["a"] = 1
vowels["e"] = 1
vowels["i"] = 1
vowels["o"] = 1
vowels["u"] = 1
vowels["A"] = 1
vowels["E"] = 1
vowels["I"] = 1
vowels["O"] = 1
vowels["U"] = 1


def translate_word(word, idx):
    global vowels
    first = word[0]
    trans_word = (word[1:] + first) if first not in vowels else word
    trans_word += "ma" + "".join((idx + 1) * ["a"])
    return trans_word


class Solution:
    def toGoatLatin(self, S: str) -> str:
        words = S.split(" ")
        trans_words = [translate_word(words[i], i) for i in range(len(words))]
        return " ".join(trans_words).strip()
