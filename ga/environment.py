from random import sample, randrange, random

from agents.ga_agent import GaAgent


class Environment:
    def __init__(self, evaluator, ):
        self.stop_generation:int = 5
        self.best_individual:GaAgent = None
        self.size_pop:int = 20
        self.crossover_rate: float = 0.9
        self.mutation_rate: float = 0.05
        self.evaluator = evaluator
        
    def start(self, )->GaAgent:
        population:list = self.generateInitialPop()
        self.evaluate(population)
        for geracao in range( self.stop_generation ):
            #print(population)
            self.reproduce(population)
            self.evaluate(population)
            self.findBest(population)
        self.evaluate([self.best_individual])

        return self.best_individual
    
    def generateInitialPop(self, )->list:
        temp_population = [GaAgent() for _ in range(self.size_pop) ]
        #print(temp_population)
        return temp_population

    def evaluate(self, population):
        #print(len(population))
        self.evaluator.populate(population)
        #print(population)
        self.evaluator.start()
        #print(population)

    def reproduce(self, population:list ):
        #print(population)
        mating_pool:list = self.selection(population)
        new_pop = self.crossover(mating_pool)
        self.mutate(new_pop)
        population.sort(key=lambda indv: indv.fitness)
        percent = int(self.size_pop * self.crossover_rate )
        percent = percent if percent%2 == 0 else percent + 1
        print(population)
        population = new_pop + population[percent: ]
        print(population)

    def selection(self, population:list)->list:
        mating_pool = []
        amount = 3
        percent = int(self.size_pop * self.crossover_rate )
        percent = percent if percent%2 == 0 else percent + 1 
    
        for _ in range(percent):
            #print(population)
            selecteds: list = sample(population, amount)
            selecteds.sort(key = lambda indv: indv.fitness)
            #print(selecteds)
            winner = selecteds[-1]
            mating_pool.append(winner)
        return mating_pool
    
    def crossover(self,mating_pool: list) -> list:
        size = len(mating_pool)
        new_pop = []
        while mating_pool:
            indv = mating_pool.pop(randrange(size))
            indv2 = mating_pool.pop(randrange(size - 1))
            chrm1, chrm2 = self.onePointCrossover(indv.chromosome,indv2.chromosome)
            new_pop.append(GaAgent(chrm1))
            new_pop.append(GaAgent(chrm2))
            size -= 2
        return new_pop
    
    def onePointCrossover(self, seq1:str, seq2:str)->tuple:

        part1 = randrange(len(seq1))
        part2 = randrange(len(seq2))
        
        seq12 = seq1[:part1] + seq2[part2:]
        seq21 = seq2[:part2] + seq1[part1:]

        return (seq12, seq21)

    def mutate(self, population:list):
        for indiv in population:
            mutate = random() < self.mutation_rate
            
            if mutate:
                size = len(indiv.chromosome)
                n1, n2 = randrange(size), randrange(size)
                indiv.chromosome = indiv.chromosome[:n1] + indiv.chromosome[n2] + indiv.chromosome[n1+1:n2] + indiv.chromosome[n1] + indiv.chromosome[n2+1: ]

    def findBest(self, population:list):
        print(sorted(population, key=lambda indv: indv.fitness))
        best = sorted(population, key=lambda indv: indv.fitness)[-1]
        
        
        if not self.best_individual:
            self.best_individual = best
            print(self.best_individual.fitness)
            return
        # print('-----------------------')
        # print(best.fitness)
        # print(self.best_individual.fitness)
        # print('-----------------------')

        if best.fitness > self.best_individual.fitness:
            self.best_individual = best
            
       

