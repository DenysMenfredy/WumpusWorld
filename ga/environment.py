from random import sample, randrange

from agents.ga_agent import GaAgent


class Environment:
    def __init__(self, ):
        self.stop_generation:int = None
        self.best_individual:GaAgent = None
        self.size_pop:int = None
        self.crossover_rate: float = None
        
    def start(self, )->GaAgent:
        population:list = self.generateInitialPop()
        for geracao in range( self.stop_generation ):
            self.evaluate(population)
            self.reproduce(population)

        return self.best_individual  #TODO: onde atualizar

    
    def generateInitialPop(self, )->list:
        temp_population = [GaAgent() for _ in range(self.size_pop) ]
        return temp_population

    def reproduce(self, population:list )->None:
        mating_pool:list = self.selection(population)
        new_pop = self.crossover(mating_pool)
        self.mutate(new_pop)
        population = new_pop

    def selection(self, population:list)->list:
        mating_pool = []
        amount = 3
        percent = int(self.size_pop * self.crossover_rate )
        percent = percent if percent%2 == 0 else percent + 1 
    
        for _ in range(percent):
            selecteds: list = sample(population, amount).sort(key = lambda indv: indv.fitness)
            winner = selecteds[-1]
            mating_pool.append(winner)
        return mating_pool
    
    def crossover(self,mating_pool: list) -> list:
        size = len(mating_pool)
        new_pop = []
        while mating_pool:
            indv = mating_pool.pop(randrange(size))
            indv2 = mating_pool.pop(randrange(size - 1))
            chrm1, chrm2 = self.onePointCrossover(indv,indv2)
            new_pop.append(GaAgent(chrm1))
            new_pop.append(GaAgent(chrm2))
            size -= 2
        return new_pop
    
    def onePointCrossover(self, seq1:str, seq2:str)->str,str
        pass