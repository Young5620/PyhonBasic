# Builtins 함수(내장 함수)
# 
# help()    # 함수, 객체에 대한 설명(도움말)
# print()   # 터미널 화면에 결과를 출력
# input()   # 표준입력으로 받은 결과를 처리
# sum()     # 인자값으로 여러개의 숫자를 받아서 합(딕셔너리제외)
# max()     # 인자값들 중에서 가장 큰 수를 반환
# min()     # 인자값들 중에서 가장 작은 수를 반환
# pow()     # 인자값을 통해서 제곱 처리하는 함수
# 
# 내장함수들은 도움말(help) -> in module builtins...(p.118)
# 
# import ** : 모듈을 불러오는 명령어
# 
#  import builtins
#  dir(builtins)    # 내장클래스, 내장함수 목록을 보여줌
# 1. abs(x) : x를 대상으로 절대값을 반환하는 함수
print(abs(10))
print(abs(-10))

# 2. all(iterable) : 모든 요소가 True이면 True를 반환
lst = [1,2,36,7,-9,49]
lst2 = [0,1,2,3,4,5,7]
print(all(lst))
print(all(lst2))

# 3. any(iterable) : 하나 이상의 요소가 True일때 True를 반환
lst3 = [0,False,'',[]]
lst4 = [1,False,0,-15,4]
print(any(lst3))
print(any(lst4))

# 4. bin(number) : 10진수 정수를 2진수로 변환, 표현식 0b
#    oct(number) - 0o , hex(number) - 0x

# 5. dir(x) : 객체 x에서 제공하는 변수, 내장함수, 내장클래스 목록을 반환
# print(dir(lst3))

# 6. eval(expr) : 문자열 수식을 인수로 받아서 계산 가능한 파이썬 수식으로 변환
print(eval("10+20"))
# print(eval(10+"20+30")) 이거 안됨!    print(10+eval("20+30")) 이거는 됨
print(10+eval("20+30"))

# 7. ord(charactor) : charactor를 아스키코드값(문자코드값)으로 반환
# ' ' -> 0x20, 0 -> 0x30(48), A -> 0x41(65), a -> 0x61(97)
print(ord('0'))     # 0x30(48)
print(ord('A'))     # 0x41(65)
print(ord('a'))     # 0x61(97)
print(ord('가'))    # 0xac00

# 8. chr(number) : number를 코드값으로 반환
print(chr(0x30))
print(chr(0xac00))

# 9. pow(x,y) : x에 대한 y의 제곱을 계산하여 반환
print(pow(2, 3))
print(pow(10, 3))
print(pow(10, -1))
print(pow(-8, -2))

# 10. round(number,자리수) : 올림값 처리
print(round(3.141592))      # 3
print(round(3.141592,3))    # 3.142

# 11. sorted(iterable) : 반복 가능한 원소들을 오름차순 또는 내림차순으로 정렬한 결과를 반환

# 12. zip(iterable*) : 반복 가능한 객체롸 객체간의 원소들을 묶어서 튜플로 반환
zi = zip([1,3,5],[2,4,6])
print(list(zi))             # [(1, 2), (3, 4), (5, 6)]



