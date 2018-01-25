def closestTime(time):
    h, m = time.split(":")
    curr = int(h) * 60 + int(m)
    result = None
    for i in xrange(curr + 1, curr + 1441):
        t = i % 1440
        h, m = t // 60, t % 60
        result = "%02d:%02d" % (h, m)
        if set(result) <= set(time):
            break
    return result


def solution(flowers,k):
    n = len(flowers)
    f = [0] * (n + 1)
    i = 0

    def isValid(x, k, n, f):
        f[x] = 1
        if x + k + 1 <= n and f[x + k + 1] == 1:
            valid = True
            for i in range(k):
                if f[x + i + 1] == 1:
                    valid = False
                    break
            if valid: return True
        if x - k - 1 > 0 and f[x - k - 1] == 1:
            for i in range(k):
                if f[x - i - 1] == 1:
                    return False
            return True
        return False

    for x in flowers:
        i += 1
        if isValid(x, k, n, f): return i

    return -1

# print solution([3,1,5,4,2], 1)




def divide(dividend, divisor):
    result, dvd, dvs = 0, abs(dividend), abs(divisor)
    while dvd >= dvs:
        inc = dvs
        i = 0
        while dvd >= inc:
            dvd -= inc
            result += 1 << i
            inc <<= 1
            i += 1
    if dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0:
        return -result
    else:
        return result

print -1%2










def rose(p,k):
    table = [[0 for x in range(len(p))] for y in range(len(p))]
    for i, ele in enumerate(p):
        for j in range(i, len(p)):
            table[j][ele-1] = 1
    print table
rose([3,1,5,4,2], 1)