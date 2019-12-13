from game.environment import Environment as GameEnvironment
from ga.environment import Environment as GAEnvironment
from agents.ga_agent import GaAgent
from game.game import Game
from numpy import array
#from matplotlib import pyplot as plt

class EfficienceCalculation(object):
    def __init__(self, identifier):
        self.percent_victories = []
        self.percent_took_gold = []
        self.percent_killed_wumpus = []
        self.best = []
        self.worst = []
        self.average = []
        self.set = identifier
    def loadEnvironment(self, dimension, n_pits):
        self.environment = GameEnvironment(dimension = dimension, n_pits = n_pits)
        #self.environment.printGraph()
    def loadWeights(self,size_chrm ,weights:list):
        self.weights = weights
        w1, w2, w3, w4, w5, w6, w7, w8 = self.weights
        self.ag_params = {
            "stop_gen": 100,
            "size_pop": 100,
            "crossover_rate": 0.9,
            "mutation_rate": 0.05,
            "evaluator": None,
            "cooperators": 5,
            "size_chromosome": size_chrm,
            "fitness_function": lambda got_gold, wumpus_died, escaped, \
                                agent_died, size, hits, errors, distance: got_gold * w1 + wumpus_died * w2 + escaped * w3\
                                                                    + agent_died * w4 + size * w5 + hits * w6 + errors * w7 + distance * w8
        }
        
    def runIterations(self, iterations, environments):
        for i in range(environments):
            print(f'Running loop {i+1}')
            self.loadEnvironment(self.environment.dimension, self.environment.n_pits)
            self.runIteration(iterations)
       
    def runIteration(self, iterations):
        self.ag_params["evaluator"] = Game(self.environment, gui_enabled=False)
        # self.ag_params["evaluator"] = Game(self.environment, gui_enabled=True)
        self.iterations = iterations
        victories, took_gold, killed_wumpus = 0, 0, 0
        all_fitness = []
        for i in range(iterations):
            #print(f'Running loop {i+1}')
            ga = GAEnvironment(size_fixed = False, Agent = GaAgent, **self.ag_params)
            solution = ga.start()
            self.ag_params["evaluator"].environment.printMatrix(solution.coordinate)
            if solution.wonGame():
                victories += 1
            if solution.hasGold():
                took_gold += 1 
            if solution.killedWumpus():
                killed_wumpus += 1
            
            all_fitness.append(solution.fitness)
        
        self.percent_victories.append((victories / iterations) * 100)
        self.percent_killed_wumpus.append((killed_wumpus / iterations) * 100)
        self.percent_took_gold.append((took_gold / iterations) * 100)
        self.best.append(max(all_fitness))
        self.worst.append(min(all_fitness))
        self.average.append(sum(all_fitness) / iterations)
    
    def getAgParams(self,):
        return f'\t\tAG params:\nStop Generation: {self.ag_params["stop_gen"]},\
                            \nSize Pop: {self.ag_params["size_pop"]},\
                            \nCrossover Rate: {self.ag_params["crossover_rate"]},\
                            \nMutation rate: {self.ag_params["mutation_rate"]},\
                            \nSize chromosome: {self.ag_params["size_chromosome"]}\n'
    
    def getGameParams(self, ):
        return f'Game Params:\nDimension: {self.environment.dimension}\
                             \nNº pits: {self.environment.n_pits}\
                             \nNº golds: 1\nNº wumpus: 1\n' 
    
    
    def getPercents(self,):
        wins,wumpus,gold = array(self.percent_victories), array(self.percent_killed_wumpus), array(self.percent_took_gold)
        return f'Iterations: {self.iterations}\
            \nPercent Victories:     | {wins} | avg: {wins.mean()} | std: {wins.std()} |\
            \nPercent Killed Wumpus: | {wumpus} | avg: {wumpus.mean()} | std: {wumpus.std()} |\
            \nPercent took Gold:     | {gold} | avg: {gold.mean()} | std: {gold.std()} |\n'
    
    def getResults(self,):
        return f'Configuration {self.set}:\n{self.getAgParams()}\
             {self.getGameParams()}{self.getPercents()}'
              
    def exportResults(self, ):
        with open(f'Config {self.set}.txt', "w+") as file:
            file.write(self.getResults())
        
    
    def showResults(self, ):
        print(self.getResults())
        
    # def showGraphics(self, image_title):
    #     percents = ["Percent Victories", "Percent took gold", "Percent killed wumpus"]
    #     percents_values = [self.percent_victories, self.percent_took_gold, self.percent_killed_wumpus]
    #     xs = [i + 0.1 for i, _ in enumerate(percents)]
    #     plt.bar(xs, percents_values)
    #     plt.ylabel("# values in %")
    #     plt.title("Percents")
    #     plt.xticks([i + 0.1 for i, _ in enumerate(percents)], percents)
    #     plt.savefig(f'{image_title}.png')