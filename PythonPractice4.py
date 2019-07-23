# def printN(n) :
#     if n == 1 :
#         print(n)
#         return
#     else :
#         printN(n-1)
#         print(n)
#         return
#
#
#
# def fact(n) :
#     def loop(m, res) :
#         if m == 1 :
#             return res
#         else :
#             return loop(m-1, res)
#     loop(n, 1)

#Factorial 일반 재귀버전
# def fact(n) :
#     if n == 1:
#         return 1
#     else :
#         return n*fact(n-1)
#
# print("3! = ", fact(3))

#Factorial 꼬리 재귀버전
# def factTail(n) :
#     def loop(m, res) :
#         if m == 1 :
#             return res
#         else :
#             return loop(m-1, res+m)
#     return loop(n, 1)
# print("3! = ", factTail(3))

# 피보나치 수열 일반 재귀버전
# def fibo(n) :
#     if n == 1 or n == 2 :
#         return 1
#     return fibo(n-1) + fibo(n-2)
# print(fibo(5))

# 피보나치 수열 꼬리 재귀버전
# def fiboTail(n) :
#     def loop(n, before, next) :
#         if n == 1 :
#             return before
#         return loop(n-1, before, before + next)
#     return loop(n, 1, 1)
# print(fiboTail(5))

#Python 반복문 (While, for)
# n = 5
# while n>=1 :
#     print(n)
#     n -= 1

# n = 5
# for i in range(5, 0, -1) :
#     print(i)

# n = 1
# while n <= 5 :
#     print(n)
#     n+=1
# for i in range(1, 6) :
#     print(i)

# n = int(input("n을 입력해주세요 : "))
# for i in range(1, n+1) :
#     for j in range(1, i+1) :
#         print("*", end=" ")
#     print()

# n = 3
#
# for i in range(1, n+1) :
#     for j in range(1, n-i+1) :
#         print(" " , end = " ")
#     for j in range(1,i+1) :
#         print("*", end = " ")
#     for j in range(1,i) :
#         print("*", end = " ")
#     print()
# for i in range(n, 0, -4) :
#     for j in range(0, n-i+1) :
#         print(" ", end = " ")
#     for j in range(1,i+1) :
#         print("*", end = " ")
#     print()
# for i in range(n, 0, -4) :
#     for j in range(0, n-1) :
#         print(" ", end=" ")
#     for j in range(1, i-1):
#         print("*", end=" ")
#     print()
# for i in range(n, 0, -4) :
#     for j in range(0, n-1) :
#         print(" ", end=" ")
#     for j in range(1, i-1):
#         print("*", end=" ")
#     print()
# for i in range(n, 0, -4) :
#     for j in range(0, n-1) :
#         print(" ", end=" ")
#     for j in range(1, i-1):
#         print("*", end=" ")
#     print()
# for i in range(n, 0, -4) :
#     for j in range(0, n-1) :
#         print(" ", end=" ")
#     for j in range(1, i-1):
#         print("*", end=" ")
#     print()
# for i in range(n, 0, -4) :
#     for j in range(0, n-3) :
#         print(" ", end=" ")
#     for j in range(1, i+3):
#         print("*", end=" ")
#     print()

# n = 3
# for i in range(0,5) :
#     for j in range(0, n-2) :
#         print("*", end = " ")
