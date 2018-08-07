def long_repeat(text: str):
    # print(text)
    count = 0
    for t in text:
        for y in range(len(text)+1):
            if t*y in text:
                print(y)
                if y > count:
                    count = y
    print('the final count: ' + str(count))
    return(count)


if __name__ == '__main__':
    long_repeat("aa")
