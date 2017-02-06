import sys

from requests import Request, Session
import time
import random
from multiprocessing.dummy import Pool as ThreadPool
from Reg import reg
pool = ThreadPool(150)
pool2 = ThreadPool(4)

if __name__ == '__main__':
    print('SentBox is a main')
else:
    print('SentBox is imported')

_bearer = reg()

_url = {'main':'https://kernel.mom.life/api/v1/feed/main',
        'message':'https://kernel.mom.life/api/v1/messenger/message',
        'messageAsq': 'https://kernel.mom.life/api/v1/messenger/messages',
        'read':'https://kernel.mom.life/api/v1/messenger/messages/user/',
        'profile': 'https://kernel.mom.life/api/v1/profile/',
        'relations':'https://kernel.mom.life/api/v1/profile/relations/',
        'test':'https://kernel.mom.life/api/v1/feed/user/56af491884398335088b4567?direction=older&per_page=3'}

# _proxies = {'https': '192.168.1.25:8888',
           # 'http': '192.168.1.25:8888'}
_proxies = False

_cert = 'C://FiddlerRoot.pem'

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
            }}

def findUsersInformation(user_id):

    req = Request('GET', _url['profile'] + user_id, headers=_headers['main'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()

    if not ('user' in ans.json()):
        return[' ', ' ', 'Привет', ' ', ' ', ' ', ' ',]

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
    if 'users' in ans.json():
        return ans.json()['users'][0]['id']
    return 0

def findeUsers(user_id):
    req = Request('GET', _url['relations']+str(user_id)+'/2?page=0&per_page=1', headers=_headers['main'])
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
    if count > 3000:
        count = 3000
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

    if not('count' in ans.json()):
        print('ans.json() = ', ans.json())
        return []

    count = ans.json()['count']
    if count > 3000:
        count = 3000
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

def sent(text, user_id,nameStatus = 0):
    if not hasattr(sent, '_state'):  # инициализация значения
        sent._state = 0
    if not hasattr(sent,'_timer'):
        sent._timer = time.process_time()

    req = Request('GET', _url['messageAsq']+'/user/'+str(user_id)+'?with=topic', headers=_headers['messageAsq'])
    prepped = req.prepare()
    s = Session()
    ans = s.send(prepped,
                 proxies=_proxies,
                 verify=False
                 )
    s.close()

    print('time = ', time.process_time() - sent._timer)
    # if time.process_time() - sent._timer > 4:
    #     print('Brake sent ----------------------------------------------')
    #     return 0

    if 'status' in ans.json():
        print('sent =', sent._state)
        sent._state = sent._state + 1
        sent._timer = time.process_time()
        f = open('used_accounts.txt', 'a')
        f.writelines('\n'+str(user_id))
        f.close()
        if(nameStatus == 0):
            message = {"payload": text, "user_id": user_id}
        else:
            name = findUsersInformation(user_id)[2]
            print('name = ', name)
            message = {"payload": str(name) + text, "user_id": user_id}
        print(message)
        req = Request('POST', _url['message'], headers=_headers['message'], json=message)

        # if 'fields' in req.json():

        prepped = req.prepare()
        s = Session()
        ans = s.send(prepped,
                     proxies=_proxies,
                     verify=False
                     )
        s.close()
        return 1
    return 0

def sentAll(text,name = 0):
    user = findeUserBase()
    f = open('used_accounts.txt')
    used_accounts = set(f.readlines())
    for i in range(1000000):
        users = set(findeUsers(user))
        print('len(used_accounts) = ',len(used_accounts))
        print('len(users) = ', len(users))
        users = users - used_accounts
        print('len(users) = ', len(users))
        pool.map(lambda x: sent(text,x, name), users)
        if len(users) == 0:
            user = findeUserBase
        else:
            user = list(users)[round(len(users)/2)]

    return 0

# conection()
# print('findeUserBase() = ', findeUserBase())
# print(findUsersInformation(findeUserBase( )))
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

text = ''', привет! Я тут новенькая и хочу поделится новостью. Мой муж работает в Альфа-Банке и им предложили взять кредитную карту на очень льготных условиях. Может тебе это будет интересно? Если да, посмотри подробности https://goo.gl/3u3CiH '''
# f = open('users.txt', 'r')

sentAll(text,1)


# f.close()

