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
    
    @staticmethod
    def next_player(currPlayer):
        if currPlayer == "Human":
            return "AI"
        else:
            return "Human"

    @staticmethod
    def apply_move(state: GameState, move: Move) -> GameState:
        pile, count = move
        if pile < 0 or pile >= len(state.piles):
            raise Exception("Invalid pile")
        elif count < 1 or count > state.piles[pile]:
            raise Exception("Invalid number of objects")
       
        newPiles = state.piles
        newPiles[pile] -= count

        nextPlayer = NimEngine.next_player(state.current_player)
        
        return GameState(newPiles, nextPlayer)
    
    

       