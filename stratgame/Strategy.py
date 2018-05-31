import pygame, sys
import socket
from pygame.locals import *
import time
import webbrowser
'''-----------------------------------------------------------------
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
-----------------------------------------------------------------'''

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()

FPS = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((448, 356))
pygame.display.set_caption('Stratagem')

tiles={(1, 1): ['f1'],(1, 2): ['f1'],(1, 3): ['f2'],(1, 4): ['f1'],(1, 5): ['f1'],(1, 6): ['f1'],(1, 7): ['f1'],(1, 8): ['f1'],(1, 9): ['f2'],(1, 10): ['f1'],
       (2, 1): ['f1'],(2, 2): ['f1'],(2, 3): ['f1'],(2, 4): ['f1'],(2, 5): ['f1','redc'],(2, 6): ['f2'],(2, 7): ['f1'],(2, 8): ['f1'],(2, 9): ['f1'],(2, 10): ['f2'],
       (3, 1): ['f1'],(3, 2): ['f1'],(3, 3): ['f1'],(3, 4): ['f1'],(3, 5): ['f1'],(3, 6): ['f1'],(3, 7): ['f1'],(3, 8): ['f1'],(3, 9): ['f1'],(3, 10): ['f1'],
       (4, 1): ['f1'],(4, 2): ['f2'],(4, 3): ['f1'],(4, 4): ['f1'],(4, 5): ['f1'],(4, 6): ['f1'],(4, 7): ['f1'],(4, 8): ['f1'],(4, 9): ['f1'],(4, 10): ['f1'],
       (5, 1): ['f1'],(5, 2): ['f1'],(5, 3): ['f1'],(5, 4): ['f1'],(5, 5): ['f1'],(5, 6): ['f1'],(5, 7): ['f1'],(5, 8): ['f2'],(5, 9): ['f1'],(5, 10): ['f1'],
       (6, 1): ['f1'],(6, 2): ['f1'],(6, 3): ['f1'],(6, 4): ['f2'],(6, 5): ['f1'],(6, 6): ['f1'],(6, 7): ['f1'],(6, 8): ['f1'],(6, 9): ['f1'],(6, 10): ['f1'],
       (7, 1): ['f2'],(7, 2): ['f1'],(7, 3): ['f1'],(7, 4): ['f1'],(7, 5): ['f1'],(7, 6): ['f1'],(7, 7): ['f2'],(7, 8): ['f1'],(7, 9): ['f1'],(7, 10): ['f1'],
       (8, 1): ['f1'],(8, 2): ['f1'],(8, 3): ['f1'],(8, 4): ['f1'],(8, 5): ['f1'],(8, 6): ['f1'],(8, 7): ['f1'],(8, 8): ['f1'],(8, 9): ['f1'],(8, 10): ['f2'],
       (9, 1): ['f1'],(9, 2): ['f1'],(9, 3): ['f1'],(9, 4): ['f1'],(9, 5): ['f2'],(9, 6): ['f1'],(9, 7): ['f1'],(9, 8): ['f1'],(9, 9): ['f1'],(9, 10): ['f1'],
       (10, 1): ['f2'],(10, 2): ['f1'],(10, 3): ['f1'],(10, 4): ['f1'],(10, 5): ['f1'],(10, 6): ['f2'],(10, 7): ['f1'],(10, 8): ['f1'],(10, 9): ['f1'],(10, 10): ['f1'],
       (11, 1): ['f1'],(11, 2): ['f1'],(11, 3): ['f1'],(11, 4): ['f2'],(11, 5): ['f1'],(11, 6): ['f1'],(11, 7): ['f1'],(11, 8): ['f1'],(11, 9): ['f2'],(11, 10): ['f1'],
       (12, 1): ['f1'],(12, 2): ['f2'],(12, 3): ['f1'],(12, 4): ['f1'],(12, 5): ['f1'],(12, 6): ['f1'],(12, 7): ['f1'],(12, 8): ['f1'],(12, 9): ['f1'],(12, 10): ['f1'],
       (13, 1): ['f1'],(13, 2): ['f1'],(13, 3): ['f1'],(13, 4): ['f1'],(13, 5): ['f2','bluc'],(13, 6): ['f1'],(13, 7): ['f1'],(13, 8): ['f1'],(13, 9): ['f1'],(13, 10): ['f1'],
       (14, 1): ['f1'],(14, 2): ['f1'],(14, 3): ['f2'],(14, 4): ['f1'],(14, 5): ['f1'],(14, 6): ['f1'],(14, 7): ['f2'],(14, 8): ['f1'],(14, 9): ['f1'],(14, 10): ['f1'],
       (0, 1): [],(0,2):[],(0,3):[],(0,4):[],(0,5):[],(0,6):[],(0,7):[],(0,8):[],(0,9):[],(0,10):[],
       (15, 1): [], (15, 2): [], (15, 3): [], (15, 4): [], (15, 5): [], (15, 6): [], (15, 7): [], (15, 8): [], (15, 9): [],(15, 10): [],
       (1, 11): [],(2, 11): [],(3, 11): [],(4, 11): [],(5, 11): [],(6, 11): [],(7, 11): [],(8, 11): [],(9, 11): [],(10, 11): [],(11, 11): [],(12, 11): [],(13, 11): [],(14, 11): [],
       (1, 0):[],(2, 0):[],(3, 0):[],(4, 0):[],(5, 0):[],(6, 0):[],(7, 0):[],(8, 0):[],(9, 0):[],(10, 0): [],(11, 0): [], (0, 0): [], (12, 0): [], (13, 0): [], (14, 0): []}

meh=pygame.image.load('meh.png')

f1=pygame.image.load('desert.png')
f2=pygame.image.load('desert2.png')
c=pygame.image.load("cursor1.png")
c2=pygame.image.load("cursor3.png")
ui1=pygame.image.load("ui1.png")
atk=pygame.image.load("atk.png")
mov=pygame.image.load("mov.png")
bld=pygame.image.load("bld.png")
blds=pygame.image.load("selector.png")
unis=pygame.image.load("unitss.png")
unig=pygame.image.load("unitsg.png")
untm=pygame.image.load("unit.png")
bk=pygame.image.load("bk.png")
rk=pygame.image.load('rk.png')
bs=pygame.image.load('bs.png')
rs=pygame.image.load('rs.png')
bc=pygame.image.load('bc.png')
rc=pygame.image.load('rc.png')
rm=pygame.image.load("rm.png")
bm=pygame.image.load("bm.png")
reds=pygame.image.load("reds.png")
blus=pygame.image.load("blus.png")
redg=pygame.image.load("redg.png")
blug=pygame.image.load("blug.png")
redc=pygame.image.load("redc.png")
bluc=pygame.image.load("bluc.png")
redb=pygame.image.load("redb.png")
blub=pygame.image.load("blub.png")
redu=pygame.image.load("redu.png")
bluu=pygame.image.load("bluu.png")
arrr=pygame.image.load("arrr.png")
arru=pygame.image.load("arru.png")
arrd=pygame.image.load("arrd.png")
arrl=pygame.image.load("arrl.png")
win1=pygame.image.load("win1.png")
win2=pygame.image.load("win2.png")

units=['rk','rs','rc','rm']
enemyunits=['bk','bs','bc','bm']
struct=['reds','redg','redb','redu']
enemystruct=['blus','blug','blub','bluu','bluc']
unitmakers=['redb','redg']

WHITE = (255, 255, 255)
BLACK = (0,0,0)
brek=False
cursor=[1,1]
cursor2=1
hopbar=False
barhop=[]
stopbar=False
cursor3=0
commands=[]
turn=1
money=5
money2=5
singlerun=0
movement=False
dudebar=0
movecount=0
cursor4=1
ap=0
apmax=1
ap=apmax
fight=False
redchealth=30
bluchealth=30
health=0
dmg=[]
movelist=[]
fightlist=[]
flip=1
atkormov=False
tempvar=False

