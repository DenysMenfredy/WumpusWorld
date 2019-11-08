from random import randrange, choice
from game.action import Action, table_of_actions
class GaAgent(object):
    size_limit = 50

    def __init__(self, chromosome = None):
        self.chromosome = chromosome if chromosome else self.randomChromosome()
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
        return (self.score * 2) + (self.errors * 5) + (self.hits * 3) 

    def randomChromosome(self,):
        rand_size = randrange(3, self.size_limit)
        possible_actions = list(table_of_actions.keys())
        chrom = ''
        for mov in range(rand_size):
            chrom += choice(possible_actions)
        #chrom = [choice(possible_actions) for _ in range(rand_size)]

        return chrom

    def reset(self, ):
        self.hits, self.errors, self.score = 0, 0, 0
        self.coordinate, self.arrow, self.gold = (0,0), True, False

    def killedWumpus(self,):
        return self.wumpus_killed
    
    def killWumpus(self,):
        self.wumpus_killed = True

    def act(self, ) -> Action:
        try:
            act = next(self.action_generator)
            print(act)
            print(table_of_actions[act])
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

    def hasGold(self, ):
        return self.gold

    def __repr__(self,) ->str :
        return str(self.fitness) + ' ' + str(self.errors) + ' ' + str(self.hits) + ' ' + str(self.score)