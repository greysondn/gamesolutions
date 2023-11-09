#!/usr/bin/env python
#expect python >= 3.10
import argparse
import random

from enum import IntEnum
from typing import cast

# This is just a quick and dirty python script to manage my archipelago settings
# because the conditionals got too weird over time.

# settings

# which machine?
# In the mood for a certain game?
# how many checks?
# death link?
# how long?
# how hard?

class Difficulty(IntEnum):
    VERY_EASY       = 0
    EASY            = 1
    NORMAL          = 2
    HARD            = 3
    VERY_HARD       = 4
    IMPOSSIBLE      = 5
    HATE_ME_TODAY   = 6

class Game(IntEnum):
    ALL                                     = 281474976710655
    NONE                                    = 0
    ADVENTURE                               = 2 **   0
    BLASPHEMOUS                             = 2 **   1
    BUMPER_STICKERS                         = 2 **   2
    CHECKSFINDER                            = 2 **   3
    CLIQUE                                  = 2 **   4
    DARK_SOULS_III                          = 2 **   5
    DLCQUEST                                = 2 **   6
    DONKEY_KONG_COUNTRY_3                   = 2 **   7
    DOOM_1993                               = 2 **   8
    FACTORIO                                = 2 **   9
    FINAL_FANTASY                           = 2 **  10
    HOLLOW_KNIGHT                           = 2 **  11
    HYLICS_2                                = 2 **  12
    KINGDOM_HEARTS_2                        = 2 **  13
    THE_LEGEND_OF_ZELDA                     = 2 **  14
    A_LINK_TO_THE_PAST                      = 2 **  15
    LINKS_AWAKENING_DX                      = 2 **  16
    LUFIA_II_ANCIENT_CAVE                   = 2 **  17
    MEGAMAN_BATTLE_NETWORK_3                = 2 **  18
    MERITOUS                                = 2 **  19
    THE_MESSENGER                           = 2 **  20
    MINECRAFT                               = 2 **  21
    MUSE_DASH                               = 2 **  22
    NOITA                                   = 2 **  23
    OCARINA_OF_TIME                         = 2 **  24
    OVERCOOKED_2                            = 2 **  25
    POKEMON_RED_AND_BLUE                    = 2 **  26
    RAFT                                    = 2 **  27
    RISK_OF_RAIN_2                          = 2 **  28
    ROGUE_LEGACY                            = 2 **  29
    SECRET_OF_EVERMORE                      = 2 **  30
    SLAY_THE_SPIRE                          = 2 **  31
    SMZ3                                    = 2 **  32
    SONIC_ADVENTURE_2_BATTLE                = 2 **  33
    STARCRAFT_2_WINGS_OF_LIBERTY            = 2 **  34
    STARDEW_VALLEY                          = 2 **  35
    SUBNAUTICA                              = 2 **  36
    SUDOKU                                  = 2 **  37
    SUPER_MARIO_64                          = 2 **  38
    SUPER_MARIO_WORLD                       = 2 **  39
    SUPER_METROID                           = 2 **  40
    TERRARIA                                = 2 **  41
    TIMESPINER                              = 2 **  42
    UNDERTALE                               = 2 **  43
    VVVVVV                                  = 2 **  44
    WARGROOVE                               = 2 **  45
    THE_WITNESS                             = 2 **  46
    ZILLION                                 = 2 **  47

class Genre(IntEnum):
    IMPLEMENTED                 = 2 **  10
    PLEASE_NO                   = 2 **   9
    
    FARMING_SIMULATOR           = 2 **   8
    FIRST_PERSON_SHOOTER        = 2 **   0
    PLATFORMER                  = 2 **   1
    PUZZLE                      = 2 **   2
    ROGUELITE                   = 2 **   3
    SHOOTER                     = 2 **   4
    RPG                         = 2 **   5
    THIRD_PERSON_SHOOTER        = 2 **   7
    WALKING_SIMULATOR           = 2 **   6

