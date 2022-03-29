def Factorial(n):
    if n == 1:
        return 1
    else:
        result = n * Factorial(n-1)
        print(n,end=' ')
        return result
print("1",end=' ')
result_fac = Factorial(5)
print("팩토리얼 결과 : ",result_fac)