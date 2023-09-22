import pygame

from drone_instance import drone_instance

pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (128, 128, 128)


# drone starting pos

drone_start_x = 3
drone_start_y = 8

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
        drone[f'prev{num+1}_x'] = drone_start_x
        drone[f'prev{num+1}_y'] = drone_start_y
        drone[f'drone_rect{num+1}'] = drone_init.create_rect()
        
drone_instanciater(total_num)

done = False

def create_grid():

    screen.fill(WHITE)

    for x in range(0, WINDOW_SIZE, CELL_SIZE):
        for y in range(0, WINDOW_SIZE, CELL_SIZE):

            # Customize grid

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


def move_drone(num, x, y):

    pygame.draw.rect(screen, GREY, [drone[f'prev{num}_x'] * CELL_SIZE, drone[f'prev{num}_y'] * CELL_SIZE, CELL_SIZE, CELL_SIZE])
    pygame.draw.rect(
                    screen, BLACK, [drone[f'prev{num}_x'] * CELL_SIZE, drone[f'prev{num}_y'] * CELL_SIZE, CELL_SIZE, CELL_SIZE], 1)
    
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

    if x == 3 and y == 2 or x == 3 and y == 4:

        return True
    
    else:
        
        return False


def update_weights():

    return None


def check_pos():

    return None

end = 8
start_drone2 = 0

if not done:

    create_grid()

    leader = 1

    follower = leader + 1


    for move in range(7, -1, -1):

        if move_drone(leader, 3, move) == True:
            print("at junction")
            leader += 1
        
        else:
            pass



        if start_drone2 == 0:

            move_drone(follower, 3, 8)
            start_drone2 += 1

        if abs(drone[f'prev{leader}_y'] - drone[f'prev{follower}_y']) > 2:
           
           print(abs(drone[f'prev{leader}_y'] - drone[f'prev{follower}_y']))

           move_drone(2, 3, drone[f'prev{leader}_y']+2)

        if drone[f'prev{leader}_y'] == 0:
            break

    
    

