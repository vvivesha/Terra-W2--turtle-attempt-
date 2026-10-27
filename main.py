import turtle
import random
import time
print("    STARGAZERS")
time.sleep(0.5)
print("~~~~~~~~~~~~~~~~~")
print("--GAME SETTINGS--")
for gap in range(5):
    print(" ")
t=turtle
t.pendown
yellow = turtle.color("yellow")
silver = turtle.color("silver")
blue = turtle.color("blue")
purple = turtle.color("purple")
red = turtle.color("red")
orange = turtle.color("orange")
green = turtle.color("green")
white = turtle.color("white")
star_colors = [yellow, silver, blue, purple, red, orange, green, white]
skip_settings = input("==>  Randomize game settings? This will skip the rest of the game-settings-questions.  (y/n)")
if skip_settings == "y":
    random.choice(star_colors)
    random.choice(star_location)
    random.choice(star_size)
    random.choice(star_quantity)
    random.choice(leaf_count)
    random.choice(leaf_size)
    random.choice(leaf_location)
    random.choice(leaf_penalizer_count)
print("==>  ")