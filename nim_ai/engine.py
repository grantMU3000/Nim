from dataclasses import dataclass

@dataclass(frozen=True)
class GameState:
    piles = list(int, ...)
    current_player: str  # Human or AI move

Move = tuple(int, int)

class NimEngine:
    @staticmethod
    def legal_moves(state: GameState):
        actions = set()
        for i, pile in enumerate(state.piles):
            for j in range(1, pile + 1):
                actions.add((i, j))
        return actions