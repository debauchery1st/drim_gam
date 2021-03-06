from character_creation.MasteriesEnum import MasteriesEnum, MasteriesGroups
from functools import lru_cache
from common import xprint


class Masteries:
    def __init__(self):
        self.exp_spent = {m:0 for m in MasteriesEnum}

    @staticmethod
    @lru_cache(maxsize=512)
    def increment_cost(current_level):
        if current_level == 0:
            return 4
        else:
            if current_level <= 100:
                return int(2 + (current_level ** (5/3)/10) + Masteries.increment_cost(current_level-1))
            else:
                return int(2**(current_level/13) + Masteries.increment_cost(current_level-1))

    @staticmethod
    @lru_cache(maxsize=512)
    def cumulative_cost(current_level):
        return sum([Masteries.increment_cost(i) for i in range(current_level+1)])

    @staticmethod
    def achieved_level(exp):
        level = 0
        while exp > Masteries.cumulative_cost(level+1):
            level += 1

        return level

    @property
    def values(self):
        return { m: Masteries.achieved_level(exp) for m, exp in self.exp_spent.items()}

    @staticmethod
    def requirements(m, level):
        reqs = {}
        for mastery in MasteriesEnum:
            coupling = MasteriesGroups.coupling(mastery, m)
            if mastery is not m and coupling > 0:
                reqs[mastery] = int(level * coupling)

        return reqs

    def calculate_cost(self, mastery_up):

        direct_cost = self.increment_cost(self.values[mastery_up] + 1)
        indirect_costs = {}
        for mastery in MasteriesEnum:
            coupling = MasteriesGroups.coupling(mastery, mastery_up)
            if mastery is not mastery_up and coupling > 0:
                indirect_costs[mastery] = int(direct_cost * coupling) + 1

        total_cost = direct_cost + sum(indirect_costs.values())
        return total_cost, direct_cost, indirect_costs

    def level_up(self, mastery_up):
        total_cost, direct_cost, indirect_costs = self.calculate_cost(mastery_up)
        self.exp_spent[mastery_up] += direct_cost
        for m in indirect_costs:
            self.exp_spent[m] += indirect_costs[m]











if __name__ == "__main__":
    # for i in range(512):
    #     print(i, Masteries.increment_cost(i))
    #
    # for m in MasteriesEnum:
    #     print(m, Masteries.requirements(m,100))


    masteries = Masteries()
    # masteries.exp_spent[MasteriesEnum.AXE] = 5000
    # masteries.exp_spent[MasteriesEnum.SWORD] = 15000
    # masteries.exp_spent[MasteriesEnum.CLUB] = 70

    xprint(masteries.exp_spent)
    xprint(masteries.values)

    while masteries.values[MasteriesEnum.CLUB]<10:
        masteries.level_up(MasteriesEnum.CLUB)
    xprint(masteries.level_up(MasteriesEnum.CLUB))
    xprint(masteries.exp_spent)
    xprint(masteries.values)
    while masteries.values[MasteriesEnum.AXE]<30:
        masteries.level_up(MasteriesEnum.AXE)
    xprint(masteries.level_up(MasteriesEnum.AXE))
    xprint(masteries.exp_spent)
    xprint(masteries.values)
    while masteries.values[MasteriesEnum.SWORD]<50:
        masteries.level_up(MasteriesEnum.SWORD)
    xprint(masteries.level_up(MasteriesEnum.SWORD))
    xprint(masteries.exp_spent)
    xprint(masteries.values)

