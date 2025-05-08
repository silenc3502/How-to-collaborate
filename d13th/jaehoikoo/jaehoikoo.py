name = 'jaehoikoo'

# random 함수로 dice 생성
import random

# dice를 2번 던져 결과 출력
def roll_dice():
    player_a = random.randint(1, 6)
    player_b = random.randint(1, 6)
    if player_a == player_b:
        print(f'player a: {player_a}, player b:{player_b}')
        print('player a and player b are equal')
    elif player_a > player_b:
        print(f'player a: {player_a}, player b:{player_b}')
        print('player a is greater than player_b')
    else:
        print(f'player a: {player_a}, player b:{player_b}')
        print('player b is greater than player_a')

roll_dice()
