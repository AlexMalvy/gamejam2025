import pygame
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
        self.start_time = pygame.time.get_ticks()
        
        self.end_time = None
        self.endgame = False

        self.player = Player(pos=(WIDTH//2, 12500))
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)

        self.general_use = GeneralUse(screen)
        self.game_over = GameOver(screen, font50)
        self.game_menu = GameMenu(screen, font50)

        self.map = Map(self.player, screen)
        self.obstacles = Obstacle(self.map)
        self.background_entities = BackgroundEntities(self.map)

        self.background_entities.spawn_clown_fish(self.obstacles.coral_group)
        self.background_entities.spawn_doris(self.obstacles.coral_group)
        
        # Sound Gestion
        self.SoundManager = SoundManager()
        
        self.player.rect.bottom = self.map.map_rect.bottom - 200
    
    def reset(self):
        self.start_time = pygame.time.get_ticks()
        
        self.end_time = None
        self.endgame = False

        self.player = Player(pos=(WIDTH//2, 12500))
        self.player_group = pygame.sprite.Group()
        self.player_group.add(self.player)
        
        self.map.player = self.player

        self.player.rect.bottom = self.map.map_rect.bottom - 200

    def draw_window(self):
        self.map.draw_bg()

        # Update all background entities
        self.background_entities.update()
        
        # Update all obstacles
        self.obstacles.update()

        if not self.endgame:
            self.player_group.draw(self.map.map)
            self.player_group.update()

        # # Debug player rect
        # pygame.draw.rect(self.map.map, Colors.WHITE, self.player.rect, 2)
        # self.map.map.blit(self.player.mask.to_surface(), self.player.rect)

        # Foreground entities update
        self.background_entities.update_foreground()

        # Camera Update
        self.map.update()
        
        # Timer
        time = font40.render(f"Timer : {self.general_use.update_timer(self.start_time, self.end_time)}", True, Colors.WHITE)
        screen.blit(time, (10, 10))
        
        pygame.display.update()

    def game_loop(self):
        run = True
        left = False
        right = False
        up = False
        special = False
        self.endgame = False
        # init sound for music
        pygame.mixer.pre_init(44100,-16,2, 1024)
        pygame.mixer.init()
        pygame.mixer.music.load("assets/sfx/Musique/game.ogg")

        #reset timer
        self.start_time = pygame.time.get_ticks()

        while run:
            clock.tick(60)
            #start game music
            if not pygame.mixer.music.get_busy():
                pygame.mixer.music.play()

            # End Game
            if self.endgame:
                self.player.stunned = True
                self.player.stunned_timer = pygame.time.get_ticks()
                if self.obstacles.boat_group.sprites()[0].animation_done:
                    run = False
            
            # Movements
            # Left
            if left and self.player.rect.left + self.player.mask_diff["left"] > 0 and not self.player.stunned:
                self.player.rect.left -= self.player.speed
                self.player.moving = True
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
                self.player.moving = True
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
                self.player.jumping = True
                self.player.state = 2
            

            # # Apply Gravity

            # # Mask collision
            # if self.player.velocity < self.player.max_falling_speed:
            #     self.player.velocity += self.player.falling_speed
            # self.player.rect.y += self.player.velocity
            # if self.player.velocity >= 0:
            #     # Check for collision
            #     mask_collide = False
            #     rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False)
            #     if rect_collide:
            #         mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False, pygame.sprite.collide_mask)
            #         if mask_collide:
            #             self.player.rect.bottom = Collision.mask_collide_mask(self.player, mask_collide[0], "bottom")
            #             self.player.velocity = 0
            #             self.player.grounded = True
            #             self.player.fall_timer = pygame.time.get_ticks()

            # Rect Collision
            if not self.endgame:
                if self.player.velocity < self.player.max_falling_speed:
                    self.player.velocity += self.player.falling_speed
                self.player.rect.y += self.player.velocity
                if self.player.velocity >= 0:
                    # Check for collision
                    rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.obstacle_group, False)
                    if rect_collide:
                        self.player.rect.bottom = rect_collide[0].rect.top
                        self.player.velocity = 0
                        self.player.grounded = True
                        self.player.fall_timer = pygame.time.get_ticks()

            
            # Special Attack
            if special and not self.endgame:
                self.SoundManager.play_random("special")
                if up:
                    self.obstacles.projectiles_group.add(self.player.attack_bubble(self.map, True))
                else:
                    self.obstacles.projectiles_group.add(self.player.attack_bubble(self.map))
            
            # Check for collision
            for projectile in self.obstacles.projectiles_group:
                # Shark Collision
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(projectile, self.obstacles.shark_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(projectile, self.obstacles.shark_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        mask_collide[0].get_stunned()
                        projectile.kill()
                        
                # Yellow fish Collision
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(projectile, self.obstacles.yellow_fish_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(projectile, self.obstacles.yellow_fish_group, False, pygame.sprite.collide_mask)
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
                    self.player.moving = True
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
            
            # Yellow fish
            # Check for collision
            mask_collide = False
            rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.yellow_fish_group, False)
            if rect_collide:
                mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.yellow_fish_group, False, pygame.sprite.collide_mask)
                if mask_collide:
                    mask_collide[0].bounce(self.player)
            
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

            # Boat
            # Check for collision
            # # Mask collision
            if self.player.velocity >= 0:
                mask_collide = False
                rect_collide = pygame.sprite.spritecollide(self.player, self.obstacles.boat_group, False)
                if rect_collide:
                    mask_collide = pygame.sprite.spritecollide(self.player, self.obstacles.boat_group, False, pygame.sprite.collide_mask)
                    if mask_collide:
                        if self.player.rect.bottom - self.player.mask_diff["bottom"] - mask_collide[0].rect.top + mask_collide[0].mask_diff["top"] <= 150:
                            self.player.grounded = True
                            self.player.fall_timer = pygame.time.get_ticks()
                            mask_collide[0].start_endgame()
                            if not self.endgame:
                                self.endgame = True
                                self.end_time = pygame.time.get_ticks()
                                self.game_over.final_time = self.general_use.update_timer(self.start_time, self.end_time)
            

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
        self.game_menu.menu_loop()
        self.game_loop()
        self.game_over.game_over_loop()

main = MainGame()
while True:
    main.run()
    main.reset()