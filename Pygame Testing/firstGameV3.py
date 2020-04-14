import pygame
import os

game_folder = os.path.dirname(__file__)
image_folder = os.path.join(game_folder, "images")
print(image_folder)

# always need this - initializes game
pygame.init()

# (width, height) of game
size = (screenWidth, screenHeight) = (500, 480)
window = pygame.display.set_mode(size)

pygame.display.set_caption("First Game")

# pictures to load in
walkRight = [pygame.image.load(os.path.join(image_folder, 'R1.png')).convert(), pygame.image.load(os.path.join(image_folder, 'R2.png')).convert(),
             pygame.image.load(os.path.join(image_folder, 'R3.png')).convert(), pygame.image.load(os.path.join(image_folder, 'R4.png')).convert(), 
             pygame.image.load(os.path.join(image_folder, 'R5.png')).convert(), pygame.image.load(os.path.join(image_folder, 'R6.png')).convert(),
             pygame.image.load(os.path.join(image_folder, 'R7.png')).convert(), pygame.image.load(os.path.join(image_folder, 'R8.png')).convert(),
             pygame.image.load(os.path.join(image_folder, 'R9.png')).convert()]
walkLeft = [pygame.image.load(os.path.join(image_folder, 'L1.png')).convert(), pygame.image.load(os.path.join(image_folder, 'L2.png')).convert(),
            pygame.image.load(os.path.join(image_folder, 'L3.png')).convert(), pygame.image.load(os.path.join(image_folder, 'L4.png')).convert(), 
            pygame.image.load(os.path.join(image_folder, 'L5.png')).convert(), pygame.image.load(os.path.join(image_folder, 'L6.png')).convert(),
            pygame.image.load(os.path.join(image_folder, 'L7.png')).convert(), pygame.image.load(os.path.join(image_folder, 'L8.png')).convert(),
            pygame.image.load(os.path.join(image_folder, 'L9.png')).convert()]
bg = pygame.image.load(os.path.join(image_folder, 'bg.jpg')).convert()
char = pygame.image.load(os.path.join(image_folder, 'standing.png')).convert()

clock = pygame.time.Clock()

x = 50
y = 400
width = 64
height = 64
velocity = 5

isJump = False
jumpCount = 10

# variables to track walking
left = False
right = False
walkCount = 0

def redrawGameWindow():
  global walkCount
  # reset screen
  window.blit(bg, (0, 0))
  
  # drawing character to the screen
  if walkCount + 1 >= 27:
    walkCount = 0
  if left:
    window.blit(walkLeft[walkCount//3], (x,y))
    walkCount += 1
  elif right:
    window.blit(walkRight[walkCount//3], (x,y))
    walkCount += 1
  else:
    window.blit(char, (x,y))
    walkCount = 0

  # Updates display to show rect
  pygame.display.update()


run = True
while run:
  # clock ticking at 27fps
  clock.tick(27)

  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      run = False

  keys = pygame.key.get_pressed()

  # boundaries added onto movement of box
  if keys[pygame.K_LEFT] and x > 0:
    x -= velocity
    left = True
    right = False
  elif keys[pygame.K_RIGHT] and (x+width) < screenWidth:
    x += velocity
    left = False
    right = True
  else:
    left = False
    right = False
    walkCount = 0

  if not(isJump):
    if keys[pygame.K_SPACE]:
      isJump = True
      right = False
      left = False
      walkCount = 0
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

  redrawGameWindow()


pygame.quit()