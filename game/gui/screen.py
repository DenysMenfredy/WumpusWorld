import pygame
WHITE = (200,200,200)
BACKGROUND = (00,00,00)

class Screen(object):
    def __init__(self,):
        self.WIDTH = None
        self.HEIGHT = None
        self.screen = None
        self.square_size = None
        self.square_x = None
        self.square_y = None
        self.part = None
        self.generation = 0
        self.score = 0

    def show(self, dimension):
        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

        self.WIDTH = self.screen.get_width()
        self.HEIGHT = self.screen.get_height()

        initial_x, initial_y = self.WIDTH//4, 50
        self.square_size = self.HEIGHT - (self.HEIGHT//6)
        self.square_x = initial_x + self.square_size
        self.square_y = initial_y + self.square_size
        parts = dimension
        self.part = self.square_size//parts
        self.loadComponets()
    
    def updateText(self,):
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('Generation {} || Best Score: {}'.format(self.generation,self.score), True, WHITE, BACKGROUND)
        textRect = text.get_rect()
        textRect.center = (self.WIDTH // 2, 25)
    
    def loadComponets(self,):
        img_wumpus = [
            pygame.image.load('C:/Users/Lab41/Desktop/WumpusWorld/game/gui/img/monster.png'), 
            pygame.image.load('C:/Users/Lab41/Desktop/WumpusWorld/game/gui/img/monster.png')
        ]

        img_wumpus = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in img_wumpus]
        img_wumpus[0] = pygame.transform.rotate(img_wumpus[0],-5)
        img_wumpus[1] = pygame.transform.rotate(img_wumpus[1],5)

        img_pit = [
            pygame.image.load('C:/Users/Lab41/Desktop/WumpusWorld/game/gui/img/hole.png'),
        ]
        img_pit = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in img_pit]

        img_gold = [
            pygame.image.load('C:/Users/Lab41/Desktop/WumpusWorld/game/gui/img/gold.png'),
        ]
        img_gold = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in img_gold]

        img_agent = [
            pygame.image.load('C:/Users/Lab41/Desktop/WumpusWorld/game/gui/img/man.png'),
        ]
        img_agent = [pygame.transform.scale(img, (self.part-1,self.part-1)) for img in img_agent]


    def addWumpus(self, coordinates: list):
        for x,y in coordinates:
