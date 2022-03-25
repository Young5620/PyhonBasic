## 함수(Function)
# : 프로그램에서 사용할 기능을 미리 정의해서 구현한 것
#   (또 다른 의미의 프로그램 내의 작은 프로그램)

# python의 함수 정의(생성)
#   def 함수이름([인자list]):
#       함수 기능에 대한 정의1
#       함수 기능에 대한 정의2
#       함수 기능에 대한 정의3
#       ...
# - 함수 사용에 있어서 설명이 필요한 경우, 함수 내부에 주석을 사용하여 기술(여러 줄 주석 '''~''')
# - 함수를 만들 때에 함수의 기능을 바로 알 수 있는 이름으로 정의하길 권장.
# - 미리 만들어 놓은 함수를 호출시에는, "함수이름([인자...])"로 호출
# - 정의 생성된 반환값이 있는 경우, 'return' 명령어를 사용
# - 함수에 반환값이 있을 수도 있고, 없을수도 있다. 있는 경우는 return을 사용
#   없는 경우에는 return은 함수가 종료 
# - 함수에 필요하면 인자값을 전달할 수 있다. 전달된 인작밧은 함수 정의시에 만든 "매개변수"에 그 값이 저장된다.
#   이후에 함수 정의부에서 해당 내용을 가지고 구동

# 예제1 사용자가 입력한 값을 출력하는 함수 구현
# 함수 정의부
def pr():
    txt = input("입력값 : ")
    print()
    print("입력한 내용은 : ",txt)
# 함수 호출
# pr()

# 실습 - 입력값을 받아서 사칙연산하는 프로그램 함수를 사용
#        함수 이름은 calc()로 구현해보세요
#        (메인에서 calc()호출하면 모든 동작이 가능하도록 설정)
def calc():
    while True:
        import os
        os.system('cls')
        num1 = int(input("첫번째 숫자를 입력하세요 : "))
        num2 = int(input("두번째 숫자를 입력하세요 : "))
        cal = input("연산기호를 입력하세요 : ")
        if cal == '+':
            print("연산 결과 : ",num1+num2)
        elif cal == '-':
            print("연산 결과 : ",num1-num2)
        elif cal == '*':
            print("연산 결과 : ",num1*num2)
        elif cal == '/':
            if num2 == 0:
                print("0으로 나눌 수 없습니다.")
            else:
                print("연산 결과 : ",num1/num2)
        else: 
            print("연산기호를 확인해주세요.")
        if input("계속하시겠습니까? (Y/n) : ") == 'n':
            break
        
    print("프로그램을 종료합니다.")    
# calc()

# 예제2 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
#       사용자로부터 입력받은 값을 인자값으로 처리하는 함수
def pr2(str1):
    print("입력한 내용은 : ", str1)

# 메인 : 
# txt = input("입력 : ")
print()
# pr2(txt)

# 실습 입력값을 받아서 사칙연산하는 프로그램 함수를 사용하여 동작하게 만드세요
#      함수명은 "calc([문자열인자값])"로 사용하세요
'''
# 함수 생성
def calc(str1):
    if '+' in str1:
        # 더하기 연산
        num1, num2 = str1.split('+')
        num1 = int(num1);num2 = int(num2)
        print("계산 결과는 : ",num1 + num2)
    elif '-' in str1:
        # 빼기 연산
        num1, num2 = str1.split('-')
        num1 = int(num1);num2 = int(num2)
        print("계산 결과는 : ",num1 - num2)
    elif '*' in str1:
        # 곱하기 연산
        num1, num2 = str1.split('*')
        num1 = int(num1);num2 = int(num2)
        print("계산 결과는 : ",num1 * num2)
    elif '/' in str1:
        # 나누기 연산
        num1, num2 = str1.split('/')
        num1 = int(num1);num2 = int(num2)
        if num2 == 0:
            print("0으로 나눌수 없습니다.")
        else:
            print("계산 결과는 : {:.2f}".format(num1 / num2))
    else:
        print("수식입력이 잘못됐습니다.\n다시 입력해주세요!!!")

# 메인
import os
while True:
    txt = input("계산할 수식을 입력하세요[ex) 5+5] : ")
    calc(txt)       # 함수 호출
    if input("계속하시겠습니까? (Y/n) : ") == 'n':
        break
print("프로그램을 종료합니다.")
os.system('cls')
'''

