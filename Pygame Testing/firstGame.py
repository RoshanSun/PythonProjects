import pygame

# always need this - initializes game
pygame.init()

# (width, height) of game
size = (width, height) = (500, 500)
window = pygame.display.set_mode(size)

pygame.display.set_caption("First Game")

x = 250
y = 250
width = 10
height = 10
velocity = 5

run = True
while run:
  # in ms (1000 = 1s)
  pygame.time.delay(100)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()

  if keys[pygame.K_LEFT]:
    x -= velocity

  if keys[pygame.K_RIGHT]:
    x += velocity

  if keys[pygame.K_UP]:
    y -= velocity

  if keys[pygame.K_DOWN]:
    y += velocity

  # reset screen
  window.fill((0,0,0))
  # 3rd one is a "Rect" object => x, y, width, height values
  pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
  # Updates display to show rect
  pygame.display.update()


pygame.quit()