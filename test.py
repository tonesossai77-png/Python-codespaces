import pygame
from pygame import draw, display

# Set up pygame window
pygame.init()
window = display.set_mode((600, 600))
display.set_caption("A Very Big House")
window.fill("cyan")

# set up objects
background = pygame.Rect(0, 220, 600, 400)
house = pygame.Rect(90, 180, 300, 400)
door = pygame.Rect(190, 415, 100, 140)
window1 = pygame.Rect(110, 315, 60, 60)
window2 = pygame.Rect(310, 315, 60, 60)
window1_1 = pygame.Rect(110, 315, 30, 60)
window1_2 = pygame.Rect(340, 315, 30, 60)
doorKnob = pygame.Rect(265, 484, 15, 5)
tree=pygame.Rect(470,420,40,150)

# triangle roof (3 points)
roof_points = [(80, 180), (240, 100), (400, 180)]
tree_ponits=[(430, 420), (550, 420), (490, 330)]

# draw house objects
draw.rect(window, "green", background)
draw.rect(window, "pink", house)
draw.rect(window, "black", door)
draw.rect(window, "blue", window1)
draw.rect(window, "blue", window2)
draw.rect(window, "red", doorKnob)
draw.rect(window, "grey", window1_1)
draw.rect(window, "grey", window1_2)
draw.circle(window, "yellow",(500, 80),50 )
draw.rect(window, "brown", tree)
# draw triangle roof
draw.polygon(window, "black", roof_points)
draw.polygon(window, "dark green", tree_ponits)
display.flip()

# update display
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
