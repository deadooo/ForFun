# Example file showing a circle moving on screen
import pygame
from sys import exit


class Pieces(pygame.sprite.Sprite):
    def __init__(self, type, color, pos):
        super().__init__()
        self.pos = pos
        self.type = type
        self.color = color
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
                print()
            elif y == 6: # white pawns
                all_pieces.add(Pieces('pawn', 'white', (x * 80, 480)))
                print()
                
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
   
turn = 0 # 0 White / 1 BLACK           
def valid_move(sel_sprite, all_sprites):
    pre_x, pre_y = 0, 0
    cur_x, cur_y = sel_sprite.pos # Target Pos
    pre_x = (prev_pos[0] // 80) * 80
    pre_y = (prev_pos[1] // 80) * 80
    print(f'current x:{cur_x}')
    print(f'current y:{cur_y}')
    print(f'previous x:{pre_x}')
    print(f'previous y:{pre_y} \n')
    # black = blue
    # white = red
    print(f'this is pre_y in valid_move:{pre_y}')
    if sel_sprite.color == 'white' and turn == 0:
        if sel_sprite.type == 'pawn':
            if cur_x == pre_x: # FORWARD ONLY
                if pre_y == 480 and cur_y == 320:  # en passant (pawn special move)
                    print("ENPASSFUCKER")
                    
                    return occupied((pre_x,pre_y), sel_sprite, all_sprites)
                    
                elif pre_y - cur_y == 80:
                    print("Normie move\n")
                    return occupied((pre_x,pre_y), sel_sprite, all_sprites)
                    
            elif cur_x == pre_x + 80 or cur_x == pre_x - 80 and abs(pre_y - cur_y) == 80: # EAT, check for collison
                print(sel_sprite.pos) 
                print("PUT HERE EAT")
                for sprite in all_sprites:
                    print("Test")
                    if sprite.rect.topleft == sel_sprite.pos:
                        if sprite.color == 'black':
                            sprite.kill()
                            selected_piece.sprite.rect.topleft = (sprite.pos)
                            selected_piece.empty()
                            return True, True
                print(turn)
                return False, False
                
        elif sel_sprite.type == 'rook':
            if cur_x == pre_x or cur_y == pre_y: # UP DOWN or LEFT RIGHT
                print(sel_sprite.color)
                return occupied((pre_x,pre_y), sel_sprite, all_sprites)
        
        elif sel_sprite.type == 'knight':
            if abs(pre_x - cur_x) == 160 and abs(pre_y - cur_y) == 80:
                return occupied((pre_x,pre_y), sel_sprite, all_sprites)
            elif abs(pre_x - cur_x) == 80 and abs(pre_y - cur_y) == 160:
                return occupied((pre_x,pre_y), sel_sprite, all_sprites)
    
        elif sel_sprite.type == 'bishop':
            print(abs(pre_x - cur_x) == abs(pre_y - cur_y))
            if abs(pre_x - cur_x) == abs(pre_y - cur_y):
                return occupied((pre_x,pre_y), sel_sprite, all_sprites)
        
    elif sel_sprite.color == 'black' and turn == 1:
        if sel_sprite.type == 'pawn':
            if cur_x == pre_x: # FORWARD ONLY
                if pre_y == 80 and cur_y == 240:  # en passant (pawn special move)
                    print("ENPASSFUCKER")
                    return occupied((pre_x,pre_y), sel_sprite, all_sprites)
                elif cur_y - pre_y == 80:
                    print("Normie move")
                    return occupied((pre_x,pre_y), sel_sprite, all_sprites)
                else: return False, False
            elif cur_x == pre_x - 80 or cur_x == pre_x + 80 and abs(pre_y - cur_y):
                for sprite in all_sprites:
                    if sprite.rect.topleft == sel_sprite.pos:
                        if sprite.color == 'white':
                            sprite.kill()
                            selected_piece.sprite.rect.topleft = (sprite.pos)
                            selected_piece.empty()
                            return True, True
                print(turn)
                return False, False
                
        elif sel_sprite.type == 'rook': # UP DOWN or LEFT RIGHT
            if cur_x == pre_x or cur_y == pre_y:   
                print(sel_sprite.color)     
                return occupied((pre_x,pre_y), sel_sprite, all_sprites)
            
        elif sel_sprite.type == 'knight':
            if abs(pre_x - cur_x) == 160 and abs(pre_y - cur_y) == 80:
                return occupied((pre_x,pre_y), sel_sprite, all_sprites)
            elif abs(pre_x - cur_x) == 80 and abs(pre_y - cur_y) == 160:
                return occupied((pre_x,pre_y), sel_sprite, all_sprites)

        elif sel_sprite.type == 'bishop':
            if abs(pre_x - cur_x) == abs(pre_y - cur_y):
                return occupied((pre_x,pre_y), sel_sprite, all_sprites)
            
        
    return False, False

def occupied(prev_pos, sel_sprites, all_sprites):
    prev_x, prev_y = prev_pos
    cur_x, cur_y = sel_sprites.pos
    print(sel_sprites.type)
    print('\n\n\n')
    print(f'this is prev_pos:{prev_pos} \nthis is cur_pos:{sel_sprites.pos}')
    print(f'this is the minus: {abs(prev_x - cur_x)}, {abs(prev_y - cur_y)}')
    print(turn)
    if sel_sprites.color == 'white':
        if sel_sprites.type == 'pawn':
            while prev_y != cur_y - 80: # 480:320, 400:320, 320:320
                for sprite in all_sprites:
                    if sprite.rect.topleft == prev_pos:
                        return False, False
                prev_pos = (prev_x, prev_y - 80)
                prev_y -= 80
            return True, False
        elif sel_sprites.type == 'rook':
            if prev_y > cur_y: # bottom to top
                while prev_y != cur_y - 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'black':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x, prev_y - 80)
                    prev_y -= 80
            elif prev_y < cur_y: # top to bottom
                while prev_y != cur_y + 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'black':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x, prev_y + 80)
                    prev_y += 80
            elif prev_x > cur_x: # right to left
                while prev_x != cur_x - 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'black':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x - 80, prev_y)
                    prev_x -= 80
            elif prev_x < cur_x: # left to right
                while prev_x != cur_x + 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'black':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x + 80, prev_y)
                    prev_x += 80
        elif sel_sprites.type == 'knight':
            for sprite in all_sprites:
                if sprite.rect.topleft == sel_sprites.pos:
                    if sprite.color == 'black':
                        sprite.kill()
                        return True, False
            return True, False   
        elif sel_sprites.type == 'bishop':
            if prev_y > cur_y and prev_x < cur_x: # up right
                while prev_y != cur_y - 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'black':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x + 80, prev_y - 80)
                    prev_x += 80
                    prev_y -= 80
            elif prev_y > cur_y and prev_x > cur_x: # up left
                while prev_y != cur_y - 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'black':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x - 80, prev_y - 80)
                    prev_x -= 80
                    prev_y -= 80
            
            elif prev_y < cur_y and prev_x < cur_x: # down right
                while prev_y != cur_y + 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'black':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x + 80, prev_y + 80)
                    prev_x += 80
                    prev_y += 80
            
            elif prev_y < cur_y and prev_x > cur_x: # down left
                while prev_y != cur_y + 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'black':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x - 80, prev_y + 80)
                    prev_x -= 80
                    prev_y += 80        
        
    elif sel_sprites.color == 'black':
        if sel_sprites.type == 'pawn':
            print(prev_y)
            print(cur_y)
            while prev_y != cur_y + 80:
                # print("check b")
                for sprite in all_sprites:
                    if sprite.rect.topleft == prev_pos:
                        return False, False
                prev_pos = (prev_x, prev_y + 80)
                prev_y += 80
        elif sel_sprites.type == 'rook':
            if prev_y > cur_y: # bottom to top
                while prev_y != cur_y - 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'white':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x, prev_y - 80)
                    prev_y -= 80
            elif prev_y < cur_y: # top to bottom
                while prev_y != cur_y + 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'white':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x, prev_y + 80)
                    prev_y += 80
            elif prev_x > cur_x: # right to left
                while prev_x != cur_x - 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'white':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x - 80, prev_y)
                    prev_x -= 80
            elif prev_x < cur_x: # left to right
                while prev_x != cur_x + 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'white':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x + 80, prev_y)
                    prev_x += 80
        elif sel_sprites.type == 'knight':
            for sprite in all_sprites:
                if sprite.rect.topleft == sel_sprites.pos:
                    if sprite.color == 'white':
                        sprite.kill()
                        return True, False
            return True, False
        elif sel_sprites.type == 'bishop':
            if prev_y > cur_y and prev_x < cur_x: # up right
                while prev_y != cur_y - 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'white':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x + 80, prev_y - 80)
                    prev_x += 80
                    prev_y -= 80
            elif prev_y > cur_y and prev_x > cur_x: # up left
                while prev_y != cur_y - 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'white':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x - 80, prev_y - 80)
                    prev_x -= 80
                    prev_y -= 80
            
            elif prev_y < cur_y and prev_x < cur_x: # down right
                while prev_y != cur_y + 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'white':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x + 80, prev_y + 80)
                    prev_x += 80
                    prev_y += 80
            
            elif prev_y < cur_y and prev_x > cur_x: # down left
                while prev_y != cur_y + 80:
                    for sprite in all_sprites:
                        if sprite.rect.topleft == prev_pos:
                            if sprite.color == 'white':
                                sprite.kill()
                                selected_piece.sprite.rect.topleft = (sprite.pos)
                                selected_piece.empty()
                                return True, True
                            return False, False
                    prev_pos = (prev_x - 80, prev_y + 80)
                    prev_x -= 80
                    prev_y += 80
    return True, False  
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

