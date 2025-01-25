import pygame
import time

#définir une classe qui va s'occuper des animations
class AnimateSprite(pygame.sprite.Sprite):

    # définir les choses a faire a la création de l'ententité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f"assets/{sprite_name}.png")
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0 
        self.images = animations.get(sprite_name)
        self.animation = False

    #définir une méthode ppour démarrer l'animation
    def start_animation(self):
        self.animation = True

    #définir une méthode pour animer un sprite
    def animate(self, loop=False,):

        #vérifier si l'animation est active
        if self.animation:
        
            #passer à l'image suivante
            self.current_image += 1

            #vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                #remettre l'animation au débart
                self.current_image = 0
                #vérifier si l'animation n'est pas en mode boucle
                if loop is False:
                    #désactiation de l'animation
                    self.animation = False

            #modifier l'image de l'animation précédente par la suivante
            self.image = self.images[int(self.current_image)]
            ts = time.time()
            self.image = pygame.transform.scale(self.image, self.size)

#définir une fonction pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images du sprite
    images = []
    #récupérer le chemin du dossier
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier
    for num in (1, 8):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))
    #renvoyer le contenu de la liste d'image
    return images

 
#définir un dictionnaire qui va contenir les images chargées
animations = {
    "corail_bubble" : load_animation_images("corail_bubble"),
    # "player" : load_animation_images("player"),
    # "alien" : load_animation_images("alien")
    }