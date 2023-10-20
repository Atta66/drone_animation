import pygame
import numpy as np

from drone_instance import drone_instance

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

font = pygame.font.Font(None, 22)

# for probabilities comparison

compare_prob = []

# x,y, prob values to initiate drone

compare_prob.append((3, 8, 1))

# regions of interest - dead ends

dead_end = {

    (0,4):-1,
    (2,2):-1,
    (3,0):-1,
    (6,0):-1,
    (8,2):-1
}

coordinate_prob = {

    # probability 1
    (3,0):1, (3,2):1, (3,4):1,
    (3,5):1, (3,6):1, (3,7):1,
    (3,8):1,
    (0,4):1,
    (1,4):1,
    (5,2):1,
    (6,4):1, (6,2):1, (6,0):1,
    (8,2):1,
    
    # probability 0
    (2,7):0, (2,8):0, (2,6):0,
    (2,5):0, (2,3):0, (2,0):0,
    (2,1):0, (2,9):0,
    (3,3):0, (3,9):0,
    (4,7):0, (4,8):0, (4,6):0,
    (4,5):0, (4,3):0, (4,0):0,
    (4,1):0, (4,9):0,
    (1,3):0, (1,1):0, (1,2):0,
    (1,5):0,
    (0,3):0, (0,5):0,
    (5,1):0, (5,3):0, (5,0):0,
    (5,5):0,
    (7,1):0, (7,3):0, (7,0):0,
    (7,4):0, (7,5):0,
    (6,5):0,
    (8,1):0, (8,3):0,

    # inbetween
    (2,4):0.7, (3,3):0.2, (4,4):0.1,
    (2,2):0.7, (4,2):0.1, (3,1):0.2,
    (6,1):0.7, (7,2):0.2, (6,3):0.1,
    (5,4):0.9

}

covered_section = {

    (3,5):0,
    (2,4):0,
    (2,2):0,
    (3,3):0,
    (5,2):0,
    (6,1):0

}

# drone starting pos

drone_start_x = 3
drone_start_y = 8

total_num = 7

CELL_SIZE = 50

WINDOW_SIZE = CELL_SIZE * 9

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

pygame.display.set_caption("Tunnel")

drone = {}

def drone_instanciater(total_num):

    for num in range(total_num):
        
        drone_init = drone_instance(CELL_SIZE)
        drone[f'{num+1}'] = drone_init.start_instance()
        drone[f'd_{num+1}'] = num+1
        # drone[f'prev{num+1}_x'] = drone_start_x
        # drone[f'prev{num+1}_y'] = drone_start_y
        drone[f'drone_rect{num+1}'] = drone_init.create_rect()
        drone[f'{num+1}_ownX'] = 3
        drone[f'{num+1}_ownY'] = 8
        drone[f'{num+1}_coveredX'] = drone[f'{num+1}_ownX']
        drone[f'{num+1}_coveredY'] = drone[f'{num+1}_ownY'] 
        
drone_instanciater(total_num)

done = False

def create_grid():

    screen.fill(WHITE)

    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):

            # Customize grid

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            font = pygame.font.Font(None, 22)
            text_surface = font.render(str(int(x/50))+","+str(int(y/50)), True, (0, 0, 0))
            text_rect = text_surface.get_rect()
            text_rect.center = rect.center
            screen.blit(text_surface, text_rect)

            if x == CELL_SIZE * 3:

                pygame.draw.rect(
                    screen, GREY, [x, y, CELL_SIZE, CELL_SIZE])
                

                pygame.draw.rect(
                    screen, BLACK, [x, y, CELL_SIZE, CELL_SIZE], 1)

            if x == CELL_SIZE * 6:

                excluded_grid = [250, 300, 350, 400]


                if y in excluded_grid:
                    continue

                pygame.draw.rect(
                    screen, GREY, [x, y, CELL_SIZE, CELL_SIZE])
                
                pygame.draw.rect(
                    screen, BLACK, [x, y, CELL_SIZE, CELL_SIZE], 1)
                
            if y == CELL_SIZE * 2:

                excluded_grid = [0, 50]

                if x in excluded_grid:
                    continue 

                pygame.draw.rect(
                    screen, GREY, [x, y, CELL_SIZE, CELL_SIZE])
                pygame.draw.rect(
                    screen, BLACK, [x, y, CELL_SIZE, CELL_SIZE], 1)
                
            if y == CELL_SIZE * 2 or y == CELL_SIZE * 4:

                excluded_grid = [350, 400]

                if x in excluded_grid:
                    continue 

                pygame.draw.rect(
                    screen, GREY, [x, y, CELL_SIZE, CELL_SIZE])
                
                pygame.draw.rect(
                    screen, BLACK, [x, y, CELL_SIZE, CELL_SIZE], 1)
                  
            if x == CELL_SIZE * drone_start_x and y == CELL_SIZE * drone_start_y: 
                
                for num in range(total_num):

                    drone[f'drone_rect{num+1}'].center = (x + CELL_SIZE / 2, y + CELL_SIZE / 2)
                    screen.blit(drone[f'{num+1}'], drone[f'drone_rect{num+1}']) 

            # else:
            #     pygame.draw.rect(
            #         screen, BLACK, [x, y, CELL_SIZE, CELL_SIZE], 1)
    
    pygame.display.update([0, 0, WINDOW_SIZE, WINDOW_SIZE])

    pygame.time.delay(1000)

def check_prob(x, y):

    if coordinate_prob[(x,y)] > 0:

        compare_prob.append((x, y, coordinate_prob[(x,y)]))

