import pickle
from engine import GameState, Move, NimEngine

class TrainedPolicy:
    def __init__(self, model_path: str | None):
        self.model = None
        # Loading a trained Nim model from a binary file
        if model_path:
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
    
    """
    AI will choose a move.
    """
    def choose_move(self, state: GameState) -> Move:
