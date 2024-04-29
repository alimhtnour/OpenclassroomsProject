import pygame
import os

Width, Height = 600,600
Rows, Cols = 7,7
Square = Width//Rows
L_screen = 1000
l_screen = 600
White = (255,255,255)

image1 = pygame.transform.scale(pygame.image.load(os.path.join("image/image1.jpg")), (L_screen, l_screen))
'''
image2 = pygame.transform.scale(pygame.image.load(os.path.join("image/image2.jpg")), (Square, Square))
image3 = pygame.transform.scale(pygame.image.load(os.path.join("image/image3.jpg")), (Square, Square))
image4 = pygame.transform.scale(pygame.image.load(os.path.join("image/image4.png")), (Square, Square))
image5 = pygame.transform.scale(pygame.image.load(os.path.join("image/image5.jpg")), (Square, Square))
image6 = pygame.transform.scale(pygame.image.load(os.path.join("image/image6.jpg")), (Square, Square))
'''
IMAGES = []
for i in range(2,7):
	IMAGES.append(pygame.transform.scale(pygame.image.load(os.path.join(f"image/image{i}.jpg")), (Square, Square)))