## python의 모듈 및 패키지의 사용
# 
# 모듈(Module)이란? 함수, 변수, 클래스들을 모아놓은 파일
# (모듈은 만들어 놓은 다른 파이썬 프로그램에서 불러와 사용이 가능함)
# - 모듈을 만드는 방법 : *.py 확장자를 이용하여 만들 수 있음
# - 모듈을 불러오는 방법 : import 명령어를 사용하여 모듈을 불러와 사용함
#   (표준 라이브러리를 불러와 사용할 때에는 import사용함)
'''
# 시간과 관련있는 모듈들
import datetime,time
# datetime 모듈은 시간에 대해서 가공된 정보를 처리
s = datetime.datetime.now()     # 현재시간을 알아옴
print(s)
t = time.localtime()            # 현재 동작중인 지역의 시간
print(t)                        # 딕셔너리 형태로 반환
print(t.tm_year)
print(t.tm_zone)

start = time.time()             # 1970.01.01.00 시를 기점으로 초를 계산
print(start)
# time.sleep(5)
end = time.time()
print(end)
'''
# 모듈을 불러와 사용하기
# 
# (형식)
# import 모듈명 => 모듈 내에 있는 모든 함수,클래스,변수들을 호출
''' 
# 사용할 때에는 모듈명.함수(변수,클래스)
import calc             # as를 사용하여 별칭으로 호출 가능
a = 100
b = 200
c = 10
Sum = calc.Sum(a, b)
Sub = calc.Sub(a, b)
Mul = calc.Mul(a, c)
Div = calc.Div(b, a)
print(Sum,Sub,Mul,Div)

calc.result = (Sum + Sub) - int((Mul/Div))
print("((a+b)+(b-a)) - ((b*c)/(b-a)) = ",calc.result)

# (형식2)
# from 모듈 import *
# => 모듈내에 있는 모든 변수, 함수와 클래스를 호출
'''
# 모듈에 있는 내용을 사용할 경우 : 함수(변수,클래스)명을 그대로 사용
'''
from calc import *      # 테스트용으로 사용하는 경우가 많음
a = 10
b = 20
c = 30
Sum_re = Sum(a,b)
Sub_re = Sub(a,b)
Mul_re = Mul(a,b)
Div_re = Div(a,b)
result = Sum_re + Sub_re + Mul_re + int(Div_re)
print(Sum_re)
print(Sub_re)
print(Mul_re)
print(Div_re)
print(result)
'''
# (형식3)
# from 모듈 import <함수,변수,클래스명>
# =>모듈 내에 있는 특정 변수, 클래스, 함수를 호출
'''
from calc import Sum,Sub,Mul,Div,result      # 테스트용으로 사용하는 경우가 많음
a = 10
b = 20
c = 30
Sum_re = Sum(a,b)
Sub_re = Sub(a,b)
Mul_re = Mul(a,b)
Div_re = Div(a,b)
result = Sum_re + Sub_re + Mul_re + int(Div_re)
print(Sum_re)
print(Sub_re)
print(Mul_re)
print(Div_re)
print(result)
'''
# 패키지 생성후 사용하기
# 패키지란? 여러 동작과 관련된 모듈을 모아 놓은 것을 의미함

# (패키지 생성 순서)
# 1. 패키지로 사용할 폴더를 생성
# 2. 패키지 폴더에 묶어서 사용할 모듈을 저장
#   (주의사항] python3.3 이하 버전에서는 폴더에 "__init__.py"파일을 생성합니다. 파일안에 내용이 없어도 상관이 없음)
# 3. 패키지를 import 명령어를 사용하여 불러옴
#   (패키지 폴더 이름이 바로 패키지명이 된다.)
#   from 패키지명 import 모듈명
'''
from testpack import Sum,Sub,Mul,Div

print(Sum.Sum(100, 200))
print(Sub.Sub(100, 200))
print(Mul.Mul(100, 200))
print(Div.Div(100, 200))
'''

