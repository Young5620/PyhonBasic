## 연습문제
'''
문제6
다음과 같은 모형으로 출력되게 하세요
(1)       (2)       (3)         (4)
*         *****          *      *****
**        ****          **       ****
***       ***          ***        ***
****      **          ****         **
*****     *          *****          *
'''
print("-(1)-")
for x in range(5):
    print("{}{}".format("*"*(x+1)," "*(5-x)))
print("-(2)-")
for x in range(5):
    print("{}{}".format("*"*(5-x)," "*(x)))
print("-(3)-")
for x in range(5):
    print("{}{}".format(" "*(4-x),"*"*(x+1)))
print("-(4)-")
for x in range(5):
    print("{}{}".format(" "*(x),"*"*(5-x)))
print("-(5)-")
num = int(input("줄 수(홀수) : "))
for x in range(num//2):
    print("{}{}{}".format(" "*(num//2-x),"*"*(2*x+1)," "*(num//2-x)))
for x in range(num//2+1):
    print("{}{}{}".format(" "*(x),"*"*(num-2*x)," "*(x)))

'''
print("(1)")
for x in range(5):        #01234
    for y in range(x+1):
        print("*",end='')
    print()

print("while 문")
i = 0
while i<5:
    x = 0
    j = i + 1
    while x<j:
        print("*",end='')
        x+=1
    print()
    i+=1
print()

print("(2)")
for x in range(5):
    for y in range(5-x):
        print("*",end='')
    print()

print("(3)")
for x in range(5):
    for y in range(4-x):
        print(" ",end='')
    for z in range(x+1):
        print("*",end='')
    print()

print("(4)")
for x in range(5):
    for y in range(x):
        print(" ",end='')
    for z in range(5-x):
        print("*",end='')
    print()
'''

'''    
print("(5)")
num = int(input("줄 수(홀수) : "))
i = int(num/2)+1
for x in range(1,2*i):
    if x<i:
        for p in range(i-x):
            print(" ",end='')
        for q in range(2*x-1):
            print("*",end='')
        print()
    else :
        for p in range(x-i):
            print(" ",end='')
        for q in range((2*i-x)*2-1):
            print("*",end='')
        print()
'''

'''
import os   # os모듈은 파이썬에서 제공하는 기본 라이브러리 모듈로 
            # os와 관련된 함수들이 저장된 모율
            # system() => os의 시스템 명령어를 사용할 수 있게 함
import time # 시간과 관련된 제공하는 모듈
i, j = 0, 0; num = 1
while num:
    os.system('cls')        
    ln = int(input("줄 수(홀수)를 입력 : "))
    sp = ln//2          # 공백수
    st = 1              # 별 개수
    flag = True         # bool형 변수
    for i in range(ln):
        for j in range(sp): print(end=' ')  # 빈공간찍기
        for j in range(st): print(end='*')  # 별찍기
        print()
        if i == (ln//2) : flag = False
        if flag: sp -=1; st +=2
        else : sp +=1; st -=2
    num = int(input("계속하겠습니까?(0:종료,1:계속) : "))
'''

## 랜덤함수
#   : 임의의 값(난수)을 출력하는 함수
#   난수는 생성된 임의의 값을 의미한다.
#
#   랜덤 함수를 사용하기 위해서 모듈을 사용 : random

#   모듈 사용방법 : import [모듈명]
#   ex) import random                         -> 랜덤 모듈 전체를 로딩
#       or
#   ex) from [모듈] import [모듈에 있는 내용]  -> 모듈내에 일부 정보를 로드
#       from random[모듈] import random[함수]  : 랜덤 모듈내에 random()함수를 로드
#   두 방식은 기능 사용방식에 차이가 존재
#   import [모듈]인 경우, [모듈명].[사용할값]
#   from [모듈] import [모듈에 사용할 값]인 경우, 모듈에 [사용값]을 그대로 사용
from random import random
random()            # random모듈에 있는 random()
print(random())     # 0.0 ~ 1.0 미만의 임의 값을 출력(float)

# 0.0 ~ 10.0 미만의 임의값을 출력
print(random()*10)
# 0 ~ 10 미만의 임의값을 출력
print("{}".format(int(random()*10)))
# 1 ~ 10 까지의 임의값을 출력
print("{}".format(int(random()*10)+1))

# 예제1] 1~45까지 임의값 6개 출력
from random import random
for x in range(6):
    print(int(random()*45)+1,end=' ')
print()

'''
문제1
1~100까지 랜덤값을 6개 출력하는 코드작성

문제2
1~100까지 랜덤 값을 반복하여 출력하되, 출력값이 50이 되는 순간 반복이 종료되는 코드를 작성

문제3
1~15까지 랜덤 값을 중복없이 3개 생성하여 출력하는 코드 작성
'''
print("문제1")
for x in range(6):
    print(int(random()*100)+1,end=' ')
print()

print("문제2")
while True:
    ran = int(random()*100)+1
    print(ran,end=' ')
    if ran == 50:
        break
print()

print("문제3")
ran = 0
list = []
for i in range(3):
    ran = int(random()*15)+1
    while ran in list:
        ran = int(random()*15)+1
    list.append(ran)
print(list)

num1, num2, num3 = 0, 0, 0
while True:
    su = int(random()*15)+1
    if num1 != su:
        num1 = su
        break
while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su:
        num2 = su
        break
while True:
    su = int(random()*15)+1
    if num1 != su and num2 != su and num3 != su:
        num3 = su
        break
print(f"{num1},{num2},{num3}")

# random 모듈내에 있는 다른 형태의 random함수들..
# - randint() : 임의의 값을 출력하는 int 값 랜덤함수

# 사용방법
#   randint(a,b)
#     a:시작값, b:마지막값  => 시작값부터 마지막값까지의 랜덤

# 예제2 1~6까지 임의의 값 출력 
from random import randint
print(randint(1, 6))
print(randint(100, 200))

# 또 다른 random함수
#   randrange() : 범위 내에 있는 임의의 값 출력
# 예시1)
#  randrange(5,10)      => 5~10미만의 값을 출력(5,6,7,8,9)
# 예시2)
#  randrange(5,10,2)    => 5~10미만까지 2씩 증가값을 출력(5,7,9)

# 예제3
from random import randrange
print(randrange(10))
print(randrange(5,10))
print(randrange(5,10,2))

# random 모듈 내에 choice()함수
#   : 이 함수의 특징은 리스트와 같은 형태의 자료 중 일부를 랜덤하게 추출하는 함수

# 예시)
# dice = [1,2,3,4,5,6]
# choice(dice)      # dice 리스트 내에 있는 멤버중 하나를 선택

# 예제4
import random
dice = [1,2,3,4,5,6]
st = 'Hello World'
x = random.choice(st)
print("dice에서 출력된 값 : ",x)
# or
from random import choice,random,randint,randrange
dice = [1,2,3,4,5,6]
st = 'Hello World'
x = choice(dice)
print("dice에서 출력된 값 : ",x)

'''
문제4 
1~99까지 랜덤값 중에 짝수는 True, 홀수는 False를 출력하는 프로그램 코딩
'''
rand = randint(1, 99)
if rand % 2 == 0:
    print("랜덤값 : ",rand," True")
else :
    print("랜덤값 : ",rand," False")
    
'''
ASCII 코드
미국 표준 문자 코드로 7bit(0~127)로 하나의 문자를 표현할 수 있음.
ASCII코드는 통신상 기본 문자 코드로 사용되고 있음.

(특징)
1. 프린트 가능한 문자 총 95자, 나머지 33개 문자는 프린트가 불가능한 문자.
   프린트 가능한 문자의 시작 0x20(32)->"공백"부터 시작, 0x7e(123)까지임
2. 숫자는 0x30(48)="0"에서부터 0x39(57)="9"까지 값을 가진 10개의 코드
3. 영문 대문자는 0x41(65)=>"A"에서부터 0x5A(90)="Z"까지
4. 영문 소문자는 0x61(97)=>"a"에서부터 0x7A(122)="z"까지
5. ASCII코드는 문자이나 숫자(정수)로 표현이 가능함

숫자를 문자(ASCII)로 변경하는 함수 : chr()
()안에 코드값을 전달하면 그 값을 문자로 출력하는 함수
'''
print(chr(65))
print(chr(0x41))

# 문제5 'A'~'Z'까지 임의 문자 3자리를 출력하는 코드를 작성하세요.
num1, num2, num3 = 0, 0, 0
while True:
    su = int(random()*26)+65    # 65~90
    if num1 != su:
        num1 = su
        break
while True:
    su = randint(65, 90)
    if num1 != su and num2 != su:
        num2 = su
        break
while True:
    su = randint(65, 90)
    if num1 != su and num2 != su and num3 != su:
        num3 = su
        break
print("{} {} {}".format(chr(num1),chr(num2),chr(num3)))

# list
# 리스트 자료형이란?
#   - 데이터 목록을 다루는 자료형
#   - 리스트를 정의할 때는 "[]"를 사용함
#   - 리스트 안에는 어떤 종류의 자료형이든 상관없이 저장가능

# List 자료형의 기본사용
# (정의)
#   변수명 = []         # 비어있는 리스트를 선언
#   변수명 = [value1,value2,value3,...]
#   (value들의 타입은 상관없이 가능)
# (list()를 이용한 리스트 생성)
#   변수명 = list()     # 비어있는 리스트를 선언
#   변수명 = list("Hello")  # ['H','E','L','L','O']
#   변수명 = list(range(5)) # [0,1,2,3,4]

# 예제1 리스트 선언 및 값에 대한 처리
lst = [1,2,3,4,5,6,7,8]
print(type(lst))                    # <class 'list'>
# 생성된 리스트에 대한 특정 값 참조 : 인덱스(index)값을 이용
# indexing 방법 : 변수명[인덱스값]      # 주의) 인덱스 값의 시작은 0부터 시작
print(lst[0])                       # 1
print(lst[3])                       # 4

# 인덱싱을 이용한 list값 변경
lst[0] = lst[5]
print(lst[0])                       # 6
print(lst)                          # [6, 2, 3, 4, 5, 6, 7, 8]

# 리스트 자료의 길이(요소[멤버]의 개수) : len()
print("lst의 길이 : ",len(lst))     # lst의 길이 :  8

# 리스트의 결합1(병합)
lst2 = [9,10]
print(lst+lst2)                     # [6, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lst3 = lst+lst2
print(lst3)                         # [6, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트의 결합2(확장)
lst = lst + lst2
print(lst)                          # [6, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# 리스트의 반복
print(lst2*3)                       # [9, 10, 9, 10, 9, 10]

# max() : 최대값 ,min() : 최소값
print(max(lst))                     # 10
print(min(lst))                     # 2
print(sum(lst))                     # 60
print(pow(4, 2))                    # 16

# 변수를 선언, 3개의 정수를 입력받아 합을 출력
# 출력결과 : 합계 = xx <-"합계" 문자도 변수로 저장하여 사용
'''
x = int(input("첫번째 정수 : "))
y = int(input("두번째 정수 : "))
z = int(input("세번째 정수 : "))
Sum = x+y+z
lst = ['합계',Sum]
print(f"{lst[0]} = {lst[1]}")

# 예제2 리스트의 멤버를 변수처럼 사용
lst = [0,0,0,'합계']
lst[0] = int(input("첫번째 정수 : "))
lst[1] = int(input("두번째 정수 : "))
lst[2] = int(input("세번째 정수 : "))
Sum2 = lst[0] + lst[1] + lst[2]
print(f"{lst[3]} = {Sum2}")
'''
# List 인덱싱
#  : 인덱스 값을 이용한 참조
#         lst =[ 1, 2, 3, 4, 5, 6, 7, 8]
# 양의 인덱스 =  0  1  2  3  4  5  6  7
# 음의 인덱스 = -8 -7 -6 -5 -4 -3 -2 -1

# (-1) = 11111111 11111111 11111111 11111111
# (-2) = 11111111 11111111 11111111 11111110

# 예제3 List 인덱싱
lst = [1,2,3,4,5,6,7,8]
print(lst[0])
print(lst[-1])
print(lst[-2])
print(lst[-7])

# slicing방식을 이용한 시퀀스 객체(자료) 접근
# slicing이란 리스트와 같은 스퀸스 자료 값들의 범위로 접근하기 위해서 사용하는 방법으로
#             시퀸스 자료의 일부를 잘라서 새롭게 생성하는 것을 의미함.
# (형식)
# 변수명[시작인덱스:끝인덱스]
# 변수명[시작인덱스:끝인덱스:증감값]

# 예) lst = [ 1, 2, 3, 4, 5, 6]
#    index    0  1  2  3  4  5
#     (-)    -6 -5 -4 -3 -2 -1
# lst[0:3] => [1,2,3] , lst[0,3,2] = [1,3]
lst = [1,2,3,4,5,6]
print(lst[0:3])         # 1,2,3
print(lst[0:3:2])       # 1,3
print(lst[-6:-3])       # 1,2,3
print(lst[-1:-3:-1])    # 6,5
print(lst[5:0:-3])      # 6,3

## 인덱스 생략
print(lst[:3])          # 시작값 생략 = 1,2,3
print(lst[3:])          # 끝값 생략 = 4,5,6
print(lst[:])           # 둘다 생략 = 1,2,3,4,5,6

# 슬라이싱 후 새로운 리스트 생성
slc1 = lst[3:6]
print(slc1)             # [4, 5, 6]
slc2 = lst[1:5:3]
print(slc2)             # [2, 5]
slc3 = lst[5::-1]
print(slc3)             # [6, 5, 4, 3, 2, 1]
slc4 = lst[-3:-1]
print(slc4)             # [4, 5]

# 리스트 함수들
#  - append(value)      : 리스트 끝에 값을 추가(멤버추가)
#  - extend(iter)       : 리스트 끝에 list,tuple,dict의 값을 하나씩 추가
#  - insert(idx,value)  : idx에 있는 인덱스 위치에 특정값을 추가하는 함수
# ===================== 값을 추가하는 메서드
#  - pop([idx])         : 인덱스를 지정하지 않으면, 마지막 인덱스 값을 반환 후 삭제/인덱스를 지정하면 해당 인덱스 값을 반환 후 삭제
#  - remove(value)      : 특정 값을 찾아서 삭제하는 함수
#  - clear()            : 리스트의 모든 멤버를 삭제하고, 빈 리스트로 만드는 함수
# ===================== 값을 삭제하는 메서드
#  - count(value)       : 리스트 내에 특정 값의 개수를 반환하는 함수
#  - index(value)       : 리스트 내에 특정 값의 인덱스 값을 반환하는 함수
#  - reverse()          : 리스트의 멤버의 순서를 뒤집어서 나열하는 함수
#  - sort([reverse=False]) : 리스트의 값을 오름차순(False), 내림차순(True) 정렬해주는 함수

# append() : 리스트 끝에 값을 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.append('a')
print(lst1)             # [1, 2, 3, 4, 5, 6, 7, 8, 'a']
lst1.append([9,10])
print(lst1)             # [1, 2, 3, 4, 5, 6, 7, 8, 'a', [9, 10]] => len(lst1) = 10
print(len(lst1))        # 10
print(lst1[-1])         # [9, 10]

# extend() : 리스트 뒤에 추가할 리스트, 튜플, 딕셔너리 자료를 멤버에 개별적 추가
lst1 = [1,2,3,4,5,6,7,8]
lst1.extend('abcdef')
print(lst1)             # [1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd', 'e', 'f']

# insert(idx,value) : idx에 있는 인덱스 위치에 값을 추가
lst1 = [1,2,3,4,5,6,7,8]
# idx:  0,1,2,3,4,5,6,7
lst1.insert(3, 'a')
print(lst1)             # [1, 2, 3, 'a', 4, 5, 6, 7, 8]

# pop([idx]) : 마지막 인덱스 값을 반환 후 삭제, 인덱스를 지정하면 해당 인덱스 값을 반환 후 삭제
lst1 = [1,2,3,4,5]
a = lst1.pop()          # a = 5, lst1 = [1,2,3,4]
print(a)                
print(lst1)
b = lst1.pop(2)         # b = 3, lst1 = [1,2,4]
print(b)
print(lst1)

# remove(value) : 특정값을 찾아서 삭제 (검색시에 없으면 Error를 반환)
lst1 = [1,2,3,2,5,6,2,8]
lst1.remove(2)          # 첫번째 2가 삭제됨
print(lst1)             # [1, 3, 2, 5, 6, 2, 8]
lst1.remove(2)          # 두번째 2가 삭제됨
print(lst1)             # [1, 3, 5, 6, 2, 8]
lst1.remove(2)          # 세번째 2가 삭제됨
print(lst1)             # [1, 3, 5, 6, 8]
# lst1.remove(2)          # ValueError: list.remove(x): x not in list
# print(lst1)

# clear()
lst1 = [1,2,3,4,5]
lst1.clear()
print(lst1)