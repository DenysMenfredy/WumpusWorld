from game.environment import Environment as GameEnvironment
from ga.environment import Environment as GAEnvironment
from agents.ga_agent import GaAgent
from game.game import Game
from matplotlib import pyplot as plt

class EfficienceCalculation(object):
    def __init__(self, identifier):
        self.percent_victories = 0
        self.percent_took_gold = 0
        self.percent_killed_wumpus = 0
        self.best = None
        self.worst = None
        self.average = None
        self.set = identifier
    def loadEnvironment(self, dimension, n_pits):
        self.environment = GameEnvironment(dimension = dimension, n_pits = n_pits)
        
    def loadWeights(self, weights:list):
        self.weights = weights
        w1, w2, w3, w4, w5, w6, w7, w8 = self.weights
        self.ag_params = {
            "stop_gen": 100,
            "size_pop": 100,
            "crossover_rate": 0.85,
            "mutation_rate": 0.05,
            "evaluator": None,
            "size_chromosome": 100,
            "fitness_function": lambda got_gold, wumpus_died, escaped, \
                                agent_died, size, hits, errors, distance: got_gold * w1 + wumpus_died * w2 + escaped * w3\
                                                                    + agent_died * w4 + size * w5 + hits * w6 + errors * w7 + distance * w8
        }
        
       
    def runIteration(self, iterations):
        self.ag_params["evaluator"] = Game(self.environment, gui_enabled=True)
        self.iterations = iterations
        victories, took_gold, killed_wumpus = 0, 0, 0
        all_fitness = []
        for i in range(iterations):
            print(f'Running loop {i}')
            ga = GAEnvironment(size_fixed = False, Agent = GaAgent, **self.ag_params)
            solution = ga.start()
            if solution.wonGame():
                victories += 1
            if solution.hasGold():
                took_gold += 1 
            if solution.killedWumpus():
                killed_wumpus += 1
            
            all_fitness.append(solution.fitness)
        
        self.percent_victories = (victories / iterations) * 100
        self.percent_killed_wumpus = (killed_wumpus / iterations) * 100
        self.percent_took_gold = (took_gold / iterations) * 100
        self.best = max(all_fitness)
        self.worst = min(all_fitness)
        self.average = sum(all_fitness) / iterations
    
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
        return f'Iterations: {self.iterations}\nPercent Victories: {self.percent_victories}%\
                \nPercent Killed Wumpus: {self.percent_killed_wumpus}%\
                \nPercent took Gold: {self.percent_took_gold}%\n'
    
    def getResults(self,):
        return f'Configuration {self.set}:\n{self.getAgParams()}\
             {self.getGameParams()} {self.getPercents()}'
              
    def exportResults(self, ):
        with open(f'Config {self.set}.txt', "w+") as file:
            file.write(self.getResults())
        
    
    def showResults(self, ):
        print(self.getResults())
        
    def showGraphics(self, image_title):
        percents = ["Percent Victories", "Percent took gold", "Percent killed wumpus"]
        percents_values = [self.percent_victories, self.percent_took_gold, self.percent_killed_wumpus]
        xs = [i + 0.1 for i, _ in enumerate(percents)]
        plt.bar(xs, percents_values)
        plt.ylabel("# values in %")
        plt.title("Percents")
        plt.xticks([i + 0.1 for i, _ in enumerate(percents)], percents)
        plt.savefig(f'{image_title}.png')