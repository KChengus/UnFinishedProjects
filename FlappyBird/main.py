import pygame
from Settings import settings
from Bird import Flappybird
pygame.init()

class Game(settings):



    def __init__(self):
        # display
        self.display = pygame.display.set_mode((self.display_width, self.display_height))

        # picture
        self.fBird = Flappybird(200, 200)
        picture = pygame.image.load("fb_pictures\\fBird.png")
        self.picture = pygame.transform.scale(picture, self.flappy_bird_size)

    def handle_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                
                self.bird_ramp_up_multiplicator = -5

    def background(self):
        self.display.fill((255, 255, 255))

    def updateBirdPos(self):
    
        self.fBird.updatePos(0, self.bird_ramp_up_speed * self.bird_ramp_up_multiplicator)
     
        self.bird_ramp_up_multiplicator += 0.2
        

    def draw_picture(self):
        # draw bird
        self.display.blit(self.picture, self.fBird.pos)
        pygame.draw.rect(self.display, self.color["green"], pygame.Rect(30, 30, 60, 60))

    def main(self):
        clock = pygame.time.Clock()
        while self.running:
            self.background()
            self.handle_event()
            self.updateBirdPos()
            self.draw_picture()
            pygame.display.update()
            clock.tick(60)



if __name__ == "__main__":
    Game().main()
    pygame.quit()