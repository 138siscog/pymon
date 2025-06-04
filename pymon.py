import random
import os
import time


level = 1

while True:
    cpu = []
    player = []
    score = 1
    pattern = random.choices(range(1,5), k = level)
    cpu.append(pattern)

    while True:
        print(cpu)
        p1 = int(input())
        player.append(p1)            
        if player == pattern:
            level =+ 1
            score = level
            continue
        elif pattern != cpu:
            print("You Loose")
            print(f"Your Score was {score}")
            break
            
