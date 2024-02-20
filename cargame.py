import pygame 
import random 
 
pygame.init() 
 
WIDTH, HEIGHT = 800, 600 
FPS = 60 
 
screen = pygame.display.set_mode((WIDTH, HEIGHT)) 
pygame.display.set_caption("Car Race Game") 
 
WHITE = (255, 255, 255) 
RED = (255, 0, 0) 
 
player_car = pygame.Rect(WIDTH // 2, HEIGHT - 100, 50, 80) 
enemy_cars = []  
enemy_speed = 5 
score = 0 
 
clock = pygame.time.Clock() 

running = True 
while running: 
    screen.fill(WHITE) 
 
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT: 
            running = False 
 
    keys = pygame.key.get_pressed() 
    if keys[pygame.K_LEFT] and player_car.x > 0: 
        player_car.x -= 5 
    if keys[pygame.K_RIGHT] and player_car.x < WIDTH - player_car.width: 
        player_car.x += 5 
 
    if len(enemy_cars) < 3: 
        enemy_cars.append(pygame.Rect(random.randint(0, WIDTH-50),  
                                      random.randint(-150, -50), 50, 80)) 
 
    for car in enemy_cars: 
        car.y += enemy_speed 
        pygame.draw.rect(screen, RED, car) 
 
        if car.colliderect(player_car): 
            print("Game Over") 
            running = False 
 
        if car.y > HEIGHT: 
            enemy_cars.remove(car) 
            score += 1 
 
    pygame.draw.rect(screen, (0, 128, 0), player_car) 
    pygame.display.flip() 
    clock.tick(FPS) 
 
pygame.quit()