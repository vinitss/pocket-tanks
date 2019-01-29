import pygame, sys
import random
import cv2
from pygame.locals import *
from math import *
from pygame.color import *
from pygame import gfxdraw
from math import *
import pymunk as pm
from pymunk import Vec2d
import random
import time
from pymunk.pygame_util import *

import pymunk._chipmunk as cp
import pymunk._chipmunk_ffi as cpffi
import ctypes as ct
pygame.init()

FPS = 30 
fpsClock = pygame.time.Clock()
DISPLAYSURF = pygame.display.set_mode((600, 500),0,32)
screen=DISPLAYSURF
#random.seed(100)
pygame.display.set_caption('None')
BLUE = (50,0,150)
GREEN = (0,255,0)
DISPLAYSURF.fill(BLUE)
v=random.randint(15,50)
global vi
vi=v/20
def listup(p,q,screen,ti,tf):
    t=ti
    global phi
    global vi
    listx=[]
    listy=[]
    listxy=[]
    listxyd=[]
    listin=[(0,0)]
    global xi
    xi=0
    global yi
    yi=350
    yii=350
    #p=20 #
    x=0
    
    tp=0
    while (t<tf):
        
        for i in range(0,20):
            x=x+2#random.randint(xi,(xi+20))
            
            y=random.randint((yi-q),(yi+p))
            
            z=random.randint(20,30)
            
            listx.append(x)
            listy.append(y)
            
            xy=(x,y)
            listxyd.append(xy)
            if (yii-y)>0:
                listxy.append(xy)
                
            #pygame.draw.polygon(DISPLAYSURF, GREEN,tuple(listxy),0)
            if (tp==0):
                pygame.draw.rect(screen,GREEN,(xi,yi,z,(500-yi)),0)
                pygame.draw.rect(screen,(0,135,35),(xi,yi,z,(430-yi)),0)
                tp=1
            else:
                pygame.draw.rect(screen,GREEN,(x,y,z,(500-y)),0)
                pygame.draw.rect(screen,(0,135,35),(x,y,z,(430-y)),0)
            yii=y
        if (t==vi):
            yt=float(y-yi)
            xt=float(x-xi)
            o= (yt/xt)
            
            phi=atan(o)
            #phi=degrees(phi)
            print phi
        
        xi=x
        yi=y
        xiyi=(x,y)
        listin.append(xiyi)
        
        pygame.draw.polygon(DISPLAYSURF, GREEN,tuple(listxy),0)
        #pygame.draw.polygon(DISPLAYSURF, (0,135,35),tuple(listxy),0)
        #print listxy
        t=t+30
def flipy(y):
    return -y+500
listup(10,25,DISPLAYSURF,0,600)
listup(10,25,DISPLAYSURF,300,600)
pygame.transform.rotate(DISPLAYSURF,90)
imgdata = pygame.surfarray.array3d(DISPLAYSURF)
imgdata.swapaxes(0,1)
cv2.imwrite('None.png',imgdata)
my_surface = pygame.image.load('None.png')
pygame.transform.rotate(my_surface,90)
imgdata = pygame.surfarray.array3d(my_surface)
imgdata.swapaxes(0,1)
cv2.imwrite('None.png',imgdata)
#screen = pygame.display.set_mode((600, 500))
pygame.image.load('None.png')
weapon=pygame.image.load('weapon1.png')
wid=[0,0]
score=[0,0]
play_id=0
weap=[' Single Shot',' Triple Shot']
fontObj=pygame.font.SysFont('aerial',32)
textSurfaceObj = fontObj.render('Move', True, (0,0,0))
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (45,420)
fontObj1=pygame.font.SysFont('aerial',32)
textSurfaceObj1 = fontObj1.render('Angle', True, (0,0,0))
textRectObj1 = textSurfaceObj1.get_rect()
textRectObj1.center = (145,420)
fontObj11=pygame.font.SysFont('aerial',32)
textSurfaceObj11 = fontObj11.render('Power', True, (0,0,0))
textRectObj11 = textSurfaceObj11.get_rect()
textRectObj11.center = (525,420)
fontObj111=pygame.font.SysFont('aerial',32)
textSurfaceObj111 = fontObj111.render(weap[wid[play_id]], True, (0,0,0))
textRectObj111 = textSurfaceObj111.get_rect()
textRectObj111.center = (275,430)
fontObj1111=pygame.font.SysFont('aerial',32)
textSurfaceObj1111 = fontObj1111.render('FIRE', True, (0,0,0))
textRectObj1111 = textSurfaceObj1111.get_rect()
textRectObj1111.center = (275,470)
running=True
run_physics=True
move=[3,3]
ang=[20,160]
powe=[1,1]
rectangle = [pygame.rect.Rect(460,450,5,20),pygame.rect.Rect(460,450,5,20)]
rectangle_draging = False
fire=False
WHITE=(255,255,255)
def listupang(x,y,surface,angle,x2,y2,angle2):
    angle=(angle*0.0175)
    angle2=(angle2*0.0175)
    l=30
    screen.blit(pygame.image.load('None.png'),(0,0))
    screen.blit(pygame.image.load('red.png'),(x,y-25))
    screen.blit(pygame.image.load('red.png'),(x2,y2-25))
    pygame.draw.aaline(surface,WHITE,(x+15,y-25),(x+15+l*cos(angle),y-25-l*sin(angle)),60)
    pygame.draw.aaline(surface,WHITE,(x2+15,y2-25),(x2+15+l*cos(angle2),y2-25-l*sin(angle2)),60)
