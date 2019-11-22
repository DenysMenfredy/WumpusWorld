
from ga.environment import Environment as GAEnvironment
from ga.weights_evaluator import WeightEvaluator
from agents.weights_optimize import WeightOptimize
from agents.ga_agent import GaAgent
from game.game import Game
from game.environment import Environment as GameEnvironment
from time import time
def callAgForWumpus(weight1, weight2, weight3):
    params = {
            "stop_gen": 50,
            "size_pop": 100,
            "crossover_rate": 0.9,
            "mutation_rate": 0.05,
            "evaluator": None,
            "size_chromosome": 100,
            "fitness_function": lambda got_gold, wumpus_died, escaped, \
                                agent_died, size, errors, hits, distance: got_gold * weight1 + wumpus_died * weight2 + escaped * weight3\
                                                                    + agent_died * -15 + size * -2 + errors * -5 + hits * 0.1 + distance * -10
        }

    game_environment = GameEnvironment(dimension = 5, n_pits = 4)
    params["evaluator"] = Game(game_environment, gui_enabled=False)
    ga = GAEnvironment(size_fixed=False, Agent = GaAgent,**params)
    solution = ga.start()
    game_environment.printMatrix(solution.coordinate)
    print(solution)
        
def callAgForWeights():
    params = {
        "stop_gen": 20,
        "size_pop": 100,
        "crossover_rate": 0.9,
        "mutation_rate": 0.05,
        "evaluator": WeightEvaluator(),
        "size_chromosome": 3,
        "fitness_function": None
    }
    initial_time = time()
    ga = GAEnvironment(size_fixed = True, Agent = WeightOptimize, **params)
    solution = ga.start()
    #print(solution)

def main():
    callAgForWumpus(110, 100, 80)
    #callAgForWeights()
    
    

    
if __name__ == '__main__':
    main()
