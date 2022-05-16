def solution_5_2():
    values = [1,2,3,4,5]
    new_values = [v*10 for v in values]
    print(new_values)

def solution_5_3():
    values = {"one":1,"two":2,"three":3}

    for k in values:
        print(k)

def solution_5_4():
    N = int(input("N을 입력하세요 : "))
    K = int(input("K를 입력하세요 : "))
    sum=N+K
    print("1부터 10까지 3의 배수의 합은 "+str(sum)+"입니다.")

def solution_5_5():
    n = int(input("숫자를 입력하세요 : "))
    num = 1
    i=1
    while True:

        if num*i<n:
            num=num*i

        else: 
            num = i-1
            break
        i+=1

    print("곱의 결과 값이 "+str(n)+"을 넘지 않는 가장 큰 수는 "+str(num)+"입니다.")    

def solution_5_6():
    

    for i in range(11):
        if i >6:
            n=12-i
        else:
            n=i
        for j in range(1,n):
            print(j,end="")
        print()

def solution_5_7():
    values=[i*3 for i in range(1,34)]
    print(values)

def solution_5_8():
    square={n:n*n for n in range(2,11,2)}
    print(square)


solution_5_2()
solution_5_3()
solution_5_4()
solution_5_5()
solution_5_5()
solution_5_6()
solution_5_7()
solution_5_8()