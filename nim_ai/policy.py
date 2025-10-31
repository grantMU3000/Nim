import pickle
from engine import GameState, Move

class TrainedPolicy:
    def __init__(self, model_path: str | None):
        self.model = None
        # Loading a trained Nim model from a binary file
        if model_path:
            with open(model_path, "rb") as f:
                self.model = pickle.load(f)
                
    
    """
    AI will choose a move. (Model is trained, so no need to worry about epsilon)
    """
    def choose_move(self, state: GameState.piles) -> Move:
        bestAction = ()
        stateTuple = tuple(state)
        bestQ = -1

        # Adding available actions to the list, and keeping track of best action
        for i in range(len(state)):
            pileSize = state[i]
            for j in range(1, pileSize + 1):
                action = (i, j)
                qVal = 0
                # Accessing a state/action pair's q-value
                if (stateTuple, action) in self.model.q:
                    qVal = self.model.q[(stateTuple, action)]
                # Updating best action if necessary
                if qVal >= bestQ:
                    bestAction = (action)
                    bestQ = qVal
        
        return bestAction
