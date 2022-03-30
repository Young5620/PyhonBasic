'''
Chapter5
문제1
다음 height변수에 별(star)의 층수를 입력하면 각 층마다 별의 개수가 한 개씩 증가하여 출력되고,
마지막 줄에 별의 개수가 출력되도록 함수의 빈 칸을 채우시오
(출력예시)
height : 3
*
**
***
star 개수 : 6
'''
def StarCount(height):
    star = 0
    for i in range(height):
        print("*"*(i+1))
        star += (i+1)
    return star
    

height = int(input("height : "))
print('star 개수 : %d'%StarCount(height))


'''
문제2
중첩함수를 적용하여 다음<조건>에 맞게 은행계좌 함수의 빈칸을 채우세요
<조건1> 외부함수 : bank_account() : 잔액(balance) outer변수
<조건2> 내부함수 : getBalance() : 잔액확인
                  deposit(money) : 입금하기
                  withdraw(money) : 출금하기
<조건3> 출금액이 잔액보다 많은 경우 '잔액이 부족합니다.' 메시지 출력
<조건4> 기타 나머지는 출력예시 참조

(출력예시)
최초 계좌의 잔액을 입력하세요 : 1000
현재 계좌 잔액은 1000원 입니다.
입금액을 입력하세요 : 15000
15000원 입금후 잔액은 16000원 입니다.
출금액을 입력하세요 : 3000
3000원 출금후 잔액은 13000원 입니다.                  
'''
def bank_account(bal):
    balance = bal
    def getBalance():
        return balance
    def deposit(money):
        nonlocal balance
        balance +=money
    def withdraw(money):
        nonlocal balance
        if balance < money :
            print("잔액이 부족합니다.")
        else:
            balance -= money
    return getBalance,deposit,withdraw

# 메인
bal = int(input("최초 계좌의 잔액을 입력하세요 : "))
getBalance,deposit,withdraw = bank_account(bal)
print("현재 계좌 잔액은 {}원 입니다.".format(getBalance))
money = int(input("입금할 금액을 입력하세요 : "))
deposit(money)
print(money+"원 입금 후 잔액은 "+getBalance+"원 입니다.")
money = int(input("출금할 금액을 입력하세요"))
withdraw(money)
print(f"{money}원 출금 후 잔액은 {getBalance}원 입니다.")


'''
문제3
팩토리얼(Factorial)을 계산하는 재귀함수의 빈칸을 채우세요
예) 5!(5*4*3*2*1) = 120
'''
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