from agent import Agent
from environment import Environment
from game import Game

def main():
    environment = Environment(dimension = 5, n_pits = 3)
    agent = Agent(5)

    game = Game(environment, agent)
    game.start()

if __name__ == '__main__':
    main()