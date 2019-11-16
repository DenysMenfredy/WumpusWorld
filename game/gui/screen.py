import pygame
from agents.ga_agent import GaAgent as Agent
WHITE = (200,200,200)
BACKGROUND = (155,155,155)

class Screen(object):
    def __init__(self,):
        self.WIDTH = None
        self.HEIGHT = None
        self.screen = None
        self.square_size = None
        self.square_x = None
        self.square_y = None
        self.initial_x = None
        self.initial_y = None
        self.part = None
        self.parts = None
        self.generation = 0
        self.score = 0
        self.img_wumpus = None
        self.img_pit = None
        self.img_gold = None
        self.img_agent = None
        self.img_status_agent = None
        self.agents = []
        self.generation = None
        self.clock = pygame.time.Clock()
        self.fps = 120

    def show(self, dimension, generation, fitness):
        pygame.init()
        self.screen = pygame.display.set_mode((1000, 600))

        self.WIDTH = self.screen.get_width()
        self.HEIGHT = self.screen.get_height()
        self.generation = generation
        self.fitness = fitness
        self.initial_x, self.initial_y = self.WIDTH//4, 50
        self.square_size = self.HEIGHT - (self.HEIGHT//6)
        self.square_x = self.initial_x + self.square_size
        self.square_y = self.initial_y + self.square_size
        self.parts = dimension
        self.part = self.square_size//self.parts
        self.loadComponets()
        
    
    def updateText(self,):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Generation {} || Best Score: {}'.format(self.generation,self.score), True, WHITE, BACKGROUND)
        textRect = text.get_rect()
        textRect.center = (self.WIDTH // 2, 25)
    
    def loadComponets(self,):
        self.img_wumpus = [
            pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/monster.png'), 
            pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/monster.png')
        ]

        self.img_wumpus = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in self.img_wumpus]
        self.img_wumpus[0] = pygame.transform.rotate(self.img_wumpus[0],-5)
        self.img_wumpus[1] = pygame.transform.rotate(self.img_wumpus[1],5)

        self.img_pit = [
            pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/hole.png'),
        ]
        self.img_pit = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in self.img_pit]

        self.img_gold = [
            pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/gold.png'),
        ]
        self.img_gold = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in self.img_gold]

        self.img_agent = [
            pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/man.png'),
        ]
        
        self.img_agent = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in self.img_agent]

        self.img_status_agent ={
            "success":pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/success.png'), 
            "died": pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/gravestone.png'),
            "got_gold": pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/robber.png'),
            "killed_wumpus":pygame.image.load('/home/denysm7/I.C/wumpus/game/gui/img/superhero.png')
         }
        
        self.img_status_agent = {
            "success":pygame.transform.scale(self.img_status_agent["success"], (self.part-1,self.part-1)), 
            "died": pygame.transform.scale(self.img_status_agent["died"], (self.part-1,self.part-1)),
            "got_gold": pygame.transform.scale(self.img_status_agent["got_gold"], (self.part-1,self.part-1)),
            "killed_wumpus":pygame.transform.scale(self.img_status_agent["killed_wumpus"], (self.part-1,self.part-1)),
        }
    def addAgents(self, agents: list):
        self.agents = [agent for agent in agents]
        
    
    def addWumpus(self, coordinates: list):
        self.wumpus_coordinates = [ self.getPositionElement(x, y) for x, y in coordinates ]
        
    def addPits(self, coordinates: list):
        #print(coordinates)
        self.pits_coordinates = [ self.getPositionElement(x, y) for x, y in coordinates ]
        #print(self.pits_coordinates)
    def addGold(self, coordinates: list):
        self.gold_coordinates = [ self.getPositionElement(x, y) for x, y in coordinates ]
    
    def getPositionElement(self, y, x) ->tuple:
        return self.initial_x + (self.part * x), self.square_y - (self.part * y) - self.part
    
    def moveAgent(self, ):
        pass
    
    def updateComponents(self, ):
        self.screen.fill(BACKGROUND)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   quit()
        self.printInfo()
        
        pygame.draw.line(self.screen, WHITE, (self.initial_x, self.initial_y), (self.initial_x , self.square_y), 2)
        pygame.draw.line(self.screen, WHITE, (self.initial_x, self.initial_y), (self.square_x, self.initial_y), 2)

        for i in range(self.parts):
            pygame.draw.line(self.screen, WHITE, (self.initial_x, self.initial_y  + (self.part * (i+1))),  (self.square_x,  self.initial_y  + (self.part * (i+1))), 4)

        for i in range(self.parts):
            pygame.draw.line(self.screen, WHITE, (self.initial_x  + (self.part * (i+1)), self.initial_y),  (self.initial_x  + (self.part * (i+1)), self.square_y), 2)

        for coordinate in self.wumpus_coordinates:
            self.screen.blit(self.img_wumpus[0], coordinate)
        
        for coordinate in self.gold_coordinates:
            self.screen.blit(self.img_gold[0], coordinate)

        for coordinate in self.pits_coordinates:
            self.screen.blit(self.img_pit[0], coordinate)
        
        for agent in self.agents:
            if agent.agent_died:
                self.screen.blit(self.img_status_agent["died"], self.getPositionElement(*agent.coordinate))
            elif agent.killedWumpus() and agent.hasGold():
                self.screen.blit(self.img_status_agent["success"], self.getPositionElement(*agent.coordinate))
            elif agent.killedWumpus():
                self.screen.blit(self.img_status_agent["killed_wumpus"], self.getPositionElement(*agent.coordinate))
            elif agent.hasGold():
                self.screen.blit(self.img_status_agent["got_gold"], self.getPositionElement(*agent.coordinate))
            else:
                self.screen.blit(self.img_agent[0], self.getPositionElement(*agent.coordinate));
        pygame.display.update()
        
        if self.generation == 'x':
            self.fps = 2
        self.clock.tick(self.fps)
        
    def printInfo(self,):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Generation {} || Best Fitness {}'.format(self.generation, self.fitness), True, WHITE, BACKGROUND)
        textRect = text.get_rect()
        textRect.center = (self.WIDTH // 2, 25)  
        self.screen.blit(text, textRect) 