import pygame
from sys import exit
import os

pygame.display.init()
pygame.font.init()
F = pygame.font.SysFont('couriernew', 30)
FONT = pygame.font.SysFont('couriernew', 28)
             
pygame.display.set_caption(("SpaceStar"))

capsule1 = pygame.image.load( 'capsule.png')
left_fuel_tank = pygame.image.load('Left fuel tank.png')
right_fuel_tank = pygame.image.load('Right fuel ank.png')
body = pygame.image.load('2nd stage.png')
spacestar = pygame.image.load('SpaceStar.png')
SpaceStar = pygame.transform.scale(spacestar,(250,150))

W, H = 600, 600
screen = pygame.display.set_mode((W, H))
Isp = 4600
Isp2 = 3800
FPS = 5
A = 0
High = 0
Time = 0
Speed = 0
gravity = 10
Q = 80
Throtle = 0
MASS = 1200
Fuel = 8000
Fuel2 = 7200
Mass_of_the_rocket = MASS + Fuel + Fuel2
nd_stage = False
st_stage = True

def Speed_text():
  global Speed
  img = F.render(f"Speed: {round(Speed)} m/s", True, (0, 0, 0))
  screen.blit(img, (0, -1))

def En():
  if nd_stage == True:
      On = F.render("En 2:On", True, (0, 0, 0))
      screen.blit(On, (450, 120))
  elif nd_stage == False:
    On = F.render("En 2:Off", True, (0, 0, 0))
    screen.blit(On, (450, 120))
    
  if st_stage == True:
    On = F.render("En 1:On", True, (0, 0, 0))
    screen.blit(On, (450, 85))
  elif st_stage == False:
    On = F.render("En 1:Off", True, (0, 0, 0))
    screen.blit(On, (450, 85))

def Mass_text():
  global Mass_of_the_rocket
  img3 = F.render(f"Rocket Mass: {Mass_of_the_rocket}", True, (0, 0, 0))
  screen.blit(img3, (0, 69))

def Fuel_text():
  global Fuel
  img1 = F.render(f"1st stage fuel: {round(Fuel)} kg", True, (0, 0, 0))
  screen.blit(img1, (0, 22))

def Fuel2_text():
  global Fuel
  img5 = F.render(f"2nd stage fuel: {round(Fuel2)} kg", True, (0, 0, 0))
  screen.blit(img5, (0, 116))
def High_text():
  global High
  img2 = F.render(f"Height: {round(abs(High))} m", True, (0, 0, 0))
  screen.blit(img2, (0, 46))

def Throtle_text():
  global Throtle
  img4 = F.render(f"Throttle:{Throtle}", True, (0, 0, 0))
  screen.blit(img4, (0, 93))

