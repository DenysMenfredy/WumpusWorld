
class Game(object):
    def __init__(self, environment, agent = None):
        self.environment = environment
        self.agent = agent
        self.game_over = False
        self.payoff = {
            'move': -1,
            'gold': 50,
            'death': -10,
            'wumpus': 1000,
        }
        self.agents = []


    def start(self,) -> None:
        while(self.agents):
            for agent in self.agents:
                #self.environment.printMatrix(agent.coordinate)
                #perceptions = self.environment.getPerceptions(agent.coordinate)
                #print(perceptions)
                #agent_action = agent.act(perceptions)
                agent_action = agent.act()
                if not agent_action:
                    print('morreu ' + str(agent.score))
                    if(agent.score == 0 ): print(agent.chromosome)
                    self.agents.remove(agent)
                    continue

                agent.score += self.payoff['move']
                #print(agent.coordinate)
                if agent_action.name == 'move':

                    agent.move(agent_action.direction)
                    coordinate = agent.coordinate
                    if self.environment.isValid(coordinate):
                        agent.hits += 1
                    else:
                        agent.errors += 1 
                    #print('agent moved ' + agent_action.direction)
                    if self.environment.isPit(coordinate):
                        agent.score += self.payoff['death']
                        self.agents.remove(agent)
                        continue
                        #print('agent died')
                    if self.environment.isWumpus(coordinate) and not agent.killedWumpus():
                        agent.score += self.payoff['death']
                        self.agents.remove(agent)
                        continue
                        #print('agent died')
                    if self.environment.isExit(coordinate):
                        if agent.hasGold(): 
                            self.agents.remove(agent)
                            continue
                            #print('agent wins')
                            
                if agent_action.name == 'shoot':
                    agent.shoot()
                    targetCoordinate = self.targetCoordinate(agent.coordinate, agent_action.direction)
                    #print('agent shooted: ' + agent_action.direction)
                    if self.environment.isWumpus(targetCoordinate) and not agent.killedWumpus():
                        agent.killWumpus()
                        agent.score += self.payoff['wumpus']
                        #print('agent killed wumpus')
                if agent_action.name == 'pickup' and not agent.hasGold():
                    agent.score += self.payoff['gold']
                    agent.pickUp()

                    #print('agent took gold')
                

    
    def targetCoordinate(self, coordinate:tuple, direction:str) -> tuple:
        x,y = coordinate

        if   direction == 'N': return (x+1,y)
        elif direction == 'S': return (x-1,y)
        elif direction == 'L': return (x,y+1)
        elif direction == 'O': return (x,y-1)
    
    def populate(self, population:list):
        for indv in population:
            indv.reset()
            self.agents.append(indv)
        

