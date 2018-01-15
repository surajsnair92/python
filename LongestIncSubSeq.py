def longestSubsequence(seq):
    lis = [1 for x in seq]
    for i in range(1, len(seq)):
        for j in range(0,i):
            if seq[i] > seq[j]:
                lis[i] = max(lis[i], lis[j]+ 1)
    return lis[len(seq) - 1]

if __name__ == '__main__':
    seq = [11,22,9,33,21,50,41,60]
    print longestSubsequence(seq)
