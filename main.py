from tws_api import *
import notion_api
from notion_api import databaseId

list = []
newList = getpos(list=list)


def main():
    notion_api.deleteTable(databaseId)
    for i in newList:
        notion_api.updateDatabase(databaseId, i)


if __name__ == "__main__":
    main()
