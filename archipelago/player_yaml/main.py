#!/usr/bin/env python
#expect python >= 3.10
import argparse
import random

from enum import IntEnum
from typing import cast

from config import ApConfig
from config import Doom1993
from enums import Difficulty
from enums import Game
from enums import Genre
from enums import Machine
from enums import GAMES_TO_GENRES
from enums import MACHINES_TO_GAMES

# This is just a quick and dirty python script to manage my archipelago settings
# because the conditionals got too weird over time.
    
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
        
        # TODO: Exclude Soda Lake and other "impossible" stages.
        # TODO: Experiment with early climb and plando to lock a single stage and swim, climb into place. Maybe Yoshi's Island 2?
        
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
            Doom1993(),
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
                            type = str,
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

# ye olde main guard
if (__name__ == "__main__"):
    cmd = CommandLine()
    cmd.main()