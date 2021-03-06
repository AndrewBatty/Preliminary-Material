# Skeleton Program code for the AQA COMP1 Summer 2015 examination
# this code should be used in conjunction with the Preliminary Material
# written by the AQA COMP1 Programmer Team
# developed in the Python 3.4 programming environment

BOARDDIMENSION = 8

def CreateBoard():
  Board = []
  for Count in range(BOARDDIMENSION + 1):
    Board.append([])
    for Count2 in range(BOARDDIMENSION + 1):
      Board[Count].append("  ")
  return Board

def DisplayWhoseTurnItIs(WhoseTurn):
  if WhoseTurn == "W":
    print("It is White's turn")
  else:
    print("It is Black's turn")

def display_menu():
    print("Main Menu")
    print()
    MainMenu = ["1. Start new game",
                "2. Load existing game",
                "3. Play sample game",
                "4. View high scores",
                "5. Settings",
                "6. Quit program"]
    for count in MainMenu:
        print(count)

def get_menu_selection():
    print()
    Valid = False
    while Valid == False:
      try:
        UserSelection = int(input("Please select an option: "))
        if UserSelection in [1,2,3,4,5,6]:
          Valid = True
        elif UserSelection not in [1,2,3,4,5,6]:
          print("Please enter an option from the list.")
      except ValueError:
          print("Please enter an option from the list.")
    return UserSelection

def make_selection(UserSelection,Quit):
  if UserSelection == 1:
    play_game("N")
  elif UserSelection == 2:
    pass
  elif UserSelection == 3:
    play_game("Y")
  elif UserSelection == 4:
    pass
  elif UserSelection == 5:
    pass
  elif UserSelection == 6:
    Quit = True
  return Quit

def GetTypeOfGame():
  TypeOfGame = None
  while TypeOfGame != "y" or TypeOfGame != "n":
    TypeOfGame = input("Do you want to play the sample game (enter Y for Yes)? ")
    if TypeOfGame in ["Y","Yes","yes","y"]:
      TypeOfGame = "y"
      break
    elif TypeOfGame in ["N","No","no","n"]:
      TypeOfGame = "n"
      break
    else:
      print("Please enter Y or N")
  return TypeOfGame

def DisplayWinner(WhoseTurn):
  if WhoseTurn == "W":
    print("Black's Sarrum has been captured.  White wins!")
  else:
    print("White's Sarrum has been captured.  Black wins!")

def CheckIfGameWillBeWon(Board, FinishRank, FinishFile):
  if Board[FinishRank][FinishFile][1] == "S":
    return True
  else:
    return False

def DisplayBoard(Board):
  print()
  for RankNo in range(1, BOARDDIMENSION + 1):
    print("     -----------------------")
    print("R{0}".format(RankNo), end="  ")
    for FileNo in range(1, BOARDDIMENSION + 1):
      print("|" + Board[RankNo][FileNo], end="")
    print("|")
  print("     -----------------------")
  print()
  print("     F1 F2 F3 F4 F5 F6 F7 F8")
  print()
  print()    

def CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, ColourOfPiece):
  CheckRedumMoveIsLegal = False
  if StartRank == 7: #To make sure that this piece can only move 2 squares on it's first turn. on the whites turn.
    if ColourOfPiece == "W":  
      if FinishRank == StartRank - 2: #Allows the piece to move 2 squares.
        if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
          CheckRedumMoveIsLegal = True
        elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
          CheckRedumMoveIsLegal = True
  if FinishRank == StartRank - 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "B":
      CheckRedumMoveIsLegal = True
  elif StartRank == 2: #To make sure that this piece can only move 2 squares on it's first turn. on the blacks turn.
    if FinishRank == StartRank + 2: #Allows the piece to move 2 squares.
      if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
        CheckRedumMoveIsLegal = True
      elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
        CheckRedumMoveIsLegal = True
  elif FinishRank == StartRank + 1:
    if FinishFile == StartFile and Board[FinishRank][FinishFile] == "  ":
      CheckRedumMoveIsLegal = True
    elif abs(FinishFile - StartFile) == 1 and Board[FinishRank][FinishFile][0] == "W":
      CheckRedumMoveIsLegal = True
  return CheckRedumMoveIsLegal

def CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckSarrumMoveIsLegal = False
  if abs(FinishFile - StartFile) <= 1 and abs(FinishRank - StartRank) <= 1:
    CheckSarrumMoveIsLegal = True
  return CheckSarrumMoveIsLegal

def CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  GisgigirMoveIsLegal = False
  RankDifference = FinishRank - StartRank
  FileDifference = FinishFile - StartFile
  if RankDifference == 0:
    if FileDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, FileDifference):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
    elif FileDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, FileDifference, -1):
        if Board[StartRank][StartFile + Count] != "  ":
          GisgigirMoveIsLegal = False
  elif FileDifference == 0:
    if RankDifference >= 1:
      GisgigirMoveIsLegal = True
      for Count in range(1, RankDifference):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
    elif RankDifference <= -1:
      GisgigirMoveIsLegal = True
      for Count in range(-1, RankDifference, -1):
        if Board[StartRank + Count][StartFile] != "  ":
          GisgigirMoveIsLegal = False
  return GisgigirMoveIsLegal

def CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckNabuMoveIsLegal = False
  if abs(FinishFile - StartFile) == abs(FinishRank - StartRank):
    CheckNabuMoveIsLegal = True
  return CheckNabuMoveIsLegal

def CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckMarzazPaniMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) ==1):
    CheckMarzazPaniMoveIsLegal = True
  elif abs(FinishFile - StartFile) == 1 and abs(FinishRank - StartRank) == 1:
    CheckMarzazPaniMoveIsLegal = True
  return CheckMarzazPaniMoveIsLegal

def CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile):
  CheckEtluMoveIsLegal = False
  if (abs(FinishFile - StartFile) == 2 and abs(FinishRank - StartRank) == 0) or (abs(FinishFile - StartFile) == 0 and abs(FinishRank - StartRank) == 2):
    CheckEtluMoveIsLegal = True
  return CheckEtluMoveIsLegal

def CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn):
  MoveIsLegal = True
  if (FinishFile == StartFile) and (FinishRank == StartRank):
    MoveIsLegal = False
  else:
    try:
      PieceType = Board[StartRank][StartFile][1]
      PieceColour = Board[StartRank][StartFile][0]
    except IndexError:
      MoveIsLegal = False
    if WhoseTurn == "W":
      if PieceColour != "W":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "W":
        MoveIsLegal = False
    else:
      if PieceColour != "B":
        MoveIsLegal = False
      if Board[FinishRank][FinishFile][0] == "B":
        MoveIsLegal = False
    if MoveIsLegal == True:
      if PieceType == "R":
        MoveIsLegal = CheckRedumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, PieceColour)
      elif PieceType == "S":
        MoveIsLegal = CheckSarrumMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "M":
        MoveIsLegal = CheckMarzazPaniMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "G":
        MoveIsLegal = CheckGisgigirMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "N":
        MoveIsLegal = CheckNabuMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
      elif PieceType == "E":
        MoveIsLegal = CheckEtluMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile)
  return MoveIsLegal

def InitialiseBoard(Board, SampleGame):
  if SampleGame == "Y":
    InitialiseSampleBoard(Board, SampleGame)
  else:
    InitialiseNewBoard(Board, SampleGame)

def InitialiseSampleBoard(Board, SampleGame):
  for RankNo in range(1, BOARDDIMENSION + 1):
    for FileNo in range(1, BOARDDIMENSION + 1):
      Board[RankNo][FileNo] = "  "
  Board[1][2] = "BG"
  Board[1][4] = "BS"
  Board[1][8] = "WG"
  Board[2][1] = "WR"
  Board[3][1] = "WS"
  Board[3][2] = "BE"
  Board[3][8] = "BE"
  Board[6][8] = "BR"

