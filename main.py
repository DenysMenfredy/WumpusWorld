from agents.agent import Agent
from game.environment import Environment as GameEnvironment
from game.game import Game
from ga.environment import Environment as GAEnvironment

def main():
    game_environment = GameEnvironment(dimension = 5, n_pits = 3)
    game = Game(game_environment)

    ga = GAEnvironment(game)
    
    solution = ga.start()
    
    print(solution)
    
if __name__ == '__main__':
    main()