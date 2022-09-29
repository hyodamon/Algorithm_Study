import sys
from collections import deque

exp = sys.stdin.readline()

stack = deque()

score = {
    '+' : 1,
    '-' : 1,
    '*' : 2,
    '/' : 2
}

answer = ''
for word in exp :
    if ord(word) >= 65 and ord(word) <= 90 :
        answer += word
    elif word == '(' :
        stack.append(word)
    elif word in score :
        while len(stack) > 0 and stack[-1] != '(' and score[stack[-1]] >= score[word] :
            answer += stack.pop()
        stack.append(word)     
    elif word == ')' :
        while len(stack) > 0 and stack[-1] != '(' :
            answer += stack.pop()
        stack.pop()
        
while len(stack) :
    answer += stack.pop()
    
print(answer)