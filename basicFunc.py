import json
import requests
from loginMirai import checkWords
urlBase = "http://175.24.37.72:8080"

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

def sendMessage(order):
    if len(order) >= 2:
        qNumb = order[1]
        str = order[2]
    else:
        qNumb = ""
        str = ""
    sessionHere = getSession()
    if qNumb == None or qNumb == "":
        qNumb = '1311765133'
        str = "default message"
    print('[ SendF ] Sending message to ' + qNumb + ' as 【 ' + str + ' 】')
    if sessionHere != "" and sessionHere != None:
        dataSend = {
            'sessionKey' : sessionHere,
            'target' : int(qNumb),
            'messageChain' : [
                {"type" : "Plain","text" : str}
            ]
        }
        url = "http://175.24.37.72:8080/sendFriendMessage"
        res = requests.post(url = url,data = json.dumps(dataSend)).text
        print('[ SendF ] Sending status : '+ json.loads(res)['msg'])
        return 
    print('[ SendF ] Error!')

def sendGroupMessage(order):
    url = urlBase + '/sendGroupMessage'
    if len(order) > 2:
        groupNumb = order[1]
        text = order[2]
    else:
        groupNumb = "233600966"
        text = "Default test message ..."
    sessionHere = getSession()
    print('[ SendG ] Sending message to ' + groupNumb + ' as 【 ' + text + ' 】')
    if sessionHere != None and sessionHere != "":
        dataHere = {
            'sessionKey' : sessionHere,
            'target' : int(groupNumb),
            'messageChain' : [
                {'type': "Plain", "text" : text}
            ]
        }
        res = requests.post(url = url,data = json.dumps(dataHere)).text
        print('[ SendG ] Sending status : '+json.loads(res)['msg'])
        return
    print('[ SendG ] Send Error ! ')

# def addFriend(order):
#     qNumb = order[1]
#     url = "http://175.24.37.72/resp/newFriendRequestEvent"
#     sessionHere = getSession()
#     if sessionHere != None and sessionHere != "":
#         data_here = {
#             'sessionKey' : sessionHere,
#             'e'
#         }