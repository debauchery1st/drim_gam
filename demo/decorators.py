from functools import wraps

import json

import my_globals

from common import xprint


def get_location(unit):
    assert unit in my_globals.the_game.battlefield.unit_locations
    return my_globals.the_game.battlefield.unit_locations[unit]


def war_gps(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if len(args) == 4:
            e, s, t, w = args
        elif len(args) == 3:
            s, t, w = args
        elif len(args) == 2:
            s, t = args
            w = 'none'
        else:
            return
        source = {'name': s.type_name, 'location': get_location(s)}
        weapon = w.name
        target = {'name': t.type_name, 'location': get_location(t)}
        battle = json.dumps({'a': source, 'd': target, 'w': weapon})
        output = "[WAR_GPS] {} [/WAR_GPS]".format(battle)
        xprint(output)
        return f(*args, **kwargs)
    return decorated_function
