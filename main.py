import random
import pygame

from config import *
from sorts import *

def datagen():
    data = [[i,'white'] for i in range(1,n+1)]
    random.shuffle(data)
    return data

def animate(datalist):
    pygame.init()
    clk = pygame.time.Clock()
    dis = pygame.display.set_mode((w,h))
    running = True

    while running:
        for data in datalist:
            dis.fill('black')

            for i in range(n):
                pygame.draw.rect(dis,data[i][1],[i*(w/n),h-(h/n)*data[i][0],(w/n),(h/n)*data[i][0]])
            
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
                    pygame.quit()
                    return
            clk.tick(fps)
        pygame.event.wait()

algos = [bubble]

def main():
    data = datagen()

    algo = int(input('\nAlgorithms:\n1. Bubble\nEnter choice:'))

    datalist = algos[algo-1](data)
    animate(datalist)

if __name__ == "__main__":
    main()