def Intro():
  global running
  running = True 
  screen.fill((255,255,255))
  screen.blit(SpaceStar,(W//2 -150,0))
  St = F.render("Welcome to the Rocket Simulator",True,(0,0,0))
  screen.blit(St,(20,200))
  pygame.display.update()
  pygame.time.delay(2000)
  St = F.render("Use Up arrow to accelerate",True,(0,0,0))
  screen.blit(St,(40,240))
  pygame.display.update()
  pygame.time.delay(2000)
  St = F.render("Use A/Q to On/Off En 1",True,(0,0,0))
  screen.blit(St,(W//2 - 200,280))
  pygame.display.update()
  pygame.time.delay(2000)
  St = F.render("Use D/E to On/Off En 2",True,(0,0,0))
  screen.blit(St,(W//2 - 200,320))
  pygame.display.update()
  pygame.time.delay(2000)
  St = FONT.render("Shift/Ctr-Increase/Decrease Throttle",True,(0,0,0))
  screen.blit(St,(0,360))
  pygame.display.update()
  pygame.time.delay(2000)
def main():
  global A, High, Time, Speed, Isp, Q, Throtle, MASS, Fuel, Mass_of_the_rocket, st_stage, nd_stage, Fuel2, Isp2
  clock = pygame.time.Clock()
  Start_time = time.time()
  run = True
  while run:
    key = pygame.key.get_pressed()
    A -= gravity
    High -= A
    Speed += A
    screen.fill((0, 40, 120))
    pygame.draw.rect(screen, (150, 150, 150), (0, 0, W-5, 152))
    En()
    screen.blit(body, (W / 2 - 123, H - 208))
    screen.blit(capsule1, (W / 2 - 123, H - 268))
    if not key[pygame.K_SPACE]:
      screen.blit(left_fuel_tank, (W / 2 - 123, H - 268))
      screen.blit(right_fuel_tank, (W / 2 - 123, H - 268))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    
    if key[pygame.K_d]:#___________
      if not Fuel2 <= 0:
        nd_stage = True
        On = F.render("En 2:On", True, (0, 0, 0))
      else:
        Fuel2 = 0
        nd_stage = False
        On = F.render("En 2:Off", True, (0, 0, 0))
        screen.blit(On, (450, 120))
    

    if key[pygame.K_e]:
        nd_stage = False
        On = F.render("En 2:Off", True, (0, 0, 0))
        screen.blit(On, (450, 120))
    
    if key[pygame.K_a]:
        if not Fuel <= 0:
          st_stage = True
          On = F.render("En 1:On", True, (0, 0, 0))
          screen.blit(On, (450, 85))
        else:
            Fuel = 0
            st_stage = False
            On = F.render("En 1:Off", True, (0, 0, 0))
            screen.blit(On, (450, 85))
    
    if key[pygame.K_q]:
        st_stage = False
        On = F.render("En 1:Off", True, (0, 0, 0))
        screen.blit(On, (450, 85))
    if key[pygame.K_LSHIFT]:
      if Throtle != 100:
        Throtle += 2
      else:
          Throtle += 0
       
    if key[pygame.K_LCTRL]:
      if Throtle != 0:
        Throtle -= 2
      else:
        Throtle -= 0

    if key[pygame.K_UP]:
      if nd_stage == True:
        if Fuel2 > 0:
          A += (Isp2 * (Q * (Throtle / 100))) / Mass_of_the_rocket
          A -= gravity
          Mass_of_the_rocket = MASS + Fuel + Fuel2 
          Fuel2 -= Q * (Throtle / 100)
          Speed += A
          High -= A#____

      if st_stage == True:
        if Fuel > 0:
          A += (Isp * (Q * (Throtle / 100))) / Mass_of_the_rocket
          A -= gravity
          Mass_of_the_rocket = MASS + Fuel + Fuel2 
          Fuel -= Q * (Throtle / 100)
          Speed += A
          High -= A#____


    if High > -2:
      Speed = 0
      A = 0
      High = 0
    
    elif Fuel < 0:
      st_stage = False
      Fuel = 0
      Isp = 0
      A -= gravity
    
    elif Fuel2 < 0:
      nd_stage=False
      Fuel2 = 0
      Isp2 = 0
      A -= gravity
    
    pygame.draw.rect(screen, (0, 0, 20),(W // 2 + 180 , (H-200) - High, 80, 50))
    pygame.draw.rect(screen, (0, 100, 0), (pygame.Rect(0, (H - 150) - High, W, 2000)))  #Earth
    pygame.draw.rect(screen, (0, 0, 0), (W // 2 - 25, (H - 240) - High, 10, 90))
    pygame.draw.rect(screen, (0, 0, 0), (175, (H - 170) - High, 55, 20))
    pygame.draw.rect(screen, (0, 0, 0), (W // 2 - 20, (H - 170) - High, 50, 20))
    pygame.draw.rect(screen, (0, 0, 0), (220, (H - 200) - High, 15, 50))
    
    Speed_text()
    Fuel_text()
    High_text()
    Mass_text()
    Throtle_text()
    Fuel2_text()
    pygame.display.update()
    clock.tick(FPS)
if __name__== '__main__':
  Intro()
  main()
