# IMPORTS
import pygame, sys
from settings.assets import *
from settings.variables import *
from settings.functions import *

pygame.init()
pygame.time.set_timer(pygame.USEREVENT, 1000)

# MAIN LOOP
run = True
while run:    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        # MENU - CHOICE
        if button == 0:
            if button1_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(menu20, (0, 0))
            elif button2_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(menu30, (0, 0))
            elif button3_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(menu45, (0, 0))
            elif button4_rect.collidepoint(pygame.mouse.get_pos()):
                screen.blit(menu60, (0, 0))
            else:
                screen.blit(time_menu, (0, 0))

            # MENU CLICK NAD TIME SETUP
            if event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and button1_rect.collidepoint(pygame.mouse.get_pos()):
                button = 1
                m = 20
                counter = countdown(m)
                text = str(counter)
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and button2_rect.collidepoint(pygame.mouse.get_pos()):
                button = 2
                m = 30
                counter = countdown(m)
                text = str(counter)
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and button3_rect.collidepoint(pygame.mouse.get_pos()):
                button = 3
                m = 45
                counter = countdown(m)
                text = str(counter)
            elif event.type == pygame.MOUSEBUTTONDOWN and pygame.mouse.get_pressed()[0] and button4_rect.collidepoint(pygame.mouse.get_pos()):
                button = 4
                m = 60
                counter = countdown(m)
                text = str(counter)

        # COUNTDOWN AND EXCERCISE CHOICE AFTER TIME˙S UP
        if button > 0: 
            if event.type == pygame.USEREVENT:
                counter -= 1
                if counter > 0:
                    text = str(convert(counter))
                    screen.blit(programer, (0, 0))
                    screen.blit(text_font.render(text, True, (0, 0, 0)),(text_half_screen, 215))
                elif counter == 0:
                    text = f'{my_choice.upper()}'
                    screen.blit(programer2, (0, 0))
                    screen.blit(text_font.render(text, True, (0, 0, 0)),(text_half_screen, 215))
                    write_choice()  
                    alarm.play()
                else:
                    pass

    # REFRESH SCREEN WITH FPS
    pygame.display.update()
    clock.tick(60)