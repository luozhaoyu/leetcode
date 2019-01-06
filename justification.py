class Solution:

    def pad_words(self, accumulated, L):
        if len(accumulated) == 1:
            return accumulated[0].ljust(max(len(accumulated[0]), L), ' ')

        raw_size = sum([len(i) for i in accumulated])
        remain_padding_size = L - raw_size
        result = []
        padded_words = 0
        while padded_words < len(accumulated):
            w = accumulated[padded_words]
            if len(accumulated) - 1 == padded_words:
                result.append(accumulated[-1])
                break

            if remain_padding_size % (len(accumulated) - padded_words - 1) == 0:
                pad_size = remain_padding_size / (len(accumulated) - padded_words - 1)
            else:
                pad_size = remain_padding_size / (len(accumulated) - padded_words - 1) + 1
            result.append(w.ljust(len(w) + pad_size, ' '))
            remain_padding_size -= pad_size
            padded_words += 1
        return ''.join(result)

    def deal_last_line(self, words, L):
        return ' '.join(words).ljust(L, ' ')
    # @param words, a list of strings

    # @param L, an integer

    # @return a list of strings

    def fullJustify(self, words, L):
        if len(words) == 1:
            return [words[0].ljust(max(len(words[0]), L), ' ')]

        accumulated = [words[0]]
        accumulated_size = len(words[0])
        result = []
        lines = []
        for w in words[1:]:
            if accumulated_size + 1 + len(w) <= L:
                accumulated.append(w)
                accumulated_size += 1 + len(w) 
            else:
                lines.append(accumulated)
                accumulated = [w]
                accumulated_size = len(w)
        if len(accumulated) > 0:
            lines.append(accumulated)
        i = 0
        while i < len(lines) - 1:
            result.append(self.pad_words(lines[i], L))
            i += 1
        result.append(self.deal_last_line(lines[-1], L))
        return result

s = Solution()
l = ["This", "is", "an", "example", "of", "text", "justification."]
print s.fullJustify(l, 1)
print s.fullJustify(l, 16)
print s.fullJustify([""], 6)
print s.fullJustify([""], 0)
print s.fullJustify(["a", "b", "c", "d", "e"], 3)
print s.fullJustify(["What","must","be","shall","be."], 12)
