
# matrix = [['empty' for column in range(3)] for line in range(3)]
# for line in matrix:
#     print(line)
    
# matrix[0][0] = 'qwll'
    
# print()
# for line in matrix:
#     print(line)
    
# print(      [i**2 for i in range(3)]        )

a = (i for i in range(100000000000))
print( [a.next() for _ in range(10)] )