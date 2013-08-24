# -*- coding: latin-1 -*-

# tape pointer
tptr = 0

# execution pointer
eptr = 0

# creates a tape with 100 positions
tape = [0] * 100

# example code to compile
bfcode = '++++++++++[>+++++++>++++++++++>+++>+<<<<-]>++.>+.+++++++..+++.>++.<<+++++++++++++++.>.+++.------.--------.>+.>.'


def getLoops(bfcode):
    tralha = []

    parentesis = {}

    for i, c in enumerate(bfcode):
        if c == '[':
            tralha.append(i)

        if c == ']':
            temp = tralha.pop()

            parentesis[temp] = i
            parentesis[i] = temp

    return parentesis


loops = getLoops(bfcode)

result = ''

tp = 0

while eptr < len(bfcode):

    comando = bfcode[eptr]

    if comando == '+':
        tape[tptr] += 1
        eptr += 1

    elif comando == '-':
        tape[tptr] -= 1
        eptr += 1

    elif comando == '.':
        result += chr(tape[tptr])
        eptr += 1

    elif comando == '>':
        tptr += 1
        eptr += 1

    elif comando == '<':
        tptr -= 1
        eptr += 1

    elif comando == '[':

        if tape[tptr] > 0:
            eptr += 1
        else:
            eptr = loops[eptr] + 1

    elif comando == ']':
        if tape[tptr] > 0:
            eptr = loops[eptr]
        else:
            eptr += 1

    else:
        eptr += 1



print "Output: ", result