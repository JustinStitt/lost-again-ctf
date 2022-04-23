import sys, os
import util
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide" # suppress pygame output on launch
import pygame
pygame.init()
screen = pygame.display.set_mode((800, 800))
cell_size = 100
dims=8
bgs = {}
all_data = None

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP:
            handle_mouse_click()

def handle_mouse_click():
    global bgs
    bgs = {}
    pos = pygame.mouse.get_pos()
    r = pos[1] // cell_size
    c = pos[0] // cell_size
    bgs[(r, c)] = (0, 0, 255)
    res = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    for (ro, co) in res:
        bgs[(r+ro, c+co)] = (23, 55, 211//2)
    neighbours = util.get_neighbours(all_data[c+r*8])
    print(neighbours)

def draw(data):
    global all_data
    all_data = data
    check_events()
    screen.fill((42, 42, 42))
    draw_cells(data)
    pygame.display.flip()

def draw_cells(data):
    global bgs
    font = pygame.font.SysFont('arial', int(cell_size*.12))
    r, c = (0, 0)
    for d in data:
        background = bgs.get((c, r), (42, 42, 42))
        pygame.draw.rect(screen, background, (r*cell_size, c*cell_size, cell_size, cell_size))
        pygame.draw.rect(screen, (255, 0, 0), (r*cell_size, c*cell_size, cell_size, cell_size), 1)
        text = font.render(d, True, (0, 255, 0))
        text_rect = text.get_rect(center=(r*cell_size+cell_size/2, c*cell_size+cell_size/2))
        screen.blit(text, text_rect)
        r += 1
        if r%dims == 0 and r > 0: c += 1; r = 0