def InitialiseNewBoard(Board, SampleGame):
    for RankNo in range(1, BOARDDIMENSION + 1):
      for FileNo in range(1, BOARDDIMENSION + 1):
        if RankNo == 2:
          Board[RankNo][FileNo] = "BR"
        elif RankNo == 7:
          Board[RankNo][FileNo] = "WR"
        elif RankNo == 1 or RankNo == 8:
          if RankNo == 1:
            Board[RankNo][FileNo] = "B"
          if RankNo == 8:
            Board[RankNo][FileNo] = "W"
          if FileNo == 1 or FileNo == 8:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "G"
          elif FileNo == 2 or FileNo == 7:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "E"
          elif FileNo == 3 or FileNo == 6:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "N"
          elif FileNo == 4:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "M"
          elif FileNo == 5:
            Board[RankNo][FileNo] = Board[RankNo][FileNo] + "S"
        else:
          Board[RankNo][FileNo] = "  "
                    
def GetMove(StartSquare, FinishSquare, Quit, WhoseTurn):
    try:
      Quit = False
      StartSquare = int(input("Enter coordinates of square containing piece to move (file first) or type '-1' for menu: "))
      if StartSquare == -1:
        DisplayInGameMenu(StartSquare)
        InGameOption = InGameSelection()
        Quit = MakeInGameSelection(InGameOption,StartSquare, FinishSquare,Quit,WhoseTurn)
      elif StartSquare < 10:
        print("Please provide both FILE and RANK for this move")
      else:
        FinishSquare = int(input("Enter coordinates of square to move piece to (file first): "))
      if not(Quit):
        if FinishSquare < 10:
          print("Please provide both FILE and RANK for this move")
    except ValueError:
      print("Please enter an integer.")
    return StartSquare, FinishSquare, Quit

def DisplayInGameMenu(StartSquare):
  print()
  print("Options")
  print()
  InGameMenu = ["1. Save Game",
                "2. Quit to Menu",
                "3. Return to game",
                "4. Surrender"]
  for count in InGameMenu:
    print(count)

def InGameSelection():
  print()
  Valid = False
  while Valid == False:
    try:
      InGameOption = int(input("Please select an option: "))
      if InGameOption in [1,2,3,4]:
        Valid = True
      elif InGameOption not in [1,2,3,4]:
        print("Please enter an option from the list.")
    except ValueError:
      print("Please enter an option from the list.")
  return InGameOption

def MakeInGameSelection(InGameOption,StartSquare, FinishSquare,Quit,WhoseTurn):
  if InGameOption == 1:
    pass
  elif InGameOption == 2:
    Quit = True
  elif InGameOption == 3:
    Quit = False
    StartSquare, FinishSquare, Quit = GetMove(StartSquare, FinishSquare, Quit, WhoseTurn)
    print()
  elif InGameOption == 4:
    print()
    print("Surrendering...")
    print()
    if WhoseTurn == "W":
      print("White surrendered. Black wins!")
      print()
    else:
      print("Black surrendered. White wins!")
      print()
    Quit = True
  return Quit

def ConfirmMove(StartRank,StartFile,FinishRank,FinishFile):
    print()
    print("Move from Rank {0}, File {1} to Rank {2}, File {3}?".format(StartRank,StartFile,FinishRank,FinishFile))
    MoveConfirmed = None
    while MoveConfirmed != "y" or MoveConfirmed != "n":
      MoveConfirmed = input("Confirm move (Yes/No): ")
      if MoveConfirmed in ["Y","Yes","yes","y"]:
        MoveConfirmed = "y"
        print("Moved confirmed")
        break
      elif MoveConfirmed in ["N","No","no","n"]:
        MoveConfirmed = "n"
        print("Moved not confirmed")
        break
      else:
        print("Please enter Y or N")
    return MoveConfirmed