### python 파일 입출력 사용
# - 디스크에 파일을 읽어 들이거나
# - 디스크에 파일을 생성하여 저장하는 기능을 의미함
# - 많은 양의 데이터를 처리(저장)할 때에 유용하게 사용됨
#  ex) 홈페이지 이미지, 데이터, 음악, 파일 정보등을 저장할때에..
# 
# [과정-순서]
# 1. open함수를 이용하여 파일(객체)을 열기
# 2. read(읽기) 또는 write(쓰기) 관련 함수를 이용하여 파일에 대해서 작업
#    진행 및 처리하는 단계
# 3. open으로 열린 파일의 내용을 close함수를 사용하여 닫는다.
'''
import os
print(os.getcwd())
# 1. open함수 사용
file = open("PyhonBasic/Day9/data/test_text.txt",mode='w',encoding='utf-8')
# /data/test_text.txt 파일에 대한 fileIO생성

# -"a" => 모드 영역
# open함수 사용시 모드 설정 ㄱ밧
# r(read-읽기) => 파일이 있는 경우, 해당 파일에 대해 읽기동작을 실행
#                 파일이 없는 경우, 에러를 출력(file not Found)
# w(write-쓰기) => 파일이 있는 경우, 해당 파일에 있는 내용을 삭제 후 새롭게 쓰기
#                  파일이 없는 경우, 파일을 생성하고, 쓰기를 진행
# a(append-추가) => 파일이 있는 경우, 파일에 마지막에 추가로 쓰기 작업을 진행
#                   파일이 없는 경우, 파일을 생성하고, 쓰기를 진행
# x             => 파일이 있는 경우, 생성 에러를 발생
#               => 파일이 없는 경우, 파일을 생성하고, 쓰기를 진행
# * Mode에 "+"를 사용하는 경우, 추가 기능이 사용됨(읽기와 쓰기 가능함)
# ** 모드에 t => text작업, b => binary작업

# - encoding : 문자 설정

# 2. open으로 생성된 내용을 토대로 작업이 진행
str1 = input("파일에 저장할 내용 입력 : ")
i = file.write(str1)    # str1에 입력된 텍스트를 입력
print("file.write()의 반환 값 : ",i)

# 3. 작업한 파일의 내용을 close()로 종료
file.close()

## 파일읽기
# 1. open
rfile = open("PyhonBasic/Day9/data/test_text.txt","r",encoding='utf-8')
# 2. 작업
readbuffer = rfile.read()
print(readbuffer)
rfile.close()
'''
'''
[Quiz] 파일명 : data/quiz1.txt
1. 본인의 인적사항을 파일에 저장 후에 출력하세요
(이름,나이,주소)
- 당신의 이름 : 홍길동
- 홍길동님의 나이는 : 20살
- 홍길동 님의 주소는 : 산골짜기

[출력결과] => 파일에 저장된 결과를 출력
홍길동
20살
산골짜기
'''
'''
## 파일입력
# 1. open
file = open("PyhonBasic/Day9/data/quiz1.txt","a",encoding='utf-8')
# 2. work
name = input("당신의 이름 : ")
age = input(name+"님의 나이는 : ")
adr = input(name+"님의 주소는 : ")
file.write(name+"\n"+age+"\n"+adr+"\n")
# 3. close
file.close()

rfile = open("PyhonBasic/Day9/data/quiz1.txt",encoding='utf-8')
readbuffer = rfile.read()
print(readbuffer)
rfile.close()
'''

# 예제2] readline() => 데이터를 읽어들일때 '\n'을 기준으로 데이터를 읽어들이는 함수
rfile2 = open("PythonBasic/Day9/data/quiz1.txt",'r',encoding='utf8')
while True:
    readbuffer = rfile2.readline()
    if readbuffer == "": # 문자열의 마지막을 의미함
        print("\n더이상 값이 존재하지 않습니다.")
        rfile2.close()
        break
    print(readbuffer,end='')
    
# 예제3 readlines() => "\n"을 기준으로 데이터를 읽어들이는 함수, 읽어들인 문장들을 리스트에 저장하는 함수
rfile3 = open("PythonBasic/Day9/data/quiz1.txt",'r',encoding='utf8')
buf3 = rfile3.readlines()
print(buf3,type(buf3))
rfile3.close()

# 문자열 리스트에 "\n"을 제거하여 저장하세요
for i in range(len(buf3)):
    buf3[i] = buf3[i].strip('\n')
    print(buf3[i])
