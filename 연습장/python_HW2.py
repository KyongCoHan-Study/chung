

def solution_7_3():
    x = float(input("밑을 입력하세요 : "))
    n=int(input("지수를 입력하세요 : "))

    print("result = "+str(x**n))



import math

def solution_7_4():
    n = int(input("숫자를 입력하세요 : "))
   

    print(str(n)+"! = "+str(math.factorial(n)))


def solution_7_6():
    n = int(input("정수를 입력하세요 : "))

    print("1부터 "+str(n)+"까지의 합은 "+str(int((n*(n+1))/2))+"입니다.")

def solution_7_7():
    n = float(input("밑을 입력하세요 : "))
    m=int(input("지수를 입력하세요 : "))

    print("result = "+str((lambda x:x**m)(n)))

solution_7_3()
solution_7_4()
solution_7_6()
solution_7_7()