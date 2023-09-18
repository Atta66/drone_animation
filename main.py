import pygame

from drone_instance import drone_instance

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)

total_num = 2

CELL_SIZE = 50

WINDOW_SIZE = CELL_SIZE * 9

screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE))

pygame.display.set_caption("Tunnel")


drone = {}

def drone_instanciater(total_num):

    for num in range(total_num):
        
        drone_init = drone_instance(CELL_SIZE)
        drone[f'{num+1}'] = drone_init.start_instance()
        drone[f'prev{num+1}_x'] = 4
        drone[f'prev{num+1}_y'] = 8
        drone[f'drone_rect{num+1}'] = drone_init.create_rect()
        
drone_instanciater(total_num)

done = False

def create_grid():

    screen.fill(WHITE)

    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):

            if x == CELL_SIZE * 4:
                pygame.draw.rect(
                    screen, GREY, [x, y, CELL_SIZE, CELL_SIZE])  

            if y == CELL_SIZE * 3:

                pygame.draw.rect(
                    screen, GREY, [x, y, CELL_SIZE, CELL_SIZE])  
            
            if x == CELL_SIZE * 4 and y == CELL_SIZE * 8: 
                
                for num in range(total_num):

                    drone[f'drone_rect{num+1}'].center = (x + CELL_SIZE / 2, y + CELL_SIZE / 2)
                    screen.blit(drone[f'{num+1}'], drone[f'drone_rect{num+1}']) 

            else:
                pygame.draw.rect(
                    screen, BLACK, [x, y, CELL_SIZE, CELL_SIZE], 1)
    
    pygame.display.update([0, 0, WINDOW_SIZE, WINDOW_SIZE])

    pygame.time.delay(1000)


def move_drone(num, x, y):

    pygame.draw.rect(screen, GREY, [drone[f'prev{num}_x'] * CELL_SIZE, drone[f'prev{num}_y'] * CELL_SIZE, CELL_SIZE, CELL_SIZE]) 
    
    pygame.display.update([drone[f'prev{num}_x'] * CELL_SIZE, drone[f'prev{num}_y'] * CELL_SIZE, CELL_SIZE, CELL_SIZE])
    
    pygame.time.delay(1000)

    # pixel coordinates    
    x_pixel = x * CELL_SIZE
    y_pixel = y * CELL_SIZE

    # Set the center of the image rect to the center of the cell
    drone[f'drone_rect{num}'].center = (x_pixel + CELL_SIZE / 2, y_pixel + CELL_SIZE / 2)

    # Draw image on screen
    screen.blit(drone[f'{num}'], drone[f'drone_rect{num}'])

    drone[f'prev{num}_x'] = x
    drone[f'prev{num}_y'] = y

    pygame.display.flip()

    pygame.time.delay(1000)

    return None

end = 8
start_drone2 = 0

if not done:

    create_grid()


    for move in range(6, -1, -2):

        move_drone(1, 4, move)

        if start_drone2 == 0:

            move_drone(2, 4, 8)
            start_drone2 += 1

        if abs(drone['prev1_y'] - drone['prev2_y']) > 3:
           
           print(abs(drone['prev1_y'] - drone['prev2_y']))

           move_drone(2, 4, drone[f'prev1_y']+3)

        if drone['prev1_y'] == 0:
            break

    
    

