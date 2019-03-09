class Converter(object):
    
    def __init__(self):
        pass

    def roman_to_int(self, number):
        number = number.upper()
        nums = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
        result = 0
        for i in range(len(number)):
            val = nums[number[i]]
            if i+1 < len(number) and nums[number[i+1]] > val:
                result -= val
            else: result += val
        return result

    def int_to_roman(self, number):
        ints = (1000, 900,  500, 400, 100,  90, 50,  40, 10,  9,   5,  4,   1)
        nums = ('M',  'CM', 'D', 'CD','C', 'XC','L','XL','X','IX','V','IV','I')
        result = []
        for i in range(len(ints)):
            count = int(number / ints[i])
            result.append(nums[i] * count)
            number -= ints[i] * count
        return ''.join(result)