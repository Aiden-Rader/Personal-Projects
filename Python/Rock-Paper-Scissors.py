import random
import time

startTime = time.time()

def play():

    user = input("Whats your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return 'Its a Draw!\n'

    # r > s, s > p, p > r
    if is_win(user, computer):
        return 'You won!\n'

    if is_win(computer, user):
        return 'You lost!\n'


def is_win(player, opponent):
    # return true if player wins
    # r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') \
            or (player == 'p' and opponent == 'r'):
        return True
    
print(play())

(executionTime) = (time.time() - startTime)
ex = round(executionTime, 2)

print('Execution time in seconds: ' + str(ex))



if executionTime > 2:
    print("Wow that shit is slow as hell boy with your yelly belly pickle looking ass boy\n")
else:
    print("Gee that was pretty fast there buddy!\n")



