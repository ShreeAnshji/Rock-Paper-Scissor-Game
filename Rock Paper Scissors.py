from random import randint
t=['Rock', 'Paper', 'Scissors']
computer=t[randint(0, 2)]
player=False
while player==False:
    player=input('Enter Rock Paper or Scissor:')
    if (computer==player):
        print('Tie!!')
    elif (player=='Rock'):
        if (computer=='Paper'):
            print('You lose!!', computer, 'Covered', player)
        else:
            print('You Win', player, 'Smashed', computer)
    elif (player=='Paper'):
        if (computer=='Rock'):
            print('You Won!!', player, 'Covered', computer)
        else:
            print('You lose!!', computer, 'Cut', player)
    else:
        if(computer=='Rock'):
            print('You Lose!!', computer, 'Smashed', player)
        else:
            print('You Win!!', player, 'Cut', computer)
    computer=t[randint(0, 2)]
    player=False
        