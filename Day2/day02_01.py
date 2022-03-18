# 변수 선언
# 1. 변수이름 = 값
# 2. 변수이름1, 변수이름2, 변수이름3 = 값1, 값2, 값3
# 3. 변수이름1 = 변수이름2 = 값1
print("======변수선언 practice======")
num1, num2, num3 = 10, 20, 30
print(num1,num2,num3)

su1 = su2 = 100
print(su1,su2)
print(id(su1),id(su2))

su1 = 200
print(su1,su2)
print(id(su1),id(su2))

su1 = su1 + su2
print(su1)
print(id(su1),id(su2))

#print("======inpur()함수 practice======")

## input() 함수 : 문자열을 입력받는 함수로 반환값은 str(문자열)
# print(type(input()))
# print(input("입력 : "))
'''
## 문자형 숫자 입력
num = input("숫자 입력 : ")
print('num type : ', type(num))
print('num = ',num)
print('num = ',num*2)

## 숫자 연산을 위한 형변화
num1 = int(input("정수 입력 : "))
print('num1 = ',num1*2)

num2 = float(input("실수 입력 : "))
result = num1 + num2
print('result = ',result)
'''
## 정리, 인자(prompt)에 입력받기 위한 설명을 사용할 수 있다.
#  input()는 문자열로 입력을 받기 때문에 숫자로 사용하기 위해서는 필요한 형태로 형변환을 반드시 해야한다.
'''
print("======연습문제======")

## 연습 - input()를 사용하여 나이와 이름을 입력받아 다음과 같이 출력되게 코드를 만들어 주세요
#(보기)
# => '홍길동' 님의 나이는 100세입니다.
name = input("이름 : ")
age = int(input("나이 : "))
print("'{}' 님의 나이는 {}세 입니다.".format(name,age))
print(f"'{name}' 님의 나이는 {age}세 입니다.")
'''
print("======연산자 practice ======")
## 연산자
# 1. 산술연산자 : 산술연산을 위해서 사용하는 연산자
#   "+","-","*","/","//"(정수나누기),"%"(나머지),"**"(제곱)
print("====== 산술연산자 practice ======")

