from string import ascii_lowercase

letters = {}
for letter in ascii_lowercase:
    letters[letter] = 0

class Solution:
    def sortString(self, s: str) -> str:

        global letters

        for char in s:
            letters[char] += 1

        forward = True
        output = ""
        stop = False

        while not stop:
            if forward:
                last_appended = " "
                letter_gen = (letter for letter in ascii_lowercase if letters[letter] > 0 and letter > last_appended)
            else:
                last_appended = "~"
                letter_gen = (letter for letter in ascii_lowercase[::-1] if letters[letter] > 0 and letter < last_appended)
            forward = not forward
            stop = True
            for letter in letter_gen:
                stop = False
                output += letter
                last_appended = letter
                letters[letter] -= 1

        return output
