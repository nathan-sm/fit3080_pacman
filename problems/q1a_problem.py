import logging
import time
from typing import Tuple

import util
from game import Actions, Agent, Directions
from logs.search_logger import log_function
from pacman import GameState


class q1a_problem:
    """
    A search problem defines the state space, start state, goal test, successor
    function and cost function.  This search problem can be used to find paths
    to a particular point on the pacman board.
    """
    def __str__(self):
        return str(self.__class__.__module__)

    def __init__(self, gameState: GameState):
        """
        gameState: A GameState object (pacman.py)

        Store anything else that you think would helpful for your agent
        """
        self.startingGameState: GameState = gameState
        "*** YOUR CODE HERE ***"

    @log_function
    def getStartState(self):
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


    @log_function
    def isGoalState(self, state):
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()

    @log_function
    def getSuccessors(self, state):
        """
        Returns successor states, the actions they require, and a cost of 1.

         As noted in search.py:
             For a given state, this should return a list of triples,
         (successor, action, stepCost), where 'successor' is a
         successor to the current state, 'action' is the action
         required to get there, and 'stepCost' is the incremental
         cost of expanding to that successor
        """
        # ------------------------------------------
        "*** YOUR CODE HERE ***"
        util.raiseNotDefined()


