class DFA_state:
    action = ""
    newState = 0
    def __init__(self, action = "", newState = 0):
        self.action = action
        self.newState = newState

transitionTable = [
                    []
                    [[],DFA_state(",",17), DFA_state(",",17), DFA_state(",",2), DFA_state(",",10), DFA_state(",",6), DFA_state(",",7),DFA_state(",",8),DFA_state(",",9),DFA_state(",",11),DFA_state(",",0),DFA_state(",",13),DFA_state(",",14),DFA_state(",",16),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",3), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",3), DFA_state(",",18), DFA_state(",",3), DFA_state(",",3), DFA_state(",",3), DFA_state(",",3),DFA_state(",",3),DFA_state(",",3),DFA_state(",",3),DFA_state(",",3),DFA_state(",",3),DFA_state(",",3),DFA_state(",",16),DFA_state(",",3)],
                    [[],DFA_state(",",4), DFA_state(",",4), DFA_state(",",4), DFA_state(",",5), DFA_state(",",4), DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4)],
                    [[],DFA_state(",",4), DFA_state(",",4), DFA_state(",",18), DFA_state(",",5), DFA_state(",",4), DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4),DFA_state(",",4)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",12),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",15),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",15),DFA_state(",",14),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",15),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",16),DFA_state(",",16),DFA_state(",",0)],
                    [[],DFA_state(",",17), DFA_state(",",17), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)],
                    [[],DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0), DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0),DFA_state(",",0)]
                    ]

def charState(c):
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

    
def main():
    #code for main function
    inp = input()
    temp = inp.split(" ")
    if len(temp ==2) and temp[0] == "scanner":
        fp = open(temp[1], 'r')
        while fp != "":
            scan(fp)

    pass

def scan(fp):
    #code for scan function
    token = ""
    cur_char = ""
    remembered_chars = ""
    while True:
        cur_state = 0
        image = ""
        prev_state = 0
        while cur_char:
            cur_char = fp.read(1)
            action = transitionTable[cur_state][charState(cur_char)]
            if action == "move":
                pass
            elif action == "recognize":
                pass
            elif action == "error":
                pass

    pass