def GetPieceName(FinishRank, FinishFile, Board):
    Pieces = True
    PieceType = ""
    PieceColour = ""
    if Board[FinishRank][FinishFile][0] == "W":
      PieceColour = "White"
    elif Board[FinishRank][FinishFile][0] == "B":
      PieceColour = "Black"
    else:
      Pieces = False
    if Board[FinishRank][FinishFile][1] == "G":
      PieceType = "Gisgigir"
    elif Board[FinishRank][FinishFile][1] == "E":
      PieceType = "Etlu"
    elif Board[FinishRank][FinishFile][1] == "N":
      PieceType = "Nabu"
    elif Board[FinishRank][FinishFile][1] == "M":
      PieceType = "Marzaz Pani"
    elif Board[FinishRank][FinishFile][1] == "S":
      PieceType = "Sarrum"
    elif Board[FinishRank][FinishFile][1] == "R":
      PieceType = "Redum"
    return (Pieces,PieceType,PieceColour)
       
def MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn, PieceType, PieceColour):
  if WhoseTurn == "W" and FinishRank == 1 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "WM"
    Board[StartRank][StartFile] = "  "
    print()
    print("White Redum premoted to Marzaz Pani.")
  elif WhoseTurn == "B" and FinishRank == 8 and Board[StartRank][StartFile][1] == "R":
    Board[FinishRank][FinishFile] = "BM"
    Board[StartRank][StartFile] = "  "
    print()
    print("Black Redum premoted to Marzaz Pani.")
  else:
    Pieces,PieceType1,PieceColour1 = GetPieceName(FinishRank, FinishFile, Board)
    if not Pieces:
      Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
      Board[StartRank][StartFile] = "  "
    else:
      Pieces,PieceType2,PieceColour2 = GetPieceName(StartRank, StartFile, Board)
      print()
      print("{0} {1} takes {2} {3}.".format(PieceColour2,PieceType2,PieceColour1,PieceType1))
      Board[FinishRank][FinishFile] = Board[StartRank][StartFile]
      Board[StartRank][StartFile] = "  "
    
def play_game(SampleGame):
  Board = CreateBoard() #0th index not used
  StartSquare = 0 
  FinishSquare = 0
  PlayAgain = "Y"
  while PlayAgain == "Y":
    WhoseTurn = "W"
    GameOver = False
    if ord(SampleGame) >= 97 and ord(SampleGame) <= 122:
      SampleGame = chr(ord(SampleGame) - 32)
    InitialiseBoard(Board, SampleGame)
    while not(GameOver):
      DisplayBoard(Board)
      DisplayWhoseTurnItIs(WhoseTurn)
      MoveIsLegal = False
      while not(MoveIsLegal):
        Quit = False
        StartSquare, FinishSquare, Quit = GetMove(StartSquare, FinishSquare, Quit, WhoseTurn)
        if not(Quit):
          StartRank = StartSquare % 10
          StartFile = StartSquare // 10
          FinishRank = FinishSquare % 10
          FinishFile = FinishSquare // 10
          MoveIsLegal = CheckMoveIsLegal(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn)
          if not(MoveIsLegal):
            print("That is not a legal move - please try again")
        else:
          MoveIsLegal = True
      if not(Quit):
        MoveConfirmed = ConfirmMove(StartRank,StartFile,FinishRank,FinishFile)  
        Pieces,PieceType,PieceColour = GetPieceName(FinishRank, FinishFile, Board)
        GameOver = CheckIfGameWillBeWon(Board, FinishRank, FinishFile)
        if MoveConfirmed == "y":
          MakeMove(Board, StartRank, StartFile, FinishRank, FinishFile, WhoseTurn, PieceType, PieceColour)
        if GameOver:
          DisplayWinner(WhoseTurn)
        if MoveConfirmed == "y" and WhoseTurn == "W":
          WhoseTurn = "B"
        else:
          WhoseTurn = "W"
      else:
        GameOver = True
    if not(Quit):
      PlayAgain = input("Do you want to play again (enter Y for Yes)? ")
      if ord(PlayAgain) >= 97 and ord(PlayAgain) <= 122:
        PlayAgain = chr(ord(PlayAgain) - 32)
    else:
      PlayAgain = "N"
    
if __name__ == "__main__":
  Quit = False
  while not(Quit):
    display_menu()
    UserSelection = get_menu_selection()
    Quit = make_selection(UserSelection,Quit)
  
