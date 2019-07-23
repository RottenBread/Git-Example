# stack = []
#
# def push(s, n) :
#     s.append(n)
#
# def pop(s) : # len : 리스트의 길이
#     if len(s) == 0 :
#         return -1
#     else :
#         return s.pop()
#
# def empty(s) :
#     return (len(s) == 0)
#
# push(stack, 1)
# push(stack, 2)
# print(pop(stack))
# print(empty(stack))
# print(stack)


# lambda 함수

# f = lambda x,y : x+y
# print(f(1, 2))

# square = list(map(lambda x : x**2, range(10)))
# print(square)

# group = [(x,y) for x in [1,2,3] for y in [1,2,3] if x!=y]
# print(group)

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

transMat = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transMat)