class Machine(IntEnum):
    ALL           = 3
    STORM_TOWER   = 2 ** 0
    URSINE_LAPTOP = 2 ** 1
    
MACHINES_TO_GAMES:dict[Machine, int] = {
    Machine.STORM_TOWER     :   Game.DOOM_1993.value + 
                                Game.RISK_OF_RAIN_2.value + 
                                Game.ROGUE_LEGACY.value +
                                Game.SONIC_ADVENTURE_2_BATTLE.value +
                                Game.STARDEW_VALLEY.value +
                                Game.SUPER_MARIO_WORLD.value,
                                
    Machine.URSINE_LAPTOP   :   Game.DOOM_1993.value +
                                Game.SUPER_MARIO_WORLD.value,
}

GAMES_TO_GENRES:dict[Game, int] = {
    Game.DOOM_1993 :    Genre.FIRST_PERSON_SHOOTER.value +
                        Genre.SHOOTER.value,
    
    Game.RISK_OF_RAIN_2 :   Genre.ROGUELITE.value +
                            Genre.SHOOTER.value +
                            Genre.THIRD_PERSON_SHOOTER.value,
    
    Game.ROGUE_LEGACY : Genre.PLATFORMER.value +
                        Genre.ROGUELITE.value,
    
    Game.SONIC_ADVENTURE_2_BATTLE : Genre.PLATFORMER.value,
    
    Game.STARDEW_VALLEY :   Genre.FARMING_SIMULATOR.value +
                            Genre.ROGUELITE.value +
                            Genre.RPG.value,
    
    Game.SUPER_MARIO_WORLD :    Genre.IMPLEMENTED.value +
                                Genre.PLATFORMER.value,
}

