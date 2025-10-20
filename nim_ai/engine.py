from dataclasses import dataclass

@dataclass(frozen=True)
class GameState:
    piles = list(int, ...)
    current_player: str  # Human or AI move

Move = tuple[int, int]

class NimEngine:
    """
    Returns the possible actions that can be taken from a given state.
    """
    @staticmethod
    def legal_moves(state: GameState):
        actions = set()
        for i, pile in enumerate(state.piles):
            for j in range(1, pile + 1):
                actions.add((i, j))
        return actions
    
    """
    Returns the next player to go after a move is taken.
    """
    @staticmethod
    def next_player(currPlayer):
        if currPlayer == "Human":
            return "AI"
        else:
            return "Human"

    """
    Returns a new game board after applying a player's move.
    """
    @staticmethod
    def apply_move(state: GameState, move: Move) -> GameState:
        pile, count = move

        # Validating the player's move
        if pile < 0 or pile >= len(state.piles):
            raise Exception("Invalid pile")
        elif count < 1 or count > state.piles[pile]:
            raise Exception("Invalid number of objects")
       
        newPiles = state.piles
        newPiles[pile] -= count

        nextPlayer = NimEngine.next_player(state.current_player)
        
        return GameState(newPiles, nextPlayer)
    
    """
    Checking if the game is over. True is returned if it is, False otherwise.
    The game is over if all piles have no objects in them.
    """
    @staticmethod
    def game_over(state: GameState) -> bool:
        for pile in state:
            if pile > 0:
                return False
            
        return True
    
    

       