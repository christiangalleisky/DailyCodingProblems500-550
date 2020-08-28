'''
Computes a number that is either a power of 7 or a sum of unique powers of 7
1 , 7, 8, 49...
'''


def get_sevenish_numbers(n):
    powers = [7 ** i for i in range(n)]
    totals = {0}

    for p in powers:
        totals |= {x + p for x in totals}

    return totals

def nth_sevenish_number(n):
    sevenish_numbers = get_sevenish_numbers(n)

    i = 1
    count, last_sevenish_number = 0, 0

    while count < n:
        if i in sevenish_numbers:
            count += 1
            last_sevenish_number = i
        i += 1

    return last_sevenish_number
    
    
def nth_sevenish_number_faster(n):

    answer = 0
    bit_place = 0

    while n:
        if (n & 1):
            answer += 7 ** bit_place

        n >>= 1
        bit_place += 1

    return answer
    
print(nth_sevenish_number_faster(4))
print(nth_sevenish_number(5))

