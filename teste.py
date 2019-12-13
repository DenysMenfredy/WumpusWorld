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


self.matrix = [
    [
        '00'  ,'pit','02'  ,'alvo',
    ],
    [
        '10'  ,'11'  ,'pit','13'
    ],
    [
        'pit','21'  ,'pit','23'
    ],
    [
        '30'  ,'31'  ,'30'  ,'33'
    ],
    
]


grafo = {}
n = len(self.matrix)


for i in range(n):
    for j in range(n):
        cima, baixo, direita, esquerda = (i+1,j), (i-1,j), (i,j+1), (i,j-1)
        nodes = []
        if i == 0:
            if self.matrix[cima[0]][cima[1]] != 'pit': nodes.append(cima)
            if j == 0:
                if self.matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
            elif j == n-1:
                if self.matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
            else:
                if self.matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
                if self.matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)

        elif i == n-1:
            if self.matrix[baixo[0]][baixo[1]] != 'pit': nodes.append(baixo)
            if j == 0:
                if self.matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
            elif j == n-1:
                if self.matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
            else:
                if self.matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
                if self.matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
                

        else:
            if self.matrix[baixo[0]][baixo[1]] != 'pit': nodes.append(baixo)
            if self.matrix[cima[0]][cima[1]] != 'pit': nodes.append(cima)
            if j == 0:
                if self.matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
            elif j == n-1:
                if self.matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
            else:
                if self.matrix[direita[0]][direita[1]] != 'pit': nodes.append(direita)
                if self.matrix[esquerda[0]][esquerda[1]] != 'pit': nodes.append(esquerda)
        grafo.update({(i,j):nodes})


for k, v in grafo.items():
    print(f'{k}:{v}')

def buscaEmProfundidade(grafo:dict, inicio:object, alvo:object, ambiente:list):
    visitados = []
    def alvoIsProximo(atual:object):
        for vertice in grafo[atual]:
            if vertice not in visitados:
                visitados.append(vertice)
                x,y=vertice
                #if ambiente[x][y] == 'pit': continue
                if ambiente[x][y] == alvo: return True
                if alvoIsProximo(vertice): return True
    return alvoIsProximo(inicio)

achou = buscaEmProfundidade(grafo, (0,0),'alvo', self.matrix)
print(achou)