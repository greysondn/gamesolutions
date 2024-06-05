from .game    import Game
from .genre   import Genre
from .machine import Machine

MACHINES_TO_GAMES:dict[Machine, int] = {
    Machine.STORM_TOWER     :   Game.DOOM_1993.value + 
                                Game.RISK_OF_RAIN_2.value + 
                                Game.ROGUE_LEGACY.value +
                                Game.SONIC_ADVENTURE_2_BATTLE.value +
                                Game.STARDEW_VALLEY.value +
                                Game.SUPER_MARIO_WORLD.value,
                                
    Machine.URSINE_LAPTOP   :   Game.DOOM_1993.value +
                                Game.ROGUE_LEGACY.value +
                                Game.SUPER_MARIO_WORLD.value,
}

GAMES_TO_GENRES:dict[Game, int] = {
    Game.DOOM_1993 :    Genre.IMPLEMENTED.value +
                        Genre.FIRST_PERSON_SHOOTER.value +
                        Genre.SHOOTER.value,
    
    Game.RISK_OF_RAIN_2 :   Genre.ROGUELITE.value +
                            Genre.SHOOTER.value +
                            Genre.THIRD_PERSON_SHOOTER.value,
    
    Game.ROGUE_LEGACY : Genre.IMPLEMENTED.value +
                        Genre.PLATFORMER.value +
                        Genre.ROGUELITE.value,
    
    Game.SONIC_ADVENTURE_2_BATTLE : Genre.PLATFORMER.value,
    
    Game.STARDEW_VALLEY :   Genre.FARMING_SIMULATOR.value +
                            Genre.ROGUELITE.value +
                            Genre.RPG.value,
    
    Game.SUPER_MARIO_WORLD :    Genre.PLATFORMER.value,
}