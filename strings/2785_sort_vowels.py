VOWELS = ("A", "E", "I", "O", "U")
NUM_VOWELS = 2 * len(VOWELS)
VOWEL_TO_INDEX = {v: i for i, v in enumerate(VOWELS)}
VOWEL_TO_INDEX.update({v.lower(): i + len(VOWELS) for i, v in enumerate(VOWELS)})
INDEX_TO_VOWEL = {i: v for v, i in VOWEL_TO_INDEX.items()}


class Solution:
    def is_vowel(self, c: str) -> bool:
        return c.upper() in VOWELS

    def sortVowels(self, s: str) -> str:
        vowel_counts = [0] * NUM_VOWELS
        for c in s:
            if not self.is_vowel(c):
                continue
            i = VOWEL_TO_INDEX[c]
            vowel_counts[i] += 1

        i = 0
        while i < NUM_VOWELS and vowel_counts[i] == 0:
            i += 1
        if i == NUM_VOWELS:
            return s

        n = len(s)
        new_chars = list(s)

        j = 0
        while j < n:
            if not self.is_vowel(new_chars[j]):
                j += 1
                continue

            v = INDEX_TO_VOWEL[i]
            new_chars[j] = v
            j += 1

            vowel_counts[i] -= 1
            if vowel_counts[i] > 0:
                continue

            while i < NUM_VOWELS and vowel_counts[i] == 0:
                i += 1
            if i == NUM_VOWELS:
                break

        return "".join(new_chars)
