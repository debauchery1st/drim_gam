import inspect
from mechanics.events.EventsPlatform import EventsPlatform

class Trigger:
    def __init__(self, target_event_cls, conditions, source = None,
                 effect_trigger_pack = None, is_interrupt = False, event_callbacks=None):

        assert inspect.isclass(target_event_cls)
        assert isinstance(conditions, dict)
        self.target_event_cls = target_event_cls
        self.conditions = conditions
        assert (effect_trigger_pack is None) == (source is None)
        self.effect_pack = effect_trigger_pack
        self.source = source
        if event_callbacks:
            assert is_interrupt
        self.is_interrupt = is_interrupt
        self.modify_event = event_callbacks
        self.activate()

    def activate(self):
        if self.is_interrupt:
            EventsPlatform.interrupts[self.target_event_cls.channel].add(self)
        else:
            EventsPlatform.triggers[self.target_event_cls.channel].add(self)

    def check_conditions(self, event):
        assert isinstance(event, self.target_event_cls)
        for key, value in self.conditions.items():
            if getattr(event, key) != value:
                return False

        return True

    def try_on_event(self, event):
        if self.check_conditions(event):
            if self.effect_pack:
                self.effect_pack.resolve(self.source, event)
            if self.modify_event:
                for modifier in self.modify_event:
                    modifier(self, event)

    def deactivate(self):
        if self.is_interrupt:
            EventsPlatform.interrupts[self.target_event_cls.channel].remove(self)
        else:
            EventsPlatform.triggers[self.target_event_cls.channel].remove(self)