pygame.mixer.music.load('bgm.wav')
pygame.mixer.music.play(-1, 0.0)
pchu=pygame.mixer.Sound('pchu.wav')
blep=pygame.mixer.Sound('blep.wav')
ham=pygame.mixer.Sound('ham.wav')

text=pygame.font.Font(None, 25)

while True: # the main game loop
    if turn==1:
        if flip==1:
            whichmoney=money
        elif flip==2:
            whichmoney=money2
        screen.fill(WHITE)
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN and event.key == K_e:
                turn=2
            elif event.type == pygame.KEYDOWN and event.key == K_w:
                if cursor[1]>1:
                    cursor[1]-=1
            elif event.type == pygame.KEYDOWN and event.key == K_a:
                if cursor[0]>1:
                    cursor[0]-=1
            elif event.type == pygame.KEYDOWN and event.key == K_s:
                if cursor[1]<10:
                    cursor[1]+=1
            elif event.type == pygame.KEYDOWN and event.key == K_d:
                if cursor[0]<14:
                    cursor[0]+=1
            elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
                blep.play()
                hopbar=True
                if len(tiles[((cursor[0],cursor[1]))])==1 and cursor[0]<=7 and flip==1:
                    try:
                        if len(tiles[((cursor[0]+1,cursor[1]))])==2 and tiles[((cursor[0]+1,cursor[1]))][1] in struct:
                            pass
                        elif len(tiles[((cursor[0]-1,cursor[1]))])==2 and tiles[((cursor[0]-1,cursor[1]))][1] in struct:
                            pass
                        elif len(tiles[((cursor[0],cursor[1]+1))])==2 and tiles[((cursor[0],cursor[1]+1))][1] in struct:
                            pass
                        elif len(tiles[((cursor[0],cursor[1]-1))])==2 and tiles[((cursor[0],cursor[1]-1))][1] in struct:
                            pass
                        else:
                            commands.append('bld')
                    except:
                        pass
                elif len(tiles[((cursor[0],cursor[1]))])==1 and cursor[0]>7 and flip==2:
                    try:
                        if len(tiles[((cursor[0]+1,cursor[1]))])==2 and tiles[((cursor[0]+1,cursor[1]))][1] in struct:
                            pass
                        elif len(tiles[((cursor[0]-1,cursor[1]))])==2 and tiles[((cursor[0]-1,cursor[1]))][1] in struct:
                            pass
                        elif len(tiles[((cursor[0],cursor[1]+1))])==2 and tiles[((cursor[0],cursor[1]+1))][1] in struct:
                            pass
                        elif len(tiles[((cursor[0],cursor[1]-1))])==2 and tiles[((cursor[0],cursor[1]-1))][1] in struct:
                            pass
                        else:
                            commands.append('bld')
                    except:
                        pass
                elif len(tiles[((cursor[0],cursor[1]))])==2 and tiles[((cursor[0],cursor[1]))][1] in unitmakers:
                    commands.append("untm")
                elif len(tiles[((cursor[0],cursor[1]))])==2 and tiles[((cursor[0],cursor[1]))][1] in units:
                    commands.append("unt")
                    try:
                        if len(tiles[((cursor[0]+1,cursor[1]))])==2:
                            if tiles[((cursor[0]+1,cursor[1]))][1] in enemyunits or tiles[((cursor[0]+1,cursor[1]))][1] in enemystruct:
                                commands.append("atk")
                        elif len(tiles[((cursor[0]-1,cursor[1]))])==2:
                            if tiles[((cursor[0]-1,cursor[1]))][1] in enemyunits or tiles[((cursor[0]-1,cursor[1]))][1] in enemystruct:
                                commands.append("atk")
                        elif len(tiles[((cursor[0],cursor[1]+1))])==2:
                            if tiles[((cursor[0],cursor[1]+1))][1] in enemyunits or tiles[((cursor[0],cursor[1]+1))][1] in enemystruct:
                                commands.append("atk")
                        elif len(tiles[((cursor[0],cursor[1]-1))])==2:
                            if tiles[((cursor[0],cursor[1]-1))][1] in enemyunits or tiles[((cursor[0],cursor[1]-1))][1] in enemystruct:
                                commands.append("atk")
                    except:
                        pass
        screen.blit(ui1,(0,320))
        temp1=1
        temp2=1
        for i in range(14):
            temp2=1
            t1=temp1*32-32
            for i in range(10):
                t2=temp2*32-32
                if "f1" in tiles[(temp1,temp2)]:
                    screen.blit(f1,(t1,t2))
                if "f2" in tiles[(temp1, temp2)]:
                    screen.blit(f2,(t1,t2))
                if flip==1:
                    if "redc" in tiles[(temp1, temp2)]:
                        screen.blit(redc, (t1, t2))
                    if "bluc" in tiles[(temp1, temp2)]:
                        screen.blit(bluc, (t1, t2))
                    if "reds" in tiles[(temp1, temp2)]:
                        screen.blit(reds, (t1, t2))
                    if "blus" in tiles[(temp1, temp2)]:
                        screen.blit(blus, (t1, t2))
                    if "blub" in tiles[(temp1, temp2)]:
                        screen.blit(blub, (t1, t2))
                    if "redb" in tiles[(temp1, temp2)]:
                        screen.blit(redb, (t1, t2))
                    if "redg" in tiles[(temp1, temp2)]:
                        screen.blit(redg, (t1, t2))
                    if "blug" in tiles[(temp1, temp2)]:
                        screen.blit(blug, (t1, t2))
                    if "bluu" in tiles[(temp1, temp2)]:
                        screen.blit(bluu, (t1, t2))
                    if "redu" in tiles[(temp1, temp2)]:
                        screen.blit(redu, (t1, t2))
                    if "bk" in tiles[(temp1, temp2)]:
                        screen.blit(bk, (t1, t2))
                    if "rk" in tiles[(temp1, temp2)]:
                        screen.blit(rk, (t1, t2))
                    if "bm" in tiles[(temp1, temp2)]:
                        screen.blit(bm, (t1, t2))
                    if "rm" in tiles[(temp1, temp2)]:
                        screen.blit(rm, (t1, t2))
                    if "bs" in tiles[(temp1, temp2)]:
                        screen.blit(bs, (t1, t2))
                    if "rs" in tiles[(temp1, temp2)]:
                        screen.blit(rs, (t1, t2))
                    if "bc" in tiles[(temp1, temp2)]:
                        screen.blit(bc, (t1, t2))
                    if "rc" in tiles[(temp1, temp2)]:
                        screen.blit(rc, (t1, t2))
                elif flip==2:
                    if "redc" in tiles[(temp1, temp2)]:
                        screen.blit(bluc, (t1, t2))
                    if "bluc" in tiles[(temp1, temp2)]:
                        screen.blit(redc, (t1, t2))
                    if "reds" in tiles[(temp1, temp2)]:
                        screen.blit(blus, (t1, t2))
                    if "blus" in tiles[(temp1, temp2)]:
                        screen.blit(reds, (t1, t2))
                    if "blub" in tiles[(temp1, temp2)]:
                        screen.blit(redb, (t1, t2))
                    if "redb" in tiles[(temp1, temp2)]:
                        screen.blit(blub, (t1, t2))
                    if "redg" in tiles[(temp1, temp2)]:
                        screen.blit(blug, (t1, t2))
                    if "blug" in tiles[(temp1, temp2)]:
                        screen.blit(redg, (t1, t2))
                    if "bluu" in tiles[(temp1, temp2)]:
                        screen.blit(redu, (t1, t2))
                    if "redu" in tiles[(temp1, temp2)]:
                        screen.blit(bluu, (t1, t2))
                    if "bk" in tiles[(temp1, temp2)]:
                        screen.blit(rk, (t1, t2))
                    if "rk" in tiles[(temp1, temp2)]:
                        screen.blit(bk, (t1, t2))
                    if "bm" in tiles[(temp1, temp2)]:
                        screen.blit(rm, (t1, t2))
                    if "rm" in tiles[(temp1, temp2)]:
                        screen.blit(bm, (t1, t2))
                    if "bs" in tiles[(temp1, temp2)]:
                        screen.blit(rs, (t1, t2))
                    if "rs" in tiles[(temp1, temp2)]:
                        screen.blit(bs, (t1, t2))
                    if "bc" in tiles[(temp1, temp2)]:
                        screen.blit(rc, (t1, t2))
                    if "rc" in tiles[(temp1, temp2)]:
                        screen.blit(bc, (t1, t2))
                temp2+=1
            temp1+=1


        while hopbar==True:#stuff
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN and event.key == K_e:
                    hopbar = False
                    stopbar = False
            try:
                if ap > 0:
                    if commands[cursor3 - 1] == 'bld':
                        stopbar = True
                        commands = []
                    elif commands[cursor3 - 1] == 'untm':
                        blding = tiles[((cursor[0], cursor[1]))][1]
                        commands = []
                        dudebar = True
                    elif commands[cursor3 - 1] == 'unt':
                        commands = []
                        atkormov = True
                    elif commands[cursor3 - 1] == 'atk':
                        if (cursor[0], cursor[1]) in fightlist:
                            print('no')
                        else:
                            commands = []
                            atkormov = True
                else:
                    hopbar = False
            except:
                hopbar = False
            screen.blit(ui1, (0, 320))
            temp1 = 1
            temp2 = 1
            for i in range(14):
                temp2 = 1
                t1 = temp1 * 32 - 32
                for i in range(10):
                    t2 = temp2 * 32 - 32
                    if "f1" in tiles[(temp1, temp2)]:
                        screen.blit(f1, (t1, t2))
                    if "f2" in tiles[(temp1, temp2)]:
                        screen.blit(f2, (t1, t2))
                    if flip==1:
                        if "redc" in tiles[(temp1, temp2)]:
                            screen.blit(redc, (t1, t2))
                        if "bluc" in tiles[(temp1, temp2)]:
                            screen.blit(bluc, (t1, t2))
                        if "reds" in tiles[(temp1, temp2)]:
                            screen.blit(reds, (t1, t2))
                        if "blus" in tiles[(temp1, temp2)]:
                            screen.blit(blus, (t1, t2))
                        if "blub" in tiles[(temp1, temp2)]:
                            screen.blit(blub, (t1, t2))
                        if "redb" in tiles[(temp1, temp2)]:
                            screen.blit(redb, (t1, t2))
                        if "redg" in tiles[(temp1, temp2)]:
                            screen.blit(redg, (t1, t2))
                        if "blug" in tiles[(temp1, temp2)]:
                            screen.blit(blug, (t1, t2))
                        if "bluu" in tiles[(temp1, temp2)]:
                            screen.blit(bluu, (t1, t2))
                        if "redu" in tiles[(temp1, temp2)]:
                            screen.blit(redu, (t1, t2))
                        if "bk" in tiles[(temp1, temp2)]:
                            screen.blit(bk, (t1, t2))
                        if "rk" in tiles[(temp1, temp2)]:
                            screen.blit(rk, (t1, t2))
                        if "bm" in tiles[(temp1, temp2)]:
                            screen.blit(bm, (t1, t2))
                        if "rm" in tiles[(temp1, temp2)]:
                            screen.blit(rm, (t1, t2))
                        if "bs" in tiles[(temp1, temp2)]:
                            screen.blit(bs, (t1, t2))
                        if "rs" in tiles[(temp1, temp2)]:
                            screen.blit(rs, (t1, t2))
                        if "bc" in tiles[(temp1, temp2)]:
                            screen.blit(bc, (t1, t2))
                        if "rc" in tiles[(temp1, temp2)]:
                            screen.blit(rc, (t1, t2))
                    elif flip==2:
                        if "redc" in tiles[(temp1, temp2)]:
                            screen.blit(bluc, (t1, t2))
                        if "bluc" in tiles[(temp1, temp2)]:
                            screen.blit(redc, (t1, t2))
                        if "reds" in tiles[(temp1, temp2)]:
                            screen.blit(blus, (t1, t2))
                        if "blus" in tiles[(temp1, temp2)]:
                            screen.blit(reds, (t1, t2))
                        if "blub" in tiles[(temp1, temp2)]:
                            screen.blit(redb, (t1, t2))
                        if "redb" in tiles[(temp1, temp2)]:
                            screen.blit(blub, (t1, t2))
                        if "redg" in tiles[(temp1, temp2)]:
                            screen.blit(blug, (t1, t2))
                        if "blug" in tiles[(temp1, temp2)]:
                            screen.blit(redg, (t1, t2))
                        if "bluu" in tiles[(temp1, temp2)]:
                            screen.blit(redu, (t1, t2))
                        if "redu" in tiles[(temp1, temp2)]:
                            screen.blit(bluu, (t1, t2))
                        if "bk" in tiles[(temp1, temp2)]:
                            screen.blit(rk, (t1, t2))
                        if "rk" in tiles[(temp1, temp2)]:
                            screen.blit(bk, (t1, t2))
                        if "bm" in tiles[(temp1, temp2)]:
                            screen.blit(rm, (t1, t2))
                        if "rm" in tiles[(temp1, temp2)]:
                            screen.blit(bm, (t1, t2))
                        if "bs" in tiles[(temp1, temp2)]:
                            screen.blit(rs, (t1, t2))
                        if "rs" in tiles[(temp1, temp2)]:
                            screen.blit(bs, (t1, t2))
                        if "bc" in tiles[(temp1, temp2)]:
                            screen.blit(rc, (t1, t2))
                        if "rc" in tiles[(temp1, temp2)]:
                            screen.blit(bc, (t1, t2))
                    temp2 += 1
                temp1 += 1
            if len(tiles[((cursor[0], cursor[1]))]) == 1:
                screen.blit(bld, (36, 320))
            elif len(tiles[((cursor[0], cursor[1]))]) == 2 and tiles[((cursor[0], cursor[1]))][1] in unitmakers:
                screen.blit(untm, (36, 320))
            elif len(tiles[((cursor[0], cursor[1]))]) == 2 and tiles[((cursor[0], cursor[1]))][1] in units:
                screen.blit(mov, (36, 320))
                try:
                    if len(tiles[((cursor[0]+1,cursor[1]))])==2:
                        if tiles[((cursor[0]+1,cursor[1]))][1] in enemyunits or tiles[((cursor[0]+1,cursor[1]))][1] in enemystruct:
                            screen.blit(atk, (72, 320))
                    elif len(tiles[((cursor[0]-1,cursor[1]))])==2:
                        if tiles[((cursor[0]-1,cursor[1]))][1] in enemyunits or tiles[((cursor[0]-1,cursor[1]))][1] in enemystruct:
                            screen.blit(atk, (72, 320))
                    elif len(tiles[((cursor[0],cursor[1]+1))])==2:
                        if tiles[((cursor[0],cursor[1]+1))][1] in enemyunits or tiles[((cursor[0],cursor[1]+1))][1] in enemystruct:
                            screen.blit(atk, (72, 320))
                    elif len(tiles[((cursor[0],cursor[1]-1))])==2:
                        if tiles[((cursor[0],cursor[1]-1))][1] in enemyunits or tiles[((cursor[0],cursor[1]-1))][1] in enemystruct:
                            screen.blit(atk, (72, 320))
                except:
                    pass
            text2 = text.render(str(whichmoney), 6, WHITE)
            if len(str(whichmoney)) == 1:
                screen.blit(text2, (415, 320))
            if len(str(whichmoney)) == 2:
                screen.blit(text2, (405, 320))
            if len(str(whichmoney)) == 3:
                screen.blit(text2, (395, 320))
            text3=text.render(str(ap),6,WHITE)
            if len(str(ap))==1:
                screen.blit(text3,(415,340))
            if len(str(ap))==2:
                screen.blit(text3,(405,340))
            text4 = text.render(str(health), 6, WHITE)
            try:
                if tiles[((cursor[0], cursor[1]))][1] == 'rk' or tiles[((cursor[0], cursor[1]))][1] == 'bk':
                    health = 6
                if tiles[((cursor[0], cursor[1]))][1] == 'rm' or tiles[((cursor[0], cursor[1]))][1] == 'bm':
                    health = 4
                if tiles[((cursor[0], cursor[1]))][1] == 'rs' or tiles[((cursor[0], cursor[1]))][1] == 'bs':
                    health = 5
                if tiles[((cursor[0], cursor[1]))][1] == 'rc' or tiles[((cursor[0], cursor[1]))][1] == 'bc':
                    health = 7
                if flip==1:
                    if tiles[((cursor[0],cursor[1]))][1]=='redc':
                        health=redchealth
                    if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                        health=bluchealth
                if flip==2:
                    if tiles[((cursor[0],cursor[1]))][1]=='redc':
                        health=bluchealth
                    if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                        health=redchealth
                if tiles[((cursor[0], cursor[1]))][1] == 'redu' or tiles[((cursor[0], cursor[1]))][1] == 'bluu':
                    health = 10
                if tiles[((cursor[0], cursor[1]))][1] == 'redb' or tiles[((cursor[0], cursor[1]))][1] == 'blub':
                    health = 10
                if tiles[((cursor[0], cursor[1]))][1] == 'redg' or tiles[((cursor[0], cursor[1]))][1] == 'blug':
                    health = 10
                if tiles[((cursor[0], cursor[1]))][1] == 'reds' or tiles[((cursor[0], cursor[1]))][1] == 'blus':
                    health = 10
            except:
                health = 0
            if len(str(health)) == 1:
                screen.blit(text4, (14, 330))
            if len(str(health)) > 1:
                screen.blit(text4, (8, 330))
            pygame.display.flip()
            fpsClock.tick(FPS)


            while atkormov==True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == K_e:
                        atkormov=False
                        hopbar=False
                    elif event.type == pygame.KEYDOWN and event.key == K_d:
                        atkormov=False
                        hopbar=False
                        fight=True
                    elif event.type == pygame.KEYDOWN and event.key == K_a:
                        atkormov=False
                        hopbar=False
                        if (cursor[0], cursor[1]) in movelist:
                            print('no')
                        else:
                            dude=tiles[((cursor[0], cursor[1]))][1]
                            del tiles[((cursor[0], cursor[1]))][1]
                            commands=[]
                            movement=True
                            if dude == 'rk':
                                movecount = 3
                            elif dude == 'rm':
                                movecount = 5
                            elif dude == 'rc':
                                movecount = 2
                            elif dude == 'rs':
                                movecount = 4
                screen.blit(ui1, (0, 320))
                temp1 = 1
                temp2 = 1
                for i in range(14):
                    temp2 = 1
                    t1 = temp1 * 32 - 32
                    for i in range(10):
                        t2 = temp2 * 32 - 32
                        if "f1" in tiles[(temp1, temp2)]:
                            screen.blit(f1, (t1, t2))
                        if "f2" in tiles[(temp1, temp2)]:
                            screen.blit(f2, (t1, t2))
                        if flip==1:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                        elif flip==2:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                        temp2 += 1
                    temp1 += 1
                screen.blit(c, ((cursor[0] * 32 - 33), (cursor[1] * 32 - 33)))
                text3 = text.render(str(ap), 6, WHITE)
                if len(str(ap)) == 1:
                    screen.blit(text3, (415, 340))
                if len(str(ap)) == 2:
                    screen.blit(text3, (405, 340))
                text2 = text.render(str(whichmoney), 6, WHITE)
                if len(str(whichmoney)) == 1:
                    screen.blit(text2, (415, 320))
                if len(str(whichmoney)) == 2:
                    screen.blit(text2, (405, 320))
                if len(str(whichmoney)) == 3:
                    screen.blit(text2, (395, 320))
                text4 = text.render(str(health), 6, WHITE)
                try:
                    if tiles[((cursor[0], cursor[1]))][1] == 'rk' or tiles[((cursor[0], cursor[1]))][1] == 'bk':
                        health = 6
                    if tiles[((cursor[0], cursor[1]))][1] == 'rm' or tiles[((cursor[0], cursor[1]))][1] == 'bm':
                        health = 4
                    if tiles[((cursor[0], cursor[1]))][1] == 'rs' or tiles[((cursor[0], cursor[1]))][1] == 'bs':
                        health = 5
                    if tiles[((cursor[0], cursor[1]))][1] == 'rc' or tiles[((cursor[0], cursor[1]))][1] == 'bc':
                        health = 7
                    if flip==1:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=redchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=bluchealth
                    if flip==2:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=bluchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=redchealth
                    if tiles[((cursor[0], cursor[1]))][1] == 'redu' or tiles[((cursor[0], cursor[1]))][1] == 'bluu':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redb' or tiles[((cursor[0], cursor[1]))][1] == 'blub':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redg' or tiles[((cursor[0], cursor[1]))][1] == 'blug':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'reds' or tiles[((cursor[0], cursor[1]))][1] == 'blus':
                        health = 10
                except:
                    health = 0
                if len(str(health)) == 1:
                    screen.blit(text4, (14, 330))
                if len(str(health)) > 1:
                    screen.blit(text4, (8, 330))
                pygame.display.flip()
                fpsClock.tick(FPS)


            while fight==True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == K_w:
                        whicharrow=arru
                    elif event.type == pygame.KEYDOWN and event.key == K_s:
                        whicharrow=arrd
                    elif event.type == pygame.KEYDOWN and event.key == K_a:
                        whicharrow=arrl
                    elif event.type == pygame.KEYDOWN and event.key == K_d:
                        whicharrow=arrr
                    elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
                        pchu.play()
                        fightlist.append((cursor[0], cursor[1]))
                        try:
                            if len(tiles[((cursor[0] + 1, cursor[1]))]) == 2 and whicharrow==arrr:
                                if tiles[((cursor[0] + 1, cursor[1]))][1] in enemyunits or tiles[((cursor[0] + 1, cursor[1]))][1] in enemystruct:
                                    ap-=1
                                    templist=[health,(cursor[0] + 1, cursor[1])]
                                    dmg.append(templist)
                                    fight = False
                                    hopbar = False
                            elif len(tiles[((cursor[0] - 1, cursor[1]))]) == 2 and whicharrow==arrl:
                                if tiles[((cursor[0] - 1, cursor[1]))][1] in enemyunits or tiles[((cursor[0] - 1, cursor[1]))][1] in enemystruct:
                                    ap-=1
                                    templist=[health,(cursor[0] - 1, cursor[1])]
                                    dmg.append(templist)
                                    fight = False
                                    hopbar = False
                            elif len(tiles[((cursor[0], cursor[1] + 1))]) == 2 and whicharrow==arrd:
                                if tiles[((cursor[0], cursor[1] + 1))][1] in enemyunits or tiles[((cursor[0], cursor[1] + 1))][1] in enemystruct:
                                    ap-=1
                                    templist=[health,(cursor[0], cursor[1] + 1)]
                                    dmg.append(templist)
                                    fight = False
                                    hopbar = False
                            elif len(tiles[((cursor[0], cursor[1] - 1))]) == 2 and whicharrow==arru:
                                if tiles[((cursor[0], cursor[1] - 1))][1] in enemyunits or tiles[((cursor[0], cursor[1] - 1))][1] in enemystruct:
                                    ap-=1
                                    templist=[health,(cursor[0], cursor[1] - 1)]
                                    dmg.append(templist)
                                    fight = False
                                    hopbar = False
                        except:
                            pass
                    elif event.type == pygame.KEYDOWN and event.key == K_e:
                        fight=False
                        hopbar=False
                screen.blit(ui1, (0, 320))
                temp1 = 1
                temp2 = 1
                for i in range(14):
                    temp2 = 1
                    t1 = temp1 * 32 - 32
                    for i in range(10):
                        t2 = temp2 * 32 - 32
                        if "f1" in tiles[(temp1, temp2)]:
                            screen.blit(f1, (t1, t2))
                        if "f2" in tiles[(temp1, temp2)]:
                            screen.blit(f2, (t1, t2))
                        if flip==1:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                        elif flip==2:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                        temp2 += 1
                    temp1 += 1
                if len(tiles[((cursor[0], cursor[1]))]) == 1:
                    screen.blit(bld, (36, 320))
                elif len(tiles[((cursor[0], cursor[1]))]) == 2 and tiles[((cursor[0], cursor[1]))][1] in unitmakers:
                    screen.blit(untm, (36, 320))
                screen.blit(c, ((cursor[0] * 32 - 33), (cursor[1] * 32 - 33)))
                text3 = text.render(str(ap), 6, WHITE)
                if len(str(ap)) == 1:
                    screen.blit(text3, (415, 340))
                if len(str(ap)) == 2:
                    screen.blit(text3, (405, 340))
                text2 = text.render(str(whichmoney), 6, WHITE)
                if len(str(whichmoney)) == 1:
                    screen.blit(text2, (415, 320))
                if len(str(whichmoney)) == 2:
                    screen.blit(text2, (405, 320))
                if len(str(whichmoney)) == 3:
                    screen.blit(text2, (395, 320))
                text4 = text.render(str(health), 6, WHITE)
                try:
                    if tiles[((cursor[0], cursor[1]))][1] == 'rk' or tiles[((cursor[0], cursor[1]))][1] == 'bk':
                        health = 6
                    if tiles[((cursor[0], cursor[1]))][1] == 'rm' or tiles[((cursor[0], cursor[1]))][1] == 'bm':
                        health = 4
                    if tiles[((cursor[0], cursor[1]))][1] == 'rs' or tiles[((cursor[0], cursor[1]))][1] == 'bs':
                        health = 5
                    if tiles[((cursor[0], cursor[1]))][1] == 'rc' or tiles[((cursor[0], cursor[1]))][1] == 'bc':
                        health = 7
                    if flip==1:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=redchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=bluchealth
                    if flip==2:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=bluchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=redchealth
                    if tiles[((cursor[0], cursor[1]))][1] == 'redu' or tiles[((cursor[0], cursor[1]))][1] == 'bluu':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redb' or tiles[((cursor[0], cursor[1]))][1] == 'blub':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redg' or tiles[((cursor[0], cursor[1]))][1] == 'blug':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'reds' or tiles[((cursor[0], cursor[1]))][1] == 'blus':
                        health = 10
                except:
                    health = 0
                if len(str(health)) == 1:
                    screen.blit(text4, (14, 330))
                if len(str(health)) > 1:
                    screen.blit(text4, (8, 330))
                try:
                    if whicharrow==arru:
                        screen.blit(whicharrow, ((cursor[0] * 32 - 19), (cursor[1] * 32 - 42)))
                    if whicharrow==arrd:
                        screen.blit(whicharrow, ((cursor[0] * 32 - 19), (cursor[1] * 32 )))
                    if whicharrow==arrl:
                        screen.blit(whicharrow, ((cursor[0] * 32 - 42), (cursor[1] * 32 - 19)))
                    if whicharrow==arrr:
                        screen.blit(whicharrow, ((cursor[0] * 32), (cursor[1] * 32 - 19)))
                except:
                    pass
                pygame.display.flip()
                fpsClock.tick(FPS)


            while dudebar==True:
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == K_e:
                        hopbar = False
                        dudebar = False
                    elif event.type == pygame.KEYDOWN and event.key == K_d:
                        if cursor4<2:
                            cursor4+=1
                    elif event.type == pygame.KEYDOWN and event.key == K_a:
                        if cursor4>1:
                            cursor4-=1
                    elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
                        blep.play()
                        if cursor4==1:
                            if blding=="redb":
                                if whichmoney>=4:
                                    if len(tiles[(cursor[0], cursor[1]-1)])<2:
                                        tiles[(cursor[0], cursor[1]-1)].append('rk')
                                        whichmoney-=4
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap-=1
                                        dudebar=False
                                    elif len(tiles[(cursor[0], cursor[1]+1)])<2:
                                        tiles[(cursor[0], cursor[1]+1)].append('rk')
                                        whichmoney-=4
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0]-1, cursor[1])])<2:
                                        tiles[(cursor[0]-1, cursor[1])].append('rk')
                                        whichmoney-=4
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0]+1, cursor[1])])<2:
                                        tiles[(cursor[0]+1, cursor[1])].append('rk')
                                        whichmoney-=4
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    else:
                                        dudebar=False
                            elif blding=="redg":
                                if whichmoney>=3:
                                    if len(tiles[(cursor[0], cursor[1]-1)])<2:
                                        tiles[(cursor[0], cursor[1]-1)].append('rs')
                                        whichmoney-=3
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0], cursor[1]+1)])<2:
                                        tiles[(cursor[0], cursor[1]+1)].append('rs')
                                        whichmoney-=3
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0]-1, cursor[1])])<2:
                                        tiles[(cursor[0]-1, cursor[1])].append('rs')
                                        whichmoney-=3
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0]+1, cursor[1])])<2:
                                        tiles[(cursor[0]+1, cursor[1])].append('rs')
                                        whichmoney-=3
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    else:
                                        dudebar=False

                        elif cursor4==2:
                            if blding=="redb":
                                if whichmoney>=6:
                                    if len(tiles[(cursor[0], cursor[1]-1)])<2:
                                        tiles[(cursor[0], cursor[1]-1)].append('rm')
                                        whichmoney-=6
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0], cursor[1]+1)])<2:
                                        tiles[(cursor[0], cursor[1]+1)].append('rm')
                                        whichmoney-=6
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0]-1, cursor[1])])<2:
                                        tiles[(cursor[0]-1, cursor[1])].append('rm')
                                        whichmoney-=6
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0]+1, cursor[1])])<2:
                                        tiles[(cursor[0]+1, cursor[1])].append('rm')
                                        whichmoney-=6
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    else:
                                        dudebar=False
                            elif blding=="redg":
                                if whichmoney>=5:
                                    if len(tiles[(cursor[0], cursor[1]-1)])<2:
                                        tiles[(cursor[0], cursor[1]-1)].append('rc')
                                        whichmoney-=5
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0], cursor[1]+1)])<2:
                                        tiles[(cursor[0], cursor[1]+1)].append('rc')
                                        whichmoney-=5
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0]-1, cursor[1])])<2:
                                        tiles[(cursor[0]-1, cursor[1])].append('rc')
                                        whichmoney-=5
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    elif len(tiles[(cursor[0]+1, cursor[1])])<2:
                                        tiles[(cursor[0]+1, cursor[1])].append('rc')
                                        whichmoney-=5
                                        if flip == 1:
                                            money=whichmoney
                                        elif flip == 2:
                                            money2=whichmoney
                                        ap -= 1
                                        dudebar=False
                                    else:
                                        dudebar=False
                temp1 = 1
                temp2 = 1
                for i in range(14):
                    temp2 = 1
                    t1 = temp1 * 32 - 32
                    for i in range(10):
                        t2 = temp2 * 32 - 32
                        if "f1" in tiles[(temp1, temp2)]:
                            screen.blit(f1, (t1, t2))
                        if "f2" in tiles[(temp1, temp2)]:
                            screen.blit(f2, (t1, t2))
                        if flip==1:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                        elif flip==2:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                        temp2 += 1
                    temp1 += 1
                screen.blit(ui1, (0, 320))
                if blding=="redb":
                    screen.blit(unis,(191,129))
                    screen.blit(rk,(192,130))
                    screen.blit(rm,(224,130))
                if blding=="redg":
                    screen.blit(unig,(191,129))
                    screen.blit(rs,(192,130))
                    screen.blit(rc,(224,130))
                if cursor4==1:
                    screen.blit(c,(191,129))
                if cursor4==2:
                    screen.blit(c,(223,129))
                text2 = text.render(str(whichmoney), 6, WHITE)
                if len(str(whichmoney)) == 1:
                    screen.blit(text2, (415, 320))
                if len(str(whichmoney)) == 2:
                    screen.blit(text2, (405, 320))
                if len(str(whichmoney)) == 3:
                    screen.blit(text2, (395, 320))
                text3=text.render(str(ap),6,WHITE)
                if len(str(ap))==1:
                    screen.blit(text3,(415,340))
                if len(str(ap))==2:
                    screen.blit(text3,(405,340))
                text4 = text.render(str(health), 6, WHITE)
                try:
                    if tiles[((cursor[0], cursor[1]))][1] == 'rk' or tiles[((cursor[0], cursor[1]))][1] == 'bk':
                        health = 6
                    if tiles[((cursor[0], cursor[1]))][1] == 'rm' or tiles[((cursor[0], cursor[1]))][1] == 'bm':
                        health = 4
                    if tiles[((cursor[0], cursor[1]))][1] == 'rs' or tiles[((cursor[0], cursor[1]))][1] == 'bs':
                        health = 5
                    if tiles[((cursor[0], cursor[1]))][1] == 'rc' or tiles[((cursor[0], cursor[1]))][1] == 'bc':
                        health = 7
                    if flip==1:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=redchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=bluchealth
                    if flip==2:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=bluchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=redchealth
                    if tiles[((cursor[0], cursor[1]))][1] == 'redu' or tiles[((cursor[0], cursor[1]))][1] == 'bluu':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redb' or tiles[((cursor[0], cursor[1]))][1] == 'blub':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redg' or tiles[((cursor[0], cursor[1]))][1] == 'blug':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'reds' or tiles[((cursor[0], cursor[1]))][1] == 'blus':
                        health = 10
                except:
                    health = 0
                if len(str(health)) == 1:
                    screen.blit(text4, (14, 330))
                if len(str(health)) > 1:
                    screen.blit(text4, (8, 330))
                pygame.display.flip()
                fpsClock.tick(FPS)



            while movement==True:#take a guess
                if movecount==0:
                    ap-=1
                    movement=False
                    hopbar=False
                    movelist.append((cursor[0],cursor[1]))
                    if dude=='rk':
                        tiles[(cursor[0], cursor[1])].append('rk')
                    elif dude=='rm':
                        tiles[(cursor[0], cursor[1])].append('rm')
                    elif dude=='rc':
                        tiles[(cursor[0], cursor[1])].append('rc')
                    elif dude=='rs':
                        tiles[(cursor[0], cursor[1])].append('rs')
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == K_e:
                        ap-=1
                        movement=False
                        hopbar=False
                        movelist.append((cursor[0], cursor[1]))
                        if dude=='rk':
                            tiles[(cursor[0], cursor[1])].append('rk')
                        elif dude=='rm':
                            tiles[(cursor[0], cursor[1])].append('rm')
                        elif dude=='rc':
                            tiles[(cursor[0], cursor[1])].append('rc')
                        elif dude=='rs':
                            tiles[(cursor[0], cursor[1])].append('rs')
                        movement=False
                        hopbar=False
                    elif event.type == pygame.KEYDOWN and event.key == K_w:
                        if movecount!=0:
                            if cursor[1]>1:
                                cursor[1]-=1
                                if len(tiles[(cursor[0], cursor[1])]) == 2:
                                    cursor[1]+=1
                                else:
                                    movecount-=1
                    elif event.type == pygame.KEYDOWN and event.key == K_a:
                        if movecount!=0:
                            if cursor[0]>1:
                                cursor[0]-=1
                                if len(tiles[(cursor[0], cursor[1])]) == 2:
                                    cursor[0]+=1
                                else:
                                    movecount-=1
                    elif event.type == pygame.KEYDOWN and event.key == K_s:
                        if movecount!=0:
                            if cursor[1]<10:
                                cursor[1]+=1
                                if len(tiles[(cursor[0], cursor[1])]) == 2:
                                    cursor[1]-=1
                                else:
                                    movecount-=1
                    elif event.type == pygame.KEYDOWN and event.key == K_d:
                        if movecount!=0:
                            if cursor[0]<14:
                                cursor[0]+=1
                                if len(tiles[(cursor[0], cursor[1])]) == 2:
                                    cursor[0]-=1
                                else:
                                    movecount-=1
                    elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
                        if len(tiles[(cursor[0], cursor[1])]) < 2:
                            if dude=='rk':
                                tiles[(cursor[0], cursor[1])].append('rk')
                            elif dude=='rm':
                                tiles[(cursor[0], cursor[1])].append('rm')
                            elif dude=='rc':
                                tiles[(cursor[0], cursor[1])].append('rc')
                            elif dude=='rs':
                                tiles[(cursor[0], cursor[1])].append('rs')
                            ap-=1
                            movement=False
                            hopbar=False
                screen.blit(ui1, (0, 320))
                temp1 = 1
                temp2 = 1
                for i in range(14):
                    temp2 = 1
                    t1 = temp1 * 32 - 32
                    for i in range(10):
                        t2 = temp2 * 32 - 32
                        if "f1" in tiles[(temp1, temp2)]:
                            screen.blit(f1, (t1, t2))
                        if "f2" in tiles[(temp1, temp2)]:
                            screen.blit(f2, (t1, t2))
                        if flip==1:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                        elif flip==2:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                        temp2 += 1
                    temp1 += 1
                if dude=='rk':
                    screen.blit(rk, ((cursor[0] * 32 - 32), (cursor[1] * 32 - 32)))
                elif dude=='rm':
                    screen.blit(rm, ((cursor[0] * 32 - 32), (cursor[1] * 32 - 32)))
                elif dude=='rc':
                    screen.blit(rc, ((cursor[0] * 32 - 32), (cursor[1] * 32 - 32)))
                elif dude=='rs':
                    screen.blit(rs, ((cursor[0] * 32 - 32), (cursor[1] * 32 - 32)))
                text2 = text.render(str(whichmoney), 6, WHITE)
                if len(str(whichmoney)) == 1:
                    screen.blit(text2, (415, 320))
                if len(str(whichmoney)) == 2:
                    screen.blit(text2, (405, 320))
                if len(str(whichmoney)) == 3:
                    screen.blit(text2, (395, 320))
                text3=text.render(str(ap),6,WHITE)
                if len(str(ap))==1:
                    screen.blit(text3,(415,340))
                if len(str(ap))==2:
                    screen.blit(text3,(405,340))
                text4 = text.render(str(health), 6, WHITE)
                try:
                    if tiles[((cursor[0], cursor[1]))][1] == 'rk' or tiles[((cursor[0], cursor[1]))][1] == 'bk':
                        health = 6
                    if tiles[((cursor[0], cursor[1]))][1] == 'rm' or tiles[((cursor[0], cursor[1]))][1] == 'bm':
                        health = 4
                    if tiles[((cursor[0], cursor[1]))][1] == 'rs' or tiles[((cursor[0], cursor[1]))][1] == 'bs':
                        health = 5
                    if tiles[((cursor[0], cursor[1]))][1] == 'rc' or tiles[((cursor[0], cursor[1]))][1] == 'bc':
                        health = 7
                    if flip==1:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=redchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=bluchealth
                    if flip==2:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=bluchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=redchealth
                    if tiles[((cursor[0], cursor[1]))][1] == 'redu' or tiles[((cursor[0], cursor[1]))][1] == 'bluu':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redb' or tiles[((cursor[0], cursor[1]))][1] == 'blub':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redg' or tiles[((cursor[0], cursor[1]))][1] == 'blug':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'reds' or tiles[((cursor[0], cursor[1]))][1] == 'blus':
                        health = 10
                except:
                    health = 0
                if len(str(health)) == 1:
                    screen.blit(text4, (14, 330))
                if len(str(health)) > 1:
                    screen.blit(text4, (8, 330))
                pygame.display.flip()
                fpsClock.tick(FPS)


            while stopbar==True:#build menu
                for event in pygame.event.get():
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN and event.key == K_SPACE:
                        ham.play()
                        if len(tiles[(cursor[0], cursor[1])])<2:
                            if cursor2==1:
                                if whichmoney>=5:
                                    tiles[(cursor[0], cursor[1])].append('reds')
                                    whichmoney-=5
                                    if flip == 1:
                                        money=whichmoney
                                    elif flip == 2:
                                        money2=whichmoney
                                    ap-=1
                            elif cursor2==2:
                                if whichmoney>=7:
                                    tiles[(cursor[0], cursor[1])].append('redb')
                                    whichmoney-=7
                                    if flip == 1:
                                        money=whichmoney
                                    elif flip == 2:
                                        money2=whichmoney
                                    ap-=1
                            elif cursor2==3:
                                if whichmoney>=6:
                                    tiles[(cursor[0], cursor[1])].append('redg')
                                    whichmoney-=6
                                    if flip == 1:
                                        money=whichmoney
                                    elif flip == 2:
                                        money2=whichmoney
                                    ap-=1
                            elif cursor2==4:
                                if whichmoney>=4:
                                    tiles[(cursor[0], cursor[1])].append('redu')
                                    whichmoney-=4
                                    if flip == 1:
                                        money=whichmoney
                                    elif flip == 2:
                                        money2=whichmoney
                                    ap-=1
                        cursor2=1
                        hopbar=False
                        stopbar=False
                    elif event.type == pygame.KEYDOWN and event.key == K_e:
                        hopbar=False
                        stopbar=False
                    elif event.type == pygame.KEYDOWN and event.key == K_d:
                        if cursor2<4:
                            cursor2+=1
                    elif event.type == pygame.KEYDOWN and event.key == K_a:
                        if cursor2>1:
                            cursor2-=1
                screen.blit(ui1,(0,320))
                temp1=1
                temp2=1
                for i in range(14):
                    temp2 = 1
                    t1 = temp1 * 32 - 32
                    for i in range(10):
                        t2 = temp2 * 32 - 32
                        if "f1" in tiles[(temp1,temp2)]:
                            screen.blit(f1,(t1,t2))
                        if "f2" in tiles[(temp1, temp2)]:
                            screen.blit(f2,(t1,t2))
                        if flip==1:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                        elif flip==2:
                            if "redc" in tiles[(temp1, temp2)]:
                                screen.blit(bluc, (t1, t2))
                            if "bluc" in tiles[(temp1, temp2)]:
                                screen.blit(redc, (t1, t2))
                            if "reds" in tiles[(temp1, temp2)]:
                                screen.blit(blus, (t1, t2))
                            if "blus" in tiles[(temp1, temp2)]:
                                screen.blit(reds, (t1, t2))
                            if "blub" in tiles[(temp1, temp2)]:
                                screen.blit(redb, (t1, t2))
                            if "redb" in tiles[(temp1, temp2)]:
                                screen.blit(blub, (t1, t2))
                            if "redg" in tiles[(temp1, temp2)]:
                                screen.blit(blug, (t1, t2))
                            if "blug" in tiles[(temp1, temp2)]:
                                screen.blit(redg, (t1, t2))
                            if "bluu" in tiles[(temp1, temp2)]:
                                screen.blit(redu, (t1, t2))
                            if "redu" in tiles[(temp1, temp2)]:
                                screen.blit(bluu, (t1, t2))
                            if "bk" in tiles[(temp1, temp2)]:
                                screen.blit(rk, (t1, t2))
                            if "rk" in tiles[(temp1, temp2)]:
                                screen.blit(bk, (t1, t2))
                            if "bm" in tiles[(temp1, temp2)]:
                                screen.blit(rm, (t1, t2))
                            if "rm" in tiles[(temp1, temp2)]:
                                screen.blit(bm, (t1, t2))
                            if "bs" in tiles[(temp1, temp2)]:
                                screen.blit(rs, (t1, t2))
                            if "rs" in tiles[(temp1, temp2)]:
                                screen.blit(bs, (t1, t2))
                            if "bc" in tiles[(temp1, temp2)]:
                                screen.blit(rc, (t1, t2))
                            if "rc" in tiles[(temp1, temp2)]:
                                screen.blit(bc, (t1, t2))
                        temp2 += 1
                    temp1 += 1
                screen.blit(c, ((cursor[0] * 32 - 33), (cursor[1] * 32 - 33)))
                screen.blit(blds,(159,129))
                screen.blit(reds,(160,130))
                screen.blit(redb,(192,130))
                screen.blit(redg,(224,130))
                screen.blit(redu,(256,130))
                if cursor2==1:
                    screen.blit(c,(159,129))
                if cursor2==2:
                    screen.blit(c,(191,129))
                if cursor2==3:
                    screen.blit(c,(223,129))
                if cursor2==4:
                    screen.blit(c,(255,129))
                text2=text.render(str(whichmoney),6,WHITE)
                if len(str(whichmoney))==1:
                    screen.blit(text2,(415,320))
                if len(str(whichmoney))==2:
                    screen.blit(text2,(405,320))
                if len(str(whichmoney))==3:
                    screen.blit(text2,(395,320))
                text3=text.render(str(ap),6,WHITE)
                if len(str(ap))==1:
                    screen.blit(text3,(415,340))
                if len(str(ap))==2:
                    screen.blit(text3,(405,340))
                    text4 = text.render(str(health), 6, WHITE)
                try:
                    if tiles[((cursor[0], cursor[1]))][1] == 'rk' or tiles[((cursor[0], cursor[1]))][1] == 'bk':
                        health = 6
                    if tiles[((cursor[0], cursor[1]))][1] == 'rm' or tiles[((cursor[0], cursor[1]))][1] == 'bm':
                        health = 4
                    if tiles[((cursor[0], cursor[1]))][1] == 'rs' or tiles[((cursor[0], cursor[1]))][1] == 'bs':
                        health = 5
                    if tiles[((cursor[0], cursor[1]))][1] == 'rc' or tiles[((cursor[0], cursor[1]))][1] == 'bc':
                        health = 7
                    if flip==1:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=redchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=bluchealth
                    if flip==2:
                        if tiles[((cursor[0],cursor[1]))][1]=='redc':
                            health=bluchealth
                        if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                            health=redchealth
                    if tiles[((cursor[0], cursor[1]))][1] == 'redu' or tiles[((cursor[0], cursor[1]))][1] == 'bluu':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redb' or tiles[((cursor[0], cursor[1]))][1] == 'blub':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'redg' or tiles[((cursor[0], cursor[1]))][1] == 'blug':
                        health = 10
                    if tiles[((cursor[0], cursor[1]))][1] == 'reds' or tiles[((cursor[0], cursor[1]))][1] == 'blus':
                        health = 10
                except:
                    health = 0
                if len(str(health)) == 1:
                    screen.blit(text4, (14, 330))
                if len(str(health)) > 1:
                    screen.blit(text4, (8, 330))
                pygame.display.flip()
                fpsClock.tick(FPS)



        if len(tiles[((cursor[0],cursor[1]))])==1:
            screen.blit(bld,(36,320))
        elif len(tiles[((cursor[0],cursor[1]))])==2 and tiles[((cursor[0],cursor[1]))][1] in unitmakers:
            screen.blit(untm,(36,320))
        elif len(tiles[((cursor[0], cursor[1]))]) == 2 and tiles[((cursor[0], cursor[1]))][1] in units:
            screen.blit(mov, (36, 320))
            try:
                if len(tiles[((cursor[0]+1,cursor[1]))])==2:
                    if tiles[((cursor[0]+1,cursor[1]))][1] in enemyunits or tiles[((cursor[0]+1,cursor[1]))][1] in enemystruct:
                        screen.blit(atk, (72, 320))
                elif len(tiles[((cursor[0]-1,cursor[1]))])==2:
                    if tiles[((cursor[0]-1,cursor[1]))][1] in enemyunits or tiles[((cursor[0]-1,cursor[1]))][1] in enemystruct:
                        screen.blit(atk, (72, 320))
                elif len(tiles[((cursor[0],cursor[1]+1))])==2:
                    if tiles[((cursor[0],cursor[1]+1))][1] in enemyunits or tiles[((cursor[0],cursor[1]+1))][1] in enemystruct:
                        screen.blit(atk, (72, 320))
                elif len(tiles[((cursor[0],cursor[1]-1))])==2:
                    if tiles[((cursor[0],cursor[1]-1))][1] in enemyunits or tiles[((cursor[0],cursor[1]-1))][1] in enemystruct:
                        screen.blit(atk, (72, 320))
            except:
                pass
        screen.blit(c,((cursor[0]*32-33),(cursor[1]*32-33)))
        text3=text.render(str(ap),6,WHITE)
        if len(str(ap))==1:
            screen.blit(text3,(415,340))
        if len(str(ap))==2:
            screen.blit(text3,(405,340))
        text2=text.render(str(whichmoney),6,WHITE)
        if len(str(whichmoney))==1:
            screen.blit(text2,(415,320))
        if len(str(whichmoney))==2:
            screen.blit(text2,(405,320))
        if len(str(whichmoney))==3:
            screen.blit(text2,(395,320))
        text4=text.render(str(health),6,WHITE)
        try:
            if tiles[((cursor[0],cursor[1]))][1]=='rk' or tiles[((cursor[0],cursor[1]))][1]=='bk':
                health=6
            if tiles[((cursor[0],cursor[1]))][1]=='rm' or tiles[((cursor[0],cursor[1]))][1]=='bm':
                health=4
            if tiles[((cursor[0],cursor[1]))][1]=='rs' or tiles[((cursor[0],cursor[1]))][1]=='bs':
                health=5
            if tiles[((cursor[0],cursor[1]))][1]=='rc' or tiles[((cursor[0],cursor[1]))][1]=='bc':
                health=7
            if flip==1:
                if tiles[((cursor[0],cursor[1]))][1]=='redc':
                    health=redchealth
                if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                    health=bluchealth
            if flip==2:
                if tiles[((cursor[0],cursor[1]))][1]=='redc':
                    health=bluchealth
                if tiles[((cursor[0],cursor[1]))][1]=='bluc':
                    health=redchealth
            if tiles[((cursor[0],cursor[1]))][1]=='redu' or tiles[((cursor[0],cursor[1]))][1]=='bluu':
                health=10
            if tiles[((cursor[0],cursor[1]))][1]=='redb' or tiles[((cursor[0],cursor[1]))][1]=='blub':
                health=10
            if tiles[((cursor[0],cursor[1]))][1]=='redg' or tiles[((cursor[0],cursor[1]))][1]=='blug':
                health=10
            if tiles[((cursor[0],cursor[1]))][1]=='reds' or tiles[((cursor[0],cursor[1]))][1]=='blus':
                health=10
        except:
            health=0
        if len(str(health))==1:
            screen.blit(text4,(14,330))
        if len(str(health))>1:
            screen.blit(text4,(8,330))
        pygame.display.flip()
        fpsClock.tick(FPS)
    else:
        temp=c
        c=c2
        c2=temp
        movelist=[]
        fightlist=[]
        resolution={}
        templist2=[]
        singlerun=0
        while dmg:
            if tuple(dmg[0][1]) in resolution.keys():
                resolution[tuple(dmg[0][1])]+=dmg[0][0]
                del dmg[0]
            else:
                resolution[tuple(dmg[0][1])]=dmg[0][0]
                del dmg[0]
        for i in resolution:
            try:
                if tiles[i][1] == 'rk' or tiles[i][1] == 'bk':
                    health = 6
                if tiles[i][1] == 'rm' or tiles[i][1] == 'bm':
                    health = 4
                if tiles[i][1] == 'rs' or tiles[i][1] == 'bs':
                    health = 5
                if tiles[i][1] == 'rc' or tiles[i][1] == 'bc':
                    health = 7
                if tiles[i][1] == 'redu' or tiles[i][1] == 'bluu':
                    health = 10
                if tiles[i][1] == 'redb' or tiles[i][1] == 'blub':
                    health = 10
                if tiles[i][1] == 'redg' or tiles[i][1] == 'blug':
                    health = 10
                if tiles[i][1] == 'reds' or tiles[i][1] == 'blus':
                    health = 10
            except:
                health = 0
            if tiles[i][1] == 'bluc':
                if flip==1:
                    bluchealth-=resolution[i]
                if flip==2:
                    redchealth-=resolution[i]
            elif resolution[i]>=health:
                del tiles[i][1]
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                turn = 1
        for i in tiles.values():
            if "redc" in i:
                whichmoney += 2
            if "reds" in i:
                whichmoney += 3
            if "redu" in i:
                whichmoney += 1
            if flip == 1:
                money = whichmoney
            elif flip == 2:
                money2 = whichmoney
        if apmax<12:
            apmax+=1
        ap=apmax
        if flip==1:
            if bluchealth<=0:
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == K_e:
                            pygame.quit()
                            sys.exit()
                    screen.blit(win1,(0,0))
                    pygame.display.flip()
                    fpsClock.tick(FPS)
            if redchealth<=0:
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == K_e:
                            pygame.quit()
                            sys.exit()
                    screen.blit(win2,(0,0))
                    pygame.display.flip()
                    fpsClock.tick(FPS)
        if flip==2:
            if bluchealth<=0:
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == K_e:
                            pygame.quit()
                            sys.exit()
                    screen.blit(win2,(0,0))
                    pygame.display.flip()
                    fpsClock.tick(FPS)
            if redchealth<=0:
                while True:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                            sys.exit()
                        elif event.type == pygame.KEYDOWN and event.key == K_e:
                            pygame.quit()
                            sys.exit()
                    screen.blit(win1,(0,0))
                    pygame.display.flip()
                    fpsClock.tick(FPS)
        for i in tiles:
            try:
                if tiles[i][1]=='redc':
                    del tiles[i][1]
                    tiles[i].append('bluc')
                elif tiles[i][1]=='bluc':
                    del tiles[i][1]
                    tiles[i].append('redc')

                if tiles[i][1]=='redg':
                    del tiles[i][1]
                    tiles[i].append('blug')
                elif tiles[i][1]=='blug':
                    del tiles[i][1]
                    tiles[i].append('redg')

                if tiles[i][1]=='reds':
                    del tiles[i][1]
                    tiles[i].append('blus')
                elif tiles[i][1]=='blus':
                    del tiles[i][1]
                    tiles[i].append('reds')

                if tiles[i][1]=='redu':
                    del tiles[i][1]
                    tiles[i].append('bluu')
                elif tiles[i][1]=='bluu':
                    del tiles[i][1]
                    tiles[i].append('redu')

                if tiles[i][1]=='redb':
                    del tiles[i][1]
                    tiles[i].append('blub')
                elif tiles[i][1]=='blub':
                    del tiles[i][1]
                    tiles[i].append('redb')

                if tiles[i][1]=='rk':
                    del tiles[i][1]
                    tiles[i].append('bk')
                elif tiles[i][1]=='bk':
                    del tiles[i][1]
                    tiles[i].append('rk')

                if tiles[i][1]=='rs':
                    del tiles[i][1]
                    tiles[i].append('bs')
                elif tiles[i][1]=='bs':
                    del tiles[i][1]
                    tiles[i].append('rs')

                if tiles[i][1]=='rc':
                    del tiles[i][1]
                    tiles[i].append('bc')
                elif tiles[i][1]=='bc':
                    del tiles[i][1]
                    tiles[i].append('rc')

                if tiles[i][1]=='rm':
                    del tiles[i][1]
                    tiles[i].append('bm')
                elif tiles[i][1]=='bm':
                    del tiles[i][1]
                    tiles[i].append('rm')
            except:
                pass
        pygame.display.flip()
        fpsClock.tick(FPS)
        if flip==1:
            flip=2
        elif flip==2:
            flip=1
        turn=1