# 예제3 함수의 인자값 사용 - 사용자가 입력한 값을 출력하는 함수 구현
#       사용자로부터 입력받은 값을 인자값으로 처리하는 함수
#       함수에 return을 사용하여 반환값을 처리하는 예제

def pr3(str1):
    '''연산 결과 후에 반환값을 전달하는 함수'''
    return "입력한 문자열 : "+str1

# 메인 : 
# txt = input("입력 : ")
# print()
# pr_out = pr3(txt)
# print(pr_out)

'''
# 실습 위의 내용을 토대로 계산 결과를 반환값으로 처리하는 함수로 변환
def calc(str1):
    if '+' in str1:
        # 더하기 연산
        num1, num2 = str1.split('+')
        num1 = int(num1);num2 = int(num2)
        return num1 + num2
    elif '-' in str1:
        # 빼기 연산
        num1, num2 = str1.split('-')
        num1 = int(num1);num2 = int(num2)
        return num1 - num2
    elif '*' in str1:
        # 곱하기 연산
        num1, num2 = str1.split('*')
        num1 = int(num1);num2 = int(num2)
        return num1 * num2
    elif '/' in str1:
        # 나누기 연산
        num1, num2 = str1.split('/')
        num1 = int(num1);num2 = int(num2)
        return num1 / num2
    else:
        return 0

# 메인
import os
while True:

    txt = input("계산할 수식을 입력하세요[ex) 5+5] : ")
    result = calc(txt)       # 함수 호출
    if result != False:
        print("계산 결과는 : ",result)
    else : 
        print("수식입력이 잘못됐습니다.\n다시 입력해주세요!!!")
    if input("계속하시겠습니까? (Y/n) : ") == 'n':
        break
print("프로그램을 종료합니다.")
'''
# 두수에 대한 한번의 계산식을 입력받아서 결과를 출력하는 코드를 이용
# 다음과 같이 코딜을 해보세요
# - 사용자가 계산식을 입력, 이것을 이용해서 처리
# - calc()가 인자값으로 두 정수와 계산식(기초:+,-,*,/)을 인자로 받아 처리하는 함수를 만들어 동작 시키세요

def calc(num1,num2,cal):
    if '+' in cal:
        return num1 + num2
    elif '-' in cal:
        return num1 - num2
    elif '*' in cal:
        return num1 * num2
    elif '/' in cal:
        return num1 / num2
    else:
        return 0
'''
# 메인
import os
while True:
    os.system('cls')
    txt = input("계산할 수식을 입력하세요[ex) 5+5] : ")
    if '+' in txt : 
        num1,num2 = txt.split('+')
        num1 = int(num1);num2 = int(num2)
        cal = '+'
    elif '-' in txt : 
        num1,num2 = txt.split('-')
        num1 = int(num1);num2 = int(num2)
        cal = '-'
    elif '*' in txt : 
        num1,num2 = txt.split('*')
        num1 = int(num1);num2 = int(num2)
        cal = '*'
    elif '/' in txt : 
        num1,num2 = txt.split('/')
        num1 = int(num1);num2 = int(num2)
        cal = '/'
    else : 
        print("수식입력이 잘못됐습니다.\n다시 입력해주세요!!!")
        os.system('pause')
        continue
    
    result = calc(num1, num2, cal)       # 함수 호출
    
    if result != 0:                      # 0인 경우는 수식이 잘못된 경우(+,-,*,/)
        if type(result) is not float:
            print("계산 결과는 : ",result)
        else: 
            print("계산 결과는 : {:.2f}".format(result))
    if input("계속하시겠습니까? (Y/n) : ") == 'n':
        break
print("프로그램을 종료합니다.")
'''


## 함수 인자 기본값(default) 설정
# default란? 입력 인자값이 없는 경우에 기본적으로 적용되어지는 값을 의미함
# 
# (형식)
# def 함수이름(param1,param2=1):
#   함수 정의문1
#   함수 정의문2
# 이렇게 정의된 함수가 있는 경우, param2는 기본값으로 '1'을 가지고 있는 것임
# 즉, 인자값으로 param2에 전달되지 않아도 기본값으로 '1'을 갖는다.

# 예제4 함수 인자의 기본값 설정(인자1개)
def pr4(par1=10):
    print(par1)
    
# 메인
print("-----pr4-----")
pr4(10)
pr4(20)
pr4(3)
pr4()

# 인자를 2개 가진 경우(모두 default인 경우)
def pr5(par1=10,par2=20):
    print(par1,par2)

