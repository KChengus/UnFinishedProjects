import pygame
from Settings import settings
pygame.init()

class Game(settings):
    def __init__(self):
        # display
        self.display = pygame.display.set_mode((self.display_width, self.display_height))

        # picture
        picture = pygame.image.load("fb_pictures\\flappy_bird.png")
        self.picture = pygame.transform.scale(picture, self.flappy_bird_size)
        self.picture_rect = picture.get_rect(center=self.display.get_rect().center)

    def handle_event(self):

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def background(self):
        self.display.fill((255, 255, 255))

    def temp_picture(self):
        self.display.blit(self.picture, self.picture_rect)

    def main(self):
        while self.running:
            self.handle_event()
            self.background()
            self.temp_picture()
            pygame.display.update()



if __name__ == "__main__":
    Game().main()
    pygame.quit()