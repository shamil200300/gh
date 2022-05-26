import pygame
import random


pygame.init()
font = pygame.font.SysFont('Arial', 30)


blue = (68,148,74)
black = (0, 0, 0)
red = (255,255,0)
screen_width = 720
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))


snake_x = screen_width / 2
snake_y = screen_height / 2
snake_speed = 30
snake_size = 10
snake_length = 1
snake_blocks = []

fruit_x = 300
fruit_y = 400

speed_x = 0
speed_y = 10

game_over = False

running = True
clock = pygame.time.Clock()


while running:

  if not game_over:
    screen.fill((255,255,255))


    snake_head = []
    snake_head.append(snake_x)
    snake_head.append(snake_y)
    snake_blocks.append(snake_head)


    if len(snake_blocks) > snake_length:
      del snake_blocks[0]

    for block in snake_blocks:
      pygame.draw.rect(screen, blue, [block[0], block[1], snake_size, snake_size])
    pygame.draw.rect(screen, red, [fruit_x, fruit_y, snake_size, snake_size])

    # обновление скорости змецки
    snake_x += speed_x
    snake_y += speed_y

    # увелечение длины змек
    if snake_x == fruit_x and snake_y == fruit_y:
      fruit_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
      fruit_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
      snake_length += 1


    if (snake_x >= screen_width or snake_x < 0 or

      snake_y >= screen_height or snake_y < 0):

        game_over = True


  pygame.display.flip()
  clock.tick(snake_speed)


  for event in pygame.event.get():

    if event.type == pygame.KEYDOWN:

        if event.key == pygame.K_UP:
            speed_x = 0
            speed_y = -10
        if event.key == pygame.K_DOWN:
            speed_x = 0
            speed_y = 10
        if event.key == pygame.K_LEFT:
            speed_y = 0
            speed_x = -10
        if event.key == pygame.K_RIGHT:
            speed_y = 0
            speed_x = 10

    if event.type == pygame.QUIT:

      running = False