# 메인
print("-----pr5-----")
pr5(100,200)
pr5(100)
pr5(200)
pr5(par2=200)
pr5()

# 인자가 2개 이상, 기본값이 1개인 경우
def pr6(par1,par2=20):
    print(par1,par2)

# 메인
print("-----pr6-----")
pr6(100,200)
pr6(100)
pr6(200)
# pr6()                 # par1 자리에 반드시 값을 입력해줘야 한다!

# 인자의 기본값이 맨 앞에 있는 경우
# def pr7(par1=10,par2):  # 기본값 뒤에는 일반 인자가 존재하면 안된다.
#     print(par1,par2)

# pr7()                   # SyntaxError
'''
# [Quiz]
# 1. 짝, 홀수를 구분하는 함수를 작성해주세요
def qu1(par1):
    if par1 % 2==0:
        return '짝수'
    else :
        return '홀수'
# 메인
print("Quiz 1번")
txt = int(input("정수를 입력하세요 : "))
result = qu1(txt)
print(result)

# 2. "3"의 배수를 판별하는 함수를 작성해주세요
print("Quiz 2번")
def qu2(par1):
    if par1 % 3 == 0:                       # not num%3 -> 3의 배수이면 True 아니면 False
        return True
    else : 
        return False
# 메인
txt = int(input("자연수를 입력하세요 : "))
result = qu2(txt)
if result:
    print("3의배수 입니다.")
else : 
    print("3의배수가 아닙니다.")
    
# 3. 계산기를 입력,출력,연산기능으로 나눠서 실행되게 작성해주세요
def calc(num1,num2,giho):
    if giho == '+':
        return num1 + num2
    elif giho == '-':
        return num1 - num2
    elif giho == '*':
        return num1 * num2
    elif giho == '/':
        return num1 / num2
    
def Output(num1,num2,giho,result):
    print(num1,giho,num2," = ",result)

def Input():
    num1, giho, num2 = int(input("첫번째 숫자를 입력하세요. : ")),input("계산기호 입력 : (+,-,*,/)"),int(input("두번째 숫자를 입력하세요. : "))
    result = calc(num1, num2, giho)
    Output(num1, num2, giho, result)
    
# 4. 예제 거꾸로 수를 반환하는 함수를 계산, 출력 기능으로 나눠서 작성해주세요 (321->123)
'''
'''
def rever(par1):
    par1 = int(par1)
    lst = []
    while True:
        if par1 > 10:
            lst.append(par1 % 10)
            par1 = par1 // 10
        else :
            break
        print("계산결과 : ")
        for i in range(0,len(lst)):
            print(lst[i],end='')
    
# 메인
print("Quiz4번")
txt = int(input("숫자 입력 : ")) 
rever(txt)


def reverseCode(result):
    tmp, su = 0,0
    while True:
        tmp = result%10
        result = result//10
        su = (su + tmp) * 10
        if not result:
            return su//10

def display():
    result,su = 0,0
    result = int(input("정수 입력 : "))
    su = reverseCode(result)
    print("변환 전 값 : {} , 변환 후 값 : {}".format(result,su))
    
# 메인
display()
'''

# 예제 친구이름 관리를 함수로 기능을 나눠서 작성해주세요
# (1. 친구목록보기, 2. 친구추가, 3. 친구삭제, 4. 친구수정, 0. 종료)

def fr_list(lst):               # 친구목록보기
    print("="*15,"친구목록 보기","="*15)
    if lst !=[]:
        for i in range(len(lst)):
            print(f"{i} : {lst[i]}")
    else :
        print("등록된 친구가 없습니다.")

def fr_add(lst):                # 친구목록추가
    name = input("추가할 친구 이름을 입력하세요. : ")
    lst.append(name)

def fr_del(lst):                # 친구목록삭제
    name = input("삭제할 친구 이름을 입력하세요 : ")
    if name in lst:
        lst.remove(name)
    else: 
        print("삭제할 친구가 없습니다.")

def fr_mod(lst):                # 친구목록수정
    name = input("수정할 친구 이름 입력하세요 : ")
    if name in lst:
        idx = lst.index(name)
    else:
        print("수정할 친구가 없습니다.")
        return
    name_mod = input("변경할 이름 입력하세요 : ")
    lst[idx] = name_mod

