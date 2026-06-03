class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res = []
        line = []          # words in the current line
        line_len = 0       # sum of word lengths (no spaces) in current line

        for w in words:
            # +len(line) accounts for one min space between each existing word and w
            if line_len + len(w) + len(line) > maxWidth:
                # flush current line, fully justified
                gaps = len(line) - 1
                if gaps == 0:
                    # single word: left-justify, pad right
                    res.append(line[0] + ' ' * (maxWidth - line_len))
                else:
                    spaces = maxWidth - line_len
                    base, extra = divmod(spaces, gaps)
                    # left gaps get one extra space when it doesn't divide evenly
                    built = []
                    for i, word in enumerate(line):
                        built.append(word)
                        if i < gaps:
                            built.append(' ' * (base + (1 if i < extra else 0)))
                    res.append(''.join(built))
                line = []
                line_len = 0
            line.append(w)
            line_len += len(w)

        # last line: left-justified, single spaces, pad right
        last = ' '.join(line)
        res.append(last + ' ' * (maxWidth - len(last)))
        return res
