import pygame  
import time  
import random                                                                                                                     
pygame.init() 

width=800
height=600


black=(0,0,0)
white=(255,255,255)
red=(200,0,0)
green=(0,200,0)
B_red=(255,0,0)
B_green=(0,255,0)

vel=5
left=False
right=False


win=pygame.display.set_mode((width,height))                                                                                                
pygame.display.set_caption("Alien")
clock=pygame.time.Clock()
carBac=pygame.image.load("A.jpeg")
carBa=pygame.image.load("b.jpeg")
u=pygame.image.load("U.png")
walkRight=[pygame.image.load('R1.png'),pygame.image.load('R2.png'),pygame.image.load('R3.png'),pygame.image.load('R4.png'),pygame.image.load('R5.png'),pygame.image.load('R6.png'),pygame.image.load('R7.png'),pygame.image.load('R8.png'),pygame.image.load('R9.png')]                                                                                           
walkLeft=[pygame.image.load('L1.png'),pygame.image.load('L2.png'),pygame.image.load('L3.png'),pygame.image.load('L4.png'),pygame.image.load('L5.png'),pygame.image.load('L6.png'),pygame.image.load('L7.png'),pygame.image.load('L8.png'),pygame.image.load('L9.png')]            
walkCount=0
char=pygame.image.load('standing.png') 


def things(thingx,thingy):
	win.blit(u,(thingx,thingy))
	
def car(x,y):
	global walkCount 
	if walkCount + 1>=27:
		walkCount = 0
        
	if left:  
		win.blit(walkLeft[walkCount//3], (x,y))
		walkCount += 1                          
	elif right:
		win.blit(walkRight[walkCount//3], (x,y))
		walkCount += 1
	else:
		win.blit(char, (x, y))
		walkCount = 0
        
	pygame.display.update() 
	




def score(count):
	myfont = pygame.font.SysFont('comicsansms', 35)
	textsurface = myfont.render('score: '+str(count), True, (255,242,0))
	win.blit(textsurface,(0,0))


def crash(count):
	

	myfont = pygame.font.SysFont('comicsansms', 90)
	textsurface = myfont.render('Your Score: '+str(count), True, (5, 255, 0))
	
	win.blit(textsurface,(180,300))
	
	pygame.display.update()
	time.sleep(2)
	game_loop()
	pygame.quit()



def game_intro():
	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()
                
		win.blit(carBac,(0,0))
		myfont = pygame.font.SysFont('comicsansms', 90)
		textsurface = myfont.render('ALIENWARE', True, (0,117,210))
		win.blit(textsurface,(width/2-165,height/2-220))

		mouse=pygame.mouse.get_pos()
		click=pygame.mouse.get_pressed()

		if 150+100> mouse[0]>150 and 350+50> mouse[1]> 350:
			pygame.draw.rect(win, B_green,(150,350,100,50))
			if click[0]==1:
				game_loop()
		else:			
			pygame.draw.rect(win, green,(150,350,100,50))
		
		if 550+100> mouse[0]>550 and 350+50> mouse[1]> 350:
			pygame.draw.rect(win, B_red,(550,350,100,50))
			if click[0]==1:
				pygame.quit()
				quit()

		else:
			pygame.draw.rect(win, red,(550,350,100,50))

		myfont = pygame.font.SysFont('comicsansms', 20)
		textsurface = myfont.render('START', True, (0, 0, 0))
		win.blit(textsurface,(170,365))

		myfont = pygame.font.SysFont('comicsansms', 20)
		textsurface = myfont.render('EXIT', True, (0, 0, 0))
		win.blit(textsurface,(570,365))
		
		pygame.display.update()
		clock.tick(15)



def game_loop():
	x=180
	y=520
	crashed=False
	thing_startx=random.randrange(0,width)
	thing_starty=-600
	thing_speed=4
	thing_width=50
	thing_height=100
	count=0

	while not crashed: 
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				 crashed=True

		keys=pygame.key.get_pressed()

		if keys[pygame.K_LEFT] and x>vel: 
			x -= vel
			left=True
			right=False
		elif keys[pygame.K_RIGHT]and x< width-50-vel:
			x += vel
			left=False
			right=True
		else:
			right=False
			left=False
			walkCount=0

		
		win.blit(carBa,(0,0))

		things(thing_startx,thing_starty)
		thing_starty+=thing_speed
		car(x,y)
		
		score(count)

		if x==vel or x==width-50-vel:
			crash(count)

		if thing_starty > height:
			thing_starty =0 - thing_height
			thing_startx=random.randrange(0,width)
			count+=1
			thing_speed+=0.5
		


		if y < (thing_starty + thing_height) and y+ height >= thing_starty + thing_height:
			if x > thing_startx and x < (thing_startx + thing_width) or x + width > thing_startx and x + width < thing_startx + thing_width :
				crash(count)
		


		pygame.display.update()
		clock.tick(60)



game_intro()
game_loop()
pygame.quit()
quit()
