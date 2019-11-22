from random import sample, randrange, random


class Environment:
    def __init__(self, size_fixed, Agent, **params):
        self.stop_generation:int = params["stop_gen"]
        self.best_individual = None
        self.size_pop:int = params["size_pop"]
        self.crossover_rate: float = params["crossover_rate"]
        self.mutation_rate: float = params["mutation_rate"]
        self.evaluator = params["evaluator"]
        self.Agent = Agent
        self.Agent.size_limit = params["size_chromosome"]
        self.Agent.fitness_function = params["fitness_function"]
        self.size_fixed = size_fixed
        
        
    def start(self, ):
        population:list = self.generateInitialPop()
        self.evaluate(population)
        self.findBest(population)
        for generation in range( 1, self.stop_generation ):
            population = self.reproduce(population, generation)
            self.evaluate(population, generation, self.best_individual)
            self.findBest(population)
        self.evaluate([self.best_individual], generation = "x")

        return self.best_individual
    
    def generateInitialPop(self, )->list:
        temp_population = [self.Agent(generation=0, count=i) for i in range(self.size_pop) ]
        return temp_population

    def evaluate(self, population, generation=0, best_individual=None):
        self.evaluator.populate(population)
        self.evaluator.start(generation, best_individual)

    def reproduce(self, population:list , generation:int)->list:
        mating_pool:list = self.selection(population)
        new_pop:list = self.crossover(mating_pool,generation)
        self.mutate(new_pop)
        population.sort(key=lambda indv: indv.fitness)
        percent = int(self.size_pop * self.crossover_rate )
        percent = percent if percent%2 == 0 else percent + 1
        return new_pop + population[percent: ]

    def selection(self, population:list)->list:
        mating_pool = []
        amount = 3
        percent = int(self.size_pop * self.crossover_rate )
        percent = percent if percent%2 == 0 else percent + 1 
    
        for _ in range(percent):
            selecteds: list = sample(population, amount)
            selecteds.sort(key = lambda indv: indv.fitness)
            winner = selecteds[-1]
            mating_pool.append(winner)
        return mating_pool
    
    def crossover(self,mating_pool:list, generation:int) -> list:
        size = len(mating_pool)
        new_pop = []
        indv_count = 0
        while mating_pool:
            indv = mating_pool.pop(randrange(size))
            indv2 = mating_pool.pop(randrange(size - 1))
            chrm1, chrm2 = self.onePointCrossover(indv.chromosome,indv2.chromosome)
            new_pop.append(self.Agent(chromosome=chrm1, generation=generation,count=indv_count))
            new_pop.append(self.Agent(chromosome=chrm2, generation=generation,count=indv_count+1))
            indv_count += 2
            size -= 2
        return new_pop
    
    def onePointCrossover(self, seq1:str, seq2:str)->tuple:
        p_seq1 = randrange(len(seq1))
        p_seq2 = randrange(len(seq2)) if not self.size_fixed else p_seq1
        
        seq12 = seq1[:p_seq1] + seq2[p_seq2:]
        seq21 = seq2[:p_seq2] + seq1[p_seq1:]

        return (seq12, seq21)
    
    def doublePointCrossover(self, seq1:str, seq2:str)->tuple:
        p_seq1 = sorted([randrange(len(seq1)), randrange(len(seq1))])
        p_seq2 = sorted([randrange(len(seq2)), randrange(len(seq2))])
                
        seq12 = seq1[:p_seq1[0]] +seq2[p_seq2[0]:p_seq2[1]] +seq1[p_seq1[1]:]
        seq21 = seq2[:p_seq2[0]] + seq1[p_seq1[0]:p_seq1[1]]+seq2[p_seq1[1]:]

        return (seq12, seq21)

    def mutate(self, population:list):
        for indiv in population:
            mutate = random() < self.mutation_rate
            
            if mutate:
                indiv.chromosome = indiv.randomChromosome()
                #size = len(indiv.chromosome)
                #n1, n2 = randrange(size), randrange(size)
                #indiv.chromosome = indiv.chromosome[:n1] + indiv.chromosome[n2] + indiv.chromosome[n1+1:n2] + indiv.chromosome[n1] + indiv.chromosome[n2+1: ]

    def findBest(self, population:list):
        best = sorted(population, key=lambda indv: indv.fitness)[-1]

        if not self.best_individual:
            self.best_individual = best.copy()
            return
        if best.fitness > self.best_individual.fitness:
            self.best_individual = best.copy()
            
       

