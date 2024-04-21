# making an knight :
import pygame
pygame.init()
import workspace.knight_helper as knight_helper

screen = pygame.display.set_mode((401,301))
rects = []

for x in range(1,301,100) :
    for j in range(1,401,100) :
        ret = pygame.Rect(j,x,99,99)
        rects.append(ret)
print(rects)
locked = False
pos = 0
run = True
all_rout = []
locked_pos = False
while run :
    screen.fill((255,255,255))
    for events in pygame.event.get() :
        if events.type == pygame.QUIT :
            run = False
        if events.type == pygame.MOUSEBUTTONDOWN :
            if events.button == 1 :
                if locked == True :
                    real_pos = knight_helper.move_to_pos(pos)
                    all_rout = knight_helper.all_routes(real_pos)
                    locked_pos = pos


    pos_mou = pygame.mouse.get_pos()
    c  = 1
    for x in rects :
        a = x.collidepoint((pos_mou[0],pos_mou[1]))
        if a == True  :
            locked = True
            pos = c
            pygame.draw.rect(screen,(255,0,0),x)
        else :
            pygame.draw.rect(screen, (0, 0, 0), x)
        c += 1
        pygame.draw.rect(screen,(0,0,0),x)
    c = 1
    for x in rects :

        if c in all_rout:
            print(all_rout,c,x)
            pygame.draw.rect(screen, (0, 255, 0), x)

        if c == locked_pos :
            pygame.draw.rect(screen, (255, 255, 0), x)
        c += 1

    pygame.display.update()

