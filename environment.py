
from random import randrange

class Environment(object):
    def __init__(self, dimension:int, n_pits:int, n_golds:int=1, n_wumpus:int=1):
        self.matrix = [['empty' for column in range(dimension)] for line in range(dimension)]
        self.matrix[0][0] = 'start'
        self.matrix_perceptions = [[ [] for column in range(dimension)] for line in range(dimension)]
        self.dimension = dimension
        self.generate({'name': 'pit','amount':n_pits})
        self.generate({'name': 'gold','amount':n_golds})
        self.generate({'name': 'wumpus','amount':n_wumpus})
        self.screamTrigger = False

    def generate(self, obj:dict)->None:
        #print(obj['amount'])
        for _ in range(obj['amount']):
            x,y = self.randomCoordinate()
            print(x,y)
            self.matrix[x][y] = obj['name']
            
    def printMatrix(self):
      for line in self.matrix:
          print(line)
    
    def getPerceptions(self, coordinate:tuple)->list:
        perceptions = []
        if self.isPerception(coordinate, 'breeze'): perceptions.append('breeze')
        if self.isPerception(coordinate, 'stentch'): perceptions.append('stench')
        if self.isPerception(coordinate, 'glitter'): perceptions.append('glitter')
        if self.screamTrigger: 
            perceptions.append('scream')
            self.screamTrigger = False         
        return perceptions

    def isPerception(self, coordinate, perception)-> bool:
        x,y = coordinate
        return perception in self.matrix_perceptions[x][y]
            
        
    def isPit(self, coordinate:tuple)->bool:
        x, y = coordinate
        return self.matrix[x][y] == 'pit'

    def isWumpus(self, coordinate:tuple)->bool:
        x, y = coordinate
        return self.matrix[x][y] == 'wumpus'

    def isExit(self, coordinate:tuple)->bool:
        return coordinate == (0,0)

    def removeWumpus(self, coordinate:tuple)->None:
        self.screamTrigger = True
        x, y = coordinate
        self.matrix[x][y] = 'empty'

    def removeGold(self, coordinate:tuple)->None:
        x, y = coordinate
        self.matrix[x][y] = 'empty'


    def randomCoordinate(self, )->tuple:
        x,y = (0,0)
        while( ((x,y) == (0,0)) or (self.matrix[x][y] != 'empty') ):
            x, y = randrange(self.dimension), randrange(self.dimension)
            
        return (x,y)