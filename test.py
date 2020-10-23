# a, b = 1, 2
# print(a)
# print(b)
# print(type(a))
# print(type(b))
# print(type((a,b)))

test = [[1,2,3,4],[5,6,7,8]]
# print(type(*test))
for row in test:
    print(*row)
    # print(type(*row))