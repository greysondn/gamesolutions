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

class SuperMarioWorldBase(ApConfig):
    def __init__(self):
        # parent
        super().__init__()
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.SUPER_MARIO_WORLD
        self.apgame = "Super Mario World"
        self.requires_version = "0.4.4"
        
        self.progression_balancing.set(50)

        self.components.append(self.death_link)

        # standard defaults and docs for game-specific settings
        #
        # read the template for the game for insight into what the settings mean
        # and their legal values
        self.goal:StrComp = StrComp("goal", "bowser", 4)
        self.components.append(self.goal)
        
        self.bosses_required:IntComp = IntComp("bosses_required", 7, 4)
        self.components.append(self.bosses_required)
        
        self.number_of_yoshi_eggs:IntComp = IntComp("number_of_yoshi_eggs", 50, 4)
        self.components.append(self.number_of_yoshi_eggs)
        
        self.percentage_of_yoshi_eggs:IntComp = IntComp("percentage_of_yoshi_eggs", 100, 4)
        self.components.append(self.percentage_of_yoshi_eggs)
        
        self.dragon_coin_checks:BoolComp = BoolComp("dragon_coin_checks", False, 4)
        self.components.append(self.dragon_coin_checks)
        
        self.bowser_castle_doors:StrComp = StrComp("bowser_castle_doors", "vanilla", 4)
        self.components.append(self.bowser_castle_doors)
        
        self.bowser_castle_rooms:StrComp = StrComp("bowser_castle_rooms", "random_two_room", 4)
        self.components.append(self.bowser_castle_rooms)
        
        self.level_shuffle:BoolComp = BoolComp("level_shuffle", False, 4)
        self.components.append(self.level_shuffle)
        
        self.exclude_special_zone:BoolComp = BoolComp("exclude_special_zone", False, 4)
        self.components.append(self.exclude_special_zone)
        
        self.boss_shuffle:StrComp = StrComp("boss_shuffle", "none", 4)
        self.components.append(self.boss_shuffle)
        
        self.swap_donut_gh_exits:BoolComp = BoolComp("swap_donut_gh_exits", False, 4)
        self.components.append(self.swap_donut_gh_exits)
        
        self.display_received_item_popups:StrComp = StrComp("display_received_item_popups", "progression", 4)
        self.components.append(self.display_received_item_popups)
        
        self.trap_fill_percentage:IntComp = IntComp("trap_fill_percentage", 0, 4)
        self.components.append(self.trap_fill_percentage)
        
        # I'll just reuse the same list for all the traps
        _trapWeights:list[str] = [
            "none",
            "low",
            "medium",
            "high",
        ]
        
        self.ice_trap_weight:StrEnumComp = StrEnumComp("ice_trap_weight", "medium", _trapWeights, 4)
        self.components.append(self.ice_trap_weight)
        
        self.stun_trap_weight:StrEnumComp = StrEnumComp("stun_trap_weight", "medium", _trapWeights, 4)
        self.components.append(self.stun_trap_weight)
        
        self.literature_trap_weight:StrEnumComp = StrEnumComp("literature_trap_weight", "medium", _trapWeights, 4)
        self.components.append(self.literature_trap_weight)
        
        self.timer_trap_weight:StrEnumComp = StrEnumComp("timer_trap_weight", "medium", _trapWeights, 4)
        self.components.append(self.timer_trap_weight)
        
        self.autosave:BoolComp = BoolComp("autosave", True, 4)
        self.components.append(self.autosave)
        
        self.early_climb:BoolComp = BoolComp("early_climb", False, 4)
        self.components.append(self.early_climb)
        
        _overworldSpeeds:list[str] = [
            "slow",
            "vanilla",
            "fast",
        ]
        self.overworld_speed:StrEnumComp = StrEnumComp("overworld_speed", "vanilla", _overworldSpeeds, 4)
        self.components.append(self.overworld_speed)
        
        _musicShuffleTypes:list[str] = [
            "none",
            "consistent",
            "full",
            "singularity",
        ]
        self.music_shuffle:StrEnumComp = StrEnumComp("music_shuffle", "none", _musicShuffleTypes, 4)
        self.components.append(self.music_shuffle)
        
        _marioPalettes:list[str] = [
            "mario",
            "luigi",
            "wario",
            "waluigi",
            "geno",
            "princess",
            "dark",
            "sponge",
        ]
        self.mario_palette:StrEnumRandomizableComp = StrEnumRandomizableComp("mario_palette", "mario", _marioPalettes, 4)
        self.components.append(self.mario_palette)
        
        self.foreground_palette_shuffle:BoolComp = BoolComp("foreground_palette_shuffle", False, 4)
        self.components.append(self.foreground_palette_shuffle)
        
        self.background_palette_shuffle:BoolComp = BoolComp("background_palette_shuffle", False, 4)
        self.components.append(self.background_palette_shuffle)
        
        self.overworld_palette_shuffle:BoolComp = BoolComp("overworld_palette_shuffle", False, 4)
        self.components.append(self.overworld_palette_shuffle)
        
        self.starting_life_count:IntComp = IntComp("starting_life_count", 5, 4)
        self.components.append(self.starting_life_count)

