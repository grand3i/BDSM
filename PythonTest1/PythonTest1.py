
import pygame
import random
import math
import tkinter as tk

root = tk.Tk()
screensize = (root.winfo_screenwidth(), root.winfo_screenheight())
spielfeld = [0, 0, 0, 0]

if(screensize[0]<screensize[1]): spielfeld = [screensize[0], screensize[0]]
else: spielfeld = [screensize[1], screensize[1], 0, 0]

if(spielfeld[0]%10 != 0): 
    länge = len(str(spielfeld[0]))
    spielfeld[0] -= int(str(spielfeld[0])[länge-1])
    spielfeld[1] -= int(str(spielfeld[1])[länge-1])  #alan

spielfeld[2] = math.floor((screensize[0]-spielfeld[0])/2)
spielfeld[3] = math.floor((screensize[1]-spielfeld[1])/2)
print(screensize)
print(spielfeld)

class Rechteck:
    def __init__(self, position = [0, 0], größe = [ 0, 0], geschwindigkeit = [-5, 5], farbe = [0, 0, 0], mainblock = False):
         self.farbe = farbe
         self.größe = größe
         self.position = position
         self.bewegung = geschwindigkeit 
         self.mainblock = mainblock

         if(mainblock):
            #rechteck = Rechteck(self, [])
             print()
    
    def update(self):
        pos = [spielfeld[2]+self.position[0], spielfeld[1]-self.position[1]]
        pygame.draw.rect(screen, self.farbe, [pos[0], pos[1], self.größe[0], self.größe[1]])

    def änderung(self):
         self.farbe = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
         mov = self.movement
         if self.größe[0] > 1900 : mov[0] = 0
         if self.größe[0] < 0 : mov[1] = 0
         if self.größe[1] > 1000 : mov[0] = 0
         if self.größe[1] < 0 : mov[1] = 0
         self.größe = (self.größe[0] + random.randint(self.movement[0], self.movement[1]), self.größe[1] + random.randint(self.movement[0], self.movement[1]), random.randint(36, 44),  random.randint(36, 44))
         
         pygame.draw.ellipse(screen, self.farbe, self.größe)

pygame.init()
run = True
clock = pygame.time.Clock()


screen = pygame.display.set_mode(screensize)
pygame.display.set_caption("Tetris")

#Aktiv
rechteck = Rechteck([10, 10], [40, 40], [0, 0], [255, 0, 0])

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    
    gedrueckt = pygame.key.get_pressed()
    
    rechteck.update()
    #screen.fill([0, 0, 0])     
    
    pygame.display.update()
    clock.tick(60)

pygame.quit()





