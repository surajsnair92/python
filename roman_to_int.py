def roman_to_int(roman):
    d = {
        'I':1, 'V':5,
        'X':10, 'L':50,
        'C': 100, 'D':500,
        'M':1000
    }
    index = 0
    number = 0
    while index < len(roman):
        if index > 0 and d[roman[index]] > d[roman[index-1]]:
            number = number + d[roman[index]] - 2 * number
        else:
            number +=d[roman[index]]
        index +=1
    return number



if __name__ == '__main__':
    roman = raw_input('Enter the roman number')
    print roman_to_int(roman);