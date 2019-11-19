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
            "stop_gen": 10,
            "size_pop": 50,
            "crossover_rate": 0.9,
            "mutation_rate": 0.05,
            "evaluator": None,
            "size_chromosome": 120,
            "fitness_function": lambda got_gold, wumpus_died, agent_died, \
                                    escaped, errors, size, distance: got_gold * 150 + wumpus_died * 350 + agent_died * -20\
                                                                        + escaped * 500 + errors * -2 + size * -1.5 - distance * 5  
        }
        
        for agent in self.agents:
            peso1,peso2,peso3 = agent.getWeights()
            params['fitness_function'] = lambda got_gold, wumpus_died, agent_died, \
                                    escaped, errors, size, distance: got_gold * peso1 + wumpus_died * peso2 + escaped * peso3\
                                                                        + agent_died * -20 + errors * -2 + size * -1.5 + distance * -5
           
            results = []
            
            for _ in range(20):
                game_environment = GameEnvironment(dimension = 5, n_pits = 8)
                params["evaluator"] = Game(game_environment, gui_enabled=False)
                ga = GAEnvironment(size_fixed=False, Agent = GaAgent,**params)
                solution = ga.start()
                #game_environment.printMatrix(solution.coordinate)
                #print(solution)
                results.append(solution.fitness)

            average = sum(results) / len(results)
            agent.fitness = average
    
    def populate(self, population):
        for indv in population:
            indv.reset()
            self.agents.append(indv)
            
        