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
    pass