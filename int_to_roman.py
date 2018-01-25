def int_to_roman(number):
    number = int(number)
    d ={
        1:'I', 4:'IV', 5:'V', 9:'IX',
        10:'X', 40:'XL', 50:'L', 90:'XC',
        100:'C', 400:'CD', 500:'D', 900:'CM',
        1000:'M'
    }
    keys = list(reversed(sorted(d.keys())))
    roman = ''
    for x in keys:
        while number/x > 0:
            roman = roman + d[x]
            number = number - x
    return roman



if __name__ == '__main__':
    number = raw_input('Enter a number')
    print int_to_roman(number)