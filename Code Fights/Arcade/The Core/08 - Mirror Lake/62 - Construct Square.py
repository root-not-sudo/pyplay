def constructSquare(s):
    lowerBound = (1, 4, 10, 32, 100, 317, 1000, 3163, 10000, 31623)
    upperBound = (3, 9, 31, 99, 316, 999, 3162, 9999, 31622, 99999)
    s_len = len(s)
    str_lens = []
    for i in range(s_len):
        if s[i] not in s[0:i]:
            str_lens.append(s.count(s[i]))
    str_lens.sort()
    for i in range(upperBound[s_len-1], lowerBound[s_len-1]-1, -1):
        square_lens = []
        square = str(i * i)
        for j in range(s_len):
            if square[j] not in square[0:j]:
                square_lens.append(square.count(square[j]))
        square_lens.sort()
        if square_lens == str_lens:
            return int(square)
    return -1


print(constructSquare('aaaaaabbbb'))
