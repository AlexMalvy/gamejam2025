import random

class BubbleScreenMenu:
    def __init__(self, screen_width, screen_height, image):
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.image = image
        self.reset()

    def reset(self):
        self.x = random.choice([random.randint(0, self.screen_width // 4), random.randint(self.screen_width * 3 // 4, self.screen_width)])
        self.y = self.screen_height + random.randint(0, self.screen_height) 
        self.speed = random.uniform(1, 3)

    def update(self):
        self.y -= self.speed
        if self.y < -self.image.get_height():
            self.reset()

    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
