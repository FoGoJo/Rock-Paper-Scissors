#Making a simple rock paper scissors game

from random import randint



print("Welcome to the Rock , Paper, Scissors game")
print("\nThe best of three games wins")
#Rock is 1, paper is 2, scissors is 3

choice_comp = ['rock','paper','scissors']
score_comp = 0
score_player = 0
counter = 0
while (counter !=3) :
 #computers choice
 choice = choice_comp[randint(0,2)]
 player_choice = input("Please choose one of the following: rock, paper, or scissors: ")
 if player_choice[0].lower() == choice[0].lower() :
  score_comp = score_comp + 0
  score_player = score_player + 0
  print("\nDraw! No one wins!")
  #Choose Rock versus Paper
 elif player_choice[0].lower() == 'r'  and choice[0].lower() == 'p' :
  score_comp += 1 
  print("\npaper beats rock, you lose this round")
 elif choice[0].lower() == 'r'  and player_choice[0].lower() == 'p' :
  score_player += 1 
  print("\npaper beats rock,you win this round")
  #Choose Rock versus scissors
 elif player_choice[0].lower() == 'r'  and choice[0].lower() == 's' :
  score_player += 1
  print("\nrock beats scissors, you win this round")
 elif choice[0].lower() == 'r'  and player_choice[0].lower() == 's' :
  score_comp += 1 
  print("\nrock beats scissors,you lose this round")
  #Paper versus Scissors
 elif player_choice[0].lower() == 's'  and choice[0].lower() == 'p' :
  score_player += 1
  print("\nscissors beats paper, you win this round")
 elif choice[0].lower() == 's'  and player_choice[0].lower() == 'p' :
  score_comp += 1 
  print("\nscissors beats paper, you lose this round")
 else :
  continue
 counter +=1
 
if score_player > score_comp :
 print("Congratulations you won with a final score {score_p} to {score_c}".format(score_p=score_player, score_c = score_comp))
elif score_player == score_comp :
 print("It was a draw!  with a final score {score_p} to {score_c}".format(score_p=score_player, score_c = score_comp))
else :
 print("Sorry you lost! Final score {score_p} to {score_c}".format(score_p=score_player, score_c = score_comp))
 
 
 
 
 