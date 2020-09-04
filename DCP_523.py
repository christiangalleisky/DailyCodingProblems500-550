def num_pairs(m, n):
    pairs = []

    for i in range(m // 2):
        if i ^ (m - i) == n:
            pairs.append((i, m - i))

    return pairs
    
def num_pairs_best(m, n):
    xor_bits = bin(n)[2:]
    and_bits = bin((m - n) // 2)[2:]

    max_len = max(len(xor_bits), len(and_bits))
    xor_bits = list(map(int, xor_pair.rjust(max_len, '0')))
    and_bits = list(map(int, and_pair.rjust(max_len, '0')))

    count = 1
    for i in range(max_len):
        if and_bits[i] == 1:
            continue
        elif xor_bits[i] == 1:
            count *= 2

    return count // 2
