from enums import Difficulty
from enums import Game

from .apconfig import ApConfig


class Doom1993(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.DOOM_1993
        self.apgame = "DOOM 1993"
        self.requires_version = "0.4.3"
        
        # standard defaults and docs for game-specific settings
        #
        # read the template for the game for insight into what the settings mean
        # and their legal values
        self.difficulty:str                     = "medium"
        self.random_monsters:str                = "shuffle"
        self.random_pickups:str                 = "shuffle"
        self.allow_death_logic:bool             = False
        self.start_with_computer_area_maps:bool = False
        self.episode1:bool                      = True
        self.episode2:bool                      = True
        self.episode3:bool                      = True
        self.episode4:bool                      = False
        
    def reconfigure_start(self) -> None:
        # explicit is better than implicit
        self.progression_balancing  = "50"
        self.accessibility          = "items"
        self.death_link = False
        
        self.difficulty = "baby"
        self.random_monsters = "vanilla"
        self.random_pickups = "vanilla"
        self.allow_death_logic = False
        self.start_with_computer_area_maps = False
        self.episode1 = True
        self.episode2 = False
        self.episode3 = False
        self.episode4 = False
        
    def reconfigure_difficulty(self, difficulty:int) -> None:
        # so the starting default should be very easy
        # so we just progressively increase the difficulty with the timer
        if (difficulty >= Difficulty.VERY_EASY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
            
            self.checks = 0
            # unrecorded
        
        if (difficulty >= Difficulty.EASY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
            
            self.checks = 0
            # unrecorded
        
            # actual config
            self.difficulty = "easy"
            self.episode2 = False
            
        
        if (difficulty >= Difficulty.NORMAL.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
            
            self.checks = 0
            # unrecorded
        
            # actual config
            self.difficulty = "medium"
            
        
        if (difficulty >= Difficulty.HARD.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            self.difficulty = "hard"
            self.episode2 = True
            
        if (difficulty >= Difficulty.VERY_HARD.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded            
             
            # actual config
            self.random_monsters = "shuffle"
            self.random_pickups  = "shuffle"
            self.episode3 = True
            
        if (difficulty >= Difficulty.IMPOSSIBLE.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            self.difficulty = "nightmare"


        if (difficulty >= Difficulty.HATE_ME_TODAY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            self.random_monsters = "random_balanced"
            self.random_pickups  = "random_balanced"

    def prep_game_specific_settings(self) -> str:
        ret:str = ""
        
        ret = ret + self.prep_bool("death_link", self.death_link, 4)
        ret = ret + self.prep_simple("difficulty", self.difficulty, 4)
        ret = ret + self.prep_simple("random_monsters", self.random_monsters, 4)
        ret = ret + self.prep_simple("random_pickups", self.random_pickups, 4)
        ret = ret + self.prep_bool("allow_death_logic", self.allow_death_logic, 4)
        ret = ret + self.prep_bool("start_with_computer_area_maps", self.start_with_computer_area_maps, 4)
        ret = ret + self.prep_bool("episode1", self.episode1, 4)
        ret = ret + self.prep_bool("episode2", self.episode2, 4)
        ret = ret + self.prep_bool("episode3", self.episode3, 4)
        ret = ret + self.prep_bool("episode4", self.episode4, 4)
        
        return ret
    
    def print_goal(self, difficulty:int) -> None:
        out:str = "\n\n"
        
        if (difficulty == Difficulty.VERY_EASY): # baby 1
            out = out + f"Doomguy is too young to die Knee-deep in the Dead"
        elif (difficulty == Difficulty.EASY): # easy 12
            out = out + f"Doomguy hopes it's not too rough on The Shores of Hell"
        elif (difficulty == Difficulty.NORMAL): # medium 12
            out = out + f"Doomguy is going to hurt plenty on The Shores of Hell"
        elif (difficulty == Difficulty.HARD): # hard 123
            out = out + f"Doomguy is ultra-violent in the Inferno"
        elif (difficulty == Difficulty.VERY_HARD): # hard 1234
            out = out + f"Doomguy is ultra-violent with his flesh consumed"
        elif (difficulty == Difficulty.IMPOSSIBLE): # nightmare 1234
            out = out + f"Doomguy is having that same nightmare about his flesh being consumed again"
        elif (difficulty == Difficulty.HATE_ME_TODAY): # nightmare 1234 randomized
            out = out + f"Doomguy is having unfamilar nightmares about his flesh being consumed"

        out = out + "\n\n"
        
        print(out)