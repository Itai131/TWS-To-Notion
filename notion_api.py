import requests
import json

f = open('secrets.json', 'r')
secrets = json.load(f)
token = secrets['token']
databaseId = secrets['databaseId']
f.close()


headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}


def readDatabase():
    url = f"https://api.notion.com/v1/databases/{databaseId}/query"
    res = requests.request("POST", url, headers=headers)
    return res.json()


def deleteTable(databaseId):
    # get all ids of the pages in the database
    database = readDatabase()["results"]
    page_ids = [p["id"] for p in database]

    for id in page_ids:
        url = f"https://api.notion.com/v1/pages/{id}/"
        data = json.dumps({"archived": True})
        res = requests.request("PATCH", url, headers=headers, data=data)
        if (res.status_code != 200):
            print(res.text)


def updateDatabase(databaseId, arr_element):
    url = "https://api.notion.com/v1/pages"

    newPageData = {
        "parent": {"database_id": databaseId},
        "properties":  {
            "Symbol": {
                "title": [
                    {
                        "text": {
                            "content": arr_element["Symbol"]
                        }
                    }
                ]
            },
            "Position Type": {
                "type": "select",
                "select": {
                    "name": arr_element["PosType"]
                }
            },
            "Position": {
                "type": "number",
                "number": arr_element["Position"]
            },
            "Average Cost": {
                "type": "number",
                "number": arr_element["AvgCost"]
            }
        }
    }
    data = json.dumps(newPageData)
    res = requests.request("POST", url, headers=headers, data=data)
    if (res.status_code != 200):
        print(res.text)
