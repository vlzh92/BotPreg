import sys


from requests import Request, Session
import time
import random
import http
import socket
from multiprocessing.dummy import Pool as ThreadPool
pool = ThreadPool(16)
TEMP = 0

_bearer = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE0ODU4NjAyOTUsImV4cCI6MTQ4NjQ2NTA5NSwiZGV2aWNlIjoiNjA5MDA0NjQ0MzMyNTE2NDQzMjUwNDk0IiwidXNlciI6IjU4MjM3ODFmODEzOTgzNzA1YzhiNDU2ZCIsInR5cGUiOjF9.lhWXMh1AqxFxycdKZAOz9Bzq35jCEQBpoZJxdVQo5394EbTCa_Xaf1grMTG0CmJeWNaO5y3LLve-i9EZc_pYnrkbALoQ3a3ky2mP6MMpJehhWhRhzkG22K4sgLDHhcSdQeKa6V1Ctor8P6559fbotSqX-rORnYEUL_8MMlcu1jGv5v7btILFkmHSR7DA9cdj0jz6wKyipkj2IYc2yzIjp63tPimRmTN5pKdzKjwojk8nUeJa9cI_rJtmr9EE8RXX20vTfYQqg6MyOQKrIeqEPqvyylfV4gZUcC1UAh4amEz7nFGJI3mwUUMsqKy-vMPfRniXY0M2e60sf3KaZnfzxpRuj_rYZOpx6If9EFWtd7hHnv1Ua852LAx_fIEdRdZBkKvNzeZdVyZ-GCmF_UlcOQfNLPLJtfCGXrC097NwD7yhesaxxf9YnZ95SxCPbgu4t2Hhzvi-oro1yDuqXd7GxUAIZb4zP0z-SQ0gmPei-v7yO0ogDjGh7wWRdpOecxp7tCIakVM9aCcKU8L7-CkT0B7xqvbdjxgtW7DGV4j7Wki9hG5pSJRL4hJ02QHDSng4Nn0V0UHMqU0Fle06k13sqrOiMr4V3t88yShDQ3F9G_T2dHoF5efb-K2jfaVLwTQizTq2ZzSDFT05jt6d9uf9UrnQRV61h74gJdIHv6O0YG0'

if __name__ == '__main__':
    print('SentBox is a main')
else:
    print('SentBox is imported')

_url = {'main':'https://kernel.mom.life/api/v1/feed/main',
        'message':'https://kernel.mom.life/api/v1/messenger/message',
        'messageAsq': 'https://kernel.mom.life/api/v1/messenger/messages',
        'read':'https://kernel.mom.life/api/v1/messenger/messages/user/',
        'profile': 'https://kernel.mom.life/api/v1/profile/',
        'relations':'https://kernel.mom.life/api/v1/profile/relations/',
        'conect':'kernel.mom.life:443',
        'test':'https://kernel.mom.life/api/v1/feed/user/56af491884398335088b4567?direction=older&per_page=3'}


_proxies = {'https': '192.168.1.25:8888',
           'http': '192.168.1.25:8888'}

_cert = 'C:/FiddlerRoot.cer'

