# Example file showing a circle moving on screen
import pygame
from sys import exit

class Pieces(pygame.sprite.Sprite):
    def __init__(self, type, color, pos):
        super().__init__()
        if color == 'white': # white
            if type == 'pawn':
                self.image = pygame.image.load('gameasset/White/white_pawn.png').convert_alpha()
            elif type == 'knight':
                self.image = pygame.image.load('gameasset/White/white_knight.png').convert_alpha()
            elif type == 'bishop':
                self.image = pygame.image.load('gameasset/White/white_bishop.png').convert_alpha()
            elif type == 'rook':
                self.image = pygame.image.load('gameasset/White/white_rook.png').convert_alpha()
            elif type == 'queen':
                self.image = pygame.image.load('gameasset/White/white_queen.png').convert_alpha()
            else: # 'king'
                self.image = pygame.image.load('gameasset/White/white_king.png').convert_alpha()
        else: # black
            if type == 'pawn':
                self.image = pygame.image.load('gameasset/Black/black_pawn.png').convert_alpha()
            elif type == 'knight':
                self.image = pygame.image.load('gameasset/Black/black_knight.png').convert_alpha()
            elif type == 'bishop':
                self.image = pygame.image.load('gameasset/Black/black_bishop.png').convert_alpha()
            elif type == 'rook':
                self.image = pygame.image.load('gameasset/Black/black_rook.png').convert_alpha()
            elif type == 'queen':
                self.image = pygame.image.load('gameasset/Black/black_queen.png').convert_alpha()
            else: # 'king'
                self.image = pygame.image.load('gameasset/Black/black_king.png').convert_alpha()
        
        self.rect = self.image.get_rect(topleft = pos)
        

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
                
def draw_pieces():
    for y in range(8): # col
        for x in range(8): # row
            if y == 1: # black pawns
                all_pieces.add(Pieces('pawn', 'black', (x * 80, 80)))
            elif y == 6: # white pawns
                all_pieces.add(Pieces('pawn', 'white', (x * 80, 480)))
                
            
                
            if y == 0:
                if x == 0 or x == 7: all_pieces.add(Pieces('rook', 'black', (x * 80, y * 80))) # black rook
                if x == 1 or x == 6: all_pieces.add(Pieces('knight', 'black', (x * 80, y * 80))) # black horse
                if x == 2 or x == 5: all_pieces.add(Pieces('bishop', 'black', (x * 80, y * 80))) # black bishop
                if x == 3: all_pieces.add(Pieces('queen', 'black', (x * 80, y * 80))) # black queen
                if x == 4: all_pieces.add(Pieces('king', 'black', (x * 80, y * 80))) # black king
                
            if y == 7:
                if x == 0 or x == 7: all_pieces.add(Pieces('rook', 'white', (x * 80, y * 80))) # white rook
                if x == 1 or x == 6: all_pieces.add(Pieces('knight', 'white', (x * 80, y * 80))) # white horse
                if x == 2 or x == 5: all_pieces.add(Pieces('bishop', 'white', (x * 80, y * 80))) # white bishop
                if x == 3: all_pieces.add(Pieces('queen', 'white', (x * 80, y * 80))) # white queen
                if x == 4: all_pieces.add(Pieces('king', 'white', (x * 80, y * 80))) # white king
                
            
                

# Init Pieces
all_pieces = pygame.sprite.Group()
selected_piece = pygame.sprite.GroupSingle()


# pygame setup
pygame.init()
screen = pygame.display.set_mode((640, 640)) # 640 640 
clock = pygame.time.Clock()
dt = 0

# Add Pieces (Add Function or For Loop w/Logic)
draw_pieces()
# all_pieces.add(Pieces("pawn", "white", (0 * 80, 6 * 80)))
# all_pieces.add(Pieces("pawn", "white", (1 * 80, 6 * 80)))
# all_pieces.add(Pieces("knight", "black", (0 * 80, 6 * 80)))

dragging = False

while True:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        
        if event.type == pygame.MOUSEBUTTONDOWN: # Press On Piece
            for piece in all_pieces:
                if piece.rect.collidepoint(event.pos):
                    selected_piece.add(piece)
                    dragging = True
            
                
        if event.type == pygame.MOUSEBUTTONUP and dragging: # Drop
            if selected_piece.sprite:
                x, y = event.pos
                col, row = x // 80, y // 80 # Double // for division + floor
                selected_piece.sprite.rect.topleft = (col * 80, row * 80)
            selected_piece.empty()
            dragging = False
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                all_pieces.empty()
                draw_pieces()
            
    if dragging and selected_piece.sprite:
        selected_piece.sprite.rect.center = pygame.mouse.get_pos()
            
    draw_chess_board()
    all_pieces.draw(screen)
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

