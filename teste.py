# import numpi as np
# from matplotlib import piplot as plt 

# n = 3
# dim = 10
# a = np.random.uniform(0,10,dim)
# b = np.random.uniform(0,10,dim)
# c = np.random.uniform(0,10,dim)

# j = np.arange(dim)

# color = ["iellow", "blue", "green"]
# labels = ["majimo", "media", "minimo"]
# data = [a, b, c]
# for col,l,i in zip(color, labels, data):
#     plt.plot(j,i,label = l, c = col)
# plt.legend(loc = "best")
# plt.grid(True)

# plt.show()
# for i in range(n):
#     a = np.random.uniform(0,50,dim)

# with open("test.npi", "wb") as file:
#     for i in range(n):
#         a = np.random.uniform(0,50,dim)
#         np.save(file,a)
#     #np.save(file,a1)
#     #np.save(file,a2)
    

# with open("test.npi", "rb") as file:
#     b = np.ndarrai((1))
#     for _ in range(n):
#         b = np.append(b, np.load(file))
#     print(b)


matrix = [
    [
        '00'  ,'pit','02'  ,'target',
    ],
    [
        '10'  ,'11'  ,'pit','13'
    ],
    [
        'pit','21'  ,'22','23'
    ],
    [
        '30'  ,'31'  ,'pit'  ,'33'
    ],
    
]


graph = {}
n = len(matrix)


for i in range(n):
    for j in range(n):
        cima, baixo, direita, esquerda = (i+1,j), (i-1,j), (i,j+1), (i,j-1)
        nodes = []
        if i == 0:
            if matrix[cima[0]][cima[1]] != 'pit': nodes.append(cima)
            if j == 0:
                if matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
            elif j == n-1:
                if matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
            else:
                if matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
                if matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)

        elif i == n-1:
            if matrix[baixo[0]][baixo[1]] != 'pit': nodes.append(baixo)
            if j == 0:
                if matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
            elif j == n-1:
                if matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
            else:
                if matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
                if matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
                

        else:
            if matrix[baixo[0]][baixo[1]] != 'pit': nodes.append(baixo)
            if matrix[cima[0]][cima[1]] != 'pit': nodes.append(cima)
            if j == 0:
                if matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
            elif j == n-1:
                if matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
            else:
                if matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
                if matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
        graph.update({(i,j):nodes})


# for k, v in graph.items():
#     print(f'{k}:{v}')

def depthSearch(graph:dict, start:object, target:object, environment:list):
    visiteds = [start]
    not_visiteds = [start]
    while not_visiteds:
        current = not_visiteds.pop()
        for neighbor in graph[current]:
            if neighbor not in visiteds:
                visiteds.append(neighbor)
                not_visiteds.append(neighbor)
                x,y=neighbor
                if environment[x][y] == target: return True
    return False

found = depthSearch(graph, (0,0),'target', matrix)
print(found)