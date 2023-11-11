from . import constants
GAMES_TO_GENRES   = constants.GAMES_TO_GENRES
MACHINES_TO_GAMES = constants.MACHINES_TO_GAMES

from .difficulty import Difficulty

from . import game
Game = game.Game

from . import genre
Genre = genre.Genre

from . import machine
Machine = machine.Machine