junction_coord = [(3,4), (6,2), (3,2), (6,4)]

def move_drone(num, compare_prob):

    # extract max prob from compare_prob and then use the x, y coordinates corresponding to max prob

    max_prob = max(compare_prob, key=lambda x: x[2])

    x = max_prob[0]
    y = max_prob[1]

    print("probabilities > 0 at current location: ", compare_prob)

    print("of which max belongs to coordinates: (%d,%d)" % (x,y))

    if (x,y) in covered_section and covered_section[(x,y)] == 0:
        covered_section[(x,y)] = 1

    
        
    pygame.draw.rect(screen, GREY, [drone[f'{num}_ownX'] * CELL_SIZE, drone[f'{num}_ownY'] * CELL_SIZE, CELL_SIZE, CELL_SIZE])
    pygame.draw.rect(
                    screen, BLACK, [drone[f'{num}_ownX'] * CELL_SIZE, drone[f'{num}_ownY'] * CELL_SIZE, CELL_SIZE, CELL_SIZE], 1)
    
    pygame.display.update([drone[f'{num}_ownX'] * CELL_SIZE, drone[f'{num}_ownY'] * CELL_SIZE, CELL_SIZE, CELL_SIZE])
    
    # pygame.time.delay(2000)

    # grid coordinates    
    x_pixel = x * CELL_SIZE
    y_pixel = y * CELL_SIZE

    # Set the center of the image rect to the center of the cell
    drone[f'drone_rect{num}'].center = (x_pixel + CELL_SIZE / 2, y_pixel + CELL_SIZE / 2)

    # Draw image on screen
    screen.blit(drone[f'{num}'], drone[f'drone_rect{num}'])

    drone[f'{num}_ownX'] = x
    drone[f'{num}_ownY'] = y

    pygame.display.flip()

    if (x,y) in junction_coord:
        print("junction with x,y: (%d,%d)" % (x,y))

    elif (x, y) in dead_end:
        print("dead_end with x,y: (%d,%d)" % (x, y))

    else:
        print("current x,y: (%d,%d)" % (x,y))

    pygame.time.delay(500)

    return max_prob[0], max_prob[1]



def search_find(own_x, own_y, covered_x, covered_y, drone):

    for x in range(own_x-1, own_x+2, 1):

        for y in range(own_y-1, own_y+2, 1):

            if x == 5 and y == 4:
                print(coordinate_prob)
                print(covered_section)

            if (own_x, own_y) in junction_coord and (x,y) in covered_section and covered_section[(x,y)] ==1:
                coordinate_prob[(x,y)] = 0.01
            
            if (x,y) == (own_x, own_y):
                continue

            # out of displayed grid
            elif x < 0 or y < 0 or x > 8 or y > 8:
                continue
            
            # in case we are at the dead end: previous pos's probability is important and should not be ignored
            elif (own_x, own_y) in dead_end and (x,y) == (covered_x, covered_y):
                check_prob(x,y)


            # to keep going in same direction 
            elif (x,y) == (covered_x, covered_y):
                continue

            # at junction check which section has been covered
            # elif (x,y) in covered_section and covered_section[(x,y)] == 1 and (own_x,own_y) in junction_coord:
            #     continue

            else:
                check_prob(x,y)

    # important to know which direction the drone is moving
    covered_x, covered_y = own_x, own_y

    # update self pos
    own_x, own_y = move_drone(drone,compare_prob)

    compare_prob.clear()

    return own_x, own_y, covered_x, covered_y


if not done:

    create_grid()

    # leader = 1
    # follower = leader + 1

    # place drones on grid

    move_drone(1, compare_prob)

    # for drone_placer in range(total_num):
    #     move_drone(drone_placer+1, compare_prob)

    # print(drone)

    # current position



    # own_x = 3
    # own_y = 8
    # covered_x = own_x
    # covered_y = own_y

    drone_inGrid = 1
    grid_step = 0

    while(True):

        for uav in range(drone_inGrid):
            uav += 1
            print(uav)
            drone[f'{uav}_ownX'], drone[f'{uav}_ownY'], drone[f'{uav}_coveredX'], drone[f'{uav}_coveredY'] = search_find(drone[f'{uav}_ownX'],drone[f'{uav}_ownY'],
                                                                             drone[f'{uav}_coveredX'], drone[f'{uav}_coveredY'],
                                                                             drone[f'd_{uav}'])
        
        grid_step += 1

        if grid_step % 2 == 0:
            drone_inGrid += 1
            # print(drone_inGrid)

            if drone_inGrid == 8:
                drone_inGrid = 7


            
        


        # drone['1_ownX'], drone['1_ownY'], drone['1_coveredX'], drone['1_coveredY'] = search_find(drone['1_ownX'],drone['1_ownY'],
        #                                                                      drone['1_coveredX'], drone['1_coveredY'],
        #                                                                      drone['d_1'])
        # grid_step += 1
        

        # if grid_step % 2 == 0:

        #     follower += 1

            
        
        #       drone[f'{num+1}_ownX'], drone[f'{num+1}_ownY'],
        # drone[f'{num+1}_coveredX'], drone[f'{num+1}_coveredX'] = search_find(drone[f'{num}_ownX'],drone[f'{num+1}_ownY'],
        #                                                                      drone[f'{num}_coveredX'], drone[f'{num+1}_coveredY'],
        #                                                                      drone[f'{num}'])

# the first time 3,8 is already in the dictionary that is why the drone moves to 3, 8 (stays in the same square)
