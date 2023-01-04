import pygame
from settings.variables import *

pygame.init()

# SET SCREEN AND FPS-TIMER
screen = pygame.display.set_mode((300, 300))
pygame.display.set_caption('Break TIME')
clock = pygame.time.Clock()

# SET FONT AND FONT-SIZE
text_font = pygame.font.Font(None, 50)

# LOAD ALL IMAGES, BUTTONS, TEXTS AND MUSIC
alarm = pygame.mixer.Sound('source/sound/alarm.wav')
alarm.set_volume(0.1)
time_menu_surface = pygame.image.load('source/img/menu.png').convert_alpha()
time_menu = pygame.transform.scale(time_menu_surface, (300, 300))
menu20_surface = pygame.image.load('source/img/menu20.png').convert_alpha()
menu20 = pygame.transform.scale(menu20_surface, (300, 300))
menu30_surface = pygame.image.load('source/img/menu30.png').convert_alpha()
menu30 = pygame.transform.scale(menu30_surface, (300, 300))
menu45_surface = pygame.image.load('source/img/menu45.png').convert_alpha()
menu45 = pygame.transform.scale(menu45_surface, (300, 300))
menu60_surface = pygame.image.load('source/img/menu60.png').convert_alpha()
menu60 = pygame.transform.scale(menu60_surface, (300, 300))
programer_surface = pygame.image.load('source/img/panak.png').convert_alpha()
programer = pygame.transform.scale(programer_surface, (300, 300))
programer2_surface = pygame.image.load('source/img/panak2.png').convert_alpha()
programer2 = pygame.transform.scale(programer2_surface, (300, 300))
text_width, text_height = text_font.size(f'{my_choice}')
text_half_screen = screen.get_width() // 2 - text_width // 2
button1_surf = pygame.Surface((width, height))
button1_rect = button1_surf.get_rect(topleft=(left, top[0]))
button2_surf = pygame.Surface((width, height))
button2_rect = button2_surf.get_rect(topleft=(left, top[1]))
button3_surf = pygame.Surface((width, height))
button3_rect = button3_surf.get_rect(topleft=(left, top[2]))
button4_surf = pygame.Surface((width, height))
button4_rect = button4_surf.get_rect(topleft=(left, top[3]))
