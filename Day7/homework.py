'''
Chapter2
문제4
3개의 단어를 키보드로 입력받아서 각 단어의 첫글자를 추출하여 단어의 약자를 출력하시오
<처리조건>
  1. 각 단어 변수(word1,word2,word3) 저장
  2. 입력과 출력 구분선 : 문자열 연산
  3. 각 변수의 첫 단어만 추출하여 변수(abbr) 저장
(출력예시)
첫번쨰 단어 : Korea
두번째 단어 : Baseball
세번째 단어 : Orag
======================
약자 : KBO
'''
word1 = input("첫번째 단어 : ")
word2 = input("두번째 단어 : ")
word3 = input("세번째 단어 : ")
print("="*15)
abbr = word1[0] + word2[0] + word3[0]
print("약자 : ",abbr)

'''
Chapter3 
문제1 조건문을 이용한 '짐의 무게 계산하기'
A형] 항공사에서는 짐을 부칠 때, 10kg이상이면 수수료 10,000원을 내야한다. 만약 10kg 미만이면 수수료는 없다.
사용자의 짐의 무게를 키보드로 입력 받아서 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하시오
(출력예시)
짐의 무게는 얼마입니까? 8
수수료는 없습니다.

짐의 무게는 얼마입니까? 15
수수료는 10,000원 입니다.

B형] 항공사에서는 짐을 부칠 때, 10kg이상부터 수수료를 내야한다. 수수료는 10의 배수 단위로 10,000원씩 증가한다.
만약 10kg미만이면 수수료는 없다. 사용자의 짐의 무게를 키보드로 입력받고, 사용자가 지불하여야 할 금액을 계산하는 프로그램을 작성하시오
(출력예시)
짐의 무게는 얼마입니까? 8
수수료는 없습니다.

짐의 무게는 얼마입니까? 15
수수료는 10,000원 입니다.

짐의 무게는 얼마입니까? 21
수수료는 20,000원 입니다.
'''
print("문제1 - A형")
gim = int(input("짐의 무게(kg)는 얼마입니까?"))
if gim < 10:
    print("수수료는 없습니다.")
elif gim >10 :
    print("수수료는 10,000원 입니다.")
else:
    print("잘못 입력하셨습니다.")
    
print("문제1 - B형")
gim = int(input("짐의 무게(kg)는 얼마입니까?"))
price = 0
if gim < 10 :
    print("수수료는 없습니다.")
