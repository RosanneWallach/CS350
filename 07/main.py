import random

# List of suits
SUITS = ["clubs", "diamonds", "hearts", "spades"]
# List of ranks
RANKS = list(range(2, 11)) + ["Jack", "Queen", "King", "Ace"]


def generate_deck(shuffle_fn=None):
  """
  Generates a shuffled standard deck with 52 card
  """
  deck = []
  # Iterate through suits and ranks to generate card combinations
  for s_i, suit in enumerate(SUITS):
    for r_i, rank in enumerate(RANKS):
      # Generate a card given a suit and a rank
      card = {
          "suit": suit,
          "suit_i": s_i,
          "rank": rank,
          "rank_i": r_i}
      deck.append(card)
  # Shuffle the list of all cards (deck)
  if not shuffle_fn:
    return deck
  else:
    shuffle_fn(deck)
    return deck


def split_deck(deck):
  """
  Takes a deck (list of cards) and split it evenly for 2 players
  return a game_state dictionary
  """
  # Split first half for player 1
  deck_1 = deck[:int(len(deck)/2)]
  # Split second half for player 2
  deck_2 = deck[int(len(deck)/2):]
  # Creates game state object
  game_state = {"P1": deck_1, "P2": deck_2}
  return game_state


def display_state(gs, round=0, verbose=0):
  """
  Takes a game state object and round number and print details of the game state
  based on the given verbose argument
  """
  print(f"Round #{round:03d}: =======================================================")
  for player, pcards in gs.items():
    print(f"Player {player} | Total cards ({len(pcards)})")
    if verbose > 0:
      # Display cards per suit set
      for suit in SUITS:
        cards = [card for card in pcards if card["suit"] == suit]
        print(f"  Suit: {suit} ({len(cards)})")
        if verbose > 1:
          for card in cards:
            print(f"    + {card['rank']}")
    print("-------------------------------------------------------------------")


def play_round(card1, card2, level="rank_i"):
  """
  Plays a single round given two cards and level of comparison
  Returns the name of winner and loser for a single round
  """
  # Comparing cards by either rank or suit based on level argument
  if card1[level] >  card2[level]:
   taker, loser = "P1", "P2"
  elif card1[level] < card2[level]:
    taker, loser = "P2", "P1"
  elif level == "rank_i":
    # Play the same round Recursively using suit level
    taker, loser = play_round(card1, card2, "suit_i")
  # Print round information
  print(f"(P1[{card1['rank']}-{card1['suit']}]  <-VS->  P2[{card2['rank']}-{card2['suit']}])  ===>  {taker}")
  return taker, loser


def play(gs):
  """
  Plays the game given a game state until there's a winner/loser
  """
  # Initialize round number
  round = 0
  while True:
    round += 1
    card1 = gs["P1"][0]
    card2 = gs["P2"][0]
    taker, loser = play_round(card1, card2)
    # Updates new state after playing a single round
    gs_new = {
        taker: gs[taker][1:] + [card1, card2],
        loser: gs[loser][1:]
    }
    # Display updated game state after playing a single round
    display_state(gs_new, round, 1)
    # Checking if the game is over
    if len(gs[loser]) == 0:
      return taker, round
    # if round > 26:
    #   return taker, round
    # played.append(str(card1["rank"])+ "-" +card1["suit"])
    # if round > 26:
    #   print(set(played))
    #   print(len(set(played)))
    #   return taker, round


if __name__ == "__main__":
  deck = generate_deck(random.shuffle)
  game_state = split_deck(deck)
  display_state(game_state, 0, 2)
  winner, rounds = play(game_state)
  print("**************************** END **********************************")
  print(f"The winner is {winner} after {rounds} round. Congratulations!")