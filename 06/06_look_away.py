import random

DIRECTIONS = ["UP", "DOWN", "LEFT", "RIGHT"]

def generate_player():
  return {"looks": [], "flag": 'O'}

def generate_game_state():
  game_state = {"blue": [], "red": []}
  for i in range(3):
    game_state["blue"].append(generate_player())
  game_state["red"].append(generate_player())
  return game_state

def look_somewhere(player):
  direction = DIRECTIONS[random.randint(0, 3)]
  player["looks"].append(direction)
  return player

def run_round(game_state):
  look_somewhere(game_state["red"][0])
  for i in range(3):
    look_somewhere(game_state["blue"][i])
    if game_state["blue"][i]["looks"][-1] == game_state["blue"][0]["looks"][-1]:
      game_state["blue"][i]["flag"] = 'X'

def get_winner(game_state, round=5):
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
  print("Starting the game!")
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
  game_state = generate_game_state()
  winner = play(game_state)
  print_game_state(game_state)
  print("=====================================================================")
  print("*********************************************************************")
  print("The winner is the", winner, "team!")

if __name__ == "__main__":
  look_away()