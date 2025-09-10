# Example file showing a circle moving on screen
import pygame

# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640))
clock = pygame.time.Clock()
running = True
reset = True
drag = False
dt = 0

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)
test_surf = pygame.image.load('gameasset/black_chess_pawn.png').convert_alpha()
test_rect = test_surf.get_rect(center = (40, 40)) # for x and y plus 80
current_mouse_coords = ""

def draw_chess_board():
    for x in range(8):
        for y in range(8):
            if(x + y) % 2 == 0:
                chess_pos_x = x * 80
                chess_pos_y = y * 80 
                pygame.draw.rect(screen,'brown',(chess_pos_x, chess_pos_y, 80, 80))
            else:
                chess_pos_x = x * 80
                chess_pos_y = y * 80 
                pygame.draw.rect(screen, 'white', (chess_pos_x, chess_pos_y, 80, 80))
                
def valid_move(mouse_pos): # Walmart version
    x, y = mouse_pos
    x_row = 0
    y_col = 0
    pawn = True
    if(pawn):
        while(x >= 0):
            x = x - 80
            x_row = x_row + 1
            # print("This is X " + str(x_row)) # Test
        while(y >= 0):
            y = y - 80
            y_col = y_col + 1
            # print("This is Y " + str(y_col)) # Test
        print("This is X " + str(x_row)) # Test
        print("This is Y " + str(y_col)) # Test
        if(x_row > 8):x_row = 8
        if(x_row < 1):x_row = 1
        if(y_col > 8):y_col = 8
        if(y_col < 1):y_col = 1
        
            
        
        x_row -= 1 #ease of calculating lawl
        y_col -= 1
        x = 40 + (x_row * 80) 
        y = 40 + (y_col * 80)

    mouse_pos = x, y
    return mouse_pos
    
    # if(x == 40 and y == 0):
    #     return
    # return

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        mouse_pos = pygame.mouse.get_pos()
        if(event.type == pygame.MOUSEBUTTONDOWN): # Press On Img 
            if(test_rect.collidepoint(mouse_pos)):
                print(mouse_pos) # Test
                drag = True
        if(event.type == pygame.MOUSEBUTTONUP and drag): # Drop
            print(mouse_pos) # Test
            mouse_pos = valid_move(mouse_pos)
            test_rect.center = mouse_pos
            drag = False
                
                
    if reset:
        draw_chess_board()
        reset == False       
    
        
    
    screen.blit(test_surf, test_rect)
    
            
                    
    
        
        
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
# gui.mainloop()    

