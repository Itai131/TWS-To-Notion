from tws_api import *
from notion_api import *

list = []

newList = getpos(list=list)

for i in newList:
    updateDatabase(databaseId, i)


