from flask import Blueprint
import sys
from os import path
import base64
import json
from launch import demo_game
from common import qlog, xprint, genkey, xor_strings


demo_app = Blueprint('demo_app', __name__)

if not path.isfile("log.txt"):
    f = open("log.txt", "w")
    f.close()

out_log = open("log.txt", "r+")
sys.stdout = out_log


@demo_app.route('/demo/')
def demo():
    data = {}
    del qlog.buf[:]
    test_game = demo_game()
    all_units = test_game.print_all_units()
    xprint(all_units)
    hero_turns = test_game.loop(player_berserk=True)
    xprint("hero has made {} turns.".format(hero_turns))
    message = json.dumps({'log': qlog.buf})
    key = genkey(len(message))
    byt1 = base64.standard_b64encode(xor_strings(bytes(message, "ascii"), key))
    byt2 = base64.standard_b64encode(key)
    data['b1'] = byt1.decode('ascii')
    data['b2'] = byt2.decode('ascii')
    output = json.dumps(data)
    return output, 200

