from random import sample, randrange, random
import numpy as np 
import matplotlib.pyplot as plt
a = 1

class Environment:
    def __init__(self, size_fixed, Agent, **params):
        self.stop_generation:int = params["stop_gen"]
        self.best_individual = None
        self.size_pop:int = params["size_pop"]
        self.crossover_rate: float = params["crossover_rate"]
        self.mutation_rate: float = params["mutation_rate"]
        self.evaluator = params["evaluator"]
        self.amount = params["cooperators"]
        self.Agent = Agent
        self.Agent.size_limit = params["size_chromosome"]
        self.Agent.fitness_function = params["fitness_function"]
        self.size_fixed = size_fixed
        self.graphs_enableds = False  
        
        
        
    def start(self,):
        self.resetData()
        populations:list = [{"population":self.generateInitialPop(),"best_individual": None} for _ in range(self.amount)]
        for i,pop in enumerate(populations):
            self.evaluate(pop["population"])
            self.findBest(pop)
            if self.graphs_enableds: self.saveFitness(pop["population"], i)
    
        for generation in range(1, self.stop_generation ):
            self.shareKnowledge(populations)
            populations = [{"population": self.reproduce(pop["population"], generation), "best_individual": pop["best_individual"]} for pop in populations]
            for i,pop in enumerate(populations):
                self.evaluate(pop["population"], generation, pop["best_individual"])
                self.findBest(pop)
                if self.graphs_enableds: self.saveFitness(pop["population"],i)
        self.evaluate([pop["best_individual"] for pop in populations], generation = "x")
        if self.graphs_enableds: self.showGraph()
        self.resetData()

        return self.best_individual
    
    def generateInitialPop(self, )->list:
        temp_population = [self.Agent(generation=0, count=i) for i in range(self.size_pop) ]
        return temp_population

    def evaluate(self, population, generation=0, best_individual=None):
        self.evaluator.populate(population)
        self.evaluator.start(generation, best_individual)

    def reproduce(self, population:list , generation:int)->list:
        mating_pool:list = self.selection(population)
        new_pop:list = self.crossover(mating_pool, generation)
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
        
        percent = int(self.size_pop * self.crossover_rate )
        percent = percent if percent%2 == 0 else percent + 1
        for _ in range(0,percent,2):
           indv = mating_pool[randrange(size)]
           indv2 = mating_pool[randrange(size)]
           chrm1, chrm2 = self.doublePointCrossover(indv.chromosome,indv2.chromosome)
           new_pop.append(self.Agent(chromosome=chrm1, generation=generation,count=indv_count))
           new_pop.append(self.Agent(chromosome=chrm2, generation=generation,count=indv_count+1))
           indv_count += 2
        
        # while mating_pool:
        #     indv = mating_pool.pop(randrange(size))
        #     indv2 = mating_pool.pop(randrange(size - 1))
        #     chrm1, chrm2 = self.doublePointCrossover(indv.chromosome,indv2.chromosome)
        #     new_pop.append(self.Agent(chromosome=chrm1, generation=generation,count=indv_count))
        #     new_pop.append(self.Agent(chromosome=chrm2, generation=generation,count=indv_count+1))
        #     indv_count += 2
        #     size -= 2
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

    def findBest(self, population:dict):
        population["population"].sort(key=lambda indv: indv.fitness)
        best = population["population"][-1]

        if not population["best_individual"]:
            population["best_individual"] = best.copy()
    
        if best.fitness > population["best_individual"].fitness:
            population["best_individual"] = best.copy()
        
        if not self.best_individual:
            self.best_individual = best.copy()
            
        if best.fitness > self.best_individual.fitness:
            self.best_individual = best.copy()
            
    def shareKnowledge(self, populations:dict):
        for pop in populations:
            for neighbor in populations:
                if pop != neighbor:
                    pop["population"].append(neighbor["best_individual"].copy())
                    pop["population"].pop(0)
    
    def saveFitness(self, population: list, iD):
        all_fitness = np.array([ind.fitness for ind in population])
        with open(f'pop_{iD}.npy',"ab") as file:
            np.save(file,all_fitness)
    
    def showGraph(self, ):
        x = np.arange(self.stop_generation)
        
        for i in range(self.amount):
            average = np.ndarray((0))
            bests = np.ndarray((0))
            worst = np.ndarray((0))
            with open(f'pop_{i}.npy',"rb") as file:
                for j in range(self.stop_generation):
                    all_fitness = np.load(file)
                    average = np.append(average,all_fitness.mean())
                    bests = np.append(bests, max(all_fitness))
                    worst = np.append(worst, min(all_fitness))
            labels = ["average", "best", "worst"]
            data = [average, bests, worst]
            plt.subplot(self.amount,1,i+1)
            for l,y in zip(labels, data):
                plt.plot(x,y,label = l)
            plt.title(f'pop_{i}')
            plt.legend(loc = "best")
            plt.grid(True)
        plt.tight_layout()
        plt.show()
    
    def resetData(self, ):
        for iD in range(self.amount):
            open(f'pop_{iD}.npy',"wb").close()
                

