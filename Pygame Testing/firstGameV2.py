import pygame

# always need this - initializes game
pygame.init()

# (width, height) of game
size = (screenWidth, screenHeight) = (500, 500)
window = pygame.display.set_mode(size)

pygame.display.set_caption("First Game")

x = 250
y = 490
width = 10
height = 10
velocity = 5

isJump = False
jumpCount = 10

run = True
while run:
  # in ms (1000 = 1s)
  pygame.time.delay(50)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()

  # boundaries added onto movement of box
  if keys[pygame.K_LEFT] and x > 0:
    x -= velocity
  if keys[pygame.K_RIGHT] and (x+width) < screenWidth:
    x += velocity
  if not(isJump):
    if keys[pygame.K_UP] and y > 0 :
      y -= velocity 
    if keys[pygame.K_DOWN] and (y+height) < screenHeight:
      y += velocity
    if keys[pygame.K_SPACE]:
      isJump = True
  else:
    if jumpCount >= -10:
      neg = 1
      if jumpCount < 0:
        neg = -1
      # TODO: Stop jumping from leaving the screen maybe
      y -= (jumpCount ** 2) / 2 * neg
      jumpCount -= 1
    else:
      isJump = False
      jumpCount = 10

  # reset screen
  window.fill((0,0,0))
  # 3rd one is a "Rect" object => x, y, width, height values
  pygame.draw.rect(window, (255, 255, 255), (x, y, width, height))
  # Updates display to show rect
  pygame.display.update()


pygame.quit()