h=0
pos_for1=random.randint(10,55)
mov1=[0,0,0,0,0,0,0]
mov2=[0,0,0,0,0,0,0]
for j in range(0,500):
        color=screen.get_at((pos_for1, j))
	#print color
        if (color==(0,255,0,255)):
            h=j
	    break
#print h
screen.blit(pygame.image.load('red.png'),(pos_for1,h-25))
pos_for2=random.randint(450,485)
mov1[3]=h
for i in range(3):
	for j in range(0,500):
		color=screen.get_at((pos_for1+20*i+20, j))
		#print color
		if (color==(0,255,0,255)):
		    h=j
		    mov1[i+4]=h
		    break
flg=0
for i in range(3):
	
	for j in range(0,500):
		color=screen.get_at((max(0,pos_for1-20*i-20), j))
		#print color
		if (color==(0,255,0,255)):
		    h=j
		    mov1[2-i]=h
		    if (mov1[2-i]==430 and flg==0):
			mov1[2-i]=mov1[3-i]+5
			flg=1
		    elif (mov1[2-i]==430 and flg==1):
			mov1[2-i]=mov1[3-i]
		    break
h1=0
hj1=3
hj2=3
for j in range(0,500):
        color=screen.get_at((pos_for2, j))
	#print color
        if (color==(0,255,0,255)):
            h1=j
	    break
#print h
mov2[3]=h1
hi1=pos_for1
hi2=pos_for2
selecton=0
print mov1
for i in range(3):
	for j in range(0,500):
		color=screen.get_at((pos_for2+20*i+20, j))
		#print color
		if (color==(0,255,0,255)):
		    h1=j
		    mov2[i+4]=h1
		    break
for i in range(3):
	for j in range(0,500):
		color=screen.get_at((pos_for2-20*i-20, j))
		#print color
		if (color==(0,255,0,255)):
		    h1=j
		    if (h1==430):
			mov2[2-i]=mov2[3-i]
		    else:		    
			mov2[2-i]=h1
		    break
