#!/usr/bin/env python
#expect python >= 3.10
import argparse
import random

from enum import IntEnum
from typing import cast

from config import *
from enums import *

# This is just a quick and dirty python script to manage my archipelago settings
# because the conditionals got too weird over time.

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
        
        
    def machine_create(self) -> int:
        triples = [
            ("Storm Tower",         Machine.STORM_TOWER.value,          1),
            ("Ursine Laptop",       Machine.URSINE_LAPTOP.value,        1),
        ]
        
        return self.enum_create("MACHINE", triples)

    def genre_create(self) -> int:
        triples = [
            ("Farming Simulator", Genre.FARMING_SIMULATOR.value, 0),
            ("First Person Shooter", Genre.FIRST_PERSON_SHOOTER.value, 0),
            ("Joke", Genre.JOKE, 0),
            ("Platformer", Genre.PLATFORMER.value, 0),
            ("Puzzle", Genre.PUZZLE.value, 0),
            ("Roguelite", Genre.ROGUELITE.value, 0),
            ("Shooter", Genre.SHOOTER.value, 0),
            ("RPG", Genre.RPG.value, 0),
            ("Third Person Shooter", Genre.THIRD_PERSON_SHOOTER, 0),
            ("Walking Simulator", Genre.WALKING_SIMULATOR, 0),
        ]
        
        return self.enum_create("GENRE", triples)
    
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
            Clique(),
            Doom1993(),
            RogueLegacy(),
            SuperMarioWorld()
        ]
        
        # and eventually the list we actually choose from
        games:list[ApConfig] = []
        
        # need to interpret the genre and machine fields
        genres:ApGenre = ApGenre()
        genres.fromNumber(args.genres)
        
        machines:ApMachine = ApMachine()
        machines.fromNumber(args.machines)
        
        # now we pare down the games list - twice
        for game in games_swp:
            if (game.machines.overlapsWith(machines)):
                if (not (game in games)):
                    games.append(game)
        
        games_swp = []
        
        for game in games:
            if (game.genres.overlapsWith(genres)):
                if (not (game in games_swp)):
                    games_swp.append(game)

        games = games_swp.copy()
        
        # we're good, games are games
        # pick one
        gam:ApConfig = random.choice(games)
        
        # reconfigure
        gam.reconfigure(args.name, args.checks, args.deathlink, args.duration, args.difficulty, args.extra)
        
        # prep output
        fOut:str = gam.prep_output()
    
        # output it - clobber
        with open(f"{args.name}.yaml", "w") as f:
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