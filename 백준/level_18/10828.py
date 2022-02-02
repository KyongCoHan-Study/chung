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

class stack():
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
            return 0
        return 1
    def top():
        if len(stack_list)!=0:
            return stack_list[-1]
        return -1
    
stack_list=[]   
for _ in range(int(input())):
    n = str(input())
    if 'push' in n:
        n,m=n.split()
        stack.push(m)
    elif 'pop' == n:
        print(stack.pop())
    elif 'size' == n:
        print(stack.size())
    elif 'empty' == n:
        print(stack.empty())
    elif 'top' == n:
        print(stack.top())