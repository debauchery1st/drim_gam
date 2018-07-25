from __future__ import print_function, unicode_literals
from os import urandom
from datetime import datetime

import json
import binascii


APP_TAG = "DEMO-GAME"
SERVER_IP = '127.0.0.1'
SERVER_PORT = 5000


class QuickLog:
    def __init__(self, **kwargs):
        if QuickLog.__instance is None:
            QuickLog.__instance = QuickLog.__QuickLog(**kwargs)

    class __QuickLog:
        buf = []

        def __init__(self, **kwargs):
            pass
    __instance = None

    def __getattr__(self, item):
        if QuickLog.__instance:
            return getattr(QuickLog.__instance, item)

    def __setattr__(self, key, value):
        if QuickLog.__instance:
            return setattr(QuickLog.__instance, key, value)


qlog = QuickLog()  # a highlander log

# The cli (Godot) parses the log, line by line,
# playing the AI battle scenario like a karaoke song.
#
# The only thing I found missing from the battle log was
# fixed by wrapping the **(AttackEvent) with a new decorator I called *(@war_gps)
#                  * see: demo/decorators.py
#                 ** see: mechanics/combat/AttackEvent.py:
#
# LOG_LANG is used in the Godot Project to parse the log
# (I am leaving it here as a reference)

LOG_LANG = {
    "INIT": "There is a ",
    "ATTR": " with ",
    "LOCATION": " at ",
    "MOVES": " moves from ",
    "A2B": " to ",
    "ATTACK": " attacks ",
    "DAMAGE": "DamageTypes",
    "IMPACT": "ImpactFactor",
    "DEATH": " is killed by ",
    "WIN": "VICTORY",
    "MISS": "MISS",
    "HIT": "HIT",
    "GRAZE": "GRAZE",
    "CRUSH": "CRUSH",
    "CRITICAL": "CRIT",
    "TAKES0": " recieves ",
    "TAKES1": " receives ",
    "WAR_GPS": "[WAR_GPS]"
}


def xprint(*args):
    """ use "xprint" instead of "print" if you want the Godot client to hear you. """
    # wrap with a timestamp and echo to highlander log
    now = datetime.utcnow().replace(second=0, microsecond=0)
    test = now.isoformat("T") + "Z"
    res = "[{}]".format(test)
    for arg in args:
        if arg is not None:
            res += " {}".format(arg)
    res += " [/{}]".format(APP_TAG)
    qlog.buf.append(res)
    print(res)


def genkey(length):
    return urandom(length)


def xor_strings(s, t):
    if isinstance(s, str):
        return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s, t))
    else:
        return bytes([a ^ b for a, b in zip(s, t)])


def decode_log(jobj):
    return json.loads(xor_strings(
        binascii.a2b_base64(jobj['b1']),
        binascii.a2b_base64(jobj['b2'])
    ).decode('utf8'))


def unwrap_log(decoded):
    end_tag = "[/{}]".format(APP_TAG)
    return [_.split('Z] ')[1].split(end_tag)[0].strip() for _ in decoded]

