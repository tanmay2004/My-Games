import sys

from getpass import getpass
from random import randint

def random_num(board):
  return randint(0, len(board) - 1)
    
player1_board = [] # computer's board to guess, user's to place ship, it is user's board.
player2_board = [] # user's board to guess, computer's to place ship, it is computer's board.

def print_board(board):
  for row in board:
    print (" ".join(row))
  
# making the boards (5x5) of both players and storing them in variables, which are to be used in both game modes.
for x in range(5):
  player1_board.append(["O"] * 5)
  player2_board.append(["O"] * 5)

game_mode = ""
game_mode = input("To play against computer, type 'computer', to play in multiplayer mode press the 'enter' key: ").lower()

if game_mode == "computer" or game_mode == "c":
  print ("\nYou chose computer mode! To exit game, you can simply press the 'enter' key twice when guessing the location of my ship. \n")
  print ("Your board:")
  print_board(player1_board)

  computer_guess_row = random_num(player2_board)
  computer_guess_col = random_num(player2_board) 

  print ("\nComputer's board:")
  print_board(player2_board)
  
else:
  print ("\nYou chose multiplayer mode! To exit game, press Ctrl + C. \n")
  player1_name = input("Enter player 1's name: ")
  player2_name = input("Enter player 2's name: ")
  print ()
  print (player1_name + "'s board:")
  print_board(player1_board)

  print ()

  print (player2_name + "'s board:")
  print_board(player2_board) 
  print ("\nAll your guesses will be shown marked as an 'X' on the board (your opponent's) displayed below your guess.")

turn = 0

if game_mode == "computer" or game_mode == "c":
  # Ask the user to specify their ship coordinates
  print ("\nEnter your ship coordinates (any 2 numbers between 1 to 5) - ") 

  computer_ship_row = random_num(player2_board) 
  computer_ship_col = random_num(player2_board) 
  
  user_coordinates = False
  
  while user_coordinates == False:
    user_ship_row = int(input("Row: "))
    user_ship_col = int(input("Column: "))
  
    if (user_ship_row > 5 or user_ship_row < 1) or (user_ship_col > 5 or user_ship_col < 1):
      print ("\nYou entered invalid ship coordinates. Please try again. \n")
     
    else:
      user_coordinates = True
      user_ship_row -= 1
      user_ship_col -= 1

else:
  correct_ship_coordinates_player1 = False
  correct_ship_coordinates_player2 = False
  
  while correct_ship_coordinates_player1 == False:
    # Ask players 1 and 2 to specify their ship coordinates and store them in a variable
    print ("\n" + player1_name + ", place your ship on your board by entering your ship's coordinates (any 2 numbers between 1 to 5) - ")

    # Preventing opponent from seeing player1_ship_row input and player1_ship_col input 
    player1_ship_row = int(getpass(prompt = "Row: "))
    player1_ship_col = int(getpass(prompt = "Column: ")) 
    
    if (player1_ship_row > 5 or player1_ship_row < 1) or (player1_ship_col > 5 or player1_ship_col < 1):
      print ("\n" + player1_name + ", you entered invalid ship coordinates. Please try again.") 
      
    else:
      correct_ship_coordinates_player1 = True
      
  while correct_ship_coordinates_player2 == False:
    print ("\n" + player2_name + ", place your ship on your board by entering your ship's coordinates (any 2 numbers between 1 to 5) - ")

    # Preventing opponent from seeing player2_ship_row = int(input("Row: ")) and player2_ship_col = int(input("Column: "))
    player2_ship_row = int(getpass(prompt = "Row: "))
    player2_ship_col = int(getpass(prompt = "Column: "))
    
    if (player2_ship_row > 5 or player2_ship_row < 1) or (player2_ship_col > 5 or player2_ship_col < 1):
      print ("\n" + player2_name + ", you entered invalid ship coordinates. Please try again.")
      
    else:
      correct_ship_coordinates_player2 = True

player1_success = False
player2_success = False
computer_success = False
user_success = False
end_game = False

