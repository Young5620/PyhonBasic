class Person :
    #생성자
    def __init__(self,name,gender,age):
        self.name = name
        self.gender = gender
        self.age = age
    #메서드 (display)
    def display(self):
        print(f"이름 : {self.name}, 성별 : {self.gender}\n나이 : {self.age}")


# 키보드 입력
name = input('이름 : ')
age = int(input('나이 : '))
gender = input('성별 (male/female)')
# 객체 생성
p = Person(age, name, gender) # 생성자 이용 전역변수 초기화
p.display()