listupang(pos_for1,mov1[hj1],screen,20,hi2,mov2[hj2],160)
#screen.blit(pygame.image.load('red.png'),(pos_for2,h1-25))
go_id=0
sht_ang=0
sht=False
tm=0
vx=0
vy=0
projx=4
stk=[]
projy=0
while running:
	if (fire==False and run_physics==False and sht==True):
		#print screen.get_at((stx+projx+5,sty-projy))	
		if ((sty-projy<=0) or (stx+projx+5>=0 and sty-projy<=450 and stx+projx+5<=600 and screen.get_at((stx+projx+5,sty-projy))!=(0,255,0,255))):
			if (play_id==0):
				listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
			else:
				listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
			pygame.draw.circle(screen,WHITE, (stx+projx,sty-projy),5, 0)
			if (wid[play_id]==1):
				pygame.draw.circle(screen,WHITE, (stx+projx+10,sty-projy+10),5, 0)
				pygame.draw.circle(screen,WHITE, (stx+projx-10,sty-projy-10),5, 0)
			tm+=1
			if (play_id==0):
				projx+=2
			else:
				projx-=1
			projy=(projx*tan(sht_ang)-5*projx*projx/(vx*vx*cos(sht_ang)*cos(sht_ang)))
			stx=int(stx)
			sty=int(sty)
			projy=int(projy)
			
		if ((sty-projy>0) and stx+projx+5>=0 and sty-projy<=450 and stx+projx+5<=590 and (screen.get_at((stx+projx+5,sty-projy))==(0,255,0,255) or screen.get_at((stx+projx+5,sty-projy))==(0,135,35,255) or 
(stx+projx+5>=hi1 and stx+projx+5<=hi1+30 and sty-projy<=mov1[hj1] and sty-projy>=mov1[hj1]-22) or (stx+projx+5>=hi2 and stx+projx+5<=hi2+30 and sty-projy<=mov2[hj2] and sty-projy>=mov2[hj2]-22)) ):
			stk=[stx+projx+5,sty-projy]
			if (play_id==0):
				if (abs(stk[0]-hi1)<=40):
					score[play_id]-=10
				if (abs(stk[0]-hi2)<=40):
					score[play_id]+=10
				listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
			else:
				if (abs(stk[0]-hi1)<=40):
					score[play_id]+=10
				if (abs(stk[0]-hi2)<=40):
					score[play_id]-=10
				listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
			play_id=(play_id ^ 1)
			
			run_physics=True
			sht=False
			#print (stk)
		if (wid[play_id]==1):
			if ((sty-projy+10>0) and stx+projx+15>=0 and sty-projy+10<=450 and stx+projx+15<=590 and (screen.get_at((stx+projx+15,sty-projy+10))==(0,255,0,255) or screen.get_at((stx+projx+15,sty-projy+10))==(0,135,35,255))):
				if (play_id==0):
					listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
				else:
					listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
				play_id=(play_id ^ 1)
				
				run_physics=True
				sht=False
		if (stx+projx+5<0 or sty-projy>450 or stx+projx+5>590):
			stk=[None,None]
			if (play_id==0):
					listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
			else:
					listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
			play_id=(play_id ^ 1)
			
			run_physics=True
			sht=False
        for event in pygame.event.get():
            if (fire):
		l=30
		stx=0
		sty=0
		if (play_id==0):
			stx,sty=hi1+15+l*cos(ang[play_id]*0.0175),mov1[hj1]-25-l*sin(ang[play_id]*0.0175)
		else:
			stx,sty=hi2+15+l*cos(ang[play_id]*0.0175),mov2[hj2]-25-l*sin(ang[play_id]*0.0175)
		sht=True
		stx=int(stx)
		sty=int(sty)
		sht_ang=ang[play_id]*0.0175
		vx=int(powe[play_id]*cos(sht_ang))
		vy=int(powe[play_id]*sin(sht_ang))
		projx=4
		projy=0
		fire=False
		stk=[None,None]
            if event.type == QUIT:
                running=False
                pygame.quit()
                sys.exit()
	    
            elif event.type == KEYDOWN and event.key == K_SPACE:    
                run_physics = not run_physics
            p0,p3 = pygame.mouse.get_pos()
	    #print str(p0)+" "+str(p3)
            keys = pygame.key.get_pressed()
            if run_physics:
                if move[play_id]>0:
                        if (keys[K_LEFT]):
			    selecton=0
			    #print "LEFT"
			    if (play_id==0):
				    hj1-=1
				    hi1-=20
				    hi1=max(hi1,0)
				    listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
		                    move[play_id]-=1
			    else:
				    hj2-=1
				    if (hj2+1<7and mov2[hj2]==mov2[hj2+1]):
					hi2+=15
				    hi2-=20
				    hi2=min(hi2,600)
				    listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
		                    move[play_id]-=1
                            
                        if (keys[K_RIGHT]):
			    selecton=0
			    #print "LEFT1"
			    if (play_id==0):
				    hj1+=1
				    hi1+=20
				    hi1=max(hi1,0)
		                    listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
		                    move[play_id]-=1
			    else:
				    hj2+=1
				    hi2+=20
				    hi2=min(hi2,600)
		                    listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
		                    move[play_id]-=1
                if (p3>455 and p3<470):
                
                    if (p0>170 and p0<210):
                        
                            if event.type == MOUSEBUTTONDOWN and event.button == 3:
				selecton=0
				#print "LEFT2"
				if (play_id==0):
					listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
			        else:
					listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
                                
                                ang[play_id]+=1
                                if ang[play_id]>359:
                                    ang[play_id]=0
                    elif (p0>70 and p0<110):
                        
                             if event.type == MOUSEBUTTONDOWN and event.button == 3:
				selecton=0
				#print "LEFT3"
                             	if (play_id==0):
					listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
			        else:
					listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
                                ang[play_id]-=1
                                if ang[play_id]<0:
                                    ang[play_id]=ang[play_id]+360
                
                if (p3>454 and p3<486):
                    if (p0>210 and p0<345):
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
			    selecton=0
			    #print "LEFT4"
                            fire=True
			    run_physics = not run_physics
			    
			    #screen.blit(pygame.image.load('shot.png'),(160,500-220))
			    #print "Fired"
		if (p3>417 and p3<440):
		    if (p0>210 and p0<345):
                        if event.type == MOUSEBUTTONDOWN and event.button == 1:
			    screen.blit(pygame.image.load('shot.png'),(160,500-220))
			    selecton=1
			    #print "Fired"
		if (selecton==1):
			#print "YES"
			if (p3>320 and p3<335):
		    		if (p0>237 and p0<370):
					if event.type == MOUSEBUTTONDOWN and event.button == 1:
						#print "selected"
						wid[play_id]=0
						if (play_id==0):
							listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
						else:
							listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
			if (p3>359 and p3<370):
		    		if (p0>237 and p0<370):
					if event.type == MOUSEBUTTONDOWN and event.button == 1:
						#print "selected"
						wid[play_id]=1
						if (play_id==0):
							listupang(hi1,mov1[hj1],screen,ang[play_id],hi2,mov2[hj2],ang[play_id^1])
						else:
							listupang(hi2,mov2[hj2],screen,ang[play_id],hi1,mov1[hj1],ang[play_id^1])
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:      
			#print "LEFT5"     
                        if rectangle[play_id].collidepoint(event.pos):
                            rectangle_draging = True
                            mouse_x, mouse_y = event.pos
                            offset_x = rectangle[play_id].x - mouse_x
                            offset_y = rectangle[play_id].y - mouse_y
                            
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.button == 1:            
                        rectangle_draging = False
                        #fire=False
                elif event.type == pygame.MOUSEMOTION:
                    
                            
                    if rectangle_draging:
                        mouse_x, mouse_y = event.pos
                       
                        rectangle[play_id].x = mouse_x + offset_x
                        #rectangle.y = mouse_y + offset_y
        fontObj111=pygame.font.SysFont('aerial',32)
	textSurfaceObj111 = fontObj111.render(weap[wid[play_id]], True, (0,0,0))
	textRectObj111 = textSurfaceObj111.get_rect()
	textRectObj111.center = (275,430)                  
        fontObj11111=pygame.font.SysFont('aerial',32)
        textSurfaceObj11111 = fontObj11111.render(str(move[play_id]), True, (0,0,0))
        textRectObj11111 = textSurfaceObj11111.get_rect()
        textRectObj11111.center = (35,465)   
        fontObj111111=pygame.font.SysFont('aerial',32)
        textSurfaceObj111111 = fontObj111111.render(str(ang[play_id]), True, (0,0,0))
        textRectObj111111 = textSurfaceObj111111.get_rect()
        textRectObj111111.center = (140,465)
        fontObj1111111=pygame.font.SysFont('aerial',32)
        textSurfaceObj1111111 = fontObj1111111.render(str(powe[play_id]), True, (0,0,0))
        textRectObj1111111 = textSurfaceObj1111111.get_rect()
        textRectObj1111111.center = (400,465)
	fontObj2=pygame.font.SysFont('aerial',26)
	textSurfaceObj2 = fontObj2.render(str(score[1]), True, (255,255,255))
	textRectObj2 = textSurfaceObj2.get_rect()
	textRectObj2.center = (500,50)
	fontObj3=pygame.font.SysFont('aerial',26)
	textSurfaceObj3 = fontObj3.render(str(score[0]), True, (255,255,255))
	textRectObj3 = textSurfaceObj3.get_rect()
	textRectObj3.center = (40,50)
        screen.blit(weapon,(0,405))
        screen.blit(textSurfaceObj, textRectObj)
        screen.blit(textSurfaceObj1, textRectObj1)
        screen.blit(textSurfaceObj11, textRectObj11)
        screen.blit(textSurfaceObj111, textRectObj111)
        screen.blit(textSurfaceObj1111, textRectObj1111)
        screen.blit(textSurfaceObj11111, textRectObj11111)
        screen.blit(textSurfaceObj111111, textRectObj111111)
	screen.blit(textSurfaceObj3, textRectObj3)
	screen.blit(textSurfaceObj2, textRectObj2)
        #pygame.draw.line(screen, pygame.color.THECOLORS["red"],(460+h2,460),(460,460),15)
        if (rectangle[play_id].x>=458 and rectangle[play_id].x<=584):
            pygame.draw.rect(screen,(0,0,0),rectangle[play_id],0)
            pygame.draw.rect(screen,(255,0,0),(458,452,rectangle[play_id].x-458,18),0)
            powe[play_id]=int(float(rectangle[play_id].x-458)*100/126)
            
        elif (rectangle[play_id].x<458):
            rectangle[play_id].x=458
            pygame.draw.rect(screen,(0,0,0),rectangle[play_id],0)
        elif (rectangle[play_id].x>584):
            rectangle[play_id].x=584
            pygame.draw.rect(screen,(0,0,0),rectangle[play_id],0)
        #rectangle_draging = False
        screen.blit(textSurfaceObj1111111, textRectObj1111111)
        pygame.display.update()
	fpsClock.tick()
	pygame.display.set_caption("fps: " + str(fpsClock.get_fps()))

