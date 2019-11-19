import re

types = ['помилковий', 'слово', 'ціле число', 'дійсне число', 'ідентифікатор', 'дата', 'пошта', 'зарезервоване','телефон']
reserved = ['shkarovska', 'shka', 'vas', 'rov', 'oka']
reserved2 = ['sin', 'cos', 'tg', 'ctg', 'break', 'continue', 'do', 'for']

def isLetter(char):
    char = char.lower()
    letters = ['s', 'h', 'k', 'a', 'r', 'o', 'v', 's']
    for i in letters:
        if char == i: return True
    return False

def isSeparator(char):
    separators = [' ', '(', ')', '"', '!', '?', '\n']
    for i in separators:
        if char == i: return True
    return False

def split_by_separators(text):
    words = []
    word = ""
    for i in text:
        if isSeparator(i):
            words.append(word)
            word = ""
        elif word != "" and (i == '.' or i == ','):
            if not word[-1:].isdigit() and (i == '.' or i == ','):
                words.append(word)
                word = ""
            else:
                word += i
        else:
            word += i
    words.append(word)
    return words


def read_from_file(path):
    f = open(path, "r")
    return f.read()


def check_data(word, origin):
    for i in range(len(word)):
        if word[i].isdigit():
            continue
        else:
            return 0
    if len(word) == 2 or len(word) == 4:
        if int(origin[0]+origin[1])>32 or int(origin[3]+origin[4])>12:
            return 0
        return 5
    return 0


def check_real_data(word, origin):
    for i in range(len(word)):
        if word[i] == '.' or word[i] == ',':
            return check_data(word[(i + 1):], origin)
        elif word[i].isdigit():
            continue
        else:
            return 0
    return 3

def isTelephone(word):
    if word[0]=="+":
        word = word[1:]
    phonePattern = re.compile(r'^(\d{3})(\d{3})(\d{4})$')
    phonePattern2 = re.compile(r'^(\d{3})-(\d{3})-(\d{4})$')
    phonePattern3 = re.compile(r'^(\d{2})(\d{3})(\d{3})(\d{4})$')
    phonePattern4 = re.compile(r'^(\d{2})-(\d{3})-(\d{3})-(\d{4})$')
    phonePattern5 = re.compile(r'^(\d{3})-(\d{2})-(\d{3})-(\d{4})$')
    if phonePattern.match(word) or phonePattern2.match(word) or phonePattern3.match(word) or phonePattern4.match(word) or phonePattern5.match(word):
        return True;
    return False;

def check_digit(word, origin):
    for i in range(len(word)):
        if word[i] == '.' or word[i] == ',':
            return check_real_data(word[(i + 1):], origin)
        elif word[i].isdigit():
            continue
        else:
            return 0
    return 2


def check_identifier(word):
    for i in word:
        if i.isdigit() or isLetter(i):
            continue
        else:
            return 0
    return 4


def check_gmail(word, dog):
    last = True
    for i in word:
        if (i == '@' or i == '.') and last:
            return 0
        elif i == '@' and not last:
            if dog:
                return 0
            else:
                dog = True
                last = True
        elif i == '.' and not last:
            last = True
        elif isLetter(i):
            last = False
        else:
            return 0
    return 6


def isChar_of_res(ch, i):
    for j in reserved:
        if i >= len(j): continue
        if ch == j[i]:
            return True
    return False


def isReserved(word):
    for i in reserved:
        if i==word: return True
    for i in range(len(word)):
        if isChar_of_res(word[i], i):
            continue
    return False

def check_word(word):
    if (isReserved(word)):
        return 7
    for i in range(len(word)):
        if isLetter(word[i]):
            continue
        elif word[i] == '@':
            return check_gmail(word[(i + 1):], True)
        elif word[i] == '.':
            return check_gmail(word[(i + 1):], False)
        elif word[i].isdigit():
            return check_identifier(word[(i + 1):])
        else:
            return 0
    return 1


def isReserved2(word):
    for i in reserved2:
        if i == word:
            return True
    return False


def print_word_type(word):
    if isReserved2(word):
        print(word + " - " + types[7])
        return
    if word == "": return
    if isSeparator(word[-1:]) or word[-1:] == '.' or word[-1:] == ',':
        word = word[:-1]
    if word == "": return
    if isSeparator(word[0]) or word[0] == '.' or word[0] == ',':
        word = word[1:]
    if word == "": return
    if isLetter(word[0]):
        print(word + " - " + types[check_word(word)])
    elif isTelephone(word):
        print(word + " - " + types[8])
    elif word[0].isdigit() or word[0]=='+' or word[0]=='-':
        print(word + " - " + types[check_digit(word[1:], word)])
    else:
        print(word + " - " + types[0])


if __name__ == "__main__":
    text = read_from_file("testText.txt")
    words = split_by_separators(text)
    for i in words:
        print_word_type(i)
