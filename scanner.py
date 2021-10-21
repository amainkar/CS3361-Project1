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
                    []
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
    1: 'Start',
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

    
def main():                             # main function to drive code
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
    while True:                         # base structure setup aka loops and if statements. Contents still need to be added/corrected to structure
        cur_state = 1
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