print(buf3)
'''
# 예제5 문자의 암호화(한글자)
readstr, content = "",""
key = 100   # 암호화 연산을 위한 값
choice = input("1. 파일 저장하기\n2. 파일 불러오기\n번호선택>>> : ")
filename = input("파일명 입력")
if choice == '1':
    content = input("단일 문자 입력 : ")
    # 1. open
    sfile = open("PyhonBasic/Day9/data/"+filename,"w",encoding='utf8')
    # 2. work
    chNum = ord(content)
    chNum = chNum + key
    content = chr(chNum)
    sfile.write(content)
    # 3. close
    sfile.close()
elif choice == '2':
    rfile = open("PyhonBasic/Day9/data/"+filename,"r",encoding='utf8')
    readstr = rfile.read()
    chNum = ord(readstr)
    chNum = chNum-100
    readstr = chr(chNum)
    print("파일에 저장된 값 : ",readstr)
    rfile.close()
'''    
'''
문제1
위 예제를 이용하여 문자열을 암호화 시켜주세요
- 현재 단일 문자만 저장이 가능
- 문자열을 암호화하여 파일에 저장할 수 있도록 코드를 수정
- 반대로 암호화 된 문자열을 복호화하여 화면에 출력할 수 있도록 코드를 수정
'''
'''
import os
readstr,savestr,printstr = "","",""
key = 100
while True:
    os.system('cls')
    choice = input("1. 파일 저장하기\n2. 파일 불러오기\n0. 종료하기\n번호선택>>> : ")
    if choice == '1':
        filename = input("파일명 입력 : ")
        sfile = open("PyhonBasic/Day9/data/"+filename,"w",encoding='utf-8')
        contents = input("문자열 입력 : ")
        for i in contents:
            if i != ' ':
                chNum = ord(i)
                chNum += key
                savestr = chr(chNum)
            else :
                savestr += i
        sfile.write(savestr)
        sfile.close()
    elif choice == '2':
        rfile = open("PyhonBasic/Day9/data/"+filename,"r",encoding='utf-8')
        readstr = rfile.read()
        for i in readstr:
            chNum = ord(i)
            chNum -= key
            printstr += chr(chNum)
        print("파일에 저장된 값 : ",printstr)
        rfile.close()
        os.system('pause')
    elif choice == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("입력값 오류, 다시 입력해주세요")
        os.system('pause')
'''   
'''
문제2
위 내용을 이용하여 문서 파일에 저장할 입력 내용을 암호화 시켜주세요
- 문자열을 암호화하여 팡리에 저장할 수 있도록 코드를 수정
  (문자열을 반복적으로 입력할 수 있게 만들어서 처리 후 암호화)
- 반대로 암호화된 문자열을 복호화하여 화면에 출력할 수 있도록 코드를 수정

import os
readstr,savestr,printstr = "","",""
key = 10
while True:
    os.system('cls')
    choice = input("1. 파일 저장하기\n2. 파일 불러오기\n0. 종료하기\n번호선택>>> : ")  
    if choice == '1':
        filename = input("파일명 입력 : ")
        sfile = open("PyhonBasic/Day9/data/"+filename,"a",encoding='utf-8')
        while True:
            contents = input("문자열 입력 : ")
            for i in contents:
                chNum = ord(i)
                chNum += key
                savestr += chr(chNum)
            savestr += "\n"
            sel = input("문자열을 계속 입력하시겠습니까?(Y/n) : ")
            if sel == 'n':
                sfile.write(savestr)
                sfile.close()
                break
    elif choice == '2':
        rfile = open("PyhonBasic/Day9/data/"+filename,"r",encoding='utf-8')
        
        while True:
            readstr = rfile.readline()
            if readstr == "":
                rfile.close()
                break
            for i in readstr:
                chNum = ord(i)
                chNum -= key
                printstr += chr(chNum)
            printstr += "\n"
        print(f"파일 {filename}에 있는 내용\n{printstr}")
        os.system('pause')
    elif choice == '0':
        print("프로그램을 종료합니다.")
        break
    else:
        print("입력값 오류, 다시 입력해주세요")
        os.system('pause')
'''      
'''
# open()의 모드에 "+" 옵션 사용하기
filename = input("파일명 입력 : ")
file = open("PythonBasic/Day9/data/"+filename,"r+",encoding='utf8')
readstr = file.read()
print(readstr,end=' ')
writestr = input("\n문서에 추가할 내용을 입력하세요 : ")
file.write(writestr+"\n")
file.close()
'''
# 모드옵션
# t => 텍스트(문서) => 생략가능
# b => 바이너리(2진 데이터)
'''
# 문제 file입출력을 이용하여 "특정 파일"을 복사하는 프로그램 코드를 작성하세요
# 복사할 대상(원본) : PyhonBasic/Day9/data/test.png
# 복사할 위치(복사본) : PyhonBasic/Day9/data/test_copy.jpg
source = input("복사할 대상(원본) : ")
destination = input("복사할 위치(복사본) : ")
# 1. open
rfile = open("PythonBasic/Day9/data/"+source,"rb")
wfile = open("PythonBasic/Day9/data/"+destination,"wb")
# 2. work
rbuffer = rfile.read()
i = wfile.write(rbuffer)
if i != 0 or i !=-1:
    print("복사를 성공적으로 마칩니다. 파일 크기는 {:,}bytes입니다.".format(i))
else : 
    print("복사가 완료되지 않았습니다.")
# 3. close
rfile.close()
wfile.close()
'''

