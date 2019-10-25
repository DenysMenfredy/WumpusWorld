from agent import Agent
from environment import Environment
from game import Game

def main():
    environment = Environment(dimension = 5, n_pits = 3)
    agent = Agent(5)
    environment.printMatrix(agent.coordinate)

    game = Game(environment, agent)
    print('Score: ', game.start())

if __name__ == '__main__':
    main()