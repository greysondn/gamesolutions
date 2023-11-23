from .apconfig import ApConfig
from enums import Difficulty
from enums import Game

import random

class SuperMarioWorld(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.SUPER_MARIO_WORLD
        self.apgame = "Super Mario World"
        self.requires_version = "0.4.3"
        
        # standard defaults and docs for game-specific settings
        #
        # read the template for the game for insight into what the settings mean
        # and their legal values
        self.goal:str                           = "bowser"
        self.bosses_required:int                = 7
        self.number_of_yoshi_eggs:int           = 50
        self.percentage_of_yoshi_eggs:int       = 100
        self.dragon_coin_checks:bool            = False
        self.bowser_castle_doors:str            = "vanilla"
        self.bowser_castle_rooms:str            = "random_two_room"
        self.level_shuffle:bool                 = False
        self.exclude_special_zone:bool          = False
        self.boss_shuffle:str                   = "none"
        self.swap_donut_gh_exits:bool           = False
        self.display_received_item_popups:str   = "progression"
        self.trap_fill_percentage:int           = 0
        self.ice_trap_weight:str                = "medium"
        self.stun_trap_weight:str               = "medium"
        self.literature_trap_weight:str         = "medium"
        self.timer_trap_weight:str              = "medium"
        self.autosave:bool                      = True
        self.early_climb:bool                   = False
        self.overworld_speed:str                = "vanilla"
        self.music_shuffle:str                  = "none"
        self.mario_palette:str                  = "mario"
        self.foreground_palette_shuffle:bool    = False
        self.background_palette_shuffle:bool    = False
        self.overworld_palette_shuffle:bool     = False
        self.starting_life_count:int            = 5
        self.plando_items:list[str]             = []
    
    def help_mario_palette_randomize(self) -> str:
        _options:list[str] = [
            "mario",
            "luigi",
            "wario",
            "waluigi",
            "geno",
            "princess",
            "dark",
            "sponge"
        ]
        
        return random.choice(_options)

    
    def reconfigure_start(self) -> None:
        # explicit is better than implicit
        self.progression_balancing  = "50"
        self.accessibility          = "items" # I never use locations, so...
        self.requires_plando        = "items"
        self.death_link = False
        
        self.goal                           = "yoshi_egg_hunt"
        self.bosses_required                = 0
        self.number_of_yoshi_eggs           = 80
        self.percentage_of_yoshi_eggs       = 1
        self.dragon_coin_checks             = False
        self.bowser_castle_doors            = "fast"
        self.bowser_castle_rooms            = "vanilla"
        self.level_shuffle                  = False
        self.exclude_special_zone           = True
        self.boss_shuffle                   = "none"
        self.swap_donut_gh_exits            = True
        self.display_received_item_popups   = "progression"
        self.trap_fill_percentage           = 0
        self.ice_trap_weight                = "none"
        self.stun_trap_weight               = "none"
        self.literature_trap_weight         = "none"
        self.timer_trap_weight              = "none"
        self.autosave                       = True
        self.early_climb                    = True
        self.overworld_speed                = "fast"
        self.music_shuffle                  = "full"
        self.mario_palette                  = self.help_mario_palette_randomize()
        self.foreground_palette_shuffle     = True
        self.background_palette_shuffle     = True
        self.overworld_palette_shuffle      = True
        self.starting_life_count            = 99
        self.plando_early_items:list[str]   = [
            "Swim: 1",
            "Climb: 1",
            "Carry: 1",
            "Progressive Powerup: 3",
            "Run: 1"
        ]


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
            self.percentage_of_yoshi_eggs       = 25 # 20 eggs
            self.dragon_coin_checks             = True
            self.starting_life_count            = 50
            self.plando_early_items:list[str]   = [
                "Swim: 1",
                "Climb: 1",
                "Carry: 1",
                "Progressive Powerup: 1",
                "Run: 1"
            ]
        
        if (difficulty >= Difficulty.NORMAL.value):
            smw_normal_records:list[int] = [
                9618,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(smw_normal_records)

            self.checks = 157
        
            # actual config
            self.percentage_of_yoshi_eggs       = 63 # 50 eggs
            self.level_shuffle                  = True
            self.boss_shuffle                   = "full"
            self.trap_fill_percentage           = 100
            self.ice_trap_weight                = "medium"
            self.plando_early_items:list[str]   = [
                "Swim: 1",
                "Climb: 1",
                "Carry: 1",
            ]
        
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
            self.percentage_of_yoshi_eggs       = 80 # 60 eggs
            self.stun_trap_weight               = "medium"
            self.starting_life_count            = 20
            
        if (difficulty >= Difficulty.VERY_HARD.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded            # actual config
            self.percentage_of_yoshi_eggs       = 100 # 80 eggs
            self.literature_trap_weight         = "medium"
            self.early_climb                    = False
            self.starting_life_count            = 10
            
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
            self.start_inventory = []
            self.timer_trap_weight              = "medium"
            self.autosave                       = False
            self.starting_life_count            = 1
            self.exclude_special_zone           = False


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
            self.swap_donut_gh_exits            = True
            self.display_received_item_popups   = "all"
            self.ice_trap_weight                = "none"
            self.stun_trap_weight               = "none"
            self.overworld_speed                = "slow"
            
    # self.reconfigure_checks(checks)
    # self.reconfigure_duration(duration)
    # self.reconfigure_extra(extra)
    # self.reconfigure_end()
    
    def prep_game_specific_settings(self) -> str:
        ret:str = ""
        
        ret = ret + self.prep_bool("death_link", self.death_link, 4)
        ret = ret + self.prep_simple("goal", self.goal, 4)
        ret = ret + self.prep_int("bosses_required", self.bosses_required, 4)
        ret = ret + self.prep_int("number_of_yoshi_eggs", self.number_of_yoshi_eggs, 4)
        ret = ret + self.prep_int("percentage_of_yoshi_eggs", self.percentage_of_yoshi_eggs, 4)
        ret = ret + self.prep_bool("dragon_coin_checks", self.dragon_coin_checks, 4)
        ret = ret + self.prep_simple("bowser_castle_doors", self.bowser_castle_doors, 4)
        ret = ret + self.prep_simple("bowser_castle_rooms", self.bowser_castle_rooms, 4)
        ret = ret + self.prep_bool("level_shuffle", self.level_shuffle, 4)
        ret = ret + self.prep_bool("exclude_special_zone", self.exclude_special_zone, 4)
        ret = ret + self.prep_simple("boss_shuffle", self.boss_shuffle, 4)
        ret = ret + self.prep_bool("swap_donut_gh_exits", self.swap_donut_gh_exits, 4)
        ret = ret + self.prep_simple("display_received_item_popups", self.display_received_item_popups, 4)
        ret = ret + self.prep_int("trap_fill_percentage", self.trap_fill_percentage, 4)
        ret = ret + self.prep_simple("ice_trap_weight", self.ice_trap_weight, 4)
        ret = ret + self.prep_simple("stun_trap_weight", self.stun_trap_weight, 4)
        ret = ret + self.prep_simple("literature_trap_weight", self.literature_trap_weight, 4)
        ret = ret + self.prep_simple("timer_trap_weight", self.timer_trap_weight, 4)
        ret = ret + self.prep_bool("autosave", self.autosave, 4)
        ret = ret + self.prep_bool("early_climb", self.early_climb, 4)
        ret = ret + self.prep_simple("overworld_speed", self.overworld_speed, 4)
        ret = ret + self.prep_simple("music_shuffle", self.music_shuffle, 4)
        ret = ret + self.prep_simple("mario_palette", self.mario_palette, 4)
        ret = ret + self.prep_bool("foreground_palette_shuffle", self.foreground_palette_shuffle, 4)
        ret = ret + self.prep_bool("background_palette_shuffle", self.background_palette_shuffle, 4)
        ret = ret + self.prep_bool("overworld_palette_shuffle", self.overworld_palette_shuffle, 4)
        ret = ret + self.prep_int("starting_life_count", self.starting_life_count, 4)
        
        if (len(self.plando_early_items) > 0):
            ret = ret + "    plando_items:\n"
            ret = ret + "        - items:\n"
            for item in self.plando_early_items:
                ret = ret + f'              {item}\n'
            ret = ret + "          locations:\n"
            ret = ret + "              - early_locations\n"
        
        return ret

    def print_goal(self, difficulty:int) -> None:
        out:str = "\n\n"
        nam:str = self.mario_palette.title()
        
        swp:float = float(self.number_of_yoshi_eggs) * (float(self.percentage_of_yoshi_eggs) / 100.0)
        egg:int = round(swp)
        
        
        if (difficulty == Difficulty.VERY_EASY):
            out = out + f"{nam} should have a very easy time finding {egg} eggs."
        elif (difficulty == Difficulty.EASY):
            out = out + f"{nam} should find it easy to find {egg} eggs."
        elif (difficulty == Difficulty.NORMAL):
            out = out + f"{nam} has to try to act normal while searching for {egg} eggs."
        elif (difficulty == Difficulty.HARD):
            out = out + f"{nam} is going to have a hard life finding {egg} eggs."
        elif (difficulty == Difficulty.VERY_HARD):
            out = out + f"{nam} will find it very hard to find {egg} eggs."
        elif (difficulty == Difficulty.IMPOSSIBLE):
            out = out + f"{nam} must believe in the impossible dream: a world with {egg} eggs."
        elif (difficulty == Difficulty.HATE_ME_TODAY):
            out = out + f"{nam} is gonna feel the world's hatred for the quest to find {egg} eggs."

        out = out + "\n\n"
        
        print(out)