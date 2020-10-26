#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Game of life
original author: Pleiades
second author: maowood
"""

import os
import random
import time


width = 40
height = 40
screen = []
pause = 0


def Init():
    for i in range(height):
        line = []
        for j in range(width):
            if random.random() > 0.8:
                line.append('#')
            else:
                line.append(' ')
        screen.append(line)


def PrintScreen():
    os.system("cls")
    for i in range(height):
        for j in range(width):
            print(screen[i][j] + ' ', end='')
        print('|')


def TryGetCell(i, j):
    i = i % height
    j = j % width
    return screen[i][j]


def GetNearbyCellsCount(i, j):
    nearby = []
    nearby.append(TryGetCell(i - 1, j - 1))
    nearby.append(TryGetCell(i - 1, j))
    nearby.append(TryGetCell(i - 1, j + 1))
    nearby.append(TryGetCell(i, j - 1))
    nearby.append(TryGetCell(i, j + 1))
    nearby.append(TryGetCell(i + 1, j - 1))
    nearby.append(TryGetCell(i + 1, j))
    nearby.append(TryGetCell(i + 1, j + 1))
    return len(list(filter(lambda x: x == '#', nearby)))


def Update():
    newScreen = [[' ' for i in range(width)]for j in range(height)]
    global screen
    for i in range(height):
        for j in range(width):
            count = GetNearbyCellsCount(i, j)
            if count == 3:
                newScreen[i][j] = '#'
            elif count < 2 or count > 3:
                newScreen[i][j] = ' '
            else:
                newScreen[i][j] = screen[i][j]
    screen = newScreen

def Loop():
    Update()
    PrintScreen()


def Start():
    os.system("cls")
    print('== Game of Life ==')
    print('Author: Pleiades')
    print('Press enter...')
    input()
    os.system("cls")
    Init()
    PrintScreen()
    c = input()
    while c != 'q':
        Loop()
        time.sleep(pause)
    print('End')


if __name__ == "__main__":
    Start()