## 예외 : 프로그램에서 벌어지는 예외적 상황(Error들)
#
# 예)
# - 파일을 읽고자 할 때, 그 파일이 존재하지 않는 경우(FileNotFound)
# - 어떤 값을 0으로 나누고자 할 때(ZeroDivision)
# - 배열의 인덱스 범위를 벗어났을 경우
# - 사용자의 요구대로 진행이 되지 않았을 경우

# 예외처리 방식
# try:      # 예외처리 시작
#   예외처리 검증 구문1
#   예외처리 검증 구문2
# except(예외처리 코드 - 에러코드):
#   예외상황에 따른 진행 코드1
#   예외상황에 따른 진행 코드2
# finally :
#   마지막에 실행할 코드1
'''
# 예제1 검증 내용은 두 수를 나누기 할때
try:
    num1 = int(input("첫번째 정수 : "))
    num2 = int(input("두번째 정수 : "))
    Div = num1/num2
    print("나눗셈 결과 : ",Div)
except ValueError:
    print("정수 값을 입력하세요.")
except ZeroDivisionError:
    print("숫자 0으로 나눌 수 없어요!")
print("예외처리 이후 프로그램 진행..")
'''
'''
# 예제2 
# try: ~ except ~ else 구문
# try:          # 예외검증
#   예외처리 검증 구문1
#   예외처리 검증 구문2
# except(예외처리 코드 - 에러코드):     # 예외발생시 동작
#   예외상황에 따른 진행 코드1
#   예외상황에 따른 진행 코드2
#   ...
# else :                                # 예외 발생 안한 경우 실행
#   예외 발생하지 않은 경우 코드1
#   예외 발생하지 않은 경우 코드1

try:
    num = int(input("수입력 : "))
except ValueError:
    print("정수만 입력하세요!")
else:
    print("입력 값 출력 {} - 예외처리 안된 경우 실행".format(num))
'''  
''' 
# 예제3 파일 관련 예외처리(파일이 없는 경우)
fileName = input("파일명 : ")
try:
    file = open(fileName,"r",encoding='utf8')
    buf = file.read()
    print(buf)
except FileNotFoundError:
    print("지정한 파일이나 디렉터리가 존재하지 않습니다.")
except Exception as e:
    print(e,"에러가 발생했습니다.")
else:           # finally : 항상 실행
    file.close()
    print("문제없이 잘 실행했습니다.")
'''    
'''
문제 나이를 입력받는 프로그램을 만들 때에 잘못된 값을 입력시 예외처리를 만들어보세요

- 입력값에러 : ValueError => 소수점 이하 문자, 문자를 입력
- 입력값이 0보다 작은 경우, 강제로 Exception작업을 해야함 => raise Exception("예외사항")
'''
try:
    age = int(input("나이를 입력해주세요 : "))
    if age < 0 :
        raise Exception("예외 사항")
except ValueError:
    print("양의 정수를 입력해주세요!")
except Exception as e:
    print(e,"0보다 작은 나이는 존재하지 않습니다.")
else:
    print("당신의 나이는 {}살 입니다.".format(age))
finally:
    print("프로그램을 종료합니다.")