import pygame
# import win32api
# import win32con
# import win32gui

# try to make the package as simple to run as possible. 

class Item:
    def __init__(self, x, y, health, happiness, image_name):
        self.x = x
        self.y = y
        self.health = health
        self.happiness = happiness
        self.image = pygame.image.load(image_name)
        rect = self.image.get_rect()
        self.image_rect = pygame.Rect(x - rect.width / 2, y - rect.height / 2, rect.width, rect.height)
                                      
class Cat:
    def _init_(self,name,x,y,hunger,smiley):
        self.name = name
        self.x = x
        self.y = y
        self.hunger = hunger 
        self.smiley = smiley
        self.image = pygame.image.load("assets/" + name + "testy.png")
        rect = self.image.get_rect()
        self.image_rect = pygame.Rect(x - rect.width / 2, y - rect.height / 2, rect.width, rect.height)

class Game:
        def __init__(self):
            self.width = 1920
            self.height = 1280
            self.background_colour = "white"
            self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
            # pygame.display.set_caption("helo")
            self.buttons_bar_height = 100
            # self.buttons_bar_colour = "orange"
            self.image_names = ["funni.png"]
            self.mist_button = Item(self.width/2, self.height / 2, 0, 0, self.image_names[0])

        def draw_everything(self):
            self.screen.fill(self.background_colour)
            # pygame.draw.rect(self.screen, self.buttons_bar_colour, pygame.Rect(0, 0, self.width, self.buttons_bar_height))
            self.screen.blit(self.mist_button.image, self.mist_button.image_rect)
            pygame.display.update()
        
        def run(self):
             while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        return
                self.draw_everything()

                    
    
pygame.init()
game = Game()
game.run()