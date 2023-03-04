#documents: https://docs.google.com/document/d/1njwlq9zclrLvaVW-G2yTwSFUUU_MBUfYH4QYQueMIfg/edit

#miro flowchart: https://miro.com/app/board/uXjVPjheU_c=/
import re

isGood = True

board = [
[" "," "," "," "," "," "],
[" "," "," "," "," "," "],
[" "," "," "," "," "," "],
[" "," "," "," "," "," "],
[" "," "," "," "," "," "],
[" "," "," "," "," "," "]
]
def greet():
  print("Welcome to Lloyd's Connect 4 Game!\n")


def display_board():#prints board
  for row in board:
    print(row)
  print("  1    2    3    4    5    6  ")#easier to use for player


def player1_selection(): #function for player selection of desired column
  player1_choice = input("\nPlayer 1: ")
  print("")
  print("------------------------------")
  print("")
  if player1_choice == "1": #player choice for move 
    for row in reversed(board):
      if row[0] == " ":
        row.pop(0)#REMOVES INDEX 0 
        row.insert(0, "X") #INSERTS X INTO INDEX
        display_board()
        break
        
  elif player1_choice == "2":
    for row in reversed(board):
      if row[1] == " ":
        row.pop(1)
        row.insert(1, "X")
        display_board()
        break
        
  elif player1_choice == "3":
    for row in reversed(board):
      if row[2] == " ":
        row.pop(2)
        row.insert(2, "X")
        display_board()
        break
        
  elif player1_choice == "4":
    for row in reversed(board):
      if row[3] == " ":
        row.pop(3)
        row.insert(3, "X")
        display_board()
        break
        
  elif player1_choice == "5":
    for row in reversed(board):
      if row[4] == " ":
        row.pop(4)
        row.insert(4, "X")
        display_board()
        break
        
  elif player1_choice == "6":
    for row in reversed(board):
      if row[5] == " ":
        row.pop(5)
        row.insert(5, "X")
        display_board()
        break
  check()
        
def player2_selection():
  player2_choice = input("\nPlayer 2: ")
  print("")
  print("------------------------------")
  print("")
  if player2_choice == "1":
    for row in reversed(board):
      if row[0] == " ":
        row.pop(0)
        row.insert(0, "O")
        display_board()
        break
        
  elif player2_choice == "2":
    for row in reversed(board):
      if row[1] == " ":
        row.pop(1)
        row.insert(1, "O")
        display_board()
        break
        
  elif player2_choice == "3":
    for row in reversed(board):
      if row[2] == " ":
        row.pop(2)
        row.insert(2, "O")
        display_board()
        break
        
  elif player2_choice == "4":
    for row in reversed(board):
      if row[3] == " ":
        row.pop(3)
        row.insert(3, "O")
        display_board()
        break
        
  elif player2_choice == "5":
    for row in reversed(board):
      if row[4] == " ":
        row.pop(4)
        row.insert(4, "O")
        display_board()
        break
        
  elif player2_choice == "6":
    for row in reversed(board):
      if row[5] == " ":
        row.pop(5)
        row.insert(5, "O")
        display_board()
        break


def gameplay():
  global isGood
  greet()
  display_board()
  while isGood: #loops player selection contiuously 
    player1_selection()
    player2_selection()


def check(): #checks for win
  def horizontal_check(): #checks horizontally by going through each row and adding each index into a string and uses regex to look for a pattern
    global isGood
    for row in reversed(board):
      string_check = " "
      for space in row:
        string_check += space 
    
      fourx = re.search("XXXX", string_check) #looks for the pattern "XXXX" in the string_check string to determine a win 
      fouro = re.search("OOOO", string_check)
      
      if fourx:
        print("Player 1 won horizontally!")
        isGood = False #BREAKS LOOP
      if fouro:
        print("Player 2 won horizontally!")
        isGood = False #BREAKS LOOP
      

  def vertical_check():
    i = 0
    for row in reversed(board):
      string_check = " "
      for row[i] in reversed(board):
        string_check += row[i]

      four = re.search("XXXX", string_check)

      if four:
        print("Player 1 won horizontally!")

    i += 1

  #diagonal check
  return horizontal_check()

def main():
  gameplay()


if __name__ == "__main__":
  main()