class ApConfig():
    def __init__(self):
        # details about duration
        self.duration_max:int = 0
        '''longest this has taken to get goal in seconds'''
        self.duration_avg:int = 0
        '''average time this has taken to get goal in seconds'''
        self.duration_min:int = 0
        '''shortest time this has taken to get goal in seconds'''
        
        # details about checks etc
        self.checks:int = 0
        '''number of checks we expect the game to have for this configuration'''
        
        # main settings
        self.game:Game = Game.NONE
        '''Which game this is for'''
        
        self.description:str = "Generated by greysondn's person config generator"
        '''Description used as metadata for generator'''
        
        self.name:str = "ERR"
        '''Name for player slot'''
        
        self.apgame:str = "ERR"
        '''Name of game this is for, as goes in an archipelago config'''
        
        self.requires_version:str = "ERR"
        '''Version of Archipelago this config requires'''
        
        self.requires_plando:str = ""
        '''Plando settings this config requires'''

        # game settings
        self.accessibility:str = "items"
        '''Archipelago accessibility setting. Probably want to leave this alone.'''
        
        self.progression_balancing:str = "50"
        '''Archipelago progression balancing - probably want to leave this alone'''
        
        self.triggers:str = "IGNORED."
        '''Archipelago triggers. This var and feature is currently unused in this config generator.'''
        
        self.local_items:list[str] = []
        '''Items from the item pool to guarantee are available locally'''
        
        self.non_local_items:list[str] = []
        '''Items from the item pool to guarantee are not available locally'''
        
        self.start_inventory:list[str] = []
        '''Items to give to player at start.'''
        
        self.start_hints:list[str] = []
        '''hints to guarantee are available for free out of the gate'''
        
        self.start_location_hints:list[str] = []
        '''location hints to guarantee are available for free out of the gate'''
        
        self.exclude_locations:list[str] = []
        '''checks to guarantee DO NOT have a progression item in them, making them generally skippable'''
        
        self.priority_locations:list[str] = []
        '''checks to guarantee DO have a progression item in them, making them generally mandatory to complete'''
        
        self.item_links:str = "IGNORED."
        '''Don't really get this. Ignored in this config generator for now.'''
        
        self.death_link:bool = False
        '''Death link. Anyone with death link enabled dies together. This isn't output by default as it's not in every game.'''
    
    # Some stuff to override for difficulty
    def reconfigure_checks(self, checks:int) -> None:
        pass
    
    def reconfigure_deathLink(self, deathLink:bool) -> None:
        self.death_link = deathLink
    
    def reconfigure_duration(self, duration:int) -> None:
        pass

    def reconfigure_difficulty(self, difficulty:int) -> None:
        pass
    
    def reconfigure_extra(self, extra:int) -> None:
        pass
    
    def reconfigure_end(self) -> None:
        pass
    
    def reconfigure_start(self) -> None:
        """Override this to match all basic settings for the game, set for the 
        shortest conceivable game on Difficulty.VERY_EASY
        """        
        pass
    
    def reconfigure_slot(self, name:str) -> None:
        self.name = name
    
    def reconfigure(self, name:str, checks:int, deathLink:bool, duration:int, difficulty:int, extra:int) -> None:
        """Override this to reconfigure the game before prepping output.

        Args:
            slotname (str): name to give the slot in Archipelago
            checks (int): Approximate target number of checks for game to have.
            deathLink (bool): whether or not to enable death link
            duration (int): approximate max duration of play in seconds
            difficulty (int): how hard the game is meant to be
            extra(int): any extra setting flags
        """        
        self.reconfigure_start()
        self.reconfigure_slot(name)
        self.reconfigure_difficulty(difficulty)
        self.reconfigure_checks(checks)
        self.reconfigure_duration(duration)
        self.reconfigure_deathLink(deathLink)
        self.reconfigure_extra(extra)
        self.reconfigure_end()
    
    # output prep functions
    def _makeIndent(self, width:int):
        ret = ""
        
        for i in range(width):
            ret = ret + " "
        
        return ret
    
    def prep_simple(self, name:str, value:str, indent:int = 0) -> str:
        ret = ""
        ret = ret + self._makeIndent(indent)
        ret = ret + f"{name}: {value}\n"
        
        return ret
    
    def prep_optional(self, name:str, value:str, indent:int = 0) -> str:
        ret = ""
        
        if (len(value) > 0):
            ret = self.prep_simple(name, value, indent)
        
        return ret
    
    def prep_bool(self, name:str, value:bool, indent:int = 0) -> str:
        ret = ""
        
        swp = ""
        
        if (value == True):
            swp = "'true'"
        elif (value == False):
            swp = "'false'"
        
        ret = self.prep_simple(name, swp, indent)
        
        return ret
    
    def prep_int(self, name:str, value:int, indent = 0) -> str:
        return self.prep_simple(name, f"{value}", indent)
    
    def prep_list(self, name:str, value:list[str], indent:int = 0) -> str:
        ret = ""
        
        if (len(value) > 0):
            prefix = self._makeIndent(indent)
            ret = ret + prefix + f"{name}:\n"
            
            for i in value:
                ret = ret + prefix + f"    - {i}\n"
        
        return ret
    
    def prep_name(self) -> str:
        return self.prep_simple("name", self.name)
    
    def prep_game(self) -> str:
        return self.prep_simple("game", self.apgame)
    
    def prep_description(self) -> str:
        return self.prep_simple("description", self.description)
    
    def prep_requires_version(self):
        return self.prep_simple("version", self.requires_version, 4)
    
    def prep_requires_plando(self):
        return self.prep_optional("plando", self.requires_plando, 4)
    
    def prep_requires(self) -> str:
        ret = "requires:\n"
        ret = ret + self.prep_requires_version()
        ret = ret + self.prep_requires_plando()
        return ret
    
    def prep_mainSettings(self) -> str:
        ret = ""
        ret = ret + self.prep_name()
        ret = ret + self.prep_game()
        ret = ret + self.prep_description()
        ret = ret + self.prep_requires()
        return ret
    
    def prep_accessibility(self) -> str:
        return self.prep_simple("accessibility", self.accessibility, 4)
    
    def prep_progression_balancing(self) -> str:
        return self.prep_simple("progression_balancing", self.progression_balancing, 4)
    
    def prep_local_items(self) -> str:
        return self.prep_list("local_items", self.local_items, 4)
        
    def prep_nonlocal_items(self) -> str:
        return self.prep_list("non_local_items", self.non_local_items, 4)

    def prep_start_inventory(self) -> str:
        return self.prep_list("start_inventory", self.start_inventory, 4)

    def prep_start_hints(self) -> str:
        return self.prep_list("start_hints", self.start_hints, 4)
        
    def prep_start_location_hints(self) -> str:
        return self.prep_list("start_location_hints", self.start_location_hints, 4)
    
    def prep_exclude_locations(self) -> str:
        return self.prep_list("exclude_locations", self.exclude_locations, 4)
        
    def prep_priority_locations(self) -> str:
        return self.prep_list("priority_locations", self.priority_locations, 4)
    
    def prep_game_specific_settings(self) -> str:
        '''override this function to provide game specific settings.'''
        return ""
    
    def prep_gameSettings(self) -> str:
        ret = ""
        ret = ret + f"{self.apgame}:\n"
        ret = ret + self.prep_accessibility()
        ret = ret + self.prep_progression_balancing()
        ret = ret + self.prep_local_items()
        ret = ret + self.prep_nonlocal_items()
        ret = ret + self.prep_start_inventory()
        ret = ret + self.prep_start_hints()
        ret = ret + self.prep_start_location_hints()
        ret = ret + self.prep_exclude_locations()
        ret = ret + self.prep_priority_locations()
        ret = ret + self.prep_game_specific_settings()
        
        return ret
    
    def prep_output(self) -> str:
        ret = ""
        
        ret = ret + self.prep_mainSettings()
        ret = ret + self.prep_gameSettings()
        
        return ret
    
    def print_goal(self, difficulty:int) -> None:
        """Override to output the objective note for whatever the game is.
        """        
        pass
        
