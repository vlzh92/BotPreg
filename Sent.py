import sys


from requests import Request, Session
import time
import random

if __name__ == '__main__':
    print('SentBox is a main')
else:
    print('SentBox is imported')

_url = {'main':'https://kernel.mom.life/api/v1/feed/main',
        'message':'https://kernel.mom.life/api/v1/messenger/message',
        'read':'https://kernel.mom.life/api/v1/messenger/messages/user/',
        'profile': 'https://kernel.mom.life/api/v1/profile/',
        'relations':'https://kernel.mom.life/api/v1/profile/relations/'}


_proxies = {'https': '192.168.1.25:8888',
           'http': '192.168.1.25:8888'}

_cert = 'C:/FiddlerRoot.cer'

_headers = {'main':{ 'app-os': 'android',\
                    'appver': '2.8.6',\
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE0ODUwOTA1MzgsImV4cCI6MTQ4NTY5NTMzOCwiZGV2aWNlIjoiNjA5MDA0NjQ0MzMyNTE2NDQzMjUwNDk0IiwidXNlciI6IjU4MjM3ODFmODEzOTgzNzA1YzhiNDU2ZCIsInR5cGUiOjF9.hqJ2xKBo7oHIjxjhZ_lzdgDSg6zBMdz1Mk982fzX2CIfGbuU8umFIQEP-yvPHQsbjnk-O8RlHhof2uNneyrRvP97vvk_Vrsaj9dMgRfRBATw8Wh6XLDPWvCAB3PTwCDNIgHkyESGlcai2uOsq3WKz6wyZr8NVl44mgBEiAi76Nnz71YzCsdrbfcNw5xxA36c5oSaXDlR-MMkHLSzbEuuD89JZS57w2esgwKOjp-KGQK06fqegXDAWeqpPUZavQv5qfbPk9T2Zx-fp3J9RmDjZevXNiWRJWyD2CV1tCrItZaS1yzqk1_QG1Zzdd-V3Vrw4wUzyXU5MSZnVOiCxCQP6TTMOuXsa3PzZwMX95StsDbsE2WY47pz4ddZcSdkTKfxqE_EGMYdSsm86y9mMYTrOAMDP8PRFxTnS_7VDyo5r3hn9I_Pk4G4E2p1R4ABXCv0UHobLKCZokqvTKcF0IRsDdz7vsgUE8aCqfNxcSIeOFBAvmvaj0ev28oBF1Y9gTeRSu-h0DbvjvmYJbPENtnKyrCW2UoC43HxlAzqlVfoMGqUHVL-zJdZaBVPkP2t24wzanIewsD747VwiCMnaCe4JO1qbj3F5R9QIB3RmH0PgtgqGtK5K9UCtn3OgNiJCgHrHpcwg0Q1xkrBGYMYncTuty2IoMCKgHNg-UllZG2Gbo8',\
                    'Host': 'kernel.mom.life',\
                    'Connection': 'Keep-Alive',\
                    'Accept-Encoding': 'gzip',\
                    'User-Agent': 'okhttp/3.4.1'},
           'message': {'app-os': 'android', \
                    'appver': '2.8.6', \
                    'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiJ9.eyJpYXQiOjE0ODUwOTA1MzgsImV4cCI6MTQ4NTY5NTMzOCwiZGV2aWNlIjoiNjA5MDA0NjQ0MzMyNTE2NDQzMjUwNDk0IiwidXNlciI6IjU4MjM3ODFmODEzOTgzNzA1YzhiNDU2ZCIsInR5cGUiOjF9.hqJ2xKBo7oHIjxjhZ_lzdgDSg6zBMdz1Mk982fzX2CIfGbuU8umFIQEP-yvPHQsbjnk-O8RlHhof2uNneyrRvP97vvk_Vrsaj9dMgRfRBATw8Wh6XLDPWvCAB3PTwCDNIgHkyESGlcai2uOsq3WKz6wyZr8NVl44mgBEiAi76Nnz71YzCsdrbfcNw5xxA36c5oSaXDlR-MMkHLSzbEuuD89JZS57w2esgwKOjp-KGQK06fqegXDAWeqpPUZavQv5qfbPk9T2Zx-fp3J9RmDjZevXNiWRJWyD2CV1tCrItZaS1yzqk1_QG1Zzdd-V3Vrw4wUzyXU5MSZnVOiCxCQP6TTMOuXsa3PzZwMX95StsDbsE2WY47pz4ddZcSdkTKfxqE_EGMYdSsm86y9mMYTrOAMDP8PRFxTnS_7VDyo5r3hn9I_Pk4G4E2p1R4ABXCv0UHobLKCZokqvTKcF0IRsDdz7vsgUE8aCqfNxcSIeOFBAvmvaj0ev28oBF1Y9gTeRSu-h0DbvjvmYJbPENtnKyrCW2UoC43HxlAzqlVfoMGqUHVL-zJdZaBVPkP2t24wzanIewsD747VwiCMnaCe4JO1qbj3F5R9QIB3RmH0PgtgqGtK5K9UCtn3OgNiJCgHrHpcwg0Q1xkrBGYMYncTuty2IoMCKgHNg-UllZG2Gbo8',\
                    'Content-Type': 'application/json; charset=UTF-8',\
                    'Content-Length':'54',\
                    'Host': 'kernel.mom.life', \
                    'Connection': 'Keep-Alive', \
                    'Accept-Encoding': 'gzip', \
                    'User-Agent': 'okhttp/3.4.1'}
           }

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

    count = 1000
    number = 0
    start_2 = 297

    def count_user(page):
        req = Request('GET',_url['relations'] + user_id + '/' + str(page) + '?page=' + str(page) + '&per_page=' + str(15), headers=_headers['main'])
        prepped = req.prepare()
        s = Session()
        ans = s.send(prepped,
                     proxies=_proxies,
                     verify=False
                     )
        s.close()
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
    print('round(count_user(1)/1000) = ', round(count_user(1) / 1000))
    end_1 = round(count_user(1) / 1000)
    for i in range(end_1):
        print('ready_1 = ',i/ end_1 * 100, ' %')
        inspection(req_user(i, 1))
        # users_id.append(req_user(i,1))

    end_2 = round(count_user(2) / 1000)
    print('round(count_user(2)/1000) = ', end_2)
    for i in range(start_2,end_2):
        print('i = ', i )
        print('ready_2 = ', i / end_2 * 100, ' %')
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
    message = {"payload": text, "user_id": user_id}
    req = Request('POST', _url['message'], headers=_headers['message'], json=message)
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()
    print(ans.json())
    return ans.json()

# print('findeUserBase() = ', findeUserBase())
# print(findUsersInformation(findeUserBase()))
# users = findeUsers(findeUserBase())
# print(len(users))
# inspection(users)

findeUsersBig('553631b2ebad6435b0aab53a')
# multiplicateUsers()/
