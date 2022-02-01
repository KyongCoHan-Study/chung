"""
===============================
문제출처  : 백준
문제번호  : 10828
문제단계  : level_18
최초생성  : 2022.02.01
생성자    : chung
문제설명  : 스택
===============================
"""

class stack(int):
    def push(n):
        stack_list.append(n)
    def pop():
        if len(stack_list)!=0:
            return stack_list.pop()
        return -1
    def size():
        return len(stack_list)
    def empty():
        if len(stack_list)!=0:
            return 1
        return 0
    def top():
        return stack_list[-1]
    
stack_list=[]   
for _ in range(int(input())):
    n = str(input())
    if 'push' in n:
        stack.push(n[-1])
    elif 'pop' in n:
        print(stack.pop())
    elif 'size' in n:
        print(stack.size())
    elif 'empty' in n:
        print(stack.empty())
    elif 'top' in n:
        print(stack.top())