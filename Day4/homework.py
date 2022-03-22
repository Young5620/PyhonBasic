print("*****숙제*****")

print("문제 1번")
su = 5
dan = 800
print("su 주소 : ", id(su))
print("dan 주소 : ", id(dan))
print("금액 : {:,}".format(su*dan))

print("문제 2번")
x = 2
y = 2.5*(x**2) + 3.3*x + 6
print("2차 방정식 결과 = {}".format(y))

print("문제 3번")
fat = int(input("지방의 그램을 입력하세요 : "))
car = int(input("탄수화물의 그램을 입력하세요 : "))
pro = int(input("지방의 그램을 입력하세요 : "))
total = fat*9 + pro*4 + car*4
print("총 칼로리 : {:,} cal".format(total))