import pygame

class drone_instance:

    def __init__(self, CELL_SIZE):

        self.CELL_SIZE = CELL_SIZE 

        self.drone = None

        # self.drone = pygame.image.load("drone.png") 

        # self.drone = pygame.transform.scale(self.drone, (self.CELL_SIZE, self.CELL_SIZE)) 
                 

    def start_instance(self):
    
        self.drone = pygame.image.load("drone.png") 

        self.drone = pygame.transform.scale(self.drone, (self.CELL_SIZE, self.CELL_SIZE))

        return self.drone
    
    def create_rect(self):

        return self.drone.get_rect()

