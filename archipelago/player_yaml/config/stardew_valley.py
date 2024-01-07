from .apconfig import ApConfig
from enums import Difficulty
from enums import Game

class StardewValley(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.STARDEW_VALLEY
        self.apgame = "Stardew Valley"
        self.requires_version = "0.4.4"
        
        # standard defaults and docs for game-specific settings
        #
        # read the template for the game for insight into what the settings mean
        # and their legal values
        self.goal:str                       = "community_center"
        self.starting_money:int             = 5000
        self.profit_margin:int              = 100
        self.bundle_randomization:str       = "thematic"
        self.bundle_price:str               = "normal"
        self.entrance_randomization:str     = "disabled"
        self.season_randomization:str       = "randomized"
        self.cropsanity:str                 = "enabled"
        self.backpack_progression:str       = "early_progressive"
        self.tool_progression:str           = "progressive"
        self.skill_progression:str          = "progressive"
        self.building_progression:str       = "progressive_early_shipping_bin"
        self.festival_locations:str         = "easy"
        self.elevator_progression:str       = "progressive_from_previous_floor"
        self.arcade_machine_locations:str   = "full_shuffling"
        