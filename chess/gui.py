# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
running = True
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    pygame.draw.circle(screen, "red", player_pos, 40)


    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
            player_pos.y -= 300 * dt
    if keys[pygame.K_s]:
        player_pos.y += 300 * dt
    if keys[pygame.K_a]:
        player_pos.x -= 300 * dt
    if keys[pygame.K_d]:
        player_pos.x += 300 * dt
        
   
    

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()





# # Example file showing a basic pygame "game loop"
# import pygame

# # pygame setup
# pygame.init()
# screen = pygame.display.set_mode((1280, 720))
# clock = pygame.time.Clock()
# running = True

# while running:
#     # poll for events
#     # pygame.QUIT event means the user clicked X to close your window
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     # fill the screen with a color to wipe away anything from last frame
#     screen.fill("brown")

#     # RENDER YOUR GAME HERE

#     # flip() the display to put your work on screen
#     pygame.display.flip()

#     clock.tick(60)  # limits FPS to 60

# pygame.quit()


# from tkinter import * 

# gui = Tk()
# gui.geometry("600x645")
# gui.title("Your Life")

# icon = PhotoImage(file='chess/gameasset/teto_icon.png')
# gui.iconphoto(True, icon)
# gui.config(background="Brown")

# def pawn():
#     return
        
# def startButtonClicked():
#     myLabel = Label(gui, text="Cums")
#     myLabel.pack()

# startButton = Button(gui, text="Touch me now please!", command=startButtonClicked)
# startButton.pack()

# Chess GRID
# for row in range(8): 
#     for col in range(8):
#         color = "white" if (row + col) % 2 == 0 else "black"
#         cell = Label(gui, width=10, height=5, bg=color)
#         cell.grid(row=row, column=col)
gui.mainloop()    

