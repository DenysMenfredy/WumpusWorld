from .gui.screen import Screen
class Game(object):
    def __init__(self, environment, gui_enabled, agent = None):
        self.environment = environment
        self.agent = agent
        self.game_over = False
        self.agents = []
        self.screen = Screen()
        self.gui_enabled = gui_enabled


    def start(self, generation, best_solution) -> None:
        if self.gui_enabled:
            self.screen.show(self.environment.dimension, generation, best_solution)
            self.screen.addAgents(self.agents)
            self.screen.addWumpus(self.environment.getObjectCoord("wumpus"))
            self.screen.addPits(self.environment.getObjectCoord("pit"))
            self.screen.addGold(self.environment.getObjectCoord("gold"))
        
        while(self.agents):
            if self.gui_enabled: self.screen.updateComponents()
            for agent in self.agents:
                #self.environment.printMatrix(agent.coordinate)
                #perceptions = self.environment.getPerceptions(agent.coordinate)
                #print(perceptions)
                #agent_action = agent.act(perceptions)
                agent_action = agent.act()
                if not agent_action:
                    self.agents.remove(agent)
                    continue

                #print(agent.coordinate)
                #self.screen.updateComponents()
                if agent_action.name == 'move':
                    #self.screen.moveAgent(agent, agent_action.direction)
                    agent.move(agent_action.direction)
                    coordinate = agent.coordinate
                    if self.environment.isValid(coordinate): agent.hits += 1
                    else: agent.errors += 1 
                    #print('agent moved ' + agent_action.direction)
                    if self.environment.isPit(coordinate):
                        #self.screen.killAgent(agent)
                        agent.die()
                        self.agents.remove(agent)
                        continue
                        #print('agent died')
                    if self.environment.isWumpus(coordinate) and not agent.killedWumpus():
                        #self.screen.killAgent(agent)
                        agent.die()
                        self.agents.remove(agent)
                        continue
                        #print('agent died')
                    if self.environment.isExit(coordinate) and agent.hasGold(): 
                        agent.escape()
                        self.agents.remove(agent)
                        continue
                        #print('agent wins')
                if agent_action.name == 'shoot':
                    if not agent.hasArrow():
                        #agent.errors += 0.1
                        continue
                    agent.shoot()
                    targetCoordinate = self.targetCoordinate(agent.coordinate, agent_action.direction)
                    #print('agent shooted: ' + agent_action.direction)
                    if self.environment.isWumpus(targetCoordinate) and not agent.killedWumpus():
                        agent.killWumpus()
                        #print('agent killed wumpus')
                if agent_action.name == 'pickup':
                    if not agent.hasGold() and self.environment.isGold(agent.coordinate):
                        agent.pickUp()
                    else :
                        #agent.errors += 0.1
                        pass

                        #print('agent took gold')
        if self.gui_enabled: self.screen.updateComponents()
                

    
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
        
