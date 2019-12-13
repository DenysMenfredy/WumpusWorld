
from random import randrange

class Environment(object):
    def __init__(self, dimension:int, n_pits:int, n_golds:int=1, n_wumpus:int=1):
        self.perceptions = {
            "pit": "breeze",
            "gold": "glitter",
            "wumpus": "stench",
        }
        
        self.dimension = dimension
        self.coordinate = {
            "pit":[],
            "wumpus":[],
            "gold":[]
        }
        valid_environment = False
        while(not valid_environment):
            self.matrix = [['empty' for column in range(dimension)] for line in range(dimension)]
            self.matrix[0][0] = 'start'
            self.matrix_perceptions = [[ [] for column in range(dimension)] for line in range(dimension)]
            self.generate({'name': 'pit','amount':n_pits})
            self.generate({'name': 'gold','amount':n_golds})
            self.generate({'name': 'wumpus','amount':n_wumpus})
            self.screamTrigger = False
            self.n_pits = n_pits
            valid_environment = self.validEnvironment()


    def generate(self, obj: dict) -> None:
        for _ in range(obj['amount']):
            x,y = self.randomCoordinate()
            self.coordinate[obj["name"]].append((x,y))
            self.matrix[x][y] = obj['name']
            #print(x,y, end=' ')
            #print(obj['name'])

            if obj['name'] == 'gold': self.matrix_perceptions[x][y].append(self.perceptions[obj['name']])
            else:
                # verifica se estar na primeira linha
                if x == 0:
                    self.matrix_perceptions[x + 1][y].append(self.perceptions[obj['name']])

                    # verifica se estar na primeira coluna
                    if y == 0:
                        self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])

                    #verifica se estar na ultima coluna
                    elif y == (self.dimension-1):
                        self.matrix_perceptions[x][y - 1].append(self.perceptions[obj['name']])

                    #verifica se estar nas colunas do meio
                    else:
                        self.matrix_perceptions[x][y+1].append(self.perceptions[obj['name']])
                        self.matrix_perceptions[x][y-1].append(self.perceptions[obj['name']])


                # verifica se estar na ultima linha
                elif x == (self.dimension - 1):
                    self.matrix_perceptions[x - 1][y].append(self.perceptions[obj['name']])

                    # verifica se estar na primeira coluna
                    if y == 0:
                        self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])

                    # verifica se estar na ultima coluna
                    if y == (self.dimension - 1):
                        self.matrix_perceptions[x][y - 1].append(self.perceptions[obj['name']])

                    # verifica se estar nas colunas do meio
                    else:
                        self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])
                        self.matrix_perceptions[x][y - 1].append(self.perceptions[obj['name']])

                # verifica se estar nas linhas do meio
                else:
                    self.matrix_perceptions[x + 1][y].append(self.perceptions[obj['name']])
                    self.matrix_perceptions[x - 1][y].append(self.perceptions[obj['name']])

                    # verifica se estar na primeira coluna
                    if y == 0:
                        self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])

                    # verifica se estar na ultima coluna
                    if y == (self.dimension - 1):
                        self.matrix_perceptions[x][y - 1].append(self.perceptions[obj['name']])

                    # verifica se estar nas colunas do meio
                    else:
                        self.matrix_perceptions[x][y + 1].append(self.perceptions[obj['name']])
                        self.matrix_perceptions[x][y - 1].append(self.perceptions[obj['name']])


    def printMatrix(self, coordinate: tuple):
        output = ''
        #print(coordinate)
        for line in range(self.dimension -1, -1, -1):
            for column in range(self.dimension):
                if coordinate == (line,  column):
                    output += '|A'
                else:
                    if self.matrix[line][column] == 'wumpus': output += '|W'
                    elif self.matrix[line][column] == 'gold': output += '|G'
                    elif self.matrix[line][column] == 'pit': output += '|P'
                    else : output += '| '
            output += '|\n'
        print(output)
        return output
          
    
    def getPerceptions(self, coordinate:tuple)->list:
        perceptions = []
        if self.isPerception(coordinate, 'breeze'): perceptions.append('breeze')
        if self.isPerception(coordinate, 'stench'): perceptions.append('stench')
        if self.isPerception(coordinate, 'glitter'): perceptions.append('glitter')
        if self.screamTrigger: 
            perceptions.append('scream')
            self.screamTrigger = False         
        return perceptions

    def isPerception(self, coordinate, perception)-> bool:
        x,y = coordinate
        if not self.isValid(coordinate): return False
        return perception in self.matrix_perceptions[x][y]
            
        
    def isPit(self, coordinate:tuple)->bool:
        x, y = coordinate
        if not self.isValid(coordinate): return False
        return self.matrix[x][y] == 'pit'

    def isWumpus(self, coordinate:tuple)->bool:
        x, y = coordinate
        if not self.isValid(coordinate): return False
        return self.matrix[x][y] == 'wumpus'

    def isGold(self, coordinate:tuple)->bool:
        x, y = coordinate
        if not self.isValid(coordinate): return False
        return self.matrix[x][y] == 'gold'

    def isExit(self, coordinate:tuple)->bool:
        return coordinate == (0,0)

    def removeWumpus(self, coordinate:tuple)->None:
        self.screamTrigger = True
        x, y = coordinate
        if not self.isValid(coordinate): return
        self.matrix[x][y] = 'empty'

    def removeGold(self, coordinate:tuple)->None:
        x, y = coordinate
        if not self.isValid(coordinate): return
        self.matrix[x][y] = 'empty'
        self.matrix_perceptions[x][y].remove('glitter')


    def randomCoordinate(self, )->tuple:
        x,y = (0,0)
        while( ((x,y) == (0,0)) or (self.matrix[x][y] != 'empty') ):
            x, y = randrange(self.dimension), randrange(self.dimension)
            
        return (x,y)

    def isValid(self, coordinate) -> bool:
        x , y = coordinate
        if x >= self.dimension or y >= self.dimension:
            return False
        if x < 0 or y < 0:
            return False
        return True
    
    def getObjectCoord(self, name: str): return self.coordinate[name]
    
    def getGraph(self, )->dict:
        grafo = {}
        n = self.dimension

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
                
        return grafo
    
    def printGraph(self, ):
        for k, v in self.getGraph().items():
            print(f'{k}:{v}')
    
    
                
    def depthSearch(self, start:object)-> bool:
        visiteds = []
        def targetIsNext(current:object):
            for vertex in self.getGraph()[current]:
                if vertex not in visiteds:
                    visiteds.append(vertex)
                    x, y = vertex
                    if self.matrix[x][y] == 'gold': return True
                    if targetIsNext(vertex): return True
        return targetIsNext(start)
    
    def validEnvironment(self, )-> bool:
        return self.depthSearch((0,0))
