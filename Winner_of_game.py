''Write a python program which will say who win in game.The winner is the one which have 2 point.You
should try to find pc number(0-5):if find (your point +=1) otherwise (pc point +=1):'''
from random import *
pc_point = 0 
my_point = 0
pc_num = randint(0,5)
my_num = int(input("Enter your number in range 0-5: "))
find = my_num == pc_num
if find == 1:
    my_point += 1
else:
    pc_point += 1

my_num = int(input("Enter your number too: "))
find = my_num == pc_num
if find == 1:
    my_point += 1
else:
    pc_point += 1

if my_point > pc_point:
    print("pc_point is ",pc_point,"\nyour point is",my_point,"\nPC_NUMBER IS----->",pc_num,"YOU WIN")
else:
    print("pc_point is ",pc_point,"\nyour point is",my_point,"\nPC_NUMBER IS----->",pc_num,"\n YOU LOSE")
