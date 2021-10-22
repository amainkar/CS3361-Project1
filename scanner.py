import time

class DFA_state:
    action = ""
    newState = 0
    def __init__(self, action = "", newState = 0):
        self.action = action
        self.newState = newState

'''                                     Transition table
                                        each element is an object of class DFA_state so we can have action and newstate combined in one table
                                        table is padded so we index from 1 not zero E.g transitionTable[0][] is empty and transtitionTable[x][0] is also empty'''
transitionTable = [
                    [],
                    [[],DFA_state("move",17), DFA_state("move",17), DFA_state("move",2), DFA_state("move",10), DFA_state("move",6), DFA_state("move",7),DFA_state("move",8),DFA_state("move",9),DFA_state("move",11),DFA_state("stuck",0),DFA_state("move",13),DFA_state("move",14),DFA_state("move",16),DFA_state("stuck",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("move",3), DFA_state("move",4), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("move",3), DFA_state("move",18), DFA_state("move",3), DFA_state("move",3), DFA_state("move",3), DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",3),DFA_state("move",16),DFA_state("move",3)],
                    [[],DFA_state("move",4), DFA_state("move",4), DFA_state("move",4), DFA_state("move",5), DFA_state("move",4), DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4)],
                    [[],DFA_state("move",4), DFA_state("move",4), DFA_state("move",18), DFA_state("move",5), DFA_state("move",4), DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4),DFA_state("move",4)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("move",12),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0), DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("stuck",0),DFA_state("move",15),DFA_state("stuck",0),DFA_state("stuck",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("move",15),DFA_state("move",14),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("move",15),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("move",16),DFA_state("move",16),DFA_state("recognize",0)],
                    [[],DFA_state("move",17), DFA_state("move",17), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)],
                    [[],DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0), DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0),DFA_state("recognize",0)]
                    ]

tokenTable = {
    1: 'error',
    2: 'div',
    3: 'error',
    4: 'error',
    5: 'error',
    6: 'lparen',
    7: 'rparen',
    8: 'plus',
    9: 'minus',
    10: 'times',
    11: 'error',
    12: 'assign',
    13: 'error',
    14: 'number',
    15: 'number',
    16: 'identifier',
    17: 'whitespace',
    18: 'comment'
}

def charState(c):                       # pass in character returns 1-14 representing char state
    if c == '\t' or c == ' ':
        return 1
    elif c == '\n':
        return 2
    elif c == '/':
        return 3
    elif c == '*':
        return 4
    elif c == '(':
        return 5
    elif c == ')':
        return 6
    elif c == '+':
        return 7
    elif c == '-':
        return 8
    elif c == ':':
        return 9
    elif c == '=':
        return 10
    elif c == '.':
        return 11
    elif c.isdigit():
        return 12
    elif c.isalpha():
        return 13
    else:
        return 14

global unreadChar 
unreadChar = []
EOF = False
    
def main():                             # main function to drive code
    #code for main function
    inp = input("")
    temp = inp.split(" ")
    if len(temp) ==2 and temp[0] == "scanner":
        fp = open(temp[1], 'r')
        token = ""
        list_tokens = []
        while not EOF and token != 'error':
            token = scan(fp)
            list_tokens.append(token)
        if token == 'error':
            print("error")
        else:
            temp = "("
            for i in list_tokens:
                temp += (i)
                temp += ", "
            temp = temp[:-2]
            temp += ')'
            print(temp)
        time.sleep(20)

def scan(fp):
    #code for scan function
    global EOF
    token = "whitespace"
    cur_char = " "
    remembered_chars = ""
    global unreadChar
    while token == 'whitespace' or token == 'comment':                         # base structure setup aka loops and if statements. Contents still need to be added/corrected to structure
        cur_state = 1
        image = ""
        prev_state = 0
        while cur_char != "":
            if not unreadChar:
                cur_char = fp.read(1)
            else:
                cur_char = unreadChar[0]
                unreadChar = unreadChar[1:]
            if cur_char == "":
                EOF = True
                return tokenTable[prev_state]
            action = transitionTable[cur_state][charState(cur_char)].action
            if action == "move":
                if cur_state != 0:
                    prev_state = cur_state
                    remembered_chars = ""
                remembered_chars += cur_char
                cur_state = transitionTable[cur_state][charState(cur_char)].newState
            elif action == "recognize":
                token = tokenTable[cur_state]
                if cur_char == ' ' or cur_char == '\n' or cur_char == '\t':
                    pass
                else:
                    unreadChar.append(cur_char)
                break

            elif action == "stuck":
                if prev_state != 0:
                    token = tokenTable[prev_state]
                    break
                else:
                    return "error"
            image += cur_char
    if image.lower() == 'read':
        token = 'read'
    if image.lower() == 'write':
        token = 'write'
    return token

main()