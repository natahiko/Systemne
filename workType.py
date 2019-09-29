import re

types = ['помилковий','слово','ціле число','дійсне число','ідентифікатор','дата','пошта','зарезервоване']
reserved = ['shkarovska', 'sha','vas','rov','oka']

def isLetter(char):
    char = char.lower()
    letters = ['s','h','k','a','r','o','v','s']
    for i in letters:
        if char==i: return True
    return False

def isSeparator(char):
    separators = [' ','(',')','"','-','!','?','\n']
    for i in separators:
        if char==i: return True
    return False

def split_by_separators(text):
    words = []
    word = ""
    for i in text:
        if isSeparator(i):
            words.append(word)
            word = ""
        elif word!='' and (i=='.' or i==','):
            if not word[-1:].isdigit() and i==',':
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

def check_data(word):
    for i in range(len(word)):
        if word[i].isdigit():
            continue
        else:
            return 0
    if len(word)==2 or len(word)==4:
        return 5
    return 0

def check_real_data(word):
    for i in range(len(word)):
        if word[i] == '.' or word[i]==',':
            return check_data(word[(i+1):])
        elif word[i].isdigit():
            continue
        else:
            return 0
    return 3

def check_digit(word):
    for i in range(len(word)):
        if word[i] == '.' or word[i]==',':
            return check_real_data(word[(i+1):])
        elif word[i].isdigit():
            continue
        else:
            return 0
    return 2
    # digit = re.compile("^([0-9]+)+$")
    # real = re.compile("^([0-9]+{.,}+[0-9]+)+$")
    # data1 = re.compile("^[0-3][0-9]+[.,]+[0-1][0-9]+[.,]+[0-9][0-9][0-9][0-9]$")
    # data2 = re.compile("^[0-3][0-9]+[.,]+[0-1][0-9]+[.,]+[0-9][0-9]$")
    # if digit.match(word):
    #     print(word+" - "+types[2])
    # elif data1.match(word) or data2.match(word):
    #     print(word+" - "+types[5])
    # elif real.match(word):
    #     print(word+" - "+types[3])
    # else:
    #     print(word+" - "+types[0])

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
        if (i=='@' or i=='.') and last:
            print(i+'1')
            return 0
        elif i=='@' and not last:
            if dog:
                print(i+'2')
                return 0
            else:
                dog = True
                last = True
        elif i=='.' and not last:
            last = True
        elif isLetter(i):
            last = False
        else:
            print(i+'3')
            return 0
    return 6

def isChar_of_res(ch,i):
    for j in reserved:
        if i>=len(j): continue
        if ch==j[i]:
            return True
    return False

def isReserved(word):
    for i in range(len(word)):
        if isChar_of_res(word[i],i):
            continue
        else:
            return False
    return True

def check_word(word):
    if (isReserved(word)):
        return 7
    for i in range(len(word)):
        if isLetter(word[i]):
            continue
        elif word[i]=='@':
            return check_gmail(word[(i+1):], True)
        elif word[i]=='.':
            return check_gmail(word[(i+1):], False)
        elif word[i].isdigit():
            return check_identifier(word[(i+1):])
        else:
            return 0
    return 1
    # ua_word = re.compile("^([shkarovs]+)+$")
    # ident = re.compile("^([shkarovs]+[0-9]+)+$")
    # # TODO gmail
    # if ua_word.match(word):
    #     print(word+" - "+types[1])
    # elif ident.match(word):
    #     print(word+" - "+types[4])
    # else:
    #     print(word+" - "+types[0])

def print_word_type(word):
    if isSeparator(word[-1:]) or word[-1:]=='.' or word[-1:]==',':
        word = word[:-1]
    if word=='': return
    if isLetter(word[0]):
        print(word +" - "+types[check_word(word)])
    elif word[0].isdigit():
        print(word +" - "+types[check_digit(word)])
    else:
        print(word+" - "+types[0])

if __name__ == "__main__":
    text = read_from_file("testText.txt")
    words = split_by_separators(text)
    for i in words:
        print_word_type(i)




