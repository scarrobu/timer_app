import random, pygame

pygame.init()

# TEXT FILE WITH CHOICES
with open("source/text/choice.txt", mode="r") as file:
    for line in file:
        data = [line.replace('\n', '') for line in file]

with open("source/text/log.txt", mode="r") as file:
    lines = file.readlines()

if len(lines) < 1:
    lines = "START"

# VARIABLES
my_choice = random.choice(data)
last_choice = lines[-1]
button = 0
width = 90
height = 45
left = 173
top = [45, 90, 135, 180]
