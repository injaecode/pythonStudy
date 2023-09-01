import random

def compare(p_choice, c_choice):
    if p_choice == c_choice:
        print('draw!!')
    elif (p_choice - c_choice) %3 ==1:
        print('win!!')
    else:
        print('lose!!')

while True:
    rps=['sissor', 'rock', 'paper']
    
    player = int(input('sissor(0)/rock(1)/paper(2)/end(-1): '))
    computer = random.randint(0,2)
    
    if player == -1:
        break
    print(rps[player], rps[computer])
    compare(player, computer)
