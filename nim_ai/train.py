import random
from engine import NimEngine, GameState, Move

"""
This class contains all the necessary methods for the AI to learn how to play
Nim.
"""
class NimAI():
    def __init__(self, alpha=0.5, epsilon=0.1):
        """
        Initialize AI with an empty Q-learning dictionary,
        an alpha (learning) rate, and an epsilon rate.

        The Q-learning dictionary maps `(state, action)`
        pairs to a Q-value (a number).
         - `state` is a tuple of remaining piles, e.g. (1, 1, 4, 4)
         - `action` is a tuple `(i, j)` for an action
        """
        self.q = dict()
        self.alpha = alpha
        self.epsilon = epsilon

    def update(self, old_state: GameState.piles, action: Move, new_state: GameState.piles, reward):
        """
        Update Q-learning model, given an old state, an action taken
        in that state, a new resulting state, and the reward received
        from taking that action.
        """
        old = self.get_q_value(old_state, action)
        best_future = self.best_future_reward(new_state)
        self.update_q_value(old_state, action, old, reward, best_future)
    
    def get_q_value(self, state, action):
        """
        Return the Q-value for the state `state` and the action `action`.
        If no Q-value exists yet in `self.q`, return 0.
        """
        
        stateTupe = tuple(state)  
        if (stateTupe, action) in self.q:
            return self.q[(stateTupe, action)]
        return 0
    
    def update_q_value(self, state: GameState.piles, action: Move, old_q, reward, future_rewards):
        """
        Update the Q-value for the state `state` and the action `action`
        given the previous Q-value `old_q`, a current reward `reward`,
        and an estiamte of future rewards `future_rewards`.

        Use the formula:

        Q(s, a) <- old value estimate
                   + alpha * (new value estimate - old value estimate)

        where `old value estimate` is the previous Q-value,
        `alpha` is the learning rate, and `new value estimate`
        is the sum of the current reward and estimated future rewards.
        """

        newValEst = reward + future_rewards
        stateTuple = tuple(state) # Turning state into a tuple since lists can't be keys in dictionaries
        self.q[(stateTuple, action)] = old_q + self.alpha * (newValEst - old_q)

    def best_future_reward(self, state: GameState.piles):
        """
        Given a state `state`, consider all possible `(state, action)`
        pairs available in that state and return the maximum of all
        of their Q-values.

        Use 0 as the Q-value if a `(state, action)` pair has no
        Q-value in `self.q`. If there are no available actions in
        `state`, return 0.
        """

        qVal = -1
        availableActions = False  
        stateTuple = tuple(state)

        for i in range(len(state)):
            pileSize = state[i]
            for j in range(1, pileSize + 1):
                action = (i, j)
                availableActions = True

                if (stateTuple, action) in self.q:
                    qVal = max(self.q[(stateTuple, action)], qVal)
                else:
                    qVal = max(0, qVal)

        if availableActions:
            return qVal
        return 0
    
    def choose_action(self, state: GameState.piles, epsilon=True):
        """
        Given a state `state`, return an action `(i, j)` to take.

        If `epsilon` is `False`, then return the best action
        available in the state (the one with the highest Q-value,
        using 0 for pairs that have no Q-values).

        If `epsilon` is `True`, then with probability
        `self.epsilon` choose a random available action,
        otherwise choose the best action available.

        If multiple actions have the same Q-value, any of those
        options is an acceptable return value.
        """

        availableActions = []
        bestQ = -1
        bestAction = ()
        stateTuple = tuple(state)

        # Adding available actions to the list, and keeping track of best action
        for i in range(len(state)):
            pileSize = state[i]
            for j in range(1, pileSize + 1):
                action = (i, j)
                qVal = 0
                # Accessing a state/action pair's q-value
                if (stateTuple, action) in self.q:
                    qVal = self.q[(stateTuple, action)]
                # Updating best action if necessary
                if qVal >= bestQ:
                    bestAction = (action)
                    bestQ = qVal

                availableActions.append(action)

        if epsilon:
            if random.random() <= self.epsilon:
                randInd = random.randint(0, len(availableActions) - 1)
                return availableActions[randInd]

        return bestAction


def train(model_path = "model.pkl"):


