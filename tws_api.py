from ib_insync import *

def getpos(list):
    ib = IB()
    ib.connect('127.0.0.1', 7497, clientId=0, readonly=True)
    for i in ib.positions("DU6018957"):
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