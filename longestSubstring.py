def longestSubstring(str):
    n = len(str)
    d = dict()
    i = 0
    ans = 0
    for j in range(0,n):
        if str[j] in d:
            i = max(i, d[str[j]])
        ans = max(ans, j - i + 1)
        d[str[j]] = j + 1
    return ans

print longestSubstring('pwwkefew')
