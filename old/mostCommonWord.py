from re import split


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words_list = split(r"[^a-z]+", paragraph.lower())
        word_gen = (word for word in words_list if word not in banned)
        words_dict = {}
        for word in word_gen:
            if word in words_dict:
                words_dict[word] += 1
            else:
                words_dict[word] = 1
        max_count = 0
        for word, count in words_dict.items():
            if count > max_count:
                max_count = count
                most_common_word = word
        return most_common_word
