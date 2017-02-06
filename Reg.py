from requests import Request, Session
import random
import json

_email = 'vhzk' + str(random.choice(range(100, 999))) + '@gmai.com'

_device_id = '6090046' + str(random.choice(range(100, 999))) + '32516443250' + str(random.choice(range(100, 999)))

_login = 'ritalami' + str(random.choice(range(100, 999)))

_body = {
    'reg0': '{"locale":"en","model":"GT-P5210","os":"ANDROID","app_version":"3.0.3","device_id":"' + _device_id + '","maker":"samsung","os_version":"4.2.2"}',
    'reg': '{"password":"123123guu","email":"' + _email + '","device_id":"' + _device_id + '","login":"' + _login + '"}'}

_url = {'main': 'https://kernel.mom.life/api/v1/feed/main',
        'message': 'https://kernel.mom.life/api/v1/messenger/message',
        'reg0': 'https://kernel.mom.life/api/v1/device',
        'reg': 'https://kernel.mom.life/api/v1/reg',
        'reg1': 'https://kernel.mom.life/api/v1/reg/check/login?device_id=' + _device_id + '&email=' + _email + '&login=' + _login,
        'reg2': 'https://kernel.mom.life/api/v1/reg/check/email?device_id=' + _device_id + '&email=' + _email,
        'reg3': 'https://kernel.mom.life/api/v1/reg/check/login?device_id=' + _device_id + '&email=' + _email + '&login=' + _login}

# _proxies = {'https': '192.168.1.25:8888',
#             'http': '192.168.1.25:8888'}

_proxies = False

_cert = 'C://FiddlerRoot.pem'

_headers = {'reg0': {'appver': '3.0.3',
                     'User-Agent': 'Android 4.2.2 samsung GT-P5210',
                     'Content-Type': 'application/json; charset=UTF-8',
                     'Content-Length': str(len(_body['reg0'])),
                     'Host': 'kernel.mom.life',
                     'Connection': 'Keep-Alive',
                     'Accept-Encoding': 'gzip'},
            'reg': {'appver': '3.0.3',
                    'User-Agent': 'Android 4.2.2 samsung GT-P5210',
                    'Content-Type': 'application/json; charset=UTF-8',
                    'Content-Length': str(len(_body['reg'])),
                    'Host': 'kernel.mom.life',
                    'Connection': 'Keep-Alive',
                    'Accept-Encoding': 'gzip'},
            'reg1': {'appver': '3.0.3',
                     'User-Agent': 'Android 4.2.2 samsung GT-P5210',
                     'Host': 'kernel.mom.life',
                     'Connection': 'Keep-Alive',
                     'Accept-Encoding': 'gzip'}}

def findeUserBase():
    f = open('reg.txt', 'r')
    str_bearer = f.readlines()[1]
    print('str_bearer = ', str_bearer)
    headers = {'app-os': 'android',
         'appver': '2.8.6',
         'Authorization': 'Bearer ' + str_bearer, \
         'Host': 'kernel.mom.life', \
         'Connection': 'Keep-Alive', \
         'Accept-Encoding': 'gzip', \
         'User-Agent': 'okhttp/3.4.1'}

    req = Request('GET', _url['main'], headers=headers)
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    # print('ans.json() = ', ans.json())
    # if 'status' in ans.json():
    #     if ans.json()['status'] == 401:
    #         return 0
    if 'users' in ans.json():
        return ans.json()['users'][0]['id']
    return 0

def reg():
    f = open('reg.txt', 'r')
    bearer = f.readlines()[1]
    f.close()
    user_id = findeUserBase()
    headers= {'app-os': 'android', \
                'appver': '2.8.6', \
                'Authorization': 'Bearer ' + bearer, \
                'Content-Type': 'application/json; charset=UTF-8', \
                'Content-Length': '1', \
                'Host': 'kernel.mom.life', \
                'Connection': 'Keep-Alive', \
                'Accept-Encoding': 'gzip', \
                'User-Agent': 'okhttp/3.4.1'}
    message = {"payload": '-', "user_id": user_id}
    req = Request('POST', _url['message'], headers=headers, json=message)
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    print('ans.json() = ', ans.json())
    if not('fields' in ans.json()):
        print('Old accaunt')
        return bearer

    print('Create new account')
    req = Request('POST', _url['reg0'], _headers['reg0'])
    prep = req.prepare()
    prep.body = _body['reg0']
    s = Session()
    s.send(prep, proxies=_proxies, verify=False)
    s.close()

    s = Session()
    for x in [_url['reg1'], _url['reg2'], _url['reg3']]:
        s.get(x, headers=_headers['reg1'], proxies=_proxies, verify=False)
    s.close()

    req = Request('POST',_url['reg'],_headers['reg'])
    prepped = req.prepare()
    print('_body["reg"] = ', _body['reg'])
    prepped.body = _body['reg']
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    if ans.status_code == 201:
        print('reg = ',ans.json())
        print(_body['reg'])
        f = open('reg.txt', 'w')
        f.write(_body['reg'])
        f.write('\n')
        f.write(ans.json()['token'])
        f.close()
        return ans.json()['token']

    return 0