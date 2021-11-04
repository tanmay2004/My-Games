from random import choice

# Rock Paper Scissors Game!
print ("\nThis is the Rock, Paper, Scissors Game!")

is_user_playing = True
def computer_move():
  return choice(['Rock', 'Paper', 'Scissors'])

computer_score = 0
user_score = 0

while is_user_playing == True:
  comp_rps = computer_move()
  print ("Your score: " + str(user_score) + ", Computer's score: " + str(computer_score))
  print ()
  user_move = input("Please enter what you want to move ('r', 'p' or 's'), or, to finish game and view results, press 'enter': ")
  
  if user_move == "":
    is_user_playing = False
    print ("Game Over!")
    print ("\nFinal scores: ")
    print ("Computer: " + str(computer_score))
    print ("You: " + str(user_score) + "\n")
    
    if computer_score == user_score:
      print ("IT IS A TIE!")
    
    elif user_score > computer_score:
      print ("YOU BEAT THE COMPUTER!")
      
    else:
      print ("THE COMPUTER WINS!")
      
  else:
    user_move = user_move.capitalize()
   
    if user_move == "R":
        user_move = "Rock"
        
    elif user_move == "P":
      user_move = "Paper"
      
    elif user_move == "S":
      user_move = "Scissors"
      
    if user_move not in ('Rock', 'Scissors', 'Paper'):
        print ("I can't understand your answer. Please try again.")
    
    else:
      print ("You chose " + user_move)
      print ("The computer moves " + comp_rps + "\n")
      
      # stating all the possibilities and their outcomes 
      if comp_rps == user_move:
        print ("We both chose the same object!")
        
      elif comp_rps == "Rock":
        if user_move == "Paper":
          print ("YOU WIN! Your paper has covered my rock!")
          user_score += 1
          
        else: 
          print ("I WIN! My rock has broken your scissors!")
          computer_score += 1
        
      elif comp_rps == "Paper":
        if user_move == "Scissors":
          print ("YOU WIN! Your scissors has cut my paper!")
          user_score += 1
         
        else:
          print ("I WIN! My paper has covered your rock!")
          computer_score += 1
      
      else:
        if user_move == "Rock":
          print ("YOU WIN! Your rock has broken my scissors!")
          user_score += 1
         
        else:
          print ("I WIN! My scissors has cut your paper!")
          computer_score += 1
          
# Future Modifications Plan: Game is for limited turns. User can play more if he wants to. Use a for loop instead of while.
