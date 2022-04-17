import pygame

# board dimensions
width=1000
height=1000
rows=10
columns=10
squares_size=width//columns

#color used
white=(255,255,255)
whitegrey=(204, 204, 204)
grey=(70, 70, 70)
black=(0,0,0,0)
red=(255,0,0)

crown=pygame.transform.scale(pygame.image.load("checkers/crown.png"),(44,25))
