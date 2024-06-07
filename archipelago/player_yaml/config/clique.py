from .apconfig import ApConfig
from enums import Difficulty
from enums import Game

import random

from .apcomp import ApComp
from .apcomp import BoolComp
from .apcomp import IntComp
from .apcomp import StrComp
from .apcomp import StrEnumComp
from .apcomp import StrEnumRandomizableComp
from .apcomp import StrListComp
from .apcomp import PlandoItemListComp

class CliqueBase(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.CLIQUE
        self.apgame = "Clique"
        self.requires_version = "0.4.6"
        
        self.progression_balancing.set(50)

        # standard defaults and docs for game-specific settings
        #
        # read the template for the game for insight into what the settings mean
        # and their legal values
        _colors:list[str] = [
            "red",
            "orange",
            "yellow",
            "green",
            "cyan",
            "blue",
            "magenta",
            "purple",
            "pink",
            "brown",
            "white",
            "black",
        ]
        self.color:StrEnumRandomizableComp = StrEnumRandomizableComp("color", "red", _colors, 4)
        self.components.append(self.color)

        self.hard_mode:BoolComp = BoolComp("hard_mode", False, 4)
        self.components.append(self.hard_mode)

class Clique(CliqueBase):
    def __init__(self):
        # parent
        super().__init__()
    
    def reconfigure_difficulty(self, difficulty:int) -> None:
        # so the starting default should be very easy
        # so we just progressively increase the difficulty with the timer
        if (difficulty == Difficulty.VERY_EASY.value):
            clique_very_easy_records:list[int] = [
                60,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(clique_very_easy_records)
            
            self.checks = 1
            
            # actual config
            # explicit is better than implicit
            self.color.set("random")
            self.hard_mode.set(False)
        
        elif (difficulty == Difficulty.EASY.value):
            clique_easy_records:list[int] = [
                60,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(clique_easy_records)
            
            self.checks = 1
            
            # actual config
            # explicit is better than implicit
            self.color.set("random")
            self.hard_mode.set(False)

        
        if (difficulty == Difficulty.NORMAL.value):
            clique_normal_records:list[int] = [
                60,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(clique_normal_records)
            
            self.checks = 1
            
            # actual config
            # explicit is better than implicit
            self.color.set("random")
            self.hard_mode.set(False)

        
        if (difficulty == Difficulty.HARD.value):
            clique_hard_records:list[int] = [
                60,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(clique_hard_records)
            
            self.checks = 1
            
            # actual config
            # explicit is better than implicit
            self.color.set("random")
            self.hard_mode.set(False)
        if (difficulty == Difficulty.VERY_HARD.value):
            clique_very_hard_records:list[int] = [
                60,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(clique_very_hard_records)
            
            self.checks = 1
            
            # actual config
            # explicit is better than implicit
            self.color.set("random")
            self.hard_mode.set(False)
            
        if (difficulty == Difficulty.IMPOSSIBLE.value):
            clique_impossible_records:list[int] = [
                60,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(clique_impossible_records)
            
            self.checks = 1
            
            # actual config
            # explicit is better than implicit
            self.color.set("random")
            self.hard_mode.set(False)
            
        if (difficulty == Difficulty.HATE_ME_TODAY.value):
            clique_hate_me_today_records:list[int] = [
                60,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(clique_hate_me_today_records)
            
            self.checks = 1
            
            # actual config
            # explicit is better than implicit
            self.color.set("random")
            self.hard_mode.set(True)
            
    # self.reconfigure_checks(checks)
    # self.reconfigure_duration(duration)
    # self.reconfigure_extra(extra)
    # self.reconfigure_end()

    def print_goal(self, difficulty:int) -> None:
        out:str = "\n\n"
        col:str = self.color.get()
        
        if (difficulty == Difficulty.VERY_EASY):
            out = out + f"Whatever you do, don't press the {col} button."
        elif (difficulty == Difficulty.EASY):
            out = out + f"Whatever you do, don't press the {col} button."
        elif (difficulty == Difficulty.NORMAL):
            out = out + f"Whatever you do, don't press the {col} button."
        elif (difficulty == Difficulty.HARD):
            out = out + f"Whatever you do, don't press the {col} button."
        elif (difficulty == Difficulty.VERY_HARD):
            out = out + f"Whatever you do, don't press the {col} button."
        elif (difficulty == Difficulty.IMPOSSIBLE):
            out = out + f"Whatever you do, don't press the {col} button."
        elif (difficulty == Difficulty.HATE_ME_TODAY):
            out = out + f"Whatever you try, you can't seem to press the {col} button."

        out = out + "\n\n"
        
        print(out)