_headers = {'main':{ 'app-os': 'android',\
                    'appver': '2.8.6',\
                    'Authorization': 'Bearer ' + str(_bearer) ,\
                    'Host': 'kernel.mom.life',\
                    'Connection': 'Keep-Alive',\
                    'Accept-Encoding': 'gzip',\
                    'User-Agent': 'okhttp/3.4.1'},
            'message': {'app-os': 'android', \
                    'appver': '2.8.6', \
                    'Authorization': 'Bearer ' + str(_bearer), \
                    'Content-Type': 'application/json; charset=UTF-8',\
                    'Content-Length':'54',\
                    'Host': 'kernel.mom.life', \
                    'Connection': 'Keep-Alive', \
                    'Accept-Encoding': 'gzip', \
                    'User-Agent': 'okhttp/3.4.1'},
            'messageAsq': {
                'app-os': 'android', \
                'appver': '2.8.6', \
                'Authorization': 'Bearer ' + str(_bearer), \
                'Host': 'kernel.mom.life', \
                'Connection': 'Keep-Alive', \
                'Accept-Encoding': 'gzip', \
                'User-Agent': 'okhttp/3.4.1'
            },
            'test':{'app - os':'android',
                    'appver': '2.8.6',
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE0ODU4NjAyOTUsImV4cCI6MTQ4NjQ2NTA5NSwiZGV2aWNlIjoiNjA5MDA0NjQ0MzMyNTE2NDQzMjUwNDk0IiwidXNlciI6IjU4MjM3ODFmODEzOTgzNzA1YzhiNDU2ZCIsInR5cGUiOjF9.lhWXMh1AqxFxycdKZAOz9Bzq35jCEQBpoZJxdVQo5394EbTCa_Xaf1grMTG0CmJeWNaO5y3LLve - i9EZc_pYnrkbALoQ3a3ky2mP6MMpJehhWhRhzkG22K4sgLDHhcSdQeKa6V1Ctor8P6559fbotSqX - rORnYEUL_8MMlcu1jGv5v7btILFkmHSR7DA9cdj0jz6wKyipkj2IYc2yzIjp63tPimRmTN5pKdzKjwojk8nUeJa9cI_rJtmr9EE8RXX20vTfYQqg6MyOQKrIeqEPqvyylfV4gZUcC1UAh4amEz7nFGJI3mwUUMsqKy - vMPfRniXY0M2e60sf3KaZnfzxpRuj_rYZOpx6If9EFWtd7hHnv1Ua852LAx_fIEdRdZBkKvNzeZdVyZ - GCmF_UlcOQfNLPLJtfCGXrC097NwD7yhesaxxf9YnZ95SxCPbgu4t2Hhzvi - oro1yDuqXd7GxUAIZb4zP0z - SQ0gmPei - v7yO0ogDjGh7wWRdpOecxp7tCIakVM9aCcKU8L7 - CkT0B7xqvbdjxgtW7DGV4j7Wki9hG5pSJRL4hJ02QHDSng4Nn0V0UHMqU0Fle06k13sqrOiMr4V3t88yShDQ3F9G_T2dHoF5efb - K2jfaVLwTQizTq2ZzSDFT05jt6d9uf9UrnQRV61h74gJdIHv6O0YG0',
                    'Host': 'kernel.mom.life',
                    'Connection': 'Keep - Alive',
                    'Accept - Encoding': 'gzip',
                    'User - Agent': 'okhttp / 3.4.1'
}
           }

_body = '''Version: 3.1 (TLS/1.0)
Random: 58 90 74 3D E8 D3 9A FA C4 86 2A B1 58 61 06 A6 4E E7 13 38 06 81 A7 68 95 55 A9 25 EA F3 DF 83
"Time": 9/3/2002 14:35:04
SessionID: 9E 2B 00 00 09 E1 FC B2 3B EF 2C 62 55 61 F0 DC 83 9C 62 4A 1D 9B 0B F8 67 3D 5D 77 D0 96 EC 81
Extensions:
	server_name	kernel.mom.life
	ec_point_formats	uncompressed [0x0], ansiX962_compressed_prime [0x1], ansiX962_compressed_char2  [0x2]
	elliptic_curves	sect571r1 [0xE], sect571k1 [0xD], secp521r1 [0x19], sect409k1 [0xB], sect409r1 [0xC], secp384r1 [0x18], sect283k1 [0x9], sect283r1 [0xA], secp256k1 [0x16], secp256r1 [0x17], sect239k1 [0x8], sect233k1 [0x6], sect233r1 [0x7], secp224k1 [0x14], secp224r1 [0x15], sect193r1 [0x4], sect193r2 [0x5], secp192k1 [0x12], secp192r1 [0x13], sect163k1 [0x1], sect163r1 [0x2], sect163r2 [0x3], secp160k1 [0xF], secp160r1 [0x10], secp160r2 [0x11]
	SessionTicket	empty
Ciphers:
	[C00A]	TLS1_CK_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
	[C009]	TLS1_CK_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
	[C013]	TLS1_CK_ECDHE_RSA_WITH_AES_128_CBC_SHA
	[C014]	TLS1_CK_ECDHE_RSA_WITH_AES_256_CBC_SHA
	[0033]	TLS_DHE_RSA_WITH_AES_128_SHA
	[0039]	TLS_DHE_RSA_WITH_AES_256_SHA
	[002F]	TLS_RSA_AES_128_SHA
	[0035]	TLS_RSA_AES_256_SHA
	[000A]	SSL_RSA_WITH_3DES_EDE_SHA
	[00FF]	TLS_EMPTY_RENEGOTIATION_INFO_SCSV

Compression:
	[00]	NO_COMPRESSION'''


