import random

def is_win(player, opponent):
    if ((player.casefold() == 'r' and opponent == 's') 
        or (player.casefold() == 's' and opponent == 'p') 
        or (player.casefold() == 'p' and opponent == 'r')):
        return True
    
def play():
    user = input("Whats you choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user.casefold() not in {'r', 'p', 's'}:
        return "Please select valid options"
    
    if user.casefold() == computer.casefold():
        return "It\'s a tie. Computer selected: " + computer

    elif is_win(user, computer):
        return "You Won! Computer selected: " + computer

    return "You Lose :( Computer selected: " + computer 


print(play())
