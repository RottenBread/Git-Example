#(변수명) = (초기화 값)
#inputVal = input("문자열을 입력해주세요 : ")
#print(inputVal)
#print("inputVal의 자료형은 ", type(inputVal))

#Type Casting(자료형변환) 바꾸고 싶은 자료형(변수 또는 값)
#inputVal = input("숫자를 입력해주세요 : ")
#inputVal2 = input("두 번쨰 숫자를 입력해주세요 : ")
#if (inputVal.isdigit() == True) and (inputVal2.isdigit() == True) :
#    inputVal, inputVal2 = int(inputVal), int(inputVal2)
#    print(inputVal+inputVal2)
#    print(inputVal-inputVal2)
#    print(inputVal*inputVal2)
#    print(inputVal**inputVal2)
#    if not(inputVal2 == 0) == True :
#        print(inputVal/inputVal2)
#        print(inputVal%inputVal2)
#        print(inputVal//inputVal2)
#    else :
#        print(0)
#        print(0)
#        print(0)
#실습 1. 구의 부피 구하기
#inputVal = input("구의 반지름을 입력해주세요 : ")
#if inputVal.isdigit() == True :
#    inputVal = int(inputVal)
#    print(round((4/3)*(inputVal**3)*(3.14), 2))

#2진수
#print(bin(10))
#binaryNum = bin(10)
#print(int(binaryNum, 2))
#hexNum = hex(10)
#print(int(hexNum, 16))

#비트 연산자
#n, m = 2, 7
#print(bin(n), "^" , bin(m), " = " , n ^ m) #xor 연산
#print(bin(n), "|" , bin(m), " = " , n | m) #or 연산
#print(bin(n), "&" , bin(m), " = " , n & m) #and 연산

#비교연산자
# n, m = 5, 2
# print(n<=m) #F
# print(n>=m) #T
# print(n<m) #F
# print(n>m) #T
# print(n==m) #F
# print(not(n==m)) #T

#할당연산자
# a = 5
# b = 3
#
# a **= b
# print(a)

#식별연산자
# a = 5
# b = 5
#
# print(a is b)
# print(a is not b)

# l = [0, 0, 0, 0]
# m = l[:]
# l[0] = 1023
# print(m[0])

#멤버 연산자
# print("Hello" in "Hello World") #True
# print("Hello" not in "Hello World") # False