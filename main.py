import random
import pygame
import argparse
from copy import deepcopy
from config import *
from sorts import *

ap = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter,conflict_handler="resolve")

ap.add_argument(dest='algo',nargs='?',
                choices={'bubble','selection','insertion'},
                help='sort algorithm to use')
ap.add_argument('-n',
                type=int,default=n,
                help='number of elements to sort')
ap.add_argument('-w','--width',
                type=int,default=w,
                help='window width')
ap.add_argument('-h','--height',
                type=int,default=h,
                help='window height')
ap.add_argument('--fps',
                type=int,default=fps,
                help='animation frame rate')

args = ap.parse_args()

algo = args.algo
n = args.n
w = args.width
h = args.height
fps = args.fps

#generate shuffled list
def datagen():
    data = [[i+1, 'white'] for i in range(n)]
    random.shuffle(data)
    return data

#animate the sorting
def animate(algo, data):
    pygame.init()
    clk = pygame.time.Clock()
    dis = pygame.display.set_mode((w, h))
    running = True

    while running:
        animation = algo(deepcopy(data))
        for frame in animation:
            dis.fill('black')

            #drawing rectangles for the data
            for i in range(n):
                pygame.draw.rect(
                    dis, frame[i][1],
                    (
                        i*(w/n),                #bar top left corner x-coordinate
                        h-(h/n)*frame[i][0],    #bar top left corner y-coordinate
                        (w/n),                  #bar width
                        (h/n)*frame[i][0]       #bar height
                    )
                )
            
            pygame.display.flip()   #update the display

            for event in pygame.event.get():
                if event.type==pygame.QUIT:
                    running = False
                    pygame.quit()
                    return

            if fps:
                clk.tick(fps)
            else:
                pygame.event.wait()
                for event in pygame.event.get():
                    if event.type==pygame.QUIT:
                        running = False
                        pygame.quit()
                        return
                pygame.event.wait()
        pygame.event.wait()

def main():
    data = datagen()

    algo = args.algo

    if algo:
        algo = globals()[algo]
    else:
        algos = [bubble, selection, insertion]      #list of available algorithms
        algo = int(input(
            'Algorithms:\n'
            '1. Bubble\n'
            '2. Selection\n'
            '3. Insertion\n'
            'Enter choice(0 to exit):'
        ))
        if algo in range(1, len(algos)+1):
            algo = algos[algo-1]
        else:
            exit()
    
    animate(algo, data)

if __name__ == "__main__":
    main()
