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


qlog = QuickLog()


def xprint(*args):
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

