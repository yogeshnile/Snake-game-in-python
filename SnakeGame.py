import pygame
import random

pygame.mixer.init()
pygame.init()
pygame.font.init()
white=(255,255,255)
red=(255,0,0)
black=(0,0,0)
blue=(0,0,230)
s_width=900
s_hight=500
gamewindow=pygame.display.set_mode((s_width,s_hight))
pygame.display.set_caption("Snake || Yogesh Nile ||")
gamewindow.fill(white)
image=pygame.image.load("./data/bgimage.jpg")
image=pygame.transform.scale(image,(s_width,s_hight)).convert_alpha()
image_menu=pygame.image.load("./data/menu.jpg")
image_menu=pygame.transform.scale(image_menu,(s_width,s_hight)).convert_alpha()
image_social=pygame.image.load("./data/social.jpg")
image_social=pygame.transform.scale(image_social,(350,45)).convert_alpha()
image_social_1=pygame.image.load("./data/social.jpg")
image_social_1=pygame.transform.scale(image_social_1,(450,40)).convert_alpha()
font=pygame.font.SysFont(None,55)
def screen_score(text,colour,x,y):
	screen_text=font.render(text,True,colour)
	gamewindow.blit(screen_text,[x,y])
snk_list=[]
clock=pygame.time.Clock()
def plot_snake(gamewindow,colour,snk_list,snake_size):
	for x,y in snk_list:
		pygame.draw.rect(gamewindow,white,[x,y,snake_size,snake_size])

def game_menu_play():
	exit_game=False
	gamewindow.fill(white)
	gamewindow.blit(image_menu,(0,0))
	gamewindow.blit(image_social,(0,454))
	screen_score("Wellcome to Snake Game",black,70,80)
	screen_score("-by Yogesh Nile",(128,0,128),260,130)
	pygame.draw.rect(gamewindow,red,[100,270,120,40])
	pygame.draw.rect(gamewindow,red,[400,270,120,40])
	pygame.draw.rect(gamewindow,red,[235,340,150,40])
	screen_score(">Play",white,110,270)
	screen_score("Exit",white,430,270)
	screen_score("Sound",white,265,340)
	pygame.display.update()
	while(1):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					gameloop()
				if event.key==pygame.K_RIGHT:
					game_menu_exit()
				if event.key==pygame.K_DOWN:
					game_menu_sound()

def game_menu_sound():
	exit_game=False
	gamewindow.fill(white)
	gamewindow.blit(image_menu,(0,0))
	gamewindow.blit(image_social,(0,454))
	screen_score("Wellcome to Snake Game",black,70,80)
	screen_score("-by Yogesh Nile",(128,0,128),260,130)
	pygame.draw.rect(gamewindow,red,[100,270,120,40])
	pygame.draw.rect(gamewindow,red,[400,270,120,40])
	pygame.draw.rect(gamewindow,red,[235,340,150,40])
	screen_score("Play",white,130,270)
	screen_score("Exit",white,430,270)
	screen_score(">Sound",white,245,340)
	pygame.display.update()
	while(1):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					pygame.mixer.quit()
				if event.key==pygame.K_RIGHT:
					game_menu_exit()
				if event.key==pygame.K_DOWN:
					game_menu_sound()
				if event.key==pygame.K_LEFT:
					game_menu_play()

def game_menu_exit():
	exit_game=False
	gamewindow.fill(white)
	gamewindow.blit(image_menu,(0,0))
	gamewindow.blit(image_social,(0,454))
	screen_score("Wellcome to Snake Game",black,70,80)
	screen_score("-by Yogesh Nile",(128,0,128),260,130)
	pygame.draw.rect(gamewindow,red,[100,270,120,40])
	pygame.draw.rect(gamewindow,red,[400,270,120,40])
	pygame.draw.rect(gamewindow,red,[235,340,150,40])
	screen_score("Play",white,130,270)
	screen_score(">Exit",white,410,270)
	screen_score("Sound",white,265,340)
	pygame.display.update()
	while (1):
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					pygame.quit()
					quit()
				if event.key==pygame.K_LEFT:
					game_menu_play()
				if event.key==pygame.K_DOWN:
					game_menu_sound()
