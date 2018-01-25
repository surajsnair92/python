def count_and_say_impl(num):
    s = '1'
    for _ in range(num-1):
        curr = s[0]
        temp = ''
        count = 0
        for x in s:
            if curr == x:
                count+=1
            else:
                temp = temp + str(count) + curr
                curr = x
                count = 1
        temp = temp + str(count) + curr
        s = temp
    return s

if __name__ == '__main__':
    num = raw_input('Enter the number')
    print count_and_say_impl(int(num))