def conection():
    req = Request('CONNECT', _url['conect'], headers=_headers['conect'])
    prepped = req.prepare()
    prepped.body = _body
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    return 0

def findUsersInformation(user_id):
    req = Request('GET', _url['profile'] + user_id, headers=_headers['main'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    user = ans.json()['user']
    childrens = user['children']
    children = []

    for i in childrens:
        children.append([i['birthday'], i['name'], i['sex']])

    return [user['id'],
            user['locality'],
            user['name'],
            user['login'],
            children,
            user['privacy_settings'],
            user['counters']]

def findeUserBase():
    req = Request('GET', _url['main'], headers=_headers['main'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    print('ans.status = ', ans.status_code)
    return ans.json()['users'][0]['id']

def findeUsers(user_id):
    req = Request('GET', _url['relations']+user_id+'/2?page=0&per_page=1', headers=_headers['main'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()

    if not('count' in ans.json()):
        print('ans.json() = ', ans.json())
        return []

    count = ans.json()['count']
    if count > 1000:
        count = 1000
    print('count = ', count)

    req = Request('GET', _url['relations']+user_id+'/2?page=0&per_page='+ str(count), headers=_headers['main'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()

    users_id = set([])

    if not('users' in ans.json()):
        return []

    users = ans.json()['users']
    for i in users:
        users_id.add(i['id'])

    req = Request('GET', _url['relations'] + user_id + '/1?page=0&per_page=1', headers=_headers['main'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    count = ans.json()['count']
    if count > 1000:
        count = 1000
    print('count = ', count)

    req = Request('GET', _url['relations'] + user_id + '/1?page=0&per_page=' + str(count), headers=_headers['main'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()

    users = ans.json()['users']
    for i in users:
        users_id.add(i['id'])

    return users_id

def findeUsersBig(user_id):

    x = 10
    count = 1000 / x
    number = 0
    start_2 = 400 * x

    def count_user(page):
        req = Request('GET',_url['relations'] + user_id + '/' + str(page) + '?page=' + str(page) + '&per_page=' + str(15), headers=_headers['main'])
        prepped = req.prepare()
        s = Session()
        ans = s.send(prepped,
                     proxies=_proxies,
                     verify=False
                     )
        s.close()
        print('ans.status_code = ', ans.status_code)
        print('ans.json() = ', ans.json())
        if not ('count' in ans.json()):
            return []

        return ans.json()['count']

    def req_user(number, page):
        req = Request('GET', _url['relations']+user_id+'/'+str(page)+'?page='+str(number)+'&per_page='+ str(count), headers=_headers['main'])
        prepped = req.prepare()
        s = Session()
        ans = s.send(prepped,
                     proxies=_proxies,
                     verify=False
                     )
        s.close()

        print('ans.raw = ', ans.raw)
        print('ans.headers = ', ans.headers)
        print('ans.status_code = ', ans.status_code)
        print('(ans.status_code == 504)=', ans.status_code == '504')
        if ans.status_code == 504:
            print('Exit')
            time.sleep(10)
            return []

        if ans.status_code == 502:
            print('Exit')
            time.sleep(10)
            return []

        print('ans.json() = ', ans.json())
        print('not(users in ans.json()) = ', not ('users' in ans.json()))
        if not('users' in ans.json()):
            return []

        users_id = []

        print('ans.status = ', ans.status_code)
        users = ans.json()['users']
        for i in users:
            users_id.append(i['id'])

        return users_id

    users_id = []
    print('round(count_user(1)/1000) = ', round(count_user(1) / count))
    end_1 = round(count_user(1) / count)
    for i in range(end_1):
        print('ready_1 = ',i/ end_1 * 100, ' %')
        time.sleep(1 * random.weibullvariate(1, 0.5))
        inspection(req_user(i, 1))
        # users_id.append(req_user(i,1))

    end_2 = round(count_user(2) / count)
    print('round(count_user(2)/1000) = ', end_2)
    for i in range(start_2,end_2):
        print('i = ', i / x)
        print('ready_2 = ', i / end_2 * 100, ' %')
        time.sleep(5 * random.weibullvariate(1, 0.5))
        inspection(req_user(i, 2))
        # users_id.append(req_user(i,2))

    print('len(users_id) = ',len(users_id))
    return users_id

def inspection(users):
    f = open('users.txt', 'r')
    str = f.readlines()
    usersParent = set(map(lambda x: x.replace('\n',''),str))
    f.close()
    print('len(usersParent) = ', len(usersParent))
    print('len(users) = ', len(users))
    res = list(set(users) - usersParent)
    print('len(users - usersParent) = ', len(res))
    f = open('users.txt', 'a')
    f.writelines('\n'+'\n'.join(res))
    f.close()
    return res

def multiplicateUsers():
    f = open('users.txt', 'r')
    str = f.readlines()
    usersParent = set(map(lambda x: x.replace('\n',''),str))
    f.close()
    print(len(usersParent))
    for x in usersParent:
        start = time.clock()
        time.sleep(1*random.weibullvariate(1,0.5))
        inspection(findeUsers(x))
        end = time.clock()
        print('delta_t = ',end - start)
    print(len(usersParent))
    # print(multiplicateUsers[-10:0])

def sent(text, user_id):
    req = Request('GET', _url['messageAsq']+'/user/'+str(user_id)+'?with=topic', headers=_headers['messageAsq'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    if 'status' in ans.json():
        message = {"payload": text, "user_id": user_id}
        req = Request('POST', _url['message'], headers=_headers['message'], json=message)
        prepped = req.prepare()
        s = Session()
        ans = s.send(prepped,
                     proxies=_proxies,
                     verify=False
                     )
        s.close()
        return 1
        TEMP += 1
        print('TEMP = ', TEMP)
    return 0

def sentAll(text):
    user = findeUserBase()
    # user = '553631b2ebad6435b0aab53a'
    temp = 0
    temp2 = 0
    for i in range(1000000):
        users = list(findeUsers(user))
        pool.map(lambda x: sent(text,x), users)

        if len(users) < 2:
            user = findeUserBase()
        else:
            user = users[3]
    return 0

# conection()
# print('findeUserBase() = ', findeUserBase())
# print(findUsersInformation(findeUserBase()))
# users = findeUsers(findeUserBase())
# print(len(users))
# inspection(users)

# findeUsersBig('553631b2ebad6435b0aab53a')
# multiplicateUsers()/
# print('_url[test] = ', _url['test'])
# req = Request('GET', _url['test'], headers=_headers['test'])
# prepped = req.prepare()
# s = Session()
# ans = s.send(prepped
#              ,proxies=_proxies
#              ,verify=False
#              )
# print('ans = ',ans.status_code)
# s.close()

text = '''Привет! Поддержи, пожалуйста! Вступи в группу, посвященную материнству и беременности https://vk.com/mos_mam ! В ней много полезного и интересного для всех мамочек! Спасибо огромное!'''
# f = open('users.txt', 'r')

# for i in range(10000):
#     st = f.readline()

# sent(text,findeUserBase())
sentAll(text)

# f.close()

