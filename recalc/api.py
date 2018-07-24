from flask.views import MethodView
from flask import jsonify, request, abort

import base64
import json

from common import qlog, xprint, genkey, xor_strings

from DreamGame import DreamGame
from battlefield.Battlefield import Cell
from content.base_types import pirate_basetype, mud_golem_basetype
from content.base_types.demo_hero import demohero_basetype
from game_objects.battlefield_objects.Unit import Unit
from game_objects.dungeon.Dungeon import Dungeon


class DemoAPI(MethodView):
    tmp = {}

    def __init__(self):
        if not request.json:
            abort(400)

    def post(self):
        expected = ['pb1', 'pb2', 'pb3', 'mg', 'he']
        data = {}
        del qlog.buf[:]
        locs = {}

        for item in expected:
            i = request.json.get(item)
            if i:
                x, y = i.split(',')
                locs[item] = Cell(int(x), int(y))

        if len(locs.keys()) != len(expected):
            error = {
                "code": "MISSING_SOMETHING"
            }
            return jsonify({'error': error}), 400

        pirate_band = [Unit(pirate_basetype) for _ in range(3)]
        locations = [locs[item] for item in ['pb1', 'pb2', 'pb3']]
        unit_locations = {pirate_band[i]: locations[i] for i in range(3)}
        unit_locations[Unit(mud_golem_basetype)] = locs['mg']
        dun = Dungeon(unit_locations, 8, 8, hero_entrance=locs['he'])
        test_game = DreamGame.start_dungeon(dun, Unit(demohero_basetype))
        all_units = test_game.print_all_units()
        xprint(all_units)
        hero_turns = test_game.loop(player_berserk=True)
        xprint("hero has made {} turns.".format(hero_turns))
        message = json.dumps({'log': qlog.buf})
        key = genkey(len(message))
        ciphertext = xor_strings(bytes(message, "ascii"), key)
        byt1 = base64.standard_b64encode(ciphertext)
        byt2 = base64.standard_b64encode(key)
        data['b1'] = byt1.decode('ascii')
        data['b2'] = byt2.decode('ascii')
        output = json.dumps(data)
        return output, 200

    def get(self):
        return json.dumps(self.tmp), 200


