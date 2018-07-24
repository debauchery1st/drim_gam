import requests
import json
import binascii

APP_TAG = "DEMO-GAME"


def xor_strings(s1, s2):
    if isinstance(s1, str):
        return "".join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))
    else:
        return bytes([a ^ b for a, b in zip(s1, s2)])


def decode_log(jobj):
    return json.loads(xor_strings(binascii.a2b_base64(jobj['b1']), binascii.a2b_base64(jobj['b2'])).decode('utf8'))


def unwrap_log(decoded):
    end_tag = "[/{}]".format(APP_TAG)
    log = decoded['log']
    return [_.split('Z] ')[1].split(end_tag)[0].strip() for _ in log]


def demo_event_log():
    return unwrap_log(decode_log(requests.get('http://127.0.0.1:5000/demo/').json()))


def print_log(the_log):
    for item in the_log:
        print(item)


print('\n\nDEMO\n\n')


test_log = demo_event_log()
print_log(test_log)


# example POST
payload = {'pb1': '4,1', 'pb2': '4,5', 'pb3': '3,5', 'mg': '3,3', 'he': '3,2'}
url = "http://127.0.0.1:5000/recalc/"
headers = {'content-type': 'application/json'}
r = requests.post(url, data=json.dumps(payload), headers=headers)


if r.status_code == 200:
    print("\n\nRECALCULATING...\n\n")
    test_log = unwrap_log(decode_log(json.loads(r.text)))
    print_log(test_log)
