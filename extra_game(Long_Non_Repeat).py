def non_repeat(text: str):
    final_list = []
    for i in range(len(text)):
        incr = 1
        l = ''+text[i]
        while i+incr <= len(text)-1:
            if text[i+incr] not in l:
                l += text[i+incr]
            else:
                break
            incr += 1
        # print(l)
        final_list.append(l)
    return(max(final_list, key=len))


if __name__ == '__main__':
    non_repeat('aaaaa') == 'a'
    non_repeat('abdjwawk') == 'abdjw'
    non_repeat('abcabcffab') == 'abcf'
