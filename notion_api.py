import requests, json


token = "secret_FlBqt3k44erjpf0EzDPoaYbfpbUDBgJfIuu8475EvvE"
databaseId = '8b89bee8d49442b4a7ad64b412e7e537'


headers = {
    "Authorization": "Bearer " + token,
    "Content-Type": "application/json",
    "Notion-Version": "2021-05-13"
}

def readDatabase(databaseId):
    url = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", url, headers=headers)
    data = res.json()
    print(res.status_code)

    with open('./db.json', 'w', encoding='utf8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def deleterow(databaseId):
    url = f"https://api.notion.com/v1/databases/{databaseId}/query"

    res = requests.request("POST", url, headers=headers)
    data = res.json()
    data["results"] = []
    data = json.dumps(data)


    updateUrl = f"https://api.notion.com/v1/databases/{databaseId}"

    req = requests.request("PATCH",  updateUrl, headers=headers, data=data)
    newData = req.json()
    #with open('./dbNew1.json', 'w', encoding='utf8') as f:
        #json.dump(newData, f, ensure_ascii=False, indent=4)
    newData["archived"] = True
    newData = json.dumps(newData)
    print(newData)

    newReq = requests.request("PATCH", updateUrl, headers=headers, data=newData)
    print(newReq.text)


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
                    "name": arr_element["PosType"],
                    "if": {"name": "Short"},
                    "then": {"color": "red"},
                    "else": {
                        "if": {"name": "Long"},
                        "then": {"color": "green"}
                    }
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
    #print(res.text)