dragging = False
prev_pos = (0,0)


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
                    prev_pos = event.pos
            
                
        if event.type == pygame.MOUSEBUTTONUP and dragging: # Drop
            x, y = event.pos
            valid = False
            consume = False 
            
            if selected_piece.sprite and (x >= 0 and x <= 640) and (y >= 0 and y <= 640): # Grid Barrier
                col, row = x // 80, y // 80 # Double // for division + floor
                selected_piece.sprite.pos = (col * 80, row * 80)
                valid, consume = valid_move(selected_piece.sprite, all_pieces)
                # I know i can just put it in like another thing like pp = selected but ehhhhhhhhhhhhhh
            else:
                col, row = prev_pos[0] // 80, prev_pos[1] // 80 # returns to prev pos for Grid Barrier
                
                
            try:
                if consume == False: # replace with not
                    if valid:
                        if turn:
                            turn = 0
                        else:
                            turn += 1
                        # selected_piece.sprite.rect.topleft = (0, 0) # Test
                        selected_piece.sprite.rect.topleft = (col * 80, row * 80)
                        selected_piece.empty()
                        dragging = False 
                    else:
                        col, row = prev_pos[0] // 80, prev_pos[1] // 80 # returns to prev pos
                        selected_piece.sprite.rect.topleft = (col * 80, row * 80)
                        selected_piece.empty()
                        
                        # im pretty sure i can just put all of this in valid_move
                else: # consume == True
                    if turn:
                        turn = 0
                    else:
                        turn += 1
                        dragging = False
                    
            except:
                print("STOP")

            
        if event.type == pygame.KEYDOWN: # RESET PIECES POS
            if event.key == pygame.K_SPACE:
                all_pieces.empty()
                draw_pieces()
                turn = 0
            
    if dragging and selected_piece.sprite: # Drags the selected piece
        selected_piece.sprite.rect.center = pygame.mouse.get_pos()
    
    
            
        
            
    draw_chess_board()
    all_pieces.draw(screen)
        
    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    clock.tick(60)

"""
TODOLIST LOL
Rook Eat, remove -+ 80 and implement an if statement with a -+ 80 to check the final piece position if black/white
then eat

Castling when a rook and king kiss
Conditions: King not checked, Rook/King didn't move once!, nothing in the way of king and rook
"""