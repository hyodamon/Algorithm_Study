import sys

N = int(sys.stdin.readline())
S = 0
for i in range(N) :
    command = sys.stdin.readline().split()
    
    if command[0] == 'all' :
        S |= (~0)
    elif command[0] == 'empty' :
        S &= 0
    elif command[0] == 'add' :
        S |= (1 << (int(command[1]) - 1))
    elif command[0] == 'remove' :
        S &= ~(1 << (int(command[1]) - 1))
    elif command[0] == 'check' :
        if S & (1 << (int(command[1]) - 1)) :
            print(1)
        else :
            print(0)
    elif command[0] == 'toggle' :
        S ^= (1 << (int(command[1]) - 1))