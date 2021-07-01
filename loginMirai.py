from os import write
import requests
import json
global urlbase
urlbase = ""

def checkWords( res, words ):
    for i in res.keys():
        if words == i:
            return True
    return False

with open("config.json",'r') as f:
    res = json.load(f)
    if checkWords(res,'url'):
         urlbase = res['url']+":"+res['port']
    else:
        print('[ Login ] ERROR!')

def bindMirai(session, qNumb):
    url_session = urlbase + "/verify"
    data_session = '{ "sessionKey" : "' + session + '","qq" : ' + qNumb + '}'
    res = json.loads(requests.post(url = url_session,data = data_session).text)
    if checkWords(res, 'code'):
        if res['code'] == 0:
            return True
    return False

def writeStatus(session,qNumb):
       data_json = {'session': session,'qNumb': qNumb}
       with open("status.json","w") as sf:
           json.dump(data_json,sf)

def loginMirai( order ):
    if len(order) <= 2:
        authKey = 'PillRob2021'
        qNumb = '3353417136'
    else:
        authKey = order[1]
        qNumb = order[2]
    print( '[ Login ] The authKey you have inputed is ' + authKey)
    url_auth = urlbase + "/auth"
    if authKey == "" or authKey == None:
        print('[ Login ] Default authKey : PillRob2021')
        authKey = 'PillRob2021'
    data_auth = '{"authKey":"' + authKey + '"}' 
    print('[ Login ] Connecting ......')
    res = json.loads(requests.post(url = url_auth, data = data_auth).text)
    if checkWords(res, 'session'):
        print('[ Login ] Connected ...')
        print('[ Login ] SessionKey : ' + res['session'])
        if bindMirai(res['session'],qNumb):
            print('[ Login ] Login success !')
            writeStatus(res['session'],qNumb)
            return True
    else:
        print('[ Login ] Connect failed !')
        return False

