import sympy

priority = {'(': 0, '[': 0, ')': 1, ']': 1, ',': 1, ';': 1,
            'ͻ': 2, '˅': 3, '˄': 4, '¬': 5,
            '>': 6, '<': 6, '=': 6, '≤': 6, '≠': 6, '≥': 6,
            '+': 7, '-': 7,
            '*': 8, '/': 8, '%': 8, '↑': 9}

def concatt(res, steck):
    res = res + list(reversed(steck))
    res_str = ""
    for i in res:
        try:
            res_str += i
        except:
            res_str += i.__str__()
    print(res_str)

def make_poliz(str, steck, res):
    if len(str)<1:
        return concatt(res, steck)
    while str[0].isalpha() or str[0].isdigit():
        res.append(str[0])
        old = str[0]
        str = str[1:]
        if len(str)<1:
            return concatt(res, steck)
        if old.islower() and str[0]=='(':
            steck.append("Fn")
            steck.append(2)
            str = str[1:]
        if old.isupper() and str[0]=='[':
            steck.append("]")
            steck.append(2)
            str = str[1:]
    if len(str)<1:
         return concatt(res, steck)
    if str[0]==')' or str[0]==']':
        str = str[1:]
        while not (steck[(len(steck)-1)]=='(' or steck[(len(steck)-1)]=="Fn" or steck[(len(steck)-1)]==']'):
            # if type(steck[(len(steck)-1)])==type(1):
            #     res.append((steck[(len(steck)-1)]+1))
            # elif steck[(len(steck)-1)]!=',':
            #
            res.append(steck[(len(steck)-1)])
            steck = steck[:-1]
        if steck[(len(steck)-1)]=="Fn":
            res.append("Fn")
        elif steck[(len(steck)-1)]==']':
            res.append(']')
        steck = steck[:-1]
        return make_poliz(str, steck, res)
    elif str[0]==',':
        str = str[1:]
        while not type(steck[(len(steck)-1)])==type(1):
            res.append(steck[(len(steck)-1)])
            steck = steck[:-1]
        a = steck[(len(steck)-1)]+1
        steck = steck[:-1]
        steck.append(a)
        return make_poliz(str, steck, res)

    if len(str)<1:
        return concatt(res, steck)
    while not (str[0].isalpha() or str[0].isdigit()):
        if isnt_cor_char(str[0]):
            print(str[0])
            return []
        high = str[0]
        str = str[1:]
        if len(steck)>0 and high!='(' and high!='[' and type(steck[(len(steck)-1)])!=type(1):
            while priority[high]<=priority[steck[(len(steck)-1)]]:
                res.append(steck[(len(steck)-1)])
                steck = steck[:-1]
                if len(steck)<1: break
        if high=='[': high = '('
        steck.append(high)
        if len(str)<1:
            return concatt(res, steck)
    make_poliz(str, steck, res)

def add_to_stack(steck, ch):
    return [], steck

def isnt_cor_char(ch):
    for i in priority:
        if i==ch: return False
    return True

def try_to_calculate(str):
    if ("=") in str:
        while str[0]!='=':
            str = str[1:]
            if str=="": break
        str = str[1:]
    try:
        res = sympy.sympify(str)
        print(res)
    except:
        print("Uncounting")
if __name__ == '__main__':
    str = input('Write me an string to Poliz: \n')
    make_poliz(list(str),[],[])
    try_to_calculate(str)
