import os
import random

levelSizeX = 30
levelSizeY = 10
level = []

# snakeX = 18
# snakeY = 3


class Snake:
    def __init__(self, sx, sy, slength):
        self.snakeX = sx
        self.snakeY = sy
        self.snakeLength = slength


# colored print
def coloredtext(color, bgcolor, text):
    match color:
        case "RED":
            textcolor = "\033[31m"
        case "GREEN":
            textcolor = "\033[32m"
        case "YELLOW":
            textcolor = "\033[33m"
        case "BLUE":
            textcolor = "\033[34m"
        case "CYAN":
            textcolor = "\033[36m"
        case "PURPLE":
            textcolor = "\033[35m"
        case "PINK":
            textcolor = "\033[91m"
        case "LIGHT_BLUE":
            textcolor = "\033[94m"
        case "GRAY":
            textcolor = "\033[90m"
        case "BLACK":
            textcolor = "\033[30m"
        case "WHITE":
            textcolor = "\033[97m"
        case _:
            textcolor = "\033[97m"

    match bgcolor:
        case "RED":
            backgroundcolor = "\033[41m"
        case "GREEN":
            backgroundcolor = "\033[42m"
        case "YELLOW":
            backgroundcolor = "\033[43m"
        case "BLUE":
            backgroundcolor = "\033[44m"
        case "CYAN":
            backgroundcolor = "\033[46m"
        case "PURPLE":
            backgroundcolor = "\033[45m"
        case "PINK":
            backgroundcolor = "\033[101m"
        case "LIGHT_BLUE":
            backgroundcolor = "\033[104m"
        case "GRAY":
            backgroundcolor = "\033[100m"
        case "BLACK":
            backgroundcolor = "\033[40m"
        case "WHITE":
            backgroundcolor = "\033[107m"
        case _:
            backgroundcolor = "\033[107m"

    return textcolor + backgroundcolor + text + "\033[00m"


def draw():
    os.system('cls')
    for i in range(levelSizeY):
        line = ""
        for i2 in range(levelSizeX):
            if snake.snakeX-1 == i and snake.snakeX-1 == i2:
                line = line + coloredtext("GREEN", "BLACK", "s ")
            else:
                line = line + level[i*levelSizeX + i2] + coloredtext("RED", "BLACK", " ")

        print(line)


def place_apple():
    rand = random.randint(0, levelSizeX * levelSizeY - 1)
    level[rand] = coloredtext("RED", "BLACK", "♦")


def init_level():
    for i in range(levelSizeX * levelSizeY):
        level.insert(i, coloredtext("WHITE", "BLACK", "□"))


# init lv
init_level()
place_apple()

# init snake
snake = Snake(5, 5, 1)
draw()