# 메인
'''
import os
fr_lst = []
while True:
    os.system('cls')
    print("="*15,"친구 관리 프로그램","="*15)
    print("1. 친구목록보기")
    print("2. 친구목록추가")
    print("3. 친구목록삭제")
    print("4. 친구목록수정")
    print("0. 종료")
    sel = input("메뉴를 선택해주세요(0~4) : ")
    if sel == '1':
        fr_list(fr_lst)
        os.system('pause')
    elif sel =='2':
        fr_add(fr_lst)
        os.system('pause')
    elif sel =='3':
        fr_del(fr_lst)
        os.system('pause')
    elif sel =='4':
        fr_mod(fr_lst)
        os.system('pause')
    elif sel =='0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("메뉴를 잘못 선택하셨습니다.")
        os.system('pause')
'''       
        
# 문제 알바 시급 프로그램 작성 (default인자값 사용)
#   시급 : 8500원, 하루 8시간, 한달30일(기본값)
#
# 다음과 같이 출력되게 만드세요
# (출력결과)
# <<시급 계산 프로그램>>
# 1. 기본급
# 2. 일한 날짜 입력
# 번호 입력 >> 

def alba(day=30):
    time = 8 ; price = 8500
    re = time * price * day
    return re

def display():
    num = input("<< 시급 계산 프로그램 >>\n1. 기본급\n2. 일한 날짜입력\n번호입력 : ")
    if num == '1':
        result = alba()
    elif num == '2':
        day = int(input("일한 일 수 입력 : "))
        result = alba(day)
    print("당신의 급여는 : {:,}원 입니다.".format(result))

# 메인
# display()


## 인자값 처리 방식1 => 연속된 자료를 처리하는 함수의 인자 처리 방식

# 예제
def pr8(a,b,c):
    print(a,b,c)
# 메인
print("-----pr8-----")
pr8(10, 20, 30)

# "*"를 이용하여 리스트 또는 튜플과 같은 자료를 연속된 인자의 값으로 처리
# 리스트 또는 튜플의 변수값을 받아서 "unpacking"하는 방식으로 인자를 전달
x = [100,200,300]
y = [10,20]
z = 1,2,3,4

pr8(*x)                         # 100 200 300 => *를 사용
pr8(*y,30)                      # 인자값 c자리를 채워줘야한다.
# pr8(*z)                         # TypeError 개수를 맞춰줘야 한다.

# "*"를 이용하여 연속된 자료(리스트,튜플)에 데이터를 인자로 전달이 가능하나 
# 인자의 개수와 전달되는 개수는 같아야한다.(**)

# 인자값 처리 방식 2 => 가변 인자값 처리...
# - 고정인자 => 인자값을 반드시 정해진 값으로 1:1로 인자를 전해야하는 인자(일반)
# - 가변인자 => 인자값을 정해진 개수로 전달하지 않고, 가변적으로 전달 가능한 인자
#
# 가변인자 설정은 함수 정의시에 매개변수(인자) 앞에 "*"를 사용한다.

# 전달된 인자 값들의 합을 구하는 예제
def sum_func(*par):
    result = 0
    print(par,type(par))        # 전달된 인자값 처리 방식
    for su in par:
        result += su
    return result

def display() :
    Sum = 0
    Sum = sum_func()
    print(Sum)
    Sum = sum_func(10,20,30)
    print("인자가 3개(10,20,30)일 때 결과 : ",Sum)
    Sum = sum_func(10,20,30,40,50)
    print("인자가 5개(10,20,30,40,50)일 때 결과 : ",Sum)
# 메인
display()

# 주의) 인자값 처리함에 있어 고정인자와 가변인자를 동시에 사용하는 경우, 
# 고정인자를 먼저 처리하도록 한다. 즉, 가변인자는 마지막에 사용되게 해야한다.
#
# "**"를 사용하는 경우는 딕셔너리에 대한 packing을 시도한다는 의미로 처리
# 예제) 딕셔너리 자료형을 받아서 처리하는 함수
def dic_func(**par):
    print(par,type(par))
    for k in par:
        print("{}:{}".format(k,par[k]))

# 메인
dic_func(피카츄="1마리",파이리="2마리",꼬부기="없음",라이칸=1)

dic = {
    'sep' : '-',
    'end' : '\n\ntest'
}
lst = ['test1','test2','test3']
print('test','test',**dic)
print()
print('test','test',sep='-',end='\n\ntest')
print()
print(*lst,**dic)