from game.environment import Environment as GameEnvironment
from game.game import Game
from ga.environment import Environment as GAEnvironment
from agents.ga_agent import GaAgent

class WeightEvaluator(object):
    def __init__(self, ):
        self.agents=[]
        
        pass
    
    def start(self, generation, best_individual):
        print(f'Gen: {generation}')
        
        params = {
            "stop_gen": 20,
            "size_pop": 50,
            "crossover_rate": 0.9,
            "mutation_rate": 0.05,
            "evaluator": None,
            "size_chromosome": 100,
            "fitness_function": None
        }
        
        for agent in self.agents:
            
            weight1, weight2, weight3 = agent.getWeights()
            params['fitness_function'] = lambda got_gold, wumpus_died, agent_died, \
                                    escaped, errors, size, distance: got_gold * weight1 + wumpus_died * weight2 + escaped * weight3\
                                                                        + agent_died * -20 + errors * -2 + size * -1.5 + distance * -5
           
            results = []
            repetitions = 20
            for _ in range(repetitions):
                game_environment = GameEnvironment(dimension = 5, n_pits = 8)
                params["evaluator"] = Game(game_environment, gui_enabled=False)
                ga = GAEnvironment(size_fixed=False, Agent = GaAgent,**params)
                solution = ga.start()
                results.append(solution.fitness)

            average = sum(results) / repetitions
            agent.fitness = average
    
    def populate(self, population):
        self.agents = []
        for indv in population:
            indv.reset()
            self.agents.append(indv)
            
        