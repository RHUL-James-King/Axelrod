"""
Defines the core actions for the Prisoner's Dilemma:
* Cooperate
* Defect

Use Actions.C and Actions.D instead of 'C' or 'D'. For convenience you can use:

from Axelrod import Actions
C, D = Actions.C, Actions.D
"""

from enum import Enum
import random
from typing import Iterable


class UnknownAction(ValueError):
    def __init__(self, *args):
        super(UnknownAction, self).__init__(*args)


class Actions(Enum):

    C = 1
    D = 0

    def __bool__(self):
        return bool(self.value)

    def __repr__(self):
        return '{}'.format(self.name)

    def __str__(self):
        return '{}'.format(self.name)

    def flip(self):
        """Returns the opposite Action. """
        if self == Actions.C:
            return Actions.D
        if self == Actions.D:
            return Actions.C
        else:
            raise UnknownAction('Cannot flip action: {!r}'.format(self))

    @classmethod
    def from_char(cls, character):
        """Converts a single character into an Action.
        :code:`Action.from_char('C')` returns Action.C.
        :code:`Action.from_char('CC')` raises an error.  Use
        :code:`str_to_actions` instead."""
        if character == 'C':
            return cls.C
        elif character == 'D':
            return cls.D
        else:
            raise UnknownAction('Character must be "C" or "D".')

    @classmethod
    def random_choice(cls, p: float = 0.5) -> 'Action':

        if p == 0:
            return cls.D

        if p == 1:
            return cls.C

        r = random.random()
        if r < p:
            return cls.C
        return cls.D

# Type alias for actions.
Action = Actions


def flip_action(action: Action) -> Action:
    if not isinstance(action, Action):
        raise UnknownAction('Not an Action')
    return action.flip()


def str_to_actions(actions: str) -> tuple:
    """Takes a string like 'CCDD' and returns a tuple of the appropriate
    actions."""
    return tuple(Actions.from_char(element) for element in actions)


def action_sequence_to_str(actions: Iterable[Action]) -> str:
    """Takes any iterable of Action and returns a string of 'C's
    and 'D's.  ex: (D, D, C) -> 'DDC' """
    return "".join(map(repr, actions))
