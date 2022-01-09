def solution(numbers):
    answer = ''
    numbers=list(map(str,numbers))
    print(sorted([num*3 for num in numbers]))
    answer="".join(sorted(numbers,reverse=True,key=lambda x:x*3))
    return answer


print(solution([3, 30, 34, 5, 9]))