from mechanics.flexi_targeting.event.event_targeting.EventTargeting import EventTargeting
from game_objects.battlefield_objects.Unit.Unit import Unit
from battlefield.Battlefield import Coordinates
from DreamGame import DreamGame

class Event:
    def __init__(self, effects, event_targeting):
        self.effects = effects
        self.event_targeting = event_targeting

    def resolve(self, source, user_targeting):
        if self.event_targeting == EventTargeting.TARGET_UNIT:
            assert isinstance(user_targeting.target, Unit)
            target_unit = user_targeting.target
            for effect in self.effects:
                effect.apply(source, target_unit)

        elif self.event_targeting == EventTargeting.UNIT_ON_TARGET_CELL:
            assert isinstance(user_targeting.target, Coordinates)
            target_unit = DreamGame.get_unit_at(user_targeting.target)
            for effect in self.effects:
                effect.apply(source, target_unit)