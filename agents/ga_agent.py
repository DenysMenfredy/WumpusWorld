from random import randrange, choice
from game.action import Action, table_of_actions
class GaAgent(object):
    size_limit = 50

    def __init__(self, chromosome = None):
        self.chromosome = chromosome if chromosome else self.randomChromosome()
        self.initParams()
    
    def initParams(self,):
        self.action_generator = (act for act in self.chromosome)
        self.errors = 0
        self.hits = 0
        self.score = 0
        self.coordinate = (0,0)
        self.arrow = True
        self.gold = False
        self.wumpus_killed = False

    @property
    def fitness(self, ):
        return (self.score * 10) + (self.errors * -2) + (self.hits * 2)

    def randomChromosome(self,):
        rand_size = randrange(3, self.size_limit)
        possible_actions = list(table_of_actions.keys())
        chrom = ''
        for _ in range(rand_size):
            chrom += choice(possible_actions)

        return chrom

    def reset(self, ):
        self.initParams()

    def killedWumpus(self,)->bool:
        return self.wumpus_killed
    
    def killWumpus(self,):
        self.wumpus_killed = True

    def act(self, ) -> Action:
        try:
            act = next(self.action_generator)
            return table_of_actions[act]
        except StopIteration:
            return None
        

    def move(self, direction:str):
        x,y = self.coordinate

        if   direction == 'N': self.coordinate = (x+1,y)
        elif direction == 'S': self.coordinate = (x-1,y)
        elif direction == 'L': self.coordinate = (x,y+1)
        elif direction == 'O': self.coordinate = (x,y-1)

    def shoot(self, ):
        self.arrow = False

    def pickUp(self,):
        self.gold = True

    def hasGold(self, )->bool:
        return self.gold

    def __repr__(self,) ->str :
        return f'<\n\tFitness: {self.fitness}\n\tErrors: {self.errors}\n\tHits:{self.hits}\n\tScore: {self.score}\n\tChromosome: {self.chromosome}\n>'