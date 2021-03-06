from game_objects.spells import  SpellConcept
from character_creation.MasteriesEnum import MasteriesEnum
from mechanics.actives import SingleUnitTargeting, Cost
from content.spells.callbacks import healing_callback, lightning_bolt_callback

lightning_concept = SpellConcept(name="lightning bolt",
                                 school=MasteriesEnum.LIGHTNING,
                                 targeting_cls=SingleUnitTargeting,
                                 complexity=30,
                                 cost=Cost(4, 40, 0, readiness=1),
                                 amount=60, duration=None, precision_factor=1,
                                 distance=5, radius=None,
                                 resolve_callback=lightning_bolt_callback)

heal_concept = SpellConcept(name="healing",
                            school=MasteriesEnum.HOLY,
                            targeting_cls=SingleUnitTargeting,
                            complexity=30,
                            cost=Cost(4, 40, 0, readiness=1),
                            amount=60, duration=None, precision_factor=1,
                            distance=2, radius=None,
                            resolve_callback=healing_callback)