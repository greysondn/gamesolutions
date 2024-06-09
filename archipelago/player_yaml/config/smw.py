from .apconfig import ApConfig
from enums import Difficulty
from enums import Game
from enums import Genre
from enums import Machine

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
        
        # genres
        self.genres.add(Genre.IMPLEMENTED)
        self.genres.add(Genre.PLATFORMER)
        
        # machines
        self.machines.add(Machine.STORM_TOWER)
        self.machines.add(Machine.URSINE_LAPTOP)
        
        # reconfigure non-difficulty parts of base class
        self.game = Game.SUPER_MARIO_WORLD
        self.apgame = "Super Mario World"
        self.requires_version = "0.4.6"
        
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
        
        self.max_yoshi_egg_cap:IntComp = IntComp("max_yoshi_egg_cap", 50, 4)
        self.components.append(self.max_yoshi_egg_cap)
        
        self.percentage_of_yoshi_eggs:IntComp = IntComp("percentage_of_yoshi_eggs", 100, 4)
        self.components.append(self.percentage_of_yoshi_eggs)
        
        self.dragon_coin_checks:BoolComp = BoolComp("dragon_coin_checks", False, 4)
        self.components.append(self.dragon_coin_checks)
        
        self.moon_checks:BoolComp = BoolComp("moon_checks", False, 4)
        self.components.append(self.moon_checks)
        
        self.hidden_1up_checks:BoolComp = BoolComp("hidden_1up_checks", False, 4)
        self.components.append(self.hidden_1up_checks)
        
        self.bonus_block_checks:BoolComp = BoolComp("bonus_block_checks", False, 4)
        self.components.append(self.bonus_block_checks)
        
        self.blocksanity:BoolComp = BoolComp("blocksanity", False, 4)
        self.components.append(self.blocksanity)
        
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
        
        self.display_received_item_popups:StrComp = StrComp("display_received_item_popups", "progression_minus_yoshi_eggs", 4)
        self.components.append(self.display_received_item_popups)
        
        self.junk_fill_percentage:IntComp = IntComp("junk_fill_percentage", 0, 4)
        self.components.append(self.junk_fill_percentage)
        
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
        
        self.reverse_trap_weight:StrEnumComp = StrEnumComp("reverse_trap_weight", "medium", _trapWeights, 4)
        self.components.append(self.reverse_trap_weight)
        
        self.thwimp_trap_weight:StrEnumComp = StrEnumComp("thwimp_trap_weight", "medium", _trapWeights, 4)
        self.components.append(self.thwimp_trap_weight)
        
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
        
        _sfxShuffleTypes:list[str] = [
            "none",
            "full",
            "singularity",
        ]
        self.sfx_shuffle:StrEnumComp = StrEnumComp("sfx_shuffle", "none", _sfxShuffleTypes, 4)
        self.components.append(self.sfx_shuffle)
                
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
        
        _paletteShuffleTypes:list[str] = [
            "off",
            "on_legacy",
            "on_curated",
        ]
        
        self.level_palette_shuffle:StrEnumComp = StrEnumComp("level_palette_shuffle", "off", _paletteShuffleTypes, 4)
        self.components.append(self.level_palette_shuffle)
                
        self.overworld_palette_shuffle:StrEnumComp = StrEnumComp("overworld_palette_shuffle", "off", _paletteShuffleTypes, 4)
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
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.max_yoshi_egg_cap.set(80)
            self.percentage_of_yoshi_eggs.set(1)
            self.dragon_coin_checks.set(False)
            self.moon_checks.set(False)
            self.hidden_1up_checks.set(False)
            self.bonus_block_checks.set(False)
            self.blocksanity.set(False)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("none")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression_minus_yoshi_eggs")
            self.junk_fill_percentage.set(0)
            self.trap_fill_percentage.set(0)
            self.ice_trap_weight.set("none")
            self.stun_trap_weight.set("none")
            self.literature_trap_weight.set("none")
            self.timer_trap_weight.set("none")
            self.reverse_trap_weight.set("none")
            self.thwimp_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.sfx_shuffle.set("none")
            self.mario_palette.set("random")
            self.level_palette_shuffle.set("on_curated")
            self.overworld_palette_shuffle.set("on_curated")
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
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.max_yoshi_egg_cap.set(80)
            self.percentage_of_yoshi_eggs.set(25) # 20 eggs
            self.dragon_coin_checks.set(False)
            self.moon_checks.set(False)
            self.hidden_1up_checks.set(False)
            self.bonus_block_checks.set(False)
            self.blocksanity.set(False)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("none")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression_minus_yoshi_eggs")
            self.junk_fill_percentage.set(0)
            self.trap_fill_percentage.set(0)
            self.ice_trap_weight.set("none")
            self.stun_trap_weight.set("none")
            self.literature_trap_weight.set("none")
            self.timer_trap_weight.set("none")
            self.reverse_trap_weight.set("none")
            self.thwimp_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.sfx_shuffle.set("none")
            self.mario_palette.set("random")
            self.level_palette_shuffle.set("on_curated")
            self.overworld_palette_shuffle.set("on_curated")
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
            self.checks = 157
        
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.max_yoshi_egg_cap.set(80)
            self.percentage_of_yoshi_eggs.set(63) # 50 eggs
            self.dragon_coin_checks.set(False)
            self.moon_checks.set(False)
            self.hidden_1up_checks.set(False)
            self.bonus_block_checks.set(False)
            self.blocksanity.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression_minus_yoshi_eggs")
            self.junk_fill_percentage.set(25)
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("medium")
            self.stun_trap_weight.set("none")
            self.literature_trap_weight.set("none")
            self.timer_trap_weight.set("none")
            self.reverse_trap_weight.set("none")
            self.thwimp_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.sfx_shuffle.set("none")
            self.mario_palette.set("random")
            self.level_palette_shuffle.set("on_curated")
            self.overworld_palette_shuffle.set("on_curated")
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
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.max_yoshi_egg_cap.set(80)
            self.percentage_of_yoshi_eggs.set(80) # 60 eggs
            self.dragon_coin_checks.set(False)
            self.moon_checks.set(False)
            self.hidden_1up_checks.set(False)
            self.bonus_block_checks.set(False)
            self.blocksanity.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression_minus_yoshi_eggs")
            self.junk_fill_percentage.set(50)
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("medium")
            self.stun_trap_weight.set("medium")
            self.literature_trap_weight.set("none")
            self.timer_trap_weight.set("none")
            self.reverse_trap_weight.set("none")
            self.thwimp_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.sfx_shuffle.set("none")
            self.mario_palette.set("random")
            self.level_palette_shuffle.set("on_curated")
            self.overworld_palette_shuffle.set("on_curated")
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
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.max_yoshi_egg_cap.set(80)
            self.percentage_of_yoshi_eggs.set(100) # 80 eggs
            self.dragon_coin_checks.set(False)
            self.moon_checks.set(False)
            self.hidden_1up_checks.set(False)
            self.bonus_block_checks.set(False)
            self.blocksanity.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(True)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression_minus_yoshi_eggs")
            self.junk_fill_percentage.set(75)
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("medium")
            self.stun_trap_weight.set("medium")
            self.literature_trap_weight.set("medium")
            self.timer_trap_weight.set("none")
            self.reverse_trap_weight.set("none")
            self.thwimp_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.sfx_shuffle.set("none")
            self.mario_palette.set("random")
            self.level_palette_shuffle.set("on_curated")
            self.overworld_palette_shuffle.set("on_curated")
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
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.max_yoshi_egg_cap.set(80)
            self.percentage_of_yoshi_eggs.set(100) # 80 eggs
            self.dragon_coin_checks.set(False)
            self.moon_checks.set(False)
            self.hidden_1up_checks.set(False)
            self.bonus_block_checks.set(False)
            self.blocksanity.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(False)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("progression_minus_yoshi_eggs")
            self.junk_fill_percentage.set(100)
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("medium")
            self.stun_trap_weight.set("medium")
            self.literature_trap_weight.set("medium")
            self.timer_trap_weight.set("medium")
            self.reverse_trap_weight.set("none")
            self.thwimp_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("fast")
            self.music_shuffle.set("full")
            self.sfx_shuffle.set("none")
            self.mario_palette.set("random")
            self.level_palette_shuffle.set("on_curated")
            self.overworld_palette_shuffle.set("on_curated")
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
            self.checks = 0
            # unrecorded
            
            # actual config
            # explicit is better than implicit
            self.death_link.set(False)
            self.goal.set("yoshi_egg_hunt")
            self.bosses_required.set(0)
            self.max_yoshi_egg_cap.set(80)
            self.percentage_of_yoshi_eggs.set(100) # 80 eggs
            self.dragon_coin_checks.set(False)
            self.moon_checks.set(False)
            self.hidden_1up_checks.set(False)
            self.bonus_block_checks.set(False)
            self.blocksanity.set(True)
            self.bowser_castle_doors.set("fast")
            self.bowser_castle_rooms.set("vanilla")
            self.level_shuffle.set(False)
            self.exclude_special_zone.set(False)
            self.boss_shuffle.set("full")
            self.swap_donut_gh_exits.set(True)
            self.display_received_item_popups.set("all")
            self.junk_fill_percentage.set(100)
            self.trap_fill_percentage.set(100)
            self.ice_trap_weight.set("none")
            self.stun_trap_weight.set("none")
            self.literature_trap_weight.set("medium")
            self.timer_trap_weight.set("medium")
            self.reverse_trap_weight.set("none")
            self.thwimp_trap_weight.set("none")
            self.autosave.set(True)
            self.early_climb.set(False)
            self.overworld_speed.set("slow")
            self.music_shuffle.set("full")
            self.sfx_shuffle.set("none")
            self.mario_palette.set("random")
            self.level_palette_shuffle.set("on_curated")
            self.overworld_palette_shuffle.set("on_curated")
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
        
        swp:float = float(self.max_yoshi_egg_cap.get()) * (float(self.percentage_of_yoshi_eggs.get()) / 100.0)
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