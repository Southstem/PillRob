from loginMirai import loginMirai,checkWords
from basicFunc import turnOnPlugin
import json
from basicFunc import getList
import re
order = ""
loginOrNot = False

def statusJson():
    with open("status.json") as jf:
        config = json.load(jf)
    return config

def error():
    print('[ Terminal ] Progress error! please press Ctrl + C to shut it down! ')

def default():
    print('[ Command ] Please check your command !')

def markLine():
    if loginOrNot :
        config = statusJson()
        if checkWords(config, 'qNumb'):
            print('PillRob ['+config['qNumb']+'] > ', end ="")
    else:
        print('PillRob > ', end ="")
def pickDealFunc( ):
    order_split = order.split(" ")
    keyWord = order_split[0]
    print('[ Command ] Function' + keyWord + " is running ...")
    if order_split[0] == "login":
        if loginMirai(order_split):
            global loginOrNot
            loginOrNot = True
    elif order_split[0] == "turnon":
        turnOnPlugin(order_split)
    elif order_split[0] == "getlist":
        getList()
    else:
        default()

def mainTerminal():
    markLine()
    orderHere = input()
    while orderHere != "exit":
        global order
        order = orderHere
        pickDealFunc()
        markLine()
        orderHere = input()
    print("\n   Thanks for using.")

mainTerminal()