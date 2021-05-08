# https://leetcode.com/problems/number-complement/

# flip the bits of the number

def findComplement_slow_xor(num):
    num2 = num + 1

    # increment num2 until it is a power of 2
    while (num2 & (num2-1)) != 0:
        num2 += 1
    
    # xor num with all 1s
    num2 -= 1
    return num ^ num2

def findComplement_xor(num):
    number_of_bin_digits = len(bin(num)) - 2
    all_ones = 2 ** (number_of_bin_digits) - 1
    return num ^ all_ones

# print(findComplement(5))

def findComplement_str(num):
    num_binary = bin(num)
    ans = ''
    for i in num_binary[2:]:
        if i == '0':
            ans += '1'
        else:
            ans += '0'
    return int(ans, 2)

print(findComplement_str(5))
