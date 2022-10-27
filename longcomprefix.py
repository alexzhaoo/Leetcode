# strs: List[str]) -> str:
def longestCommonPrefix(strs):
    lcp = ""
    num_strs = len(strs)
    i = 0
    while True:
        try:
            c = strs[0][i]
            for x in range(1, num_strs):
                if strs[x][i] != c:
                    return lcp
            lcp += c
            i += 1
        except IndexError:
            return lcp


print(longestCommonPrefix(["baab", "bacb", "b", "cbc"]))