class Doom1993(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.DOOM_1993
        self.apgame = "DOOM 1993"
        
        raise NotImplementedError()

class RiskOfRain2(ApConfig):
    pass

class RogueLegacy(ApConfig):
    pass

class SonicAdventure2Battle(ApConfig):
    pass

class StardewValley(ApConfig):
    pass

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
        self.start_inventory            = [
            "Swim",
            "Climb",
        ]
        self.death_link = False
        
        # I need to exclude Soda Lake and a couple others, but not today
        
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
        self.swap_donut_gh_exits            = False
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
            self.percentage_of_yoshi_eggs       = 63 # 50 eggs
            self.level_shuffle                  = True
            self.boss_shuffle                   = "full"
            self.trap_fill_percentage           = 100
            self.ice_trap_weight                = "medium"
        
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

class CommandLine():
    def __init__(self):
        pass
    
    def ask(self, question:str, options:list[str], default:int) -> str:
        """ask user for input on a config question
        
        WARNING: This assumes a well-behaved user. It needs rewritten for input
        sanitization and safety.

        Args:
            question (str): question to ask
            options (list[str]): list of options the user may select, from 0 to n
            default (int): default selected option, should generally be the first

        Returns:
            str: text of option the user selected
        """        
        choice:int = default
        
        print(f"\n\n---\n\n{question} (Default: {default})\n\n")
        for i in range(len(options)):
            print(f"{i} : {options[i]}")
        
        usrIn = input("> ")
        
        if (len(usrIn.strip()) > 0):
            choice = int(usrIn)
            
        print (f"\nChose {choice} : {options[choice]}\n")
        
        return options[choice]
    
    def ask_str(self, question:str) -> str:
        """ask user for input on a config question
        
        WARNING: This assumes a well-behaved user. It needs rewritten for input
        sanitization and safety.

        Args:
            question (str): question to ask

        Returns:
            str: text of option the user selected
        """        
        choice:str = "ERR"
        
        print(f"\n\n---\n\n{question}\n\n")
        
        choice = input("> ")
            
        print (f"\nChose : {choice}\n")
        
        return choice
    
    def enum_create(self, group:str, enum_triple:list[tuple[str, int, int]]) -> int:
        """ask about all of an enum using triples

        Args:
            group (str): name of group to help cue user
            enum_triple (list[tuple[str, int, int]]): list of tuples display name, value, default from {0:"Yes", 1:"No}

        Returns:
            int: bit encoding for field
        """        
        ret:int = 0
        
        for triple in enum_triple:
            swp = self.ask(f"[{group}] : {triple[0]}?", ["Yes","No"], triple[2])
            if("Yes" == swp):
                ret = ret + triple[1]
                
        return ret
            
    def enum_parse(self, bitfield:int, enums:list[IntEnum]) -> list[IntEnum]:
        """unpack enum from bitfield

        Args:
            bitfield (int): value of packed enums
            enums (list[IntEnum]): list of enums that can be in field

        Returns:
            list[IntEnum]: unpacked enums
        """        
        ret:list[IntEnum] = []
        
        for enum in enums:
            if (bitfield & enum.value):
                ret.append(enum)
        
        return ret
        
        
    def machine_create(self) -> int:
        triples = [
            ("Storm Tower",         Machine.STORM_TOWER.value,          1),
            ("Ursine Laptop",       Machine.URSINE_LAPTOP.value,        1),
        ]
        
        return self.enum_create("MACHINE", triples)

    def machine_parse(self, bitfield:int) -> list[Machine]:
        enums:list[Machine] = [
            Machine.STORM_TOWER,
            Machine.URSINE_LAPTOP,
        ]
        
        # have to cast into and out of function
        # make sure you know your type 
        return cast(list[Machine], self.enum_parse(bitfield, cast(list[IntEnum], enums)))
    
    def genre_create(self) -> int:
        triples = [
            ("Farming Simulator", Genre.FARMING_SIMULATOR.value, 0),
            ("First Person Shooter", Genre.FIRST_PERSON_SHOOTER.value, 0),
            ("Platformer", Genre.PLATFORMER.value, 0),
            ("Puzzle", Genre.PUZZLE.value, 0),
            ("Roguelite", Genre.ROGUELITE.value, 0),
            ("Shooter", Genre.SHOOTER.value, 0),
            ("RPG", Genre.RPG.value, 0),
            ("Third Person Shooter", Genre.THIRD_PERSON_SHOOTER, 0),
            ("Walking Simulator", Genre.WALKING_SIMULATOR, 0),
        ]
        
        return self.enum_create("GENRE", triples)
    
    def genre_parse(self, bitfield:int) -> list[Genre]:
        enums:list[Genre] = [
            Genre.FARMING_SIMULATOR,
            Genre.FIRST_PERSON_SHOOTER,
            Genre.PLATFORMER,
            Genre.PUZZLE,
            Genre.ROGUELITE,
            Genre.SHOOTER,
            Genre.RPG,
            Genre.THIRD_PERSON_SHOOTER,
            Genre.WALKING_SIMULATOR,
        ]

        # have to cast into and out of function
        # make sure you know your type 
        return cast(list[Genre], self.enum_parse(bitfield, cast(list[IntEnum], enums)))
    
    def mood(self, args:argparse.Namespace) -> None:
        # name
        name:str = self.ask_str("Slot name?")
        
        # machines
        machines:int = self.machine_create()
        
        # mood/genre
        genres:int = self.genre_create()

        # extra - skipped for now
        extras:int = 0
        
        # checks
        checks:int = int(self.ask_str("How many checks to aim for?"))
        
        # duration
        duration:int = int(self.ask_str("How long (in seconds) to aim for?"))
        
        # difficulty
        difficulty:int = int(self.ask_str("Difficulty? 1-6...\n0 - Very Easy\n1 - Easy\n2 - Normal\n3 - Hard\n4 - Very Hard\n5 - Impossible\n6 - Hate Me Today"))

        # deathlink
        deathlink_input:str = self.ask_str("Deathlink? [Yes or No]")
        
        deathlink = False
        
        if (deathlink_input.lower().strip() == "yes"):
            deathlink = True
        elif (deathlink_input.lower().strip() == "no"):
            deathlink = False
            
        print(f"\n\n")
        print(f"The arguments you want are:\n")
        print(f"{name} {machines} {genres} {checks} {duration} {difficulty} {extras} {deathlink}")
    
    def conf(self, args:argparse.Namespace) -> None:
        # need a list of games
        # should be all implemented ones for config
        games_swp:list[ApConfig] = [
            SuperMarioWorld()
        ]
        
        # and eventually the list we actually choose from
        games:list[ApConfig] = []
        
        # need to interpret the genre and machine fields
        genres:list[Genre] = self.genre_parse(args.genres)
        machines:list[Machine] = self.machine_parse(args.machines)
        
        # now we pare down the games list - twice
        for machine in machines:
            for game in games_swp:
                game_removed:bool = False
                if (MACHINES_TO_GAMES[machine] & game.game.value):
                    if (not game_removed):
                        games.append(game)
                        games_swp.remove(game)
                        game_removed = True
        
        games_swp = []
        
        for game in games:
            game_removed:bool = False
            for genre in genres:
                if (GAMES_TO_GENRES[game.game] & genre.value):
                    if (not game_removed):
                        games_swp.append(game)
                        games.remove(game)
                        game_removed = True

        games = games_swp.copy()
        
        # we're good, games are games
        # pick one
        gam:ApConfig = random.choice(games)
        
        # reconfigure
        gam.reconfigure(args.name, args.checks, args.deathlink, args.duration, args.difficulty, args.extra)
        
        # prep output
        fOut:str = gam.prep_output()
    
        # output it - clobber
        with open("greysondn.yaml", "w") as f:
            f.write(fOut)
        
        # output objective
        gam.print_goal(args.difficulty)
        
    
    def main(self):
        # parse command line arguments
        parser = argparse.ArgumentParser(description='Generate configuration for archipelago.')
        
        parser.add_argument("name",
                            help = "name of the Archipelago player slot",
                            type = str,
        )
        
        parser.add_argument("machines",
                            help = "Machines user has access to presently",
                            type = int,
        )
        
        parser.add_argument("genres",
                            help = "mood player is in, regarding genres",
                            type = int,
        )
        
        parser.add_argument("checks",
                            help = "a target number of checks to go for, if possible",
                            type = int,
        )
        
        parser.add_argument("duration",
                            help = "target duration of game in seconds, if possible",
                            type = int,
        )
        
        parser.add_argument("difficulty",
                            help = "difficulty of generated game desired, from 0 to 6. (0 = Very Easy, 1 = Easy, 2 = Normal, 3 = Hard, 4 = Very Hard, 5 = Impossible, 6 = Hate Me Today)",
                            type = int,
        )
        
        parser.add_argument("extra",
                            help = "value for extra configuration, if desired",
                            type = int,
        )
        
        parser.add_argument("deathlink",
                            help = "whether or not to enable deathlink",
                            type = bool,
        )
        
        parser.add_argument('--mode', 
                            help ='what mode to run this script in',
                            type = str,
                            choices = ['conf', 'mood'],
                            default = "conf",
        )

        args:argparse.Namespace = parser.parse_args()
        
        if (args.mode == "conf"):
            self.conf(args)
        elif (args.mode == "mood"):
            self.mood(args)


# and then we need a main
# should be able to configure the mood value, maybe by an alternate run mode
# and of course output the values blah blah
# ugh
# clobbering is okay

# ye olde main guard
if (__name__ == "__main__"):
    cmd = CommandLine()
    cmd.main()