# starting of the while loop 
while computer_success == False and user_success == False and end_game == False and player1_success == False and player2_success == False:
  turn += 1 
  if game_mode == "computer" or game_mode == "c":
    print ("\nTurn " + str(turn))
    guess_row = input("Guess Row: ")     
    guess_col = input("Guess Column: ")
    
    if guess_row == "" or guess_col == "":
      print ("\nYou have ended the game!")
      print ("Correct Row: " + str(computer_ship_row + 1))  
      print ("Correct Column: " + str(computer_ship_col + 1) + "\n") 
      print ("Here is the final board: \n")
      player2_board[computer_ship_row][computer_ship_col] = "#"
      print_board(player2_board) 
      end_game = True
  
    else:
      guess_row = int(guess_row)
      guess_col = int(guess_col)
      
      guess_row -= 1
      guess_col -= 1
      
      if guess_row == computer_ship_row and guess_col == computer_ship_col: # this happens when the user guesses the battleship's location correctly, i.e hits.
        print ()
        print ("HIT! Congratulations! You sunk my battleship in " + str(turn) + " turns! \n")
        print ("YOU WIN! Game Over!")
        print ("Here is the final board: \n")
        player2_board[computer_ship_row][computer_ship_col] = "#"
        print_board(player2_board) 
        user_success = True
              
      else: # this code is enacted upon if the user misses.
        if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
          print ()
          print ("Oops, that's not even in the ocean. \n")
      
        elif player2_board[guess_row][guess_col] == "X":
          print ()
          print ("You guessed that one already. \n")
      
        else:
          print () 
          print ("MISS! You missed my battleship! \n")
          player2_board[guess_row][guess_col] = "X"
        
        print_board(player2_board)

    if user_success == False and end_game == False:
      my_row = random_num(player1_board)
      my_col = random_num(player1_board) 

      print ("\nComputer's Turn " + str(turn))
      print ("I guess the row as " + str(my_row + 1) + " and the column as " + str(my_col + 1) + ".")
      
      if player1_board[my_row][my_col] == "X":
        print ("Oops, looks like I have guessed that already! \n")
      else:
        player1_board[my_row][my_col] = "X"

      if my_row == user_ship_row and my_col == user_ship_col:  
        if turn == 1:
          print ("HIT! Yay! I sunk your ship! I did it in " + str(turn) + " turn!")
        else:
          print ()
          print ("HIT! Yay! I sunk your ship! I did it in " + str(turn) + " turns!")
        
        print ("I WIN! Game Over!")
        print ("Here is the final board: \n")

        player1_board[my_row][my_col] = "#"
        print_board(player1_board)
        computer_success = True

      else: 
        print ("MISS! I missed your battleship! \n") 
        print_board(player1_board)
    
  else:
    print ("\n" + player1_name + "'s Turn " + str(turn)) 
    player1_guess_row = int(input("Guess Row: ")) 
    player1_guess_col = int(input("Guess Column: "))
    print ()
    
    if player1_guess_row == player2_ship_row and player1_guess_col == player2_ship_col:
      player2_board[player1_guess_row - 1][player1_guess_col - 1] = "X"
      print_board(player2_board)
      print ("\n" + player1_name.upper() + " WINS!")
      print ("Congratulations " + player1_name + "! You have sunk " + player2_name + "'s battleship!")
      print ("Game Over! Here is the final board: \n")
      player2_board[player1_guess_row - 1][player1_guess_col - 1] = "#"
      print_board(player2_board) 
      player1_success = True
      
    else: # this code is enacted if player 1 misses.
      if (player1_guess_row < 1 or player1_guess_row > 5) or (player1_guess_col < 1 or player1_guess_col > 5):
        print ("Oops, that's not even in the ocean. \n")
    
      elif player2_board[player1_guess_row - 1][player1_guess_col - 1] == "X":
        print ("You guessed that one already. \n")
    
      else:
        print ("MISS! You missed " + player2_name + "'s battleship! \n")
        player2_board[player1_guess_row - 1][player1_guess_col - 1] = "X"
      
      print_board(player2_board) 
    
    if player1_success == False:
      print ("\n" + player2_name + "'s Turn " + str(turn))
      player2_guess_row = int(input("Guess Row: ")) 
      player2_guess_col = int(input("Guess Column: "))
      
      if player2_guess_row == player1_ship_row and player2_guess_col == player1_ship_col:
        player1_board[player2_guess_row - 1][player2_guess_col - 1] = "X"
        print_board(player1_board)
        print ("\n" + player2_name.upper() + " WINS!")
        print ("Congratulations " + player2_name + "! You have sunk " + player1_name + "'s battleship!")
        print ("Game Over! Here is the final board: \n")
        player1_board[player2_guess_row - 1][player2_guess_col - 1] = "#"
        print_board(player1_board) 
        player2_success = True
        
      else: # this code is enacted if player 2 misses.
        if (player2_guess_row < 1 or player2_guess_row > 5) or (player2_guess_col < 1 or player2_guess_col > 5):
          print ("\nOops, that's not even in the ocean. \n")
      
        elif player1_board[player2_guess_row - 1][player2_guess_col - 1] == "X":
          print ("\nYou guessed that one already. \n")
      
        else:
          print ("\nMISS! You missed " + player1_name + "'s battleship! \n")
          player1_board[player2_guess_row - 1][player2_guess_col - 1] = "X"
        
        print_board(player1_board) 