elif gim >= 10:
    price = 10000*(gim//10)
    print("수수료는 {:,}원 입니다.".format(price))
else:
    print("잘못 입력하셨습니다.")
    
'''
문제2] while 반복문을 이용한 '숫자 맞추기 게임'
컴퓨터에 의해서 1~10 사이의 난수가 발생될 때 사용자가 예상되는 숫자를 키보드를 입력한 경우 일치하면
'~~~성공~~~'메세지를 출력하고, 반복을 탈출한다. 만약 사용자가 입력한 수가 난수보다 더 크면 '더 작은수를 입력' 메시지를 출력하고
반복을 계속한다. 또한 사용자가 입력한 수가 난수보다 작으면 ' 더 큰 수를 입력'메시지를 출력하고 반복을 계속한다.
위 내용이 실행될 수 있도록 프로그램의 빈칸을 채우시오

'''
print("문제2")
import random
print(">> 숫자 맞추기 게임 <<")
com = random.randint(1, 10)     # 1~10 난수 정수 발생
while True:
    my = int(input("예상 숫자를 입력하시오 : ")) # 숫자 입력
    if com == my : 
        print("~~~성공~~~")
        break
    elif com > my : 
        print("더 큰 수를 입력하세요.")
        continue
    elif com < my :
        print("더 작은 수를 입력하세요.")
        continue
    else : 
        print("잘못 입력하셨습니다. 다시 입력해주세요")
        continue

'''
문제3] for 반복문을 이용한 '수열 출력하기'
1~100사이에서 3의 배수이면서 2의 배수가 아닌 수를 한줄에 출력하고, 그 누적합을 출력하시오
(출력결과)
수열 = 3 9 15 .....
누적합 = 867
'''
print("문제3")
print("수열 = ",end='')
for i in range(100):
    if i % 3 ==0 and i % 2 != 0:
        print(i,end=' ')
Sum = 0
print()
print("누적합 = ",end='')
for i in range(100):
    if i % 3 ==0 and i % 2 != 0:
        Sum +=i
print(Sum)
print()

'''
문제4] 중첩 반복문을 이용한 '단어 카운트하기(word count)'
다음과 같은 문자열 객체를 이용하여 단어를 추출하고 단어의 개수를 출력하세요

multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
'''
print("문제4")
multiline = """안녕하세요. 파이썬 세계로 오신걸
환영합니다.
파이썬은 비단뱀 처럼 매력적인 언어입니다."""
l_lst = []
w_lst = []
for i in multiline.split("\n"):
    l_lst.append(i)
    for j in i.split(" "):
        w_lst.append(j)
        print(j)
print("단어 개수 : ", len(w_lst))
print()

'''
Chapter4 
문제1]
다음 lst변수를 대상으로 각 단계별로 list를 연산하시오
<각 단계별 출력결과 예시>
1단계 : [10,1,5,2,10,1,5,2]
2단계 : [10,1,5,2,10,1,5,2,20]
3단계 : [1,2,1,2]

lst = [10,1,5,2]

단계1 : lst원소를 2배 생성하여 result변수에 저장 및 출력하기
단계2 : lst의 첫번째 원소에 2를 곱하여 result변수에 추가 및 출력하기
단계3 : result의 홀수 번째 원소만 result2변수에 추가 및 출력하기
'''
lst = [10,1,5,2]
print("문제1-1단계")
result = lst*2
print("1단계 : lst원소를 2배 생성하여 result변수에 저장 및 출력하기\n",result)
print("문제1-2단계")
last_num = 2*lst[0]
result.append(last_num)
print("2단계 : lst의 첫번째 원소에 2를 곱하여 result변수에 추가 및 출력하기\n",result)
print("문제1-3단계")
result2 = result[1:2]
print("3단계 : result의 홀수 번째 원소만 result2변수에 추가 및 출력하기\n",result2)

'''
문제2] list원소 추가 및 요소 검사하기
A형 list의 크기를 키보드로 입력받은 후, 
입력받은 크기만큼 임의 숫자를 list에 추가하고, list의 크기를 출력하세요
<출력예시>
vector 수 : 3
4
2
5
vector의 크기 : 3

B형 list크기를 키보드로 입력받은 후, 
입력받은 크기만큼 임의 숫자를 list에 추가한다. 이후 list에서 찾을 값을 키보드로 입력한 후
해당값이 list에 있으면 yes 없으면 no를 출력하세요
<출력예시>
vector 수 : 5
1
2
3
4
5
3
YES
'''
print("문제2-A형")
size = int(input("vector 수 : "))
lst = []
for i in range(size):
    lst.append(int(input()))
print("vector의 크기 : ", len(lst))

print("문제2-B형")
if int(input()) in lst:
    print("YES")
else:
    print("NO")
    
'''
문제3 list내포를 이용하여 문자열 처리하기
A형 message변수를 대상으로 'spam'원소는 1, 'ham'원소는 0으로 dummy변수를 생성하세요
<조건> list + for형식 적용
(출력예시)
[1,0,1,0,1]

B형 message변수를 대상으로 'spam'원소만 추출하여 spam_list에 추가하세요
<조건> list + for + if 형식 적용
(출력예시)
['spam','spam','spam']
message = ['spam','ham','spam','ham','spam']
'''
message = ['spam','ham','spam','ham','spam']
print("문제3-A형")
dummy = [1 if i == 'spam' else 0 for i in message]
print(dummy)
print("문제3-B형")
spam_list = [i for i in message if i=='spam']
print(spam_list)

'''
문제4]
position 변수를 대상으로 중복되지 않은 직위와 직위별 빈도수를 출력하세요
(출력예시)
중복되지 않은 직위 : ['사장','과장','대리','부장']
각 직위별 빈도수 : ['과장':2,'부장':1,'대리':2,'사장':1]
position = ['과장','부장','대리','사장','대리','과장']
'''
position = ['과장','부장','대리','사장','대리','과장']
print("문제4")
nonRepeat = list(set(position))
print("중복되지 않은 직위 : ",nonRepeat)
count_pos = {}
for i in position:
    count_pos[i] = count_pos.get(i,0)+1
print("각 직위별 빈도수 : ",count_pos)