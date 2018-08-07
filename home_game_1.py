import re


def checkio(string: str):
    # only_char = re.compile(r'^[a-z]*[a-z]$')
    # only_num = re.compile(r'^[0-9]*[0-9]$')
    # no_upper = re.compile(r'[A-Z]+')
    # if len(string) <= 9:
    #     return False
    # elif only_num.search(string) != None or only_char.search(string) != None:
    #     return False
    # elif no_upper.search(string) == None:
    #     return False
    # else:
    #     return True
    match1 = re.compile(r'.*[a-z]+')
    match2 = re.compile(r'.*[A-Z]+')
    match3 = re.compile(r'.*[0-9]+')
    # print(match1.match(string))
    # print(match2.match(string))
    # print(match3.match(string))
    # print('=============')

    if match1.match(string) != None and match2.match(string) != None and match3.match(string) != None and len(string) > 9:
        return True
    else:
        return False


if __name__ == '__main__':
    # These "asserts" using only for self-checking and not necessary for auto-testing
    # assert checkio('A1213pokl') == False, "1st example"
    # assert checkio('bAse730onE4') == True, "2nd example"
    # assert checkio('asasasasasasasaas') == False, "3rd example"
    # assert checkio('QWERTYqwerty') == False, "4th example"
    # assert checkio('123456123456') == False, "5th example"
    # assert checkio('QwErTy911poqqqq') == True, "6th example"
    checkio('A1213pokl')
    checkio('bAse730onE4')
    checkio('asasasasasasasaas')
    checkio('QWERTYqwerty')
    checkio('123456123456')
    checkio('QwErTy911poqqqq')