class SuperMarioWorld(SuperMarioWorldBase):
    def __init__(self):
        # parent
        super().__init__()
    
    def reconfigure_difficulty(self, difficulty:int) -> None:
        # so the starting default should be very easy
        # so we just progressively increase the difficulty with the timer
        if (difficulty == Difficulty.VERY_EASY.value):
            smw_very_easy_records:list[int] = [
                1250,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(smw_very_easy_records)
            
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.number_of_yoshi_eggs.set(80)
            self.percentage_of_yoshi_eggs.set(1)
            self.dragon_coin_checks.set(False)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("none")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression")
            self.trap_fill_percentage.set(0)
            self.ice_trap_weight.set("none")
            self.stun_trap_weight.set("none")
            self.literature_trap_weight.set("none")
            self.timer_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.mario_palette.set("random")
            self.foreground_palette_shuffle.set(True)
            self.background_palette_shuffle.set(True)
            self.overworld_palette_shuffle.set(True)
            self.starting_life_count.set(99)


            self.requires_plando = "items"
            _plandoItemLocations:list[str] = [
                "early_locations",
            ]
            _plandoItemItems:list[str] = [
                "Carry",
                "Climb",
                "Progressive Powerup",
                "Progressive Powerup",
                "Progressive Powerup",
                "Run",
                "Swim",
            ]
            plando:PlandoItemListComp = PlandoItemListComp(4)
            plando.add(_plandoItemItems, _plandoItemLocations)
            self.components.append(plando)
        
        elif (difficulty == Difficulty.EASY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
            
            self.checks = 0
            # unrecorded
        
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.number_of_yoshi_eggs.set(80)
            self.percentage_of_yoshi_eggs.set(25) # 20 eggs
            self.dragon_coin_checks.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("none")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression")
            self.trap_fill_percentage.set(0)
            self.ice_trap_weight.set("none")
            self.stun_trap_weight.set("none")
            self.literature_trap_weight.set("none")
            self.timer_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.mario_palette.set("random")
            self.foreground_palette_shuffle.set(True)
            self.background_palette_shuffle.set(True)
            self.overworld_palette_shuffle.set(True)
            self.starting_life_count.set(50)

            self.requires_plando = "items"
            _plandoItemLocations:list[str] = [
                "early_locations",
            ]
            _plandoItemItems:list[str] = [
                "Carry",
                "Climb",
                "Progressive Powerup",
                "Run",
                "Swim",
            ]
            plando:PlandoItemListComp = PlandoItemListComp(4)
            plando.add(_plandoItemItems, _plandoItemLocations)
            self.components.append(plando)
        
        if (difficulty == Difficulty.NORMAL.value):
            smw_normal_records:list[int] = [
                9618,
            ]
            
            self.duration_min, self.duration_max, self.duration_avg = self.helper_duration(smw_normal_records)

            self.checks = 157
        
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.number_of_yoshi_eggs.set(80)
            self.percentage_of_yoshi_eggs.set(63) # 50 eggs
            self.dragon_coin_checks.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(True)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression")
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("medium")
            self.stun_trap_weight.set("none")
            self.literature_trap_weight.set("none")
            self.timer_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.mario_palette.set("random")
            self.foreground_palette_shuffle.set(True)
            self.background_palette_shuffle.set(True)
            self.overworld_palette_shuffle.set(True)
            self.starting_life_count.set(50)

            self.requires_plando = "items"
            _plandoItemLocations:list[str] = [
                "early_locations",
            ]
            _plandoItemItems:list[str] = [
                "Carry",
                "Climb",
                "Swim",
            ]
            plando:PlandoItemListComp = PlandoItemListComp(4)
            plando.add(_plandoItemItems, _plandoItemLocations)
            self.components.append(plando)
        
        if (difficulty == Difficulty.HARD.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.number_of_yoshi_eggs.set(80)
            self.percentage_of_yoshi_eggs.set(80) # 60 eggs
            self.dragon_coin_checks.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(True)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression")
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("medium")
            self.stun_trap_weight.set("medium")
            self.literature_trap_weight.set("none")
            self.timer_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.mario_palette.set("random")
            self.foreground_palette_shuffle.set(True)
            self.background_palette_shuffle.set(True)
            self.overworld_palette_shuffle.set(True)
            self.starting_life_count.set(20)

            self.requires_plando = "items"
            _plandoItemLocations:list[str] = [
                "early_locations",
            ]
            _plandoItemItems:list[str] = [
                "Carry",
                "Climb",
                "Swim",
            ]
            plando:PlandoItemListComp = PlandoItemListComp(4)
            plando.add(_plandoItemItems, _plandoItemLocations)
            self.components.append(plando)
            
        if (difficulty == Difficulty.VERY_HARD.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded

            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.number_of_yoshi_eggs.set(80)
            self.percentage_of_yoshi_eggs.set(100) # 80 eggs
            self.dragon_coin_checks.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(True)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression")
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("medium")
            self.stun_trap_weight.set("medium")
            self.literature_trap_weight.set("medium")
            self.timer_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.mario_palette.set("random")
            self.foreground_palette_shuffle.set(True)
            self.background_palette_shuffle.set(True)
            self.overworld_palette_shuffle.set(True)
            self.starting_life_count.set(10)

            self.requires_plando = "items"
            _plandoItemLocations:list[str] = [
                "early_locations",
            ]
            _plandoItemItems:list[str] = [
                "Carry",
                "Climb",
                "Swim",
            ]
            plando:PlandoItemListComp = PlandoItemListComp(4)
            plando.add(_plandoItemItems, _plandoItemLocations)
            self.components.append(plando)
            
        if (difficulty == Difficulty.IMPOSSIBLE.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.number_of_yoshi_eggs.set(80)
            self.percentage_of_yoshi_eggs.set(100) # 80 eggs
            self.dragon_coin_checks.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(True)
            self.exclude_special_zone.set(False)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression")
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("medium")
            self.stun_trap_weight.set("medium")
            self.literature_trap_weight.set("medium")
            self.timer_trap_weight.set("medium")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.mario_palette.set("random")
            self.foreground_palette_shuffle.set(True)
            self.background_palette_shuffle.set(True)
            self.overworld_palette_shuffle.set(True)
            self.starting_life_count.set(1)

            self.requires_plando = "items"
            _plandoItemLocations:list[str] = [
                "early_locations",
            ]
            _plandoItemItems:list[str] = [
                "Carry",
                "Climb",
                "Swim",
            ]
            plando:PlandoItemListComp = PlandoItemListComp(4)
            plando.add(_plandoItemItems, _plandoItemLocations)
            self.components.append(plando)
            
        if (difficulty == Difficulty.HATE_ME_TODAY.value):
            self.duration_min = 0
            # none recorded
            
            self.duration_max = 31536000
            # none recorded
            
            self.duration_avg = 31536000
            # none recorded
        
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.number_of_yoshi_eggs.set(80)
            self.percentage_of_yoshi_eggs.set(100) # 80 eggs
            self.dragon_coin_checks.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(True)
            self.exclude_special_zone.set(False)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("all")
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("none")
            self.stun_trap_weight.set("none")
            self.literature_trap_weight.set("medium")
            self.timer_trap_weight.set("medium")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("slow")
            self.music_shuffle.set("full")
            self.mario_palette.set("random")
            self.foreground_palette_shuffle.set(True)
            self.background_palette_shuffle.set(True)
            self.overworld_palette_shuffle.set(True)
            self.starting_life_count.set(1)

            self.requires_plando = "items"
            _plandoItemLocations:list[str] = [
                "early_locations",
            ]
            _plandoItemItems:list[str] = [
                "Carry",
                "Climb",
                "Swim",
            ]
            plando:PlandoItemListComp = PlandoItemListComp(4)
            plando.add(_plandoItemItems, _plandoItemLocations)
            self.components.append(plando)
            
    # self.reconfigure_checks(checks)
    # self.reconfigure_duration(duration)
    # self.reconfigure_extra(extra)
    # self.reconfigure_end()

    def print_goal(self, difficulty:int) -> None:
        out:str = "\n\n"
        nam:str = self.mario_palette.get()
        
        swp:float = float(self.number_of_yoshi_eggs.get()) * (float(self.percentage_of_yoshi_eggs.get()) / 100.0)
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