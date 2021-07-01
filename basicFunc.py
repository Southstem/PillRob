import json
import requests
from loginMirai import checkWords

def getSession():
    with open("status.json") as jf:
        config = json.load(jf)
        if checkWords(config, 'session'):
            return config['session']
    return("")

def turnOnPlugin( order ):
    print ("coming soon")

def  getFriendList():
    sessionVal = getSession()
    if sessionVal != None and sessionVal != "":
        print('[ Getlist ] request session = ' + sessionVal)
        url = "http://175.24.37.72:8080/friendList?sessionKey=" + sessionVal
        res = json.loads(requests.get(url=url).text)
        print('[ Getlist ] Here are your friends in your list : ')
        for i in res:
            print('  -->  '+i['nickname'])

        url = "http://175.24.37.72:8080/friendList?session="
    else:
        print('[ Getlist ] session information error ! Please login first ...')

def  getGroupList():
    sessionVal = getSession()
    if sessionVal != None and sessionVal != "":
        print('[ Getlist ] request session = ' + sessionVal)
        url = "http://175.24.37.72:8080/groupList?sessionKey=" + sessionVal
        res = json.loads(requests.get(url=url).text)
        print('[ Getlist ] Here are your groups in your list : ')
        for i in res:
            print('  -->  '+i['name'])

        url = "http://175.24.37.72:8080/friendList?session="
    else:
        print('[ Getlist ] session information error ! Please login first ...')

def getList():
    getFriendList()
    getGroupList()

def sendMessage():
    text = "Hello"