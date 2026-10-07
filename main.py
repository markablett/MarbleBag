import tkinter as tk
import pygame
import random

# Window setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
checkKeypress = True

# fill the screen with a color to wipe away anything from last frame
screen.fill("white")

# Initialise marble bag
attackCritBag = [1, 1, 0, 0, 0, 0, 0, 0]

# Damage UI elements
damage_sprite = pygame.Rect(screen.get_width() / 3, 200, 50, 50) 

# Initialise font
font = pygame.font.Font(None, 24)

# Setup damage text surface
text_surface = font.render("hello", True, "black")
text_rect = text_surface.get_rect()
text_rect.center == damage_sprite.center

# Render characters
pygame.draw.circle(screen, "blue", pygame.Vector2(screen.get_width() / 3, screen.get_height() / 2), 40)
pygame.draw.circle(screen, "red", pygame.Vector2((screen.get_width() / 3) * 2, screen.get_height() / 2), 40)

def attack():
    global attackCritBag
    isCrit = 0
    length = len(attackCritBag)
    
    # Reset the marble bag if it's empty
    if length == 0:
        attackCritBag = [1, 1, 0, 0, 0, 0, 0, 0]
        length = len(attackCritBag)
        
    # Get random marble from the critical hit chance marble bag if there is more than one marble in the bag
    critBagIndex = 0
    if  length > 1:
        critBagIndex = random.randrange(0, length - 1)

    # Use marble to determine if this hit is a critical hit
    isCrit = attackCritBag[critBagIndex]
    
    # Remove the marble from the bag
    attackCritBag.remove(attackCritBag[critBagIndex])
    
    # Show the damage!
    damage = 0
    if  isCrit == 0:      
        damage = random.randrange(1, 20)
        pygame.draw.rect(screen, "green", damage_sprite)
    else:
        damage = random.randrange(1, 20) * 2
        pygame.draw.rect(screen, "red", damage_sprite)
    
    # Return damage to display
    return damage
    
while running:
    # Events handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if pygame.key.get_pressed()[pygame.K_SPACE]:                
                damage = attack()
                damage_surface = font.render(str(damage), True, "black")
                screen.blit(damage_surface, (damage_sprite.centerx - 6, damage_sprite.centery - 6))
        
    pygame.display.update()
    clock.tick(30)

pygame.quit()
