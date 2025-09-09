# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

teto_surface = pygame.image.load('D:/CODING/Python/Tutorial/graphics/teto.png')
direction = None

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                direction = "UP"
            elif event.key == pygame.K_s:
                direction = "DOWN"
            elif event.key == pygame.K_a:
                direction = "LEFT"
            elif event.key == pygame.K_d:
                direction = "RIGHT" 
            

    screen.fill("White")
    
    # pygame.draw.circle(screen, "red", player_pos, 10)
    screen.blit(teto_surface, (player_pos.x, player_pos.y))
    
    if direction == "UP":
        if player_pos.y >= 0: #160
           player_pos.y -= 300 * dt
        else:
            player_pos.y = 720 #560
    elif direction == "DOWN":
        if player_pos.y <= 720: #560
           player_pos.y += 300 * dt
        else:
            player_pos.y = 0 #160
    elif direction == "LEFT":
        if player_pos.x >= 0: #440
            player_pos.x -= 300 * dt
        else:
            player_pos.x = 1280 #840
    elif direction == "RIGHT":
        if player_pos.x <= 1280: #840
            player_pos.x += 300 * dt
        else:
            player_pos.x = 0 #440
    


    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()