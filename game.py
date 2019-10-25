
class Game(object):
    def __init__(self, environment, agent):
        self.environment = environment
        self.agent = agent
        self.game_over = False
        self.payoff = {
            'move': -1,
            'gold': 50,
            'death': -10,
            'wumpus': 1000,
        }
        self.limit_move = 20


    def start(self,) -> int:
        while(not self.game_over and self.limit_move != 0):
            self.environment.printMatrix(self.agent.coordinate)
            perceptions = self.environment.getPerceptions(self.agent.coordinate)
            print(perceptions)
            agent_action = self.agent.act(perceptions)
            self.agent.score += self.payoff['move']
            print(self.agent.coordinate)
            if agent_action.name == 'move':
                self.agent.move(agent_action.direction)
                coordinate = self.agent.coordinate
                print('agent moved ' + agent_action.direction)
                if self.environment.isPit(coordinate):
                    self.agent.score += self.payoff['death']
                    self.game_over = True
                    print('agent died')
                if self.environment.isWumpus(coordinate):
                    self.agent.score += self.payoff['death']
                    self.game_over = True
                    print('agent died')
                if self.environment.isExit(coordinate):
                    if self.agent.hasGold(): 
                        self.game_over = True
                        print('agent wins')
                        
            if agent_action.name == 'shoot':
                self.agent.shoot()
                coordinate = self.targetCoordinate(self.agent.coordinate, agent_action.direction)
                print('agent shooted: ' + agent_action.direction)
                if self.environment.isWumpus(coordinate):
                    self.environment.removeWumpus(self.agent.coordinate)
                    self.agent.score += self.payoff['wumpus']
                    print('agent killed wumpus')
            if agent_action.name == 'pickup':
                self.agent.score += self.payoff['gold']
                self.agent.pickUp()
                self.environment.removeGold(self.agent.coordinate)
                print('agent took gold')
            self.limit_move -= 1
        return self.agent.score

    
    def targetCoordinate(self, coordinate:tuple, direction:str) -> tuple:
        x,y = coordinate

        if   direction == 'N': return (x+1,y)
        elif direction == 'S': return (x-1,y)
        elif direction == 'L': return (x,y+1)
        elif direction == 'O': return (x,y-1)