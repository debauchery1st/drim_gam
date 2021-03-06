from my_utils.named_enums import auto, NameEnum

class EventsChannels(NameEnum):
    DamageChannel = auto()
    HealingChannel = auto()

    MovementChannel = auto()
    TurnChannel = auto()
    AttackChannel = auto()

    ActiveChannel = auto()

    UnitDiedChannel = auto()
    ObstacleDestroyedChannel = auto()
    ItemDestroyedChannel = auto()

    BuffAppliedChannel = auto()
    BuffDetachedChannel = auto()
    BuffDispelledChannel = auto()
    BuffExpiredChannel = auto()



from GameLog import gamelog

class EventsPlatform:

    interrupts = { ch: set() for ch in EventsChannels }
    triggers = { ch: set() for ch in EventsChannels }

    @staticmethod
    def process_event(event):

        channel = event.channel
        interrupts = EventsPlatform.interrupts[channel]
        triggers = EventsPlatform.triggers[channel]

        for interrupt in list(interrupts):
            assert isinstance(event, interrupt.target_event_cls)
            interrupt.try_on_event(event)

        if not event.interrupted and event.check_conditions():
            gamelog(event)
            event.resolve()
            for trigger in list(triggers):
                assert isinstance(event, trigger.target_event_cls)
                trigger.try_on_event(event)
        else:
            gamelog(repr(channel)+": INTERRUPTED")
