
from ga.environment import Environment as GAEnvironment
from ga.weights_evaluator import WeightEvaluator
from agents.weights_optimize import WeightOptimize

def main():
    
     
    params = {
        "stop_gen": 20,
        "size_pop": 60,
        "crossover_rate": 0.9,
        "mutation_rate": 0.05,
        "evaluator": WeightEvaluator(),
        "size_chromosome": 3,
        "fitness_function": None
    }

    ga = GAEnvironment(size_fixed = True, Agent = WeightOptimize,**params)
    solution = ga.start()
    print(solution)

    
if __name__ == '__main__':
    main()
