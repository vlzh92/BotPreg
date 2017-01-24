import sys
# non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)
##print(x.translate(non_bmp_map))

import requests
from requests import Request, Session

##headers = { 'Connection' : 'Keep-Alive','User-Agent' : 'okhttp/3.4.1' }
##
##proxies = { 'http': 'http://192.168.1.25:8888'}
##
##body = '''Version: 3.1 (TLS/1.0)
##Random: 58 85 C5 6B 9D A6 9D FD B7 AA 3A FD D4 B6 F0 DF 1C E8 35 33 5C 74 28 89 8C 38 D4 6E 24 36 42 B5
##"Time": 4/19/2027 06:54:00
##SessionID: empty
##Extensions:
##	server_name	kernel.mom.life
##	ec_point_formats	uncompressed [0x0], ansiX962_compressed_prime [0x1], ansiX962_compressed_char2  [0x2]
##	elliptic_curves	sect571r1 [0xE], sect571k1 [0xD], secp521r1 [0x19], sect409k1 [0xB], sect409r1 [0xC], secp384r1 [0x18], sect283k1 [0x9], sect283r1 [0xA], secp256k1 [0x16], secp256r1 [0x17], sect239k1 [0x8], sect233k1 [0x6], sect233r1 [0x7], secp224k1 [0x14], secp224r1 [0x15], sect193r1 [0x4], sect193r2 [0x5], secp192k1 [0x12], secp192r1 [0x13], sect163k1 [0x1], sect163r1 [0x2], sect163r2 [0x3], secp160k1 [0xF], secp160r1 [0x10], secp160r2 [0x11]
##	SessionTicket	empty
##Ciphers:
##	[C00A]	TLS1_CK_ECDHE_ECDSA_WITH_AES_256_CBC_SHA
##	[C009]	TLS1_CK_ECDHE_ECDSA_WITH_AES_128_CBC_SHA
##	[C013]	TLS1_CK_ECDHE_RSA_WITH_AES_128_CBC_SHA
##	[C014]	TLS1_CK_ECDHE_RSA_WITH_AES_256_CBC_SHA
##	[0033]	TLS_DHE_RSA_WITH_AES_128_SHA
##	[0039]	TLS_DHE_RSA_WITH_AES_256_SHA
##	[002F]	TLS_RSA_AES_128_SHA
##	[0035]	TLS_RSA_AES_256_SHA
##	[000A]	SSL_RSA_WITH_3DES_EDE_SHA
##	[00FF]	TLS_EMPTY_RENEGOTIATION_INFO_SCSV
##
##Compression:
##	[00]	NO_COMPRESSION
##'''
##
##url = 'http://kernel.mom.life:443'
####url = 'http://www.google.com'
##
##req = Request(method='CONNECT', url=url, headers=headers, data=body)
##
##prepped = req.prepare()
##
##s = Session()
##
##print(s.send(prepped,
##             proxies=proxies))
##
##
##print(requests.request('CONNECT', url))

url = {'main':'https://kernel.mom.life/api/v1/feed/main',
       'message':'https://kernel.mom.life/api/v1/messenger/message',
       'read':'https://kernel.mom.life/api/v1/messenger/messages/user/'}

proxies = {'https': '192.168.1.25:8888',
           'http': '192.168.1.25:8888'}

cert = 'C:/FiddlerRoot.cer'

headers = {'main':{ 'app-os': 'android',\
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

req = Request('GET', url['main'], headers=headers['main'])

prepped = req.prepare()

s = Session()

ans = s.send(prepped,
             proxies=proxies,
             verify=False
             )

print(ans.json()['posts'][0])
id = ans.json()['posts'][0]['id']
user_id = ans.json()['posts'][0]['user_id']

print('id = ',id)
print('user_id = ',user_id)
message = {"payload":'Привет. Как дела? Я тут новенькая, могу к вам обращатся если что?',"user_id":user_id}

req = Request('POST', url['message'], headers=headers['message'],json=message)

prepped = req.prepare()

ans = s.send(prepped,
             proxies=proxies,
             verify=False
             )

print(ans.json())




s.close()



