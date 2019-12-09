from random import randrange, choice
from game.action import Action, table_of_actions
class GaAgent(object):
    size_limit = 100
    fitness_function = lambda a, b, c, d, e, f, g,h: a * b * c**2 - 100000
    def __init__(self, generation, count, chromosome = None):
        self.chromosome = chromosome if chromosome else self.randomChromosome()
        self.id = f'{generation}.{count}'
        self._fitness = 0
        self.initParams()
    
    def initParams(self,):
        self.action_generator = (act for act in self.chromosome)
        self.size = len(self.chromosome)
        self.errors = 0
        self.hits = 0
        self.coordinate = (0,0)
        self.arrow = True
        self.got_gold = False
        self.wumpus_died = False
        self.agent_died = False
        self.escaped = False

    @property
    def fitness(self, ):
        x,y = self.coordinate
        distance = abs(x)+abs(y)
        return GaAgent.fitness_function (
              int(self.got_gold)       # 150) 
            , int(self.wumpus_died)    #* 350) 
            , int(self.escaped)        #* 500) 
            , int(self.agent_died)     #* -20)
            , (self.size)                #* -1.5)
            , (self.errors)              #* -2)
            ,(self.hits)                #* 1.5)
            , (distance)        #* 10)
        )
    @fitness.setter
    def fitness(self, value):
        self._fitness = value
        
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
        return self.wumpus_died
    
    def wonGame(self,)->bool:
        return self.escaped
    
    def killWumpus(self,):
        self.wumpus_died = True

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
        self.got_gold = True

    def hasGold(self, )->bool:
        return self.got_gold
    
    def hasArrow(self, )->bool:
        return self.arrow

    def die(self,):
        self.agent_died = True

    def escape(self,):
        self.escaped = True
    
    def copy(self,):
        generation, count = self.id.split('.')
        agent_copy = GaAgent(generation, count, self.chromosome)
        agent_copy.got_gold = self.got_gold
        agent_copy.agent_died  =self.agent_died
        agent_copy.wumpus_died = self.wumpus_died
        agent_copy.escaped = self.escaped
        agent_copy.erros = self.errors
        agent_copy.size = self.size
        agent_copy.hits = self.hits
        agent_copy.arrow = self.arrow
        agent_copy.coordinate = self.coordinate
        agent_copy.fitness = self.fitness
        return agent_copy
    
    def __repr__(self,) ->str :
        return f'<\n\tFitness: {self.fitness}\n\tErrors: {self.errors}\n\tHits:{self.hits}\n\tChromosome: {self.chromosome}\n>\n'