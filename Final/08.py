import random

SUITS = ["clubs", "diamonds", "hearts", "spades"]
SUITS = {s: si for si, s in enumerate(SUITS)}

RANKS = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]
RANKS = {r: ri for ri, r in enumerate(RANKS)}


def generate_card(suit, rank):
  """
  Generate a card object given suit and rank.
  """
  return {"suit": suit[0], "s_i": suit[1], "rank": rank[0], "rank_i": rank[1]}


def generate_suit(suit):
  """
  Generate a list of cards for a given suit
  """
  # print(suit)
  return list(map(lambda rank: generate_card(suit, rank), RANKS.items()))


def generate_deck():
  """
  Generate a shuffled deck of 52 card
  """
  deck = list(map(generate_suit, SUITS.items()))
  deck = [card for suit_cards in deck for card in suit_cards]
  random.shuffle(deck)
  return deck


def generate_player(deck, ind, split_size):
  """
  Generate a player object by assigning cards from the given deck
  """
  cards = deck[ind*split_size : (ind + 1) * split_size]
  player = {"hand": cards, "books": []}
  return (f"P{ind+1}", player)

def generate_game_state(deck, players_n:int):
  """
  Generate initial game state object containing players hands, their boks and the remaining cards in the deck
  """
  splits = {2: 7, 3: 6, 4:5}
  if players_n not in splits:
    print("Error: Wrong players number!")
    return None
  players = range(players_n)
  split_size = splits[players_n]
  players = list(map(lambda ind: generate_player(deck, ind, split_size), players))
  players = {player[0]: player[1] for player in players}
  gs = {
      "players": players,
      "left": deck[players_n * split_size : ]
      }
  return gs


def select_card(gs, pname):
  """
  Select a random card from player's hand
  """
  if len(gs["players"][pname]["hand"]) == 0:
    return None
  else:
    card_i = random.randint(0, len(gs["players"][pname]["hand"]) - 1)
    return gs["players"][pname]["hand"][card_i]


def select_other_player(gs, excluded):
  """
  Select random targeted player
  """
  others = [pn for pn in gs["players"] if pn not in excluded]
  random_ind = random.randint(0, len(others) - 1)
  return others[random_ind]


def has_rank(gs, pname, rank):
  """
  Check if a player's hand has the given rank
  """
  cards = gs["players"][pname]["hand"]
  # print(cards)
  for card in cards:
    if card["rank"] == rank:
      return True
  return False



def get_cards_of_rank(gs, pname, rank):
  """
  Gets the cards of the same given rank
  """
  rank_cards = [card for card in gs["players"][pname]["hand"] if card["rank"] == rank]
  remain = [card for card in gs["players"][pname]["hand"] if card["rank"] != rank]
  return rank_cards, remain


def give_over(gs, pname, rank):
  """
  Get the cards to be removed from player's hand
  """
  given, remain = get_cards_of_rank(gs, pname, rank)
  gs = {**gs,
        "players": {**gs["players"],
                    pname: {**gs["players"][pname],
                            "hand": remain}}
  }
  return gs, given


def aquire_cards(gs, pname, cards):
  """
  Add a list of cards to a player's hand
  """
  gs = {**gs,
        "players": {**gs["players"],
                    pname: {**gs["players"][pname],
                            "hand": gs["players"][pname]["hand"] + cards}}
  }
  return gs


def draw_from_deck(gs, pname):
  """
  Draw a new card from the remaining deck
  """
  if len(gs["left"]) == 0:
    return gs, 0
  return {
      **gs,
      "left": gs["left"][1:],
      "players": {
          **gs["players"],
          pname: {
              **gs["players"][pname],
              "hand": gs["players"][pname]["hand"] + gs["left"][:1]
          }
      } 
  }, 1

def go_fish(gs, pname):
  return draw_from_deck(gs, pname)


def update_book(gs, pname, rank):
  """
  Update the books list for a specific player with the given rank
  """
  book, remain = get_cards_of_rank(gs, pname, rank)
  if len(book) != 4:
    return gs
  return {
      **gs,
      "players": {
          **gs["players"],
          pname: {
              **gs["players"][pname],
              "hand": remain,
              "books": gs["players"][pname]["books"] + [rank]
          }
      } 
  }


def update_books(gs):
  """
  Update score pile for all players
  """
  for pname in gs["players"]:
    counts = dict()
    for card in gs["players"][pname]["hand"]:
      counts[card["rank"]] = 1 + counts.get(card["rank"], 0)
    books = [rank for rank, count in counts.items() if count == 4]
    for book in books:
      gs = update_book(gs, pname, book)
  return gs



def is_empty_hand(gs, pname):
  """
  Check if a player's hand is empty
  """
  return len(gs["players"][pname]["hand"]) == 0


def is_empty_hand_all(gs):
  """
  Check if all players have empty hand
  """
  for pname in gs["players"]:
    if not is_empty_hand(gs, pname):
      return False
  return True


def display_state(gs, round):
  """
  Display game state at a given round
  """
  print(f"Round {round}: {'-'*32}")
  for pname in gs["players"]:
    print(f"Player {pname}:  | Books: {gs['players'][pname]['books']}")


def display_winners(gs):
  """
  Find and display winners with their books
  """
  max_books = max([len(gs["players"][pname]["books"]) for pname in gs["players"]])
  winners = [pname for pname in gs["players"] if len(gs["players"][pname]["books"]) == max_books]
  print("The winners are:")
  for pname in winners:
    print(f"  - {pname} with {max_books}s books: {gs['players'][pname]['books']}")


def player_turn(gs, pname):
  """
  Recursively run a player's turn
  """
  if is_empty_hand(gs, pname):
    gs, drawn = draw_from_deck(gs, pname)
    if drawn == 0:
      return gs
  card = select_card(gs, pname)
  pname_other = select_other_player(gs, pname)
  #print("Target:", pname_other, "| Rank:", card["rank"])
  if has_rank(gs, pname_other, card["rank"]):
    gs, given = give_over(gs, pname_other, card["rank"])
    gs = aquire_cards(gs, pname, given)
    return player_turn(gs, pname)
  gs, _ = go_fish(gs, pname)
  return gs

def start_game(players_n):
  if players_n not in [2, 3, 4]:
    print("Error: Wrong number of players!")
    return None, 0
  print("Game start: ===================================")
  deck = generate_deck()
  gs = generate_game_state(deck, players_n)
  round = 0
  while True:
    round +=1
    gs = update_books(gs)
    for p_n in range(1, players_n + 1):
      pname = f"P{p_n}"
      gs = player_turn(gs, pname)
    display_state(gs, round)
    if is_empty_hand_all(gs):
      break
  print("Game end: =====================================")
  display_winners(gs)
  return gs, round




gs, r = start_game(4)

