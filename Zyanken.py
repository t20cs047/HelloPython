'''
Created on 2022/10/14

@author: t20cs047
'''
import random

a = random.randrange(3)
b = random.randrange(3)
if a == 0 :
    if b == 1:
        print('Aの手：グー v.s. Bの手：チョキ -> Aの勝ち')
    elif b == 2:
        print('Aの手：グー v.s. Bの手：パー -> Bの勝ち')
    elif b == 0:
        print('Aの手：グー v.s. Bの手：グー -> 引き分け')
elif a == 1 : 
    if b == 1:
        print('Aの手：チョキ v.s. Bの手：チョキ -> 引き分け')
    elif b == 2:
        print('Aの手：チョキ v.s. Bの手：パー -> Aの勝ち')
    elif b == 0:
        print('Aの手：チョキ v.s. Bの手：グー -> Bの勝ち')
elif a == 2 :
    if b == 1:
        print('Aの手：パー v.s. Bの手：チョキ -> Bの勝ち')
    elif b == 2:
        print('Aの手：パー v.s. Bの手：パー -> 引き分け')
    elif b == 0:
        print('Aの手：パー v.s. Bの手：グー -> Aの勝ち')

def ZyankenRule(x,y):
    z = (x - y + 3) % 3
    if z == 0:
        return "draw"
    elif z == 1:
        return "B is Win"
    else :
        return "A is Win"
    

