from battlefield.Battlefield import Battlefield, Cell
from mechanics.combat import Attack
from mechanics.turns import SequentialTM
from mechanics.fractions import Fractions
from mechanics.AI import AstarAI, RandomAI
from battlefield.MovementEvent import MovementEvent
import my_globals

from common import xprint


class DreamGame:

    def __init__(self, bf, unit_locations = None):
        self.battlefield = bf
        self.the_hero = None
        self.fractions = {}
        self.brute_ai = AstarAI(bf, self.fractions)
        self.random_ai = RandomAI(bf)
        self.turns_manager = None
        my_globals.the_game = self

        if unit_locations:
            bf.place_many(unit_locations)

    @staticmethod
    def start_dungeon(dungeon, hero):

        unit_locations = dungeon.unit_locations
        unit_locations[hero] = dungeon.hero_entrance

        game = DreamGame(Battlefield(dungeon.h, dungeon.w), unit_locations)
        game.the_hero = hero
        game.fractions.update({unit: Fractions.OBSTACLES for unit in dungeon.unit_locations
                               if "Wall" in unit.type_name})
        game.fractions.update({unit:Fractions.ENEMY for unit in dungeon.unit_locations if unit not in game.fractions})
        game.fractions[hero] = Fractions.PLAYER

        units_who_make_turns = [unit for unit in unit_locations.keys()
                                if game.fractions[unit] is not Fractions.OBSTACLES]
        game.turns_manager = SequentialTM(units_who_make_turns)

        return game


    @staticmethod
    def custom_init(bf):
        DreamGame(bf)


    @staticmethod
    def get_unit_at(coord):
        return my_globals.the_game.battlefield.units_at[coord]


    @staticmethod
    def get_units_distances_from(p):
        return my_globals.the_game.battlefield.get_units_dists_to(p)

    def order_move(self, unit, target_cell):
        # units can only go to adjecent locations
        if not self.battlefield.distance_unit_to_point(unit, target_cell) <= 1:
            return False

        if target_cell in self.battlefield.units_at:
            target = self.battlefield.units_at[target_cell]
            self.attack(unit, target)
        else:
            MovementEvent(self.battlefield, unit, target_cell)

        return True

    def attack(self, attacker, target):
        Attack.attack(attacker, target)

    @staticmethod
    def get_location(unit):
        assert unit in my_globals.the_game.battlefield.unit_locations
        return my_globals.the_game.battlefield.unit_locations[unit]

    def unit_died(self, unit):
        del self.fractions[unit]
        self.battlefield.remove(unit)
        self.turns_manager.remove_unit(unit)
        unit.alive = False

    def loop(self, player_berserk=False):
        count_hero_turns = 0
        while True:
            active_unit = self.turns_manager.get_next()
            target_cell = None
            if self.fractions[active_unit] is Fractions.PLAYER:
                count_hero_turns += 1
                if player_berserk:
                    target_cell=self.brute_ai.decide_step(active_unit, target_fraction=Fractions.ENEMY)
                else:
                    orders = input("Tell me where to go!")
                    x, y = [int(coord) for coord in orders.split()]
                    xprint(x,y)
                    target_cell = Cell(x, y)

            elif self.fractions[active_unit] is Fractions.ENEMY:
                target_cell = self.brute_ai.decide_step(active_unit)
            elif self.fractions[active_unit] is Fractions.NEUTRALS:
                target_cell = self.random_ai.decide_step(active_unit)

            self.order_move(active_unit, target_cell)
            game_over = self.game_over()
            if game_over:
                xprint(game_over)
                return count_hero_turns
            # self.print_all_units()

    def game_over(self):
        own_units = [unit for unit in self.fractions if self.fractions[unit] is Fractions.PLAYER]
        enemy_units = [unit for unit in self.fractions if self.fractions[unit] is Fractions.ENEMY]

        if len(own_units) == 0:
            return "DEFEAT"
        elif len(enemy_units) == 0:
            return "VICTORY"
        else:
            return None

    def print_all_units(self):
        for unit, xy in self.battlefield.unit_locations.items():
            x, y = xy
            xprint("There is a {} at ({},{})".format(unit, x, y))

    def __repr__(self):
        return "{} by {} dungeon with {} units in it.".format(self.battlefield.h, self.battlefield.w, len(self.battlefield.units_at))



