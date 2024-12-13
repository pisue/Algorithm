# 시험 점수를 입력받아 90 ~ 100점은 A, 80 ~ 89점은 B, 70 ~ 79점은 C, 60 ~ 69점은 D, 나머지 점수는 F를 출력하는 프로그램을 작성하시오.
n = int(input())

if n>=90 and n<=100:
    print("A")
elif n>=80 and n<=89:
    print("B")
elif n>=70 and n<=79:
    print("C")
elif n>=60 and n<=69:
    print("D")
else:
    print("F")