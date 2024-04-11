import json

def getUserDB():
    with open("db/usersDB.json", "r+") as file:
        return json.load(file)

def saveUserDB(newUsers):
    with open("db/usersDB.json", "w+") as file:
        # file.write(json.load(newUsers, indent=4))
        # You were trying to load a json file when you were supposed to "write" it instead
        file.write(json.dumps(newUsers))

def getArticles():
    with open("db/articlesDB.json", "r+") as file:
        return json.load(file)