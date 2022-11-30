from ib_insync import *

def getpos(list):
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=1)
    for i in ib.positions("DU5952012"):
        dict = {'Symbol': '', 'Position': '', 'AvgCost': '', 'PosType': ''}

        dict['Symbol'] = i.contract.symbol
        dict['Position'] = int(i.position)
        dict['AvgCost'] = round((i.avgCost) ,2)

        if i.position < 0:
            dict['PosType'] = 'Short'
        else:
            dict['PosType'] = 'Long'
        list.append(dict)
    return list