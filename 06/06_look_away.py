import random

# A list containing possible directions
DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]


def generate_player():
  """
  A function to generate a player with empty looks history, and 'O flag'
  Returns: player object
  """
  return {"looks": [], "flag": 'O'}


def generate_game_state():
  """
  Generates a game state, containing two teams (Blue and Red)
  Returns: game state object
  """
  game_state = {"blue": [], "red": []}
  for i in range(3):
    game_state["blue"].append(generate_player())
  game_state["red"].append(generate_player())
  return game_state

def look_somewhere(player):
  """
  Assigns a random direction to a player,
  and updates the given player object.
  Args: player object
  Returns: updated player object
  """
  direction = DIRECTIONS[random.randint(0, 3)]
  player["looks"].append(direction)
  return player

def run_round(game_state):
  """
  Runs 1 round by assigning a random direction to every player,
  and updates the X flad for the blue team.
  """
  # Assign a random look-away for the player in the red team.
  look_somewhere(game_state["red"][0])
  for i in range(3):
    # Assigns a random look-away for the players in the blue team.
    look_somewhere(game_state["blue"][i])
    # Updates the X flag for players in the blue team.
    if game_state["blue"][i]["looks"][-1] == game_state["blue"][0]["looks"][-1]:
      game_state["blue"][i]["flag"] = 'X'

def get_winner(game_state, round=5):
  """
  Takes a game state and round number and finds the winner
  Args: game state object, and round number.
  Returns: team name, or None if the game is not over.
  """
  xs = 0
  for i in range(3):
    if game_state["blue"][i]["flag"] == 'X':
      xs += 1
  if xs == 3:
    return "red"
  elif round == 5:
    return "blue"
  else:
    return None

def play(game_state):
  """
  Plays the game, 5 rounds or less as soon as there's a winner.
  Returns: the winner's name when the game is over.
  """
  print("Starting the game!")
  # Running 5 rounds or less
  for round in range(1,6):
    print("Playing round #", round, "...")
    run_round(game_state)
    winner = get_winner(game_state, round)
    if winner:
      return winner

def print_game_state(gs):
  print("=====================================================================")
  print("FINAL GAME STATE:")
  print("---------------------------------------------------------------------")
  print("Team RED:")
  print("1st Player's Looks: ", gs["red"][0]["looks"])
  print("---------------------------------------------------------------------")
  print("Team BLUE:")
  print("1st Player's Looks: ", gs["blue"][0]["looks"])
  print("1st Player's flag: ", gs["blue"][0]["flag"])
  print("2nd Player's Looks: ", gs["blue"][1]["looks"])
  print("2nd Player's flag: ", gs["blue"][1]["flag"])
  print("3rd Player's Looks: ", gs["blue"][2]["looks"])
  print("3rd Player's flag: ", gs["blue"][2]["flag"])

def look_away():
  """
  Generates a game state and runs the game, then prints the results.
  """
  game_state = generate_game_state()
  winner = play(game_state)
  print_game_state(game_state)
  print("=====================================================================")
  print("*********************************************************************")
  print("The winner is the", winner, "team!")

if __name__ == "__main__":
  look_away()