num1 = 3
num2 = 2
print(num1+num2) # 3+2
print(num1-num2) # 3-2
print(num1*num2) # 3*2
print(num1/num2) # 3/2 -> 나누기 결과 float(실수)로 변환됨
print(num1//num2) # 3/2 의 몫
print(num1%num2) # 3/2 의 나머지
print(num1**num2) # 3^2

# 2. 비교연산자 : 두 항의 값(기준은 좌항)을 비교하여 관계를 설명하는 연산자 -> bool로 True or False
#   "=="(같다),"!="(다르다),">"(크다),"<"(작다),">="(크거나같다),"<="(작거나같다)
print("====== 비교연산자 practice ======")
print(3==3) # T
print(3!=3) # F
print(3>2) # T
print(3<2) # F
print(3>=2) # T
print(3<=2) # F

# 3. 논리연산자 : 두 항의 값이 참인지 거짓인지 확인하여 판별하는 연산자 -> bool(True=1,False=0)
#   "and"(논리곱) - 두 항의 값이 모두 true인 경우에 True를 반환
#   "or"(논리합) - 두 항 중 하나라도 True이면 True를 반환
#   "not"(부정) - True이면 False를 False이면 True를 반환
print("====== 논리연산자 practice ======")
print("bool의 True의 int형변환 값은 ", int(True))
print("bool의 False의 int형변환 값은 ", int(False))
print(0 and 0)
print(1 and 0)
print(0 and 1)
print(1 and 1)
print(0 or 0)
print(1 or 0)
print(0 or 1)
print(1 or 1)
print(not 0)
print(not 1)

# 4. 멤버연산자 : 왼쪽 피 연산자의 값이 오른쪽 연산자 멤버 중 일치여부를 확인하는 연산자
#   "in" - 왼쪽 피 연산자의 값이 오른쪽 피연산자에 존재하는 경우 True
#   "not in" - 왼쪽 피 연산자의 값이 오른쪽 피연산자에 존재하지 않는 경우 True
print("====== 멤버연산자 practice ======")
print(1 in (1,2,3))         # True
print(1 not in (1,2,3))     # False

# 5. 식별연산자 : 식별값 비교 연산하여 처리하는 연산자
#   "is" - 두 피연산자의 식별값(객체타입)을 비교하여 동일 객체라면 True
#   "is not" - 두 피연산자의 식별값을 비교하여 동일 하지 않은 객체라면 True
print("====== 식별연산자 practice ======")
num1, num2 = 1,"1"
print(type(num1) is int)        # True
print(type(num2) is not int)    # True
print(type(num1) is not str)    # True
print(type(num2) is str)        # True
print("====== 비트연산자 practice ======")
# 6. 비트연산자 : 비트값을 연산처리하는 연산자들
#   "&" : 두 비트 and연산처리하는 연산자(논리곱)
#       00001010(10) &
#       00001111(15)
#       ============
#       00001010(10)
print(10&15)
#       00001010(10) &
#       00001101(13)
#       ============
#       00001000(8)
print(10&13)

#   "|" : 두 비트 or연산처리하는 연산자(논리합)
#       00001010(10) |
#       00001111(15)
#       ============
#       00001111(15)
print(10|15)
#       00001010(10) |
#       00000101(5)
#       ============
#       00001111(15)
print(10|5)

#   "^" : 두 비트 xor연산처리하는 연산자(배타적 논리합) / 암호문 처리할 경우에 사용됨
#         두 비교 비트가 동일하면 0을 반환하고 둘중 하나라도 1이라면 1
#       00001010(10) ^ - 원본
#       00001101(13)   - 키
#       ============
#       00000101(7)    - 암호
print(10^13)
#       00000101(7) ^  - 암호
#       00001101(13)   - 키
#       ============
#       00001010(10)   - 원본
print(7^13)

#   "<<" : 왼쪽 피 연산자 비트를 왼쪽으로 오른쪽 숫자만큼 이동
#       00001010(10) << 3
#       ============
#       01010000(80)
#   특징 : 2의 제곱승으로 곱하는 정수 곱하기
print(10<<3)

#   ">>" : 왼쪽 피 연산자 비트를 오른쪽으로 오른쪽 숫자만큼 이동
#       00001010(10) >> 3
#       ============
#       00000001|010(1)
#   특징 : 2의 제곱승으로 나누는 정수 나누기
print(10>>3)

#print("====== 연습문제 ======")
'''
문제1 num1, num2, num3 = 5, 15, 27
    위 변수에 할당된 값을 사용하여 다음의 결과가 나오도록 산술연산자를 사용하시오
    ㄱ. -12
    ㄴ. 75
    ㄷ. 25
    ㄹ. 5.4
    ㅁ. 3.0

문제2 다음의 연산자를 보고 True와 False를 구분하시오
    ㄱ. 7>18
    ㄴ. 5<2
    ㄷ. 6%3>2
    ㄹ. 5+5 !=2*5
    ㅁ. True==1
    ㅂ. 1=='1'
    ㅅ. 10//3 == 10%3
    ㅇ. 15%4 in (0,1,2)

문제3 input()으로 2개의 값을 받은 다음 더하기,빼기,곱하기,나누기 연산을 하여 그결과를 출력하는 코드를 작성

문제4 사용자로부터 이름, 키, 체중 값을 입력받아 비만도를 구하고 출력하는 코드를 작성하시오
      비만도 계산식 : 비만도(%) = 현재체중 / 표준체중*100   표준체중 계산식 : 표준체중 = (현재키-100)*0.9
      출력예제 : 홍길동님의 비만도는 112.15%입니다.
'''
'''
print("-문제1-")
num1, num2, num3 = 5, 15, 27
print("ㄱ.",num2-num3)
print("ㄴ.",num1*num2)
print("ㄷ.",num1**2)
print("ㄹ.",num3/num1)
print("ㅁ.",num2/num1)

print("-문제2-")
print("ㄱ.",7>18)
print("ㄴ.",5<2)
print("ㄷ.",6%3>2)
print("ㄹ.",5+5 !=2*5)
print("ㅁ.",True==1)
print("ㅂ.",1=='1')
print("ㅅ.",10//3 == 10%3)
print("ㅇ.",15%4 in (0,1,2))

print("-문제3-")
num1 = int(input("숫자 : "))
num2 = int(input("숫자 : "))
print("덧셈 : ",num1+num2)
print("뺄셈 : ",num1-num2)
print("곱셈 : ",num1*num2)
print("나눗셈 : ",num1/num2)

print("-문제4-")
name = input("이름 : ")
height = float(input("키(cm) : "))
weight = float(input("체중(kg) : "))
aver_wei = (height-100)*0.9
pig_per = weight/aver_wei*100
print("{}님의 비만도는 {:5.2f}% 입니다.".format(name,pig_per))

print("*****숙제*****")
su = 5
dan = 800
print("su 주소 : ", id(su))
print("dan 주소 : ", id(dan))
print("금액 : {:,}".format(su*dan))

x = 2
y = 2.5*(x**2) + 3.3*x + 6
print("2차 방정식 결과 = {}".format(y))

fat = int(input("지방의 그램을 입력하세요 : "))
car = int(input("탄수화물의 그램을 입력하세요 : "))
pro = int(input("지방의 그램을 입력하세요 : "))
total = fat*9 + pro*4 + car*4
print("총 칼로리 : {:,} cal".format(total))
'''

#### 제어문(if), 반복문(for,while)
# 제어문(if)
# 단순 if
#   사용형식1
# if 조건식 : 
#     실행문(종속문장1)
#     실행문(종속문장2)         => if 블럭
# 특징: 조건식이 참일 경우에 종속문장을 실행
#       파이썬에서는 다른 언어와 다르게 들여쓰기가 중요함.
#       들여쓰기를 가지고 블럭을 구분함
'''
#[예제]
num = int(input("정수 입력 : "))
if num % 2 == 0 :
    print("num의 값은 짝수입니다.")
    print("num의 값은 2의 배수입니다.")
print("if 다음 문장 실행")

#[예제]
print("1. Easy Game")  
print("2. Hard Game")
print("3. Exit")
num = int(input("번호 선택 >> "))
if num == 1:
    print("Easy Game Start")
if num == 2:
    print("Hard Game Start")
if num == 3:
    print("Game Exit")
    
#[예제3]
su = int(input("수 입력 : "))
if su == 1 :
    print("1 입력")
if su > 10 :
    print("10보다 큰 값을 입력하셨습니다.")    
if su < 10 :
    print("10보다 작은 값을 입력하셨습니다.")
    
#[예제4]
x = 15
if x > 10 and x !=10 :
    print("x변수의 값은 10보다 크고, 10과 같지 않다.")
if x > 10 or x !=15 :
    print("or는 둘 중 하나라도 참이면 참으로 결과를 반환")

#[예제5]
su = int(input("1~10사이의 정수를 입력하세요 : "))
if su in(1,4,7) : 
    print("멤버에 있는 숫자입니다.")

# if ~ else : if의 조건식이 참이면, if의 종속문장을 그렇지 않은 else의 종속문장을 실행
# if 조건식 : 
#     실행문(종속문장1)
#     실행문(종속문장2)         => if 블럭
# else 조건식 : 
#     실행문(종속문장1)
#     실행문(종속문장2)         => else 블럭

#[예제6]
if x > 10 and x != 15:
    print("x는 10보다 크고, 15와 같지않다.")
else :
    print("x는 10보다 크고, 15와 같다")
''' 
#print("====== 연습문제 ======")
'''
1. 입력한 데이터가 3의 배수인 경우 출력하시오
2. 절대값을 구하는 프로그램을 작성하시오
3. 수를 입력받아 짝, 홀수를 구분하여 출력하시오
4. 두수를 입력받아 큰 수를 출력하시오
5. 세수를 입력받아 큰수를 출력하시오
6. 두수를 입력받아 큰수가 짝수이면 출력하시오
7. 두수를 입력받아 합이 짝수이고 3의 배수인 수를 출력하시오
'''
'''
su1 = int(input("정수를 입력하세요 : "))
if su1 % 3 == 0 : 
    print("입력한 숫자는 3의 배수입니다.")
else : 
    print("입력한 숫자는 3의 배수가 아닙니다.")
    
su2 = int(input("정수를 입력하세요 : "))
if su2 < 0 :
    print(-su2)
if su2 > 0 :
    print(su2)
    
su3 = int(input("정수를 입력하세요 : "))
if su3 % 2 == 0 :
    print("입력한 숫자는 짝수입니다.")
else : 
    print("입력한 숫자는 홀수입니다.")

print("두 수를 입력하세요")
su4 = int(input("정수를 입력하세요 : "))
su5 = int(input("정수를 입력하세요 : "))
if su4 > su5 :
    print("큰 수는 {} 입니다.".format(su4))
if su4 < su5 :
    print("큰 수는 {} 입니다.".format(su5))
    
print("세개의 숫자를 입력하세요")
su6 = int(input("정수를 입력하세요 : "))
su7 = int(input("정수를 입력하세요 : "))
su8 = int(input("정수를 입력하세요 : "))
if su6 > su7 and su6 > su8 : 
    print("가장 큰 수는 {} 입니다.".format(su6))
if su7 > su6 and su7 > su8 : 
    print("가장 큰 수는 {} 입니다.".format(su7))
if su8 > su6 and su8 > su6 : 
    print("가장 큰 수는 {} 입니다.".format(su8))

print("두 수를 입력하세요")
su4 = int(input("정수를 입력하세요 : "))
su5 = int(input("정수를 입력하세요 : "))
if su4 > su5 and su4 % 2 == 0 :
    print("큰 숫자가 짝수입니다.")
if su5 > su4 and su5 % 2 == 0 :
    print("큰 숫자가 짝수입니다.")
else : 
    print("큰 숫자가 홀수입니다.")

print("두 수를 입력하세요")
su4 = int(input("정수를 입력하세요 : "))
su5 = int(input("정수를 입력하세요 : "))
if (su4 + su5) % 2 == 0 and (su4 + su5) % 3 ==0 :
    print("두수의 합이 짝수이면서 3의 배수입니다.")
else : 
    print("두수의 합이 홀수이거나 3의 배수가 아닙니다.")
'''

# 중첨 if 구문 : if 구문안에 if 구문을 사용하는 경우
# 다중 if 구문 : if ~ elif ~ else 구문으로 if와 elif 조건을 확인 부합되면 종속실행
#               만약 조건에 부합되지 않는 경우에는 else를 실행
'''
# [예제7] 중첩 if 구문
num1 = int(input("첫번째 정수 입력"))
num2 = int(input("두번째 정수 입력"))
Sum = num1 + num2
if Sum % 2 == 0 :
    if Sum % 3 == 0 :
        print(f"입력하신 두 수의 합은 {Sum}, 3의 배수이면서 짝수입니다.")
    else :
        print("입력하신 두 수의 합은 짝수이지만, 3의 배수는 아닙니다.")
else :
    print("입력하신 두 수의 합은 짝수가 아닙니다.2")

# [예제8] 다중 if 구문(if ~ elif ~ else)
num = int(input("1 ~ 4 숫자를 입력하세요 : "))
if num ==1 : 
    print("1 입력")
elif num ==2 : 
    print("2 입력")
elif num ==3 : 
    print("3 입력")
elif num ==4 : 
    print("4 입력")
else : 
    print("잘못 입력했습니다.2")
'''    
'''
[Quiz1]
사용자로부터 Gbyte의 값을 입력 받아 byte,Kbyte,Mbyte로 각각 출력되게 만드시오
(1.byte 2.Kbyte 3.Mbyte)

[Quiz2]
인증 프로그램을 만드시오
1. 아이디가 틀리면 등록되지 않은 아이디 입니다 출력
2. 비밀번호가 틀리면 비밀번호가 틀렸습니다 출력
3. 아이디와 비밀번호가 일치한다면 인증 통과 출력
old_id = test, old_pw = python123
'''
'''
print("=== Quiz1 ===")
data = int(input("Gbyte를 입력하세요 : "))
print("1. byte")
print("2. Kbyte")
print("3. Mbyte")
unit = int(input("원하는 단위를 선택하세요."))
if unit == 1 :
    print(data,"Gbyte = {} byte".format(data*1024**3))
elif unit == 2 :
    print(data,"Gbyte = {} Kbyte".format(data*1024**2))
elif unit == 3 :
    print(data,"Gbyte = {} Mbyte".format(data*1024))
else : 
    print("잘못 입력 하셨습니다.")
    
print("=== Quiz2 ===")
Id = input("아이디를 입력하세요 : ")
Pw = input("비밀번호를 입력하세요 : ")
old_id = 'test'
old_pw = 'python123'
if Id == old_id :
    if Pw == old_pw :
        print("로그인에 성공하였습니다.")
    else :
        print("비밀번호를 잘못 입력하였습니다.")
else :
    print("아이디를 잘못 입력하였습니다.")
'''
## 삼항 조건문 : 삼항 연산자, 조건이 참인 경우와 거짓인 경우 처리할 문장을 한 줄로 작성
# 조건식 비교결과에 따라 선택적으로 실행문이 동작합니다.
# (형식)
# 변수 = 참일 경우 동작 if (조건문 else) 거짓일 경우 동작

# 삼항 조건문 예제
# 1) 일반 조건문
num = 9
result = 0

if num >= 5 :
    result = num * 2
else :
    result = num + 2
print("result : ",result)
print("삼항연산자")
result2 = num * 2 if num >= 5 else num + 2
print("result : ",result2)
'''
문제 사용자로부터 이름, 키, 체중 값을 입력받아 비만도를 구하고 출력하는 코드를 작성하시오
비만도 계산식 : 비만도(%) = 현재체중 / 표준체중*100   표준체중 계산식 : 표준체중 = (현재키-100)*0.9
비만도가 100 미만일 경우 : "저체중"
비만도가 100~110사이인 경우 : "정상체중"
비만도가 110~120사이인 경우 : "과체중"
비만도가 120~130사이인 경우 : "비만"
비만도가 그 이상인 경우 : "고도비만"으로 표현되게 작성해주세요
'''
print("-문제-")
name = input("이름 : ")
hei = float(input("키(cm) : "))
wei = float(input("체중(kg) : "))
std = (hei-100)*0.9
pig_per = wei/std*100

if pig_per < 100 :
    result = '저체중'
elif pig_per >= 100 and pig_per < 110 : 
    result = '정상체중'
elif pig_per >= 100 and pig_per < 110 : 
    result = '과체중'
elif pig_per >= 110 and pig_per < 120 : 
    result = '비만'
elif pig_per >= 120 : 
    result = '고도비만'
print("{}님의 비만도는 {:5.2f}%로 {} 입니다.".format(name,pig_per,result))