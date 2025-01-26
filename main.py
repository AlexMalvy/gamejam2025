import pygame
import time
from src.utils.color import Colors
from src.utils.game_over import GameOver
from src.entities.player import Player
from src.utils.generaluse import GeneralUse
from src.utils.map import Map
from pygame.font import SysFont
from src.screens.game_menu import GameMenu
from pygame.locals import *
from src.utils.collision import Collision
from obstacle import Obstacle
from background_entities import BackgroundEntities
from src.utils.sounds import SoundManager


WIDTH, HEIGHT = 1600, 800

pygame.init()
pygame.display.set_caption("The rise of the Axolotl")
screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))
# screen = pygame.display.set_mode((0,0)) #pygame.FULLSCREEN
# WIDTH, HEIGHT = screen.get_width(), screen.get_height()
clock = pygame.time.Clock()

font_path = "assets/fonts/nexa_heavy.ttf"
font40 = pygame.font.Font(font_path, 40)
font50 = pygame.font.Font(font_path, 50)

class MainGame:
    def __init__(self):
        self.start_time = time.time()

        self.player = Player(pos=(WIDTH//2, 12500))
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        self.general_use = GeneralUse(screen)
        self.game_over = GameOver(screen, font50)
        # self.game_over = GameOver(
        #     self.general_use,
        #     clock,
        #     # self.get_score_text,
        #     screen,
        # )
        self.game_menu = GameMenu(screen, font50)

        self.map = Map(self.player, screen)
        self.obstacles = Obstacle(self.map)
        self.background_entities = BackgroundEntities(self.map)
        
        # Sound Gestion
        self.SoundManager = SoundManager()
        
        self.player.rect.bottom = self.map.map_rect.bottom - 200
    

    def draw_window(self):
        self.map.draw_bg()

        # Update all background entities
        self.background_entities.update()
        
        # Update all obstacles
        self.obstacles.update()

        self.player_group.draw(self.map.map)
        self.player_group.update()

        # # Debug player rect
        pygame.draw.rect(self.map.map, Colors.WHITE, self.player.rect, 2)
        # self.map.map.blit(self.player.mask.to_surface(), self.player.rect)

        self.map.update()

        pygame.display.update()

    def game_loop(self):
        run = True
        left = False
        right = False
        up = False
        self.player.grounded = False
        special = False
        # init sound for music
        pygame.mixer.pre_init(44100,-16,2, 1024)
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sfx/Musique/game.ogg")
        while run:
            clock.tick(60)
            #start game music
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()
            
            # Movements
            # Left
            if left and self.player.rect.left + self.player.mask_diff["left"] > 0 and not self.player.stunned:
                self.player.rect.left -= self.player.speed
                if self.player.rect.left + self.player.mask_diff["left"] < 0:
                    self.player.rect.left = Collision.mask_collidepoint(self.player, (0,0), "left")
                # Flip player sprite
                if self.player.facing_right:
                    self.player.flip_facing = True
                    
                # Check for collision
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        self.player.rect.left = Collision.mask_collide_mask(self.player, mask_collide[0], "left")
            
            # Right
            if right and self.player.rect.right - self.player.mask_diff["right"] < self.map.map_rect.right and not self.player.stunned:
                self.player.rect.right += self.player.speed
                if self.player.rect.right - self.player.mask_diff["right"] > self.map.map_rect.right:
                    self.player.rect.right = Collision.mask_collidepoint(self.player, (self.map.map_rect.right,0), "right")
                # Flip player sprite
                if not self.player.facing_right:
                    self.player.flip_facing = True
                    
                # Check for collision
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        self.player.rect.right = Collision.mask_collide_mask(self.player, mask_collide[0], "right")

            # Jump
            if up and self.player.grounded and not self.player.stunned:
                self.player.velocity = -self.player.jump_strength
                self.player.grounded = False
            

            # Apply Gravity
            if self.player.velocity < self.player.max_falling_speed:
                self.player.velocity += self.player.falling_speed
            self.player.rect.y += self.player.velocity
            if self.player.velocity >= 0:
                # Check for collision
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        self.player.rect.bottom = Collision.mask_collide_mask(self.player, mask_collide[0], "bottom")
                        self.player.velocity = 0
                        self.player.grounded = True
                        self.player.fall_timer = pygame.time.get_ticks()

            
            # Special Attack
            if special:
                self.SoundManager.play_random("special")
                if up:
                    self.obstacles.projectiles_group.add(self.player.attack_bubble(self.map, True))
                else:
                    self.obstacles.projectiles_group.add(self.player.attack_bubble(self.map))
            
            # Check for collision
            for projectile in self.obstacles.projectiles_group:
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(projectile, self.obstacles.shark_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(projectile, self.obstacles.shark_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        mask_collide[0].get_stunned()
                        projectile.kill()
            
            
            # Bubbles
            # Check for collision
            mask_collide = False
            rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.coral_group, False)
            if rect_collide:
                mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.coral_group, False, pygame.sprite.collide_mask)
                if mask_collide:
                    mask_collide[0].lift(self.player)
                    if not pygame.mixer.get_busy():
                        self.SoundManager.play("bubble_up")

                if not mask_collide:
                    self.SoundManager.stop("bubble_up")
            
            # Jellyfish
            # Check for collision
            # # Mask collision
            if self.player.velocity >= 0:
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.jellyfish_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.jellyfish_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        if self.player.rect.bottom - self.player.mask_diff["bottom"] - mask_collide[0].rect.top + mask_collide[0].mask_diff["top"] <= 150:
                            mask_collide[0].ascend(self.player)
                            self.player.grounded = True
                            self.player.fall_timer = pygame.time.get_ticks()

            # # Rect Collision
            # if self.player.velocity >= 0:
            #     rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.jellyfish_group, False)
            #     if rect_collide:
            #         rect_collide[0].ascend_rect(self.player)
            #         self.player.grounded = True
            #         self.player.fall_timer = pygame.time.get_ticks()
            
            
            # Sharks
            # Check for collision
            mask_collide = False
            rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.shark_group, False)
            if rect_collide:
                mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.shark_group, False, pygame.sprite.collide_mask)
                if mask_collide:
                    self.player.get_stunned()

            for shark in self.obstacles.shark_group:
                if not shark.rect.colliderect(self.map.map_rect):
                    shark.turn_around()
            

            special = False
            # Event Handler
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                    self.general_use.close_the_game()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                        self.general_use.close_the_game()
                    if event.key == pygame.K_q:
                        left = True
                    if event.key == pygame.K_d:
                        right = True
                    if event.key == K_z:
                        up = True
                    if event.key == K_SPACE:
                        special = True
                    
                    #test game over
                    if event.key == K_h:
                       run = False
                       pygame.mixer.music.stop()
                       self.game_over.game_over_loop() 
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_q:
                        left = False
                    if event.key == pygame.K_d:
                        right = False
                    if event.key == K_z:
                        up = False
            self.draw_window()

    def run(self):
        # self.game_menu.menu_loop()
        self.game_loop()
        # self.game_over.game_over_loop()
main = MainGame()
while True:
    main.run() 