def reversePrefix(word, ch):
        if ch in word:
            r = word[:word.index(ch)+1][::-1]
            return r+word[word.index(ch)+1:]
        return word