def ending(e_score):
	exit_game=False
	wellcome_sound=pygame.mixer.music.load('./data/quincas_moreira_scratch_the_itch_hip_hop_rap.mp3')
	wellcome_sound=pygame.mixer.music.play()
	gamewindow.fill(white)
	gamewindow.blit(image_menu,(0,0))
	gamewindow.blit(image_social,(0,454))
	screen_score("Game Over! Press Enter",black,70,80)
	screen_score("Score: "+str(e_score),(0,0,204),200,130)
	pygame.draw.rect(gamewindow,red,[100,270,120,40])
	pygame.draw.rect(gamewindow,red,[400,270,120,40])
	pygame.draw.rect(gamewindow,red,[235,340,150,40])
	screen_score(">Play",white,110,270)
	screen_score("Exit",white,430,270)
	screen_score("Sound",white,265,340)
	pygame.display.update()
	clock.tick(50)
	while not exit_game:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					gameloop()
				if event.key==pygame.K_LEFT:
					game_menu_play()
				if event.key==pygame.K_RIGHT:
					game_menu_exit()
				if event.key==pygame.K_DOWN:
					game_menu_sound()

def wellcome():
	exit_game=False
	wellcome_sound=pygame.mixer.music.load('./data/quincas_moreira_scratch_the_itch_hip_hop_rap.mp3')
	wellcome_sound=pygame.mixer.music.play()
	gamewindow.fill(white)
	gamewindow.blit(image_menu,(0,0))
	gamewindow.blit(image_social,(0,454))
	screen_score("Wellcome to Snake Game",black,70,80)
	screen_score("-by Yogesh Nile",(128,0,128),260,130)
	pygame.draw.rect(gamewindow,red,[100,270,120,40])
	pygame.draw.rect(gamewindow,red,[400,270,120,40])
	pygame.draw.rect(gamewindow,red,[235,340,150,40])
	screen_score(">Play",white,110,270)
	screen_score("Exit",white,430,270)
	screen_score("Sound",white,265,340)
	pygame.display.update()
	clock.tick(50)
	while not exit_game:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				exit_game=True
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_RETURN:
					gameloop()
				if event.key==pygame.K_LEFT:
					game_menu_play()
				if event.key==pygame.K_RIGHT:
					game_menu_exit()
				if event.key==pygame.K_DOWN:
					game_menu_sound()

def gameloop():
	pygame.mixer.init()
	exit_game=False
	game_over=False
	wellcome_sound=pygame.mixer.music.stop()
	game_sound=pygame.mixer.music.load('./data/causmic_business_as_usual.mp3')
	game_sound=pygame.mixer.music.play()
	snake_x=45
	snake_y=55
	v_x=0
	v_y=0
	snake_size=10
	fps=50
	s_speed=2
	s_speed_m=-2
	score=0
	snk_list=[]
	food_x=random.randint(15,s_width)
	food_y=random.randint(15,s_hight)
	snk_lenght=1
	pygame.display.update()
	while not exit_game:
		if game_over:
			gamewindow.fill(white)
			ending(score)
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit_game=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RETURN:
						gameloop()
		else:
			for event in pygame.event.get():
				if event.type==pygame.QUIT:
					exit_game=True
				if event.type==pygame.KEYDOWN:
					if event.key==pygame.K_RIGHT:
						v_x=s_speed
						v_y=0
					if event.key==pygame.K_LEFT:
						v_x=s_speed_m
						v_y=0
					if event.key==pygame.K_UP:
						v_y=s_speed_m
						v_x=0
					if event.key==pygame.K_DOWN:
						v_y=s_speed
						v_x=0
			snake_x+=v_x
			snake_y+=v_y
			if abs(snake_x-food_x)<6 and abs(snake_y-food_y)<6:
				score+=1
				food_x=random.randint(15,s_width)
				food_y=random.randint(15,s_hight)
				snk_lenght+=5

			gamewindow.fill(white)
			gamewindow.blit(image,(0,0))
			gamewindow.blit(image_social_1,(0,458))
			screen_score("Score: "+str(score),blue,5,5)
			head=[]
			head.append(snake_x)
			head.append(snake_y)
			snk_list.append(head)
			if len(snk_list)>snk_lenght:
				del snk_list[0]
			if head in snk_list[:-1]:
				game_over=True
			if snake_x<0 or snake_x>s_width or snake_y<0 or snake_y>s_hight:
				game_over=True
			pygame.draw.rect(gamewindow,red,[food_x,food_y,snake_size,snake_size])
			plot_snake(gamewindow,black,snk_list,snake_size)
		if score>10 and score<15:
			fps=70
		if score>=15 and score<20:
			fps=80
		if score>=20 and score<30:
			fps=100
		if score>=30 and score<50:
			fps=150
		if score>=50:
			fps=200
		pygame.display.update()
		clock.tick(fps)
	pygame.quit()
	quit()
if __